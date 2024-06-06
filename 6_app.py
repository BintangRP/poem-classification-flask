import numpy as np
from flask import Flask, request, render_template,jsonify
import joblib

# Create flask app
STATIC_FOLDER = 'templates/assets'
flask_app = Flask(__name__,
            static_folder=STATIC_FOLDER)
model = joblib.load(open("trained_model_svm.pkl", "rb"))
vectorizer = joblib.load("tfidf_vectorizer.pkl")


@flask_app.route("/")
def Home():
    return render_template("my-prediction.html")

@flask_app.route("/predict/api", methods = ["POST"])
def predict_api():
    try:
        # Get input data
        data1 = request.form['Poem']
        poemText = data1

        # Transform input data using the vectorizer
        input_vector = vectorizer.transform([data1])

        # Predict the topic using the model
        pred = model.predict(input_vector)

        # Return prediction as JSON
        return jsonify({'prediction': pred[0],'poem-text': poemText})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@flask_app.route("/prediksi")
def prediksi_page():
    return render_template("index.html")

    
@flask_app.route("/predict", methods = ["POST"])
def predict():
    try:
        # Get the prediction from the API
        response = predict_api().json
        print(response)

        # Extract the prediction text from the API response
        prediction = response['prediction']
        poemText = response['poem-text']
        # print(poemText)

        return render_template("index.html", poem_text=poemText ,prediction_text=prediction)
    except Exception as e:
        return render_template("index.html", prediction_text="Error: " + str(e))

if __name__ == "__main__":
    flask_app.run(debug=True)