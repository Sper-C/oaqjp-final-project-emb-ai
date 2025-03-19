"""
    Deploy server
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Get text from user and send back the result
    """
    text_to_detect = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_detect)
    if emotion["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is \
             'anger': {emotion['anger']}, 'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, \
            'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. \
            The dominant emotion is {emotion['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
        Render default page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
