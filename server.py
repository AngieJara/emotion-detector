"""Flask app for the Emotion Detector web interface."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main page and process text analysis requests."""
    text_to_analyse = request.form.get("text_to_analyse", "")
    if not text_to_analyse:
        text_to_analyse = request.args.get("text_to_analyse", "")

    if not text_to_analyse:
        return render_template(
            "index.html",
            error_message="Please enter some text to analyze.",
        )

    result = emotion_detector(text_to_analyse)
    if result.get("dominant_emotion") is None:
        return render_template(
            "index.html",
            error_message="Unable to analyze the text. Please try again.",
        )

    return render_template(
        "index.html",
        anger=result.get("anger"),
        disgust=result.get("disgust"),
        fear=result.get("fear"),
        joy=result.get("joy"),
        sadness=result.get("sadness"),
        dominant_emotion=result.get("dominant_emotion"),
    )


if __name__ == "__main__":
    app.run(debug=True)
