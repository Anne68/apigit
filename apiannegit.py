# 1. Library imports
import uvicorn
from fastapi import FastAPI
from irisapitest import IrisModel  # Importer votre modèle ML depuis irisapitest

# 2. Create the app object
app = FastAPI()

# 3. Load the ML model
model = IrisModel()  # Assurez-vous que cette classe existe dans irisapitest

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Welcome to the Iris API'}

# 5. Predict route, expects features as query parameters and returns the prediction
@app.get('/predict/')
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    return {'prediction': prediction}

# 6. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
