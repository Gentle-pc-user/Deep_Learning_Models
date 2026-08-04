* # Bengaluru House Price Prediction

A full-stack Deep Learning web application that predicts house prices in Bengaluru using a PyTorch Multi-Layer Perceptron (MLP) model.

**Live Repository:** [https://github.com/ObsidianTwilight/Deep_Learning_Models](https://github.com/ObsidianTwilight/Deep_Learning_Models)

---

* ## Project Importance

Housing prices in cities like Bengaluru are highly non-linear and influenced by multiple factors such as location, size, society, number of bathrooms, balconies, and area type. Traditional linear models often fail to capture these complex relationships.

This project demonstrates a complete end-to-end machine learning pipeline — from data preprocessing and model training to model optimization, deployment with FastAPI, and a modern React frontend. It serves as a practical example of applying Deep Learning to a real-world regression problem while following production-ready practices.

---

* ## Features

- **Deep Learning Model**: Custom PyTorch MLP for house price regression
- **Advanced Preprocessing**: Handling missing values, ordinal encoding, and robust scaling
- **Target Transformation**: Log transformation (`log1p`) to handle heavy right-skewed price distribution
- **Hyperparameter Tuning**: Optuna-based optimization of network architecture and learning parameters
- **Model Optimization**: TorchScript compilation for faster inference
- **REST API**: FastAPI backend with proper input validation (Pydantic)
- **Modern Frontend**: React + Vite interface for easy interaction
- **Production Ready**: Model + Preprocessor saved and loaded efficiently

---

* ## Techniques Used

| Technique                        | Purpose                                      |
|----------------------------------|----------------------------------------------|
| Log Transformation (`log1p`)     | Handle highly skewed target variable         |
| RobustScaler                     | Scale numerical features (outlier resistant) |
| OrdinalEncoder                   | Encode ordered categorical features          |
| SimpleImputer                    | Handle missing values                        |
| ColumnTransformer                | Apply different preprocessing to different columns |
| Optuna                           | Hyperparameter optimization                  |
| TorchScript                      | Model compilation & optimization for inference |
| FastAPI + Pydantic               | High-performance API with data validation    |
| React + Vite                     | Modern, fast frontend                        |

---

* ## Tech Stack

**Backend**
- Python 3.10+
- PyTorch
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- Optuna

**Frontend**
- React
- Vite
- Axios
- Lucide React (icons)

---

* ## Project Structure

```text
House_Price_Prediction_MLP/
├── model/
│   ├── housing_mlp_scripted.pt
│   └── preprocessing.pkl
├── models/
│   └── predict.py
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
├── app.py
├── requirements.txt
└── house-price-frontend/          # React frontend
