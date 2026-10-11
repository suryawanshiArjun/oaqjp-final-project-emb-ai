"""Flask web interface for the EmotionDetection package."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the form and display the emotion analysis result."""
    result = None
    error = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text_to_analyze", "").strip()
        if not text:
            error = "Please enter some text before submitting."
        else:
            result = emotion_detector(text)
            if result is None:
                error = "Emotion detection failed. Check the text or try again later."

    return render_template("index.html", result=result, error=error, text=text)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
