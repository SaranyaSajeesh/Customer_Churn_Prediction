# Customer_Churn_Prediction

Step 1: Project Overview
This project's primary goal is to predict customer churn, which refers to the loss of customers in a telecom company. Customer churn can have a significant impact on a company's revenue and profitability. In this project, we aim to proactively identify customers at risk of leaving the service using machine learning techniques. The ultimate objective is to develop a model that assists in retaining high-risk customers and reducing churn rates.

Streamlit App Link:- https://curvy-donuts-help.loca.lt

Step 2: Data Collection
Gather historical customer data from the telecom company's records. The dataset should include various customer attributes such as tenure, monthly charges, contract type, internet service, and more. Additionally, it should indicate whether a customer has churned (left) or not.

Step 3: Data Preprocessing
Data preprocessing is crucial to ensure that the data is clean and ready for analysis and modeling. This step involves:

Encoding categorical features: Convert categorical variables into numerical format using techniques like one-hot encoding or label encoding. For example, gender, partner, and other features were encoded.
Exploratory Data Analysis (EDA): Conduct EDA to gain insights into the data. This step includes generating summary statistics, creating visualizations, and exploring relationships between variables. EDA can reveal patterns, correlations, and potential predictive features.

Step 4: Model Building
Once the data is prepared,I implemented KNN,SVM,Decision Tree,Random Forest,Ada Boost classifiers
These models are trained using historical data to learn patterns and make predictions.

Step 5: Model Evaluation
After training the models, it's essential to assess their performance.
Accuracy: The proportion of correctly predicted churn cases.
On the basis of Accuracy I choose Random Forest that predict churn with 85% accuracy.

Step 6: Web Application Development
To make the model accessible and user-friendly, created a Streamlit web application. The application allows users to input customer information and receive real-time churn predictions. Users can interact with the application to assess whether a specific customer is likely to churn.

Step 7: Impact
The predictive model allows the telecom company to proactively target high-risk customers with retention strategies, reducing churn rates and preserving revenue.
The Streamlit web application enables the company to make quick decisions based on real-time customer data.
