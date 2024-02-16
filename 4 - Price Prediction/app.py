import pandas as pd
from pickle import load
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
SWAGGER_URL = '/swagger'
API_URL = f'/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "price prediction"
    },
)

app.register_blueprint(swaggerui_blueprint)

cars = pd.read_csv("Cleaned.csv")
model = load(open("DecisionTreeClassifier.pkl", "rb"))

@app.route("/")
def index():
    models = sorted(cars["BrandType"].unique())
    years = sorted(cars["Age"].unique())
    # states = sorted(cars["BodyState"].unique())
    return render_template("index.html", models=models, years=years)

@app.route("/predict", methods=["POST"])
def predict():

    BrandType = request.form.get("car_models")
    Age = request.form.get("year")
    Usage = request.form.get("kilo_driven")
    # BodyState = request.form.get("body_state")
    
    prediction = model.predict(pd.DataFrame([[BrandType, Age, Usage]], columns=["BrandType", "Age", "Usage"]))
    
    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug=True)