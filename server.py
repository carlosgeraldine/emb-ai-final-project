# Module docstring explaining the purpose of the server.py file
"""
This module implements a Flask web application for emotion detection using a provided text.
It includes routes to render the index page and process emotion analysis for the input text.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the main index page where the user can input text for emotion analysis.

    Returns:
        Rendered HTML template of the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handles the GET request to analyze emotions from the provided text.

    This function receives the text from the client, processes it using the emotion_detector,
    and returns the emotion analysis results or an error message if the input is invalid.

    Returns:
        JSON response containing either the emotion analysis results or an error message.
    """
    # Get the text from the URL query parameters
    text = request.args.get('textToAnalyze', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Get emotion predictions
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Format the response string
    response_text = f"For the given statement, the system response is 'anger': {result['anger']}, \
'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and \
'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
