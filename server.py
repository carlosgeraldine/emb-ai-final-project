from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """Render the main index page"""
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Process the text and return emotion analysis results
    """
    # Get the text from the URL query parameters
    text = request.args.get('textToAnalyze', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Get emotion predictions
    result = emotion_detector(text)
    
    # Format the response string
    response_text = f"For the given statement, the system response is 'anger': {result['anger']}, \
'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and \
'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)