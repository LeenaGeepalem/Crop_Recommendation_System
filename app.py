from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
rf_classifier = joblib.load('rf_model.joblib')

# Correct feature names (as used in training)
feature_columns = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        form_data = {col: request.form.get(col) for col in feature_columns}

        # Ensure all fields have values
        if None in form_data.values():
            return "Error: Missing input values", 400

        # Convert to float
        input_values = [float(form_data[col]) for col in feature_columns]

        # Convert input into a DataFrame with correct feature names
        input_data = pd.DataFrame([input_values], columns=feature_columns)

        # Make prediction
        prediction = rf_classifier.predict(input_data)[0]

        return render_template('index.html', prediction=prediction)

    except ValueError:
        return "Error: Please enter valid numerical values.", 400

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
