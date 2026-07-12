"""IBM Watson Emotion Detection client."""

import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def _load_json_setting(name, default):
    """Load a JSON value from an environment variable."""
    value = os.getenv(name)
    if value is None or not value.strip():
        return default

    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


WATSON_URL = os.getenv("WATSON_URL", "")
WATSON_HEADERS = _load_json_setting("WATSON_HEADERS", {})


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores and dominant emotion."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not text_to_analyse or not text_to_analyse.strip():
        return empty_result

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(
            WATSON_URL,
            headers=WATSON_HEADERS,
            json=payload,
            timeout=10,
        )
    except requests.RequestException:
        return empty_result

    if response.status_code == 400:
        return empty_result

    response.raise_for_status()

    data = response.json()

    emotions = data["emotionPredictions"][0]["emotion"]

    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }

    result["dominant_emotion"] = max(result, key=result.get)

    return result