import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in text using Watson NLP EmotionPredict function and formats the output.
    
    Args:
        text_to_analyze (str): The text to analyze for emotional content
        
    Returns:
        dict: Formatted emotional analysis results including dominant emotion
    """
    
    # API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input data in the required format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Make the POST request
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        response_dict = json.loads(response.text)
        
        # Extract emotion scores
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Create formatted output dictionary
        output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness']
        }
        
        # Find dominant emotion (emotion with highest score)
        dominant_emotion = max(output.items(), key=lambda x: x[1])[0]
        output['dominant_emotion'] = dominant_emotion
        
        return output
        
    except requests.exceptions.RequestException as e:
        return f"Error making request: {str(e)}"
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        return f"Error processing response: {str(e)}"