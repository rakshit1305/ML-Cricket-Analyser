**📌 Cricket Score Predictor – Machine Learning Project**

This project predicts the final score of a cricket innings using machine learning.
It is built using Python, Scikit-Learn, XGBoost, and Streamlit for deployment.

📁**Project Structure**
ML_project/
│── ML.ipynb                # Jupyter Notebook with all training code
│── cricket_pipeline.pkl    # Saved final ML pipeline
│── app.py                  # Streamlit web application
│── README.md               # Project documentation
│── data/                   # Dataset (CSV)


**📌 1. Project Overview**

The goal of this project is to build a regression model that predicts final runs scored based on match conditions such as:

Batting team
Bowling team
Current score
Balls bowled
Wickets left
Runs in last 3 overs
Current run rate
City


**📊 2. Dataset Description**
| Feature           | Description                |
| ----------------- | -------------------------- |
| batting_team      | Team currently batting     |
| bowling_team      | Team bowling               |
| current_score     | Score at prediction moment |
| balls_bowled      | Total balls bowled so far  |
| wickets_left      | Wickets remaining          |
| runs_last_3_overs | Form indicator             |
| crr               | Current Run Rate           |
| city              | Match location             |
| final_score       | Target variable            |

https://www.kaggle.com/veeralakrishna/cricsheet-a-retrosheet-for-cricket?select=t20s
Link to access datasets taken for this project. To open dataset, Click on the link mentioned. There we can find multiple sections of cricket matches such as ipl, bbl, ODIs,Tests, T20s etc. Among these, click on T20s to see the project dataset.

**🧠 3. Machine Learning Workflow**
**✔ Data Cleaning**
1.Missing value handling
2.Type conversions

**✔ Feature Engineering**
1.One-Hot Encoding for categorical columns
2.Scaling numeric columns

✔ Algorithm Testing

**Models tested:**

**Model	Status**
| Model                | Status            |
| -------------------- | ----------------- |
| Linear Regression    | ❌ High error      |
| Decision Tree        | ❌ Overfitting     |
| Random Forest        | ✔ Good            |
| AdaBoost             | ✔ Moderate        |
| XGBoost              | ✔ Strong          |
| **Voting Regressor** | **⭐⭐ Best Model** |


**🏆 4. Best Model: VOTING REGRESSOR**

The final model is an ensemble of three strong regressors:
**RandomForest + AdaBoost + XGBoost**


📌 Voting Regressor gave the lowest error and best generalization, making it the final choice.


**🧪 5. Final Machine Learning Pipeline**

The final pipeline includes:

SimpleImputer → handle missing numeric values
StandardScaler → scale numeric features
OneHotEncoder → convert teams/city to vectors
VotingRegressor → final model

**💻 6. How to Run the Code**

1. Clone the repository:
git clone <repository-link>
cd ML_project


2. Install dependencies:
pip install -r requirements.txt


3. Run the Jupyter Notebook to retrain/test the model:
jupyter notebook ML.ipynb


4. To launch the Streamlit web app:
streamlit run app.py


5.Open the displayed localhost URL in a browser to use the score predictor.


**📦 7. Dependencies**

Python ≥ 3.8, 
pandas, 
numpy, 
scikit-learn, 
xgboost, 
streamlit, 
joblib (for saving/loading pipeline)


**📈 8. Expected Outputs**

1. Jupyter Notebook:
Data preprocessing results
Model training and evaluation metrics (MAE, RMSE, R²)
Comparison of multiple models

2. Streamlit App:
User inputs match conditions: batting team, bowling team, current score, balls bowled, wickets left, last 3 overs runs, crr, city
Displays predicted final score instantly

3. Model Performance (Voting Regressor):
MAE (Test): 1.6967
R² (Test): 0.9854
RMSE: 4.81



