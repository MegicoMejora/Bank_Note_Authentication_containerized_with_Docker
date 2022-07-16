# Bank_Note_Authentication_containerized_Using_Docker

## End-to-End Machine Learning Project using Docker

The data used in this project is downloaded from Kaggle 'https://www.kaggle.com/datasets/ritesaluja/bank-note-authentication-uci-data' and also the dataset is provided in the folder 'Dataset'.

The major steps involved in this project,

1.Data Preprocessing

2.Model Building

3.Model Deployment

### 1.Data Preprocessing

Data cleaning, Feature Engineering and Outlier Detection have been explained in detail in the Notebook. 

### 2. Model Building
 
 The Model is trained and validated using the Random Forest Classifier.

### 3. Model Deployment

The model is deployed using, For backend, using the Python Flask for the http server and the for the frontend a Website is created using Swagger Api. This Web app has been containerized using Docker. This app predicts the value whether the bank note is authenticate or not by taking the inputs such as 'variance', 'skewness', 'curtosis' and 'entropy' from the user.

The Notebook provides the detailed explanation about model building and the model deployment. Also, screenshots of Postman collections testing of the Endpoints are shown.

The folder 'Docker Collections shows the app running using Docker'

## Aplication Endpoints are,
1. /predict

2. /apidocs
