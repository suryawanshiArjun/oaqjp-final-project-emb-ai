# Emotion Detection Web Application

A Python package and Flask web app that sends text to the Watson NLP emotion prediction service and displays anger, disgust, fear, joy, sadness, and the dominant emotion.

## Project structure

```text
EmotionDetectionProject/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Setup

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run unit tests

```bash
python -m unittest -v test_emotion_detection.py
```

The tests mock the HTTP service, so they can run without a network connection.

## Run the Flask application

```bash
python server.py
```

Open http://127.0.0.1:5000 in your browser. A live analysis requires access to the Watson NLP endpoint configured in `EmotionDetection/emotion_detection.py`.

## Static analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py
```

Review the score produced by your installed Pylint version. Do not claim a perfect score unless the command actually reports it.

## Evidence required for the course submission

Capture your own screenshots after running the application and tests:

- `6b_deployment_test.png`: browser showing a successful live analysis.
- `7c_error_handling_interface.png`: browser showing the blank-input validation message.
- Terminal output for package import, passing unit tests, and Pylint score.

## GitHub submission links

After creating a **public** GitHub repository and pushing this project, replace `YOUR_GITHUB_USERNAME` and `YOUR_REPOSITORY` in these URLs:

- Repository README: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/README.md`
- Package initializer: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/EmotionDetection/__init__.py`
- Emotion detector: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/EmotionDetection/emotion_detection.py`
- Flask server: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/server.py`
- Unit tests: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/test_emotion_detection.py`
