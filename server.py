'''This is a Flask server running module
The server contains two path: 
    "/" for index.html
    "/emotionDetector" for sending text to detector
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    '''This function renders index.html'''
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    '''This function receives text from GET method and sends it to detector'''
    text_to_detect = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_detect)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if not dominant_emotion:
        return "<b>Invalid text! Please try again!</b>"

    return f'''For the given statement, the system response is \
    'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. \
    The dominant emotion is <b>{dominant_emotion}</b>.'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
