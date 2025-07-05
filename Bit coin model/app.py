from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('tesla_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    open_price = float(request.form['open'])
    close_price = float(request.form['close'])
    high_price = float(request.form['high'])
    low_price = float(request.form['low'])
    month = int(request.form['month'])

    # Feature Engineering
    open_close = open_price - close_price
    low_high = low_price - high_price
    is_quarter_end = 1 if month % 3 == 0 else 0

    features = np.array([[open_close, low_high, is_quarter_end]])
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]

    result = "UP" if prediction == 1 else "DOWN"

    return render_template('index.html', prediction_text=f"Predicted Movement: {result} (Confidence: {prob:.2f})")

if __name__ == '__main__':
    app.run(debug=True)
