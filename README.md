# ❤️ Heart Disease Predictor

A **Machine Learning-based** heart disease prediction system using the **UCI Heart Disease Dataset** (available on [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)).  
This project uses a **Neural Network (TensorFlow/Keras)** to predict the likelihood of heart disease from patient health metrics.

---

## 📊 Dataset
- **Source**: [Heart Disease UCI Dataset - Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- **Rows**: 303 patients
- **Target**: `condition` (1 = Heart Disease, 0 = No Heart Disease)
- **Features**:
  - `age` — Age in years
  - `sex` — 1: Male, 0: Female
  - `cp` — Chest pain type (0-3)
  - `trestbps` — Resting blood pressure (mm Hg)
  - `chol` — Serum cholesterol (mg/dl)
  - `fbs` — Fasting blood sugar > 120 mg/dl (1 = True, 0 = False)
  - `restecg` — Resting electrocardiographic results (0-2)
  - `thalach` — Maximum heart rate achieved
  - `exang` — Exercise-induced angina (1 = Yes, 0 = No)
  - `oldpeak` — ST depression induced by exercise
  - `slope` — Slope of peak exercise ST segment (0-2)
  - `ca` — Number of major vessels (0-3)
  - `thal` — Thalassemia type (0-3)

---

## 🚀 Features
- **Data Preprocessing**: Scaling using `StandardScaler`
- **Model**: Neural Network with L2 regularization
- **Evaluation**: Accuracy, Confusion Matrix, Classification Report
- **Visualization**: Training & Validation Accuracy/Loss graphs
- **GUI**: Easy interface to input patient data and get predictions
- **Saved Model**: `.keras` model & `.pkl` scaler for future predictions

---

## 🖥 Tech Stack
- **Python 3.11**
- **TensorFlow/Keras** — Neural Network Model
- **Scikit-learn** — Preprocessing & Metrics
- **Matplotlib** — Visualization
- **Pandas & NumPy** — Data handling
- **Tkinter** — Graphical User Interface

---

