from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  
from fastapi.responses import RedirectResponse, FileResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from Models.predict import predict_output, MODEL_VERSION, model

app = FastAPI(title="Near-Earth Object Hazard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Mount static directory to serve HTML, CSS, JS, and image assets
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root_redirect():
    # Automatically redirect root URL to index.html page
    return RedirectResponse(url="/static/index.html")

@app.get("/index.html")
def index_page():
    return FileResponse("static/index.html")

@app.get("/predict.html")
def predict_page():
    return FileResponse("static/predict.html")

@app.get("/rules.html")
def rules_page():
    return FileResponse("static/rules.html")

@app.post('/predict', response_model=PredictionResponse)
def predict_hazard(data: UserInput):
    if model is None:
        raise HTTPException(status_code=500, detail="PyTorch model is not loaded properly.")
    
    try:
        prediction_result = predict_output(data)
        return prediction_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'API_Version': '1.0',
        'Model_Version': MODEL_VERSION,
        'Model_loaded': model is not None 
    }