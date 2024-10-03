Here’s a concise, clear, and narrative-style README for your binary classification project:

---

# Employee Retention Prediction

## Project Overview
This project aims to predict whether a candidate will remain with the company after completing a training program or seek new employment. The company conducts specialized courses in Big Data and Data Science, and many individuals sign up. Identifying candidates who are likely to stay allows the company to save time, reduce costs, and enhance the quality of their training programs. 

Our goal is to build a **binary classification model** that uses data such as demographics, education, and work experience from candidates' sign-up and enrollment records to predict their likelihood of staying with the company.

## Problem Statement
The company needs to categorize candidates into two groups:
1. **Likely to Stay**: Candidates who are likely to join the company after training.
2. **Likely to Leave**: Candidates who may be looking for new employment opportunities elsewhere.

By solving this problem, the company can make informed decisions to tailor their training programs and improve resource allocation.

## Dataset
*enrollee_id* : Unique ID for candidate.
*city*: City code.
*city_ development _index* : Developement index of the city (scaled).
*gender*: Gender of candidate
*relevent_experience*: Relevant experience of candidate
*enrolled_university*: Type of University course enrolled if any
*education_level*: Education level of candidate
*major_discipline* :Education major discipline of candidate
*experience*: Candidate total experience in years
*company_size*: No of employees in current employer's company
*company_type* : Type of current employer
*last_new_job*: Difference in years between previous job and current job
*training_hours*: training hours completed
*target*: 0 – Not looking for job change, 1 – Looking for a job change

  
These features are used to train the model to predict whether a candidate is likely to stay or leave after completing the courses.

## Approach
The project follows these key steps:
1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and normalizing numerical features.
2. **Model Selection**: We experimented with several machine learning models, including:
   - Decision Tree
   - Random Forest
   - Logistic Regression
   - Support Vector Machine
   - Gaussian Naive Bayes
3. **Hyperparameter Tuning**: Optimal parameters for each model were selected using grid search and cross-validation to enhance prediction accuracy.
4. **Evaluation**: The models were evaluated based on performance metrics such as accuracy, precision, recall, and F1-score.
5. **Best Model**: The best-performing model was saved using `pickle` for deployment.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-retention-prediction.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the model and make predictions:
1. Load the preprocessed data.
2. Load the saved model using `pickle`.
3. Use the model to predict whether candidates will stay or leave:
   

## Results
The best-performing model achieved an accuracy of **71%**, with a strong balance between precision and recall. This model provides reliable predictions on whether a candidate is likely to stay or seek other opportunities.

## Future Work
- Fine-tune the model further to improve its generalization.
- Include XAI