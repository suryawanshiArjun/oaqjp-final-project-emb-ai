"""Detect emotions in text using the Watson NLP emotion endpoint."""
from typing import Any, Dict, Optional

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def emotion_detector(text_to_analyze: str) -> Optional[Dict[str, Any]]:
    """Return five emotion scores and the dominant emotion, or None on failure."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return None

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            API_URL, headers=headers, json=payload, timeout=15
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        body = response.json()
        emotions = body["emotionPredictions"][0]["emotion"]
        keys = ("anger", "disgust", "fear", "joy", "sadness")
        result = {key: float(emotions[key]) for key in keys}
        result["dominant_emotion"] = max(keys, key=result.get)
        return result
    except (KeyError, IndexError, TypeError, ValueError):
        return None
