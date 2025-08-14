import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib
import tensorflow as tf

# Load trained model & scaler
model = tf.keras.models.load_model(r"E:\ML\intership\Task3\heart_model.keras")
scaler = joblib.load(r"E:\ML\intership\Task3\scaler.pkl")


# Feature names
features = ["age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak",
            "slope", "ca", "thal"]

# GUI setup
root = tk.Tk()
root.title("Heart Disease Prediction")
root.geometry("400x600")

tk.Label(root, text="Enter Patient Details", font=("Arial", 14, "bold")).pack(pady=10)

entries = {}
for feature in features:
    frame = tk.Frame(root)
    frame.pack(pady=5)
    tk.Label(frame, text=feature, width=15, anchor="w").pack(side="left")
    entry = tk.Entry(frame)
    entry.pack(side="right", fill="x", expand=True)
    entries[feature] = entry

def predict():
    try:
        values = [float(entries[f].get()) for f in features]
        scaled_values = scaler.transform([values])
        prediction = model.predict(scaled_values)[0][0]
        result = "Heart Disease Likely" if prediction > 0.5 else "No Heart Disease"
        messagebox.showinfo("Prediction Result", f"{result}\nScore: {prediction:.4f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

tk.Button(root, text="Predict", command=predict, bg="green", fg="white").pack(pady=20)

root.mainloop()
