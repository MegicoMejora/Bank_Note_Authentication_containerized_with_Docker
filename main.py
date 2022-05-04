from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

model = open('classifier.pkl','rb')
classifier = pickle.load(model)
print("The saved model is loaded.....")

@app.route('/predict',methods=['GET'])
def predict_note_authentication():

    """ Authenticating Bank Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          requried: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values    
    
    """
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "The predicted value is"+str(prediction)



if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")
