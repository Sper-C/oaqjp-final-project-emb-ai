import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test(self):
        case_1 = "I am glad this happened"
        result = emotion_detector(case_1)
        self.assertEqual(result["dominant_emotion"], "joy")

        case_2 = "I am really mad about this"
        result = emotion_detector(case_2)
        self.assertEqual(result["dominant_emotion"], "anger")

        case_3 = "I feel disgusted just hearing about this"
        result = emotion_detector(case_3)
        self.assertEqual(result["dominant_emotion"], "disgust")

        case_4 = "I am so sad about this"
        result = emotion_detector(case_4)
        self.assertEqual(result["dominant_emotion"], "sadness")

        case_5 = "I am really afraid that this will happen"
        result = emotion_detector(case_5)
        self.assertEqual(result["dominant_emotion"], "fear")

unittest.main()