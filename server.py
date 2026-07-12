"""Flask app for the Emotion Detector web interface."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def index():
    """Render the page and process emotion detection requests."""
    text_to_analyse = request.args.get("text_to_analyse", "")

    if not text_to_analyse:
        return render_template(
            "index.html",
            error_message="Invalid text! Please try again!",
        )

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return render_template(
            "index.html",
            error_message="Invalid text! Please try again!",
        )

    return render_template(
        "index.html",
        anger=result["anger"],
        disgust=result["disgust"],
        fear=result["fear"],
        joy=result["joy"],
        sadness=result["sadness"],
        dominant_emotion=result["dominant_emotion"],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    