from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from schema.user_input import HouseInput
from models.predict import predict_price, MODEL_VERSION, load_model   # ← Make sure this import works

app = FastAPI(title="Bengaluru House Price API", version=MODEL_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    load_model()
    print("✅ Model loaded successfully at startup!")

@app.post("/predict")
def predict_house_price(data: HouseInput):
    try:
        user_input = data.model_dump()
        result = predict_price(user_input)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/")
def home():
    return {"message": "🏠 Bengaluru House Price Prediction API is running!"}

@app.get("/health")
def health_check():
    return {"status": "OK", "version": MODEL_VERSION}

@app.post("/predict")
def predict_house_price(data: HouseInput):
    try:
        user_input = data.model_dump()
        result = predict_price(user_input)
        return result
    except Exception as e:
        print("Validation/Prediction Error:", str(e))   # For debugging
        return {"error": str(e), "status": "failed"}