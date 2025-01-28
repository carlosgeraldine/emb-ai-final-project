import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in text using Watson NLP EmotionPredict function.
    
    Args:
        text_to_analyze (str): The text to analyze for emotional content
        
    Returns:
        dict: The emotional analysis results from Watson NLP
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
        
        # Return the text attribute of the response
        return response.text
        
    except requests.exceptions.RequestException as e:
        return f"Error making request: {str(e)}"