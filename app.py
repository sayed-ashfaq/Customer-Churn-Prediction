from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("RandomForest_Churn_model.pkl")

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # This will render an HTML page

# Route to handle CSV file uploads and predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # Read CSV file
    data = pd.read_csv(file)

    # Ensure the columns match what the model expects
    try:
        predictions = model.predict(data)
    except Exception as e:
        return jsonify({'error': f'Invalid file format: {str(e)}'}), 400

    # Convert predictions to a list and send response
    return jsonify({'predictions': predictions.tolist()})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
