"""IBM Watson Emotion Detection client.

This module contains a placeholder-ready implementation for the official
Emotion Detection service. The Watson endpoint, headers and payload must be
filled in from the IBM lab instructions before the function can be used.
"""

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


WATSON_URL = os.getenv("WATSON_URL", "PEGAR_AQUI_URL_OFICIAL")
WATSON_HEADERS = _load_json_setting("WATSON_HEADERS", {})
WATSON_INPUT = _load_json_setting("WATSON_INPUT", {})


def emotion_detector(text_to_analyse):
    """Call IBM Watson Emotion Detection and return the formatted result."""
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if not WATSON_URL or WATSON_URL == "PEGAR_AQUI_URL_OFICIAL":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    payload = dict(WATSON_INPUT)
    payload["text"] = text_to_analyse

    try:
        response = requests.post(
            WATSON_URL,
            headers=WATSON_HEADERS,
            json=payload,
            timeout=10,
        )
    except requests.RequestException:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    data = response.json()

    emotions = data.get("emotion", {}).get("document", {}).get("emotion", {})
    if not emotions:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    normalized = {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
    }
    dominant_emotion = max(normalized, key=normalized.get)
    normalized["dominant_emotion"] = dominant_emotion
    return normalized
