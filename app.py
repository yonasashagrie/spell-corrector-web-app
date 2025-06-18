from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')
    cleaned_text = correct_spelling(text)
    
    # Render the result in the template
    return render_template('index.html', cleaned_text=cleaned_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
