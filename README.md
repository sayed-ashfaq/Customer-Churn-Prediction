## **Customer Churn Prediction using Flask & Machine Learning**  

### **Project Overview**  
This project predicts **customer churn** (whether a customer will leave the service or not) using machine learning models. The model is deployed using **Flask**, allowing users to upload a CSV file and get predictions.  

### **Technologies Used**  
- **Python** (For model training and prediction)  
- **Flask** (For deployment)  
- **Pandas, NumPy** (For data processing)  
- **Scikit-learn, XGBoost, DecisionTree, RandomForest** (For machine learning)  
- **SMOTE & ENN** (For handling imbalanced data)  

### **Project Workflow**  
1. **Data Preprocessing:**  
   - Handled missing values  
   - Converted categorical data using **One-Hot Encoding**  
   - Scaled numerical data  
   - Applied **SMOTEENN** to balance the dataset  
2. **Model Training:**  
   - Tried different models (**Decision Tree, XGBoost, Random Forest**)  
   - Selected **Random Forest** as the final model (best accuracy ~98%)  
   - Saved the trained model using **Pickle**  
3. **Flask Web App:**  
   - Users can upload a CSV file  
   - The model processes the data and returns predictions  
4. **Deployment:**  
   - Flask app can be tested **locally** using Anaconda/Command Prompt  
   - Can be hosted on cloud platforms (like **Render, Heroku, or AWS**)  

### **How to Run the Project Locally**  
#### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/sayed-ashfaq/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

#### **Step 2: Create a Virtual Environment (Recommended)**
```bash
conda create --name churn_env python=3.9
conda activate churn_env
```

#### **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

#### **Step 4: Run Flask App**  
```bash
python app.py
```
The app will start running at **http://127.0.0.1:5000/**  

#### **Step 5: Upload a CSV File**  
- Go to the browser and open **http://127.0.0.1:5000/**  
- Upload a **CSV file** with customer data  
- The model will predict whether the customer will **churn or not**  

### **Sample Test Data**  
- It is uploaded as test_data in the git repo


### **Next Steps**  
- Deploy the Flask app to **Render, AWS, or Heroku**  
- Improve the UI using **HTML & CSS**  
- Experiment with more ML models for better accuracy  
