<div align="center">
  <img src="house-price-frontend/public/BHP_Banner.png" alt="BHP Prediction Banner" width="100%">

* # Bengaluru House Price Prediction

A full-stack Deep Learning web application that predicts house prices in Bengaluru using a PyTorch Multi-Layer Perceptron (MLP) model.

**Live Repository:** [https://github.com/Gentle-pc-user/Deep_Learning_Models](https://github.com/ObsidianTwilight/Deep_Learning_Models)

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
```
* ## Setup Instructions
### 1. Clone the Repository
```bash
Bash
git clone https://github.com/Gentle-pc-user/Deep_Learning_Models.git
cd Deep_Learning_Models
```
### 2. Create & Activate Python Virtual Environment
Windows (PowerShell / CMD):
```bash
Bash
python -m venv .venv
.venv\Scripts\activate
```
macOS / Linux:
```bash
Bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install Backend Dependencies
```bash
BAsh
pip install -r requirements.txt
```
### 4. Run the FastAPI Backend
```bash
Bash
uvicorn app:app --reload
```
The API will be available at:
→ `http://127.0.0.1:8000`
→ `Interactive docs: http://127.0.0.1:8000/docs`

### 5. Setup & Run Frontend
```bash
Bash
cd house-price-frontend
npm install
npm run dev
```
Frontend will run at:
→ `http://localhost:5173`

* ## How to Use

1. Start the FastAPI backend
2. Start the React frontend
3. Fill in the house details (area type, location, size, society, total_sqft, bathrooms, balconies)
4. Click Predict House Price
5. Get the predicted price in Lakh INR

* ## Model Details

* Architecture: Fully connected MLP (n_features → 128 → 256 → 104 → 1)
* Loss Function: MSE (on log-transformed target)
* Optimizer: Tuned via Optuna (Adam / SGD / RMSprop)
* Target Transformation: np.log1p(price) during training → np.expm1() during inference
* Inference Optimization: TorchScript (torch.jit.script)

* ## Notes

* Make sure the files `model/housing_mlp_scripted.pt` and `model/preprocessing.pkl` are present before running the API.
* The preprocessing pipeline must match exactly what was used during training.
* Society is an optional field.

* ## License
This project is open-source and available under the `MIT` License.
