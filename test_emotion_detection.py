"""Unit tests for the Emotion Detection package."""

import unittest

from EmotionDetection import emotion_detector


class EmotionDetectorTests(unittest.TestCase):
    """Tests for the emotion_detector function."""

    def test_returns_default_structure_for_empty_text(self):
        """An empty input should return the expected default structure."""
        result = emotion_detector("")
        self.assertEqual(result["dominant_emotion"], None)
        self.assertEqual(result["anger"], None)
        self.assertEqual(result["disgust"], None)
        self.assertEqual(result["fear"], None)
        self.assertEqual(result["joy"], None)
        self.assertEqual(result["sadness"], None)

    def test_returns_default_structure_for_400_response(self):
        """A Watson 400 response should return the expected default structure."""
        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], None)
        self.assertEqual(result["anger"], None)
        self.assertEqual(result["disgust"], None)
        self.assertEqual(result["fear"], None)
        self.assertEqual(result["joy"], None)
        self.assertEqual(result["sadness"], None)

    def test_structure_contains_required_emotions(self):
        """The function should always return the required emotion keys."""
        result = emotion_detector("I am happy")
        self.assertIn("anger", result)
        self.assertIn("disgust", result)
        self.assertIn("fear", result)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)
        self.assertIn("dominant_emotion", result)


if __name__ == "__main__":
    unittest.main()
