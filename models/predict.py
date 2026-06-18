import torch
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
MODEL_PATH = BASE_DIR / "model" / "housing_mlp_scripted.pt"
PREPROCESSOR_PATH = BASE_DIR / "model" / "preprocessing.pkl"

MODEL_VERSION = "1.0.0"

scripted_model = None
preprocessor = None

def load_model():
    global scripted_model, preprocessor
    if scripted_model is None:
        scripted_model = torch.jit.load(str(MODEL_PATH), map_location='cpu')
        scripted_model.eval()
        preprocessor = joblib.load(str(PREPROCESSOR_PATH))
        print("✅ Model and Preprocessor loaded successfully!")
    return scripted_model


def predict_price(user_input: dict) -> dict:
    load_model()
    
    try:
        input_df = pd.DataFrame([user_input])
        X_processed = preprocessor.transform(input_df)
        
        X_tensor = torch.FloatTensor(X_processed)
        
        with torch.no_grad():
            y_pred_log = scripted_model(X_tensor)
            predicted_price = np.expm1(y_pred_log.item())
        
        return {
            "predicted_price": round(float(predicted_price), 2),
            "unit": "Lakh INR",
            "model_version": MODEL_VERSION,
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e), "status": "failed"}