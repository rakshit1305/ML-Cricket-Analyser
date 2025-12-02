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



