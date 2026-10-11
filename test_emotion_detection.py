"""Unit tests for the EmotionDetection package."""
import unittest
from unittest.mock import Mock, patch

import requests

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test successful responses and error handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_emotion_scores(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{"emotion": {
                "anger": 0.01,
                "disgust": 0.02,
                "fear": 0.03,
                "joy": 0.90,
                "sadness": 0.04,
            }}]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)
        mock_post.assert_called_once()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_non_200_returns_none(self, mock_post):
        mock_post.return_value.status_code = 400
        self.assertIsNone(emotion_detector("hello"))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_request_error_returns_none(self, mock_post):
        mock_post.side_effect = requests.RequestException("offline")
        self.assertIsNone(emotion_detector("hello"))

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_empty_input_returns_none_without_request(self, mock_post):
        self.assertIsNone(emotion_detector("   "))
        mock_post.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
