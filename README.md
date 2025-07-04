# 🌾 Crop Recommendation System

A Machine Learning-based system that recommends the most suitable crop to grow based on environmental and soil conditions. This project uses a **Random Forest Classifier** trained on agricultural data including nutrient levels, temperature, humidity, pH, and rainfall.

## 🚀 Features

- Predicts the best crop to cultivate for given conditions.
- User-friendly interface (can be integrated with web or desktop applications).
- Accurate recommendations using a trained Random Forest model.
- Easy to extend and customize for different regions and crop datasets.

---

## 🧠 Machine Learning Model

- **Algorithm Used:** Random Forest Classifier
- **Libraries:** Scikit-learn, Pandas, NumPy
- **Accuracy:** ~95% (may vary depending on dataset split and preprocessing)

---

## 📊 Dataset Features

The model is trained using data with the following features:

- `N` - Nitrogen content in soil
- `P` - Phosphorous content in soil
- `K` - Potassium content in soil
- `temperature` - Temperature in Celsius
- `humidity` - Relative humidity in %
- `ph` - pH value of the soil
- `rainfall` - Rainfall in mm

The target variable is the **recommended crop**.

---
