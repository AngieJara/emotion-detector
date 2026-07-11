# Emotion Detector

## Project Description

Emotion Detector is an AI-powered web application built with Python and Flask that uses IBM Watson Natural Language Processing to analyze a user-provided text. The application identifies the following emotions:

- anger
- disgust
- fear
- joy
- sadness

It also determines the dominant emotion for the provided text.

## Features

- Web interface for entering text
- Emotion analysis using IBM Watson NLP
- Display of all detected emotion scores
- Display of the dominant emotion
- Clear error handling for empty input and API failures

## Project Structure

emotion-detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
├── README.md
└── requirements.txt

## Technologies Used

- Python 3.13+
- Flask
- requests
- unittest
- pylint

## Installation

On Windows PowerShell, run:

```powershell
cd C:\Users\angie\Documents\cursea\IANPL
mkdir emotion-detector
cd emotion-detector
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

## Running the Application

```powershell
py server.py
```

Then open your browser at http://localhost:5000.

## Running Unit Tests

```powershell
py test_emotion_detection.py
```

## Static Code Analysis

```powershell
py -m pylint server.py
```

## Error Handling

The application handles the following cases:

- Empty text input
- Watson API errors
- Missing or invalid response data

## Author

Created for the IBM Skills Network Emotion Detection project.
