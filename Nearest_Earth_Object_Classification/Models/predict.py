import torch
import torch.nn as nn
from schema.user_input import UserInput

class NearestEarthObjClassification(nn.Module):
    def __init__(self, n_inputs, n_hidden1, n_hidden2, n_hidden3, n_classes):
        super().__init__()
        self.DNN = nn.Sequential(
            nn.Linear(n_inputs, n_hidden1),
            nn.ReLU(),
            nn.Linear(n_hidden1, n_hidden2),
            nn.ReLU(),
            nn.Linear(n_hidden2, n_hidden3),
            nn.ReLU(),
            nn.Linear(n_hidden3, n_classes)
        )
    def forward(self, X):
        return self.DNN(X)

MODEL_VERSION = '1.0.0'
model = None

# Load the model globally so it only initializes once upon server startup
try:
    loaded_data = torch.load("Models/Nearest_Earth_Objects_CLS.pt", weights_only=True)
    # Ensure these keys match exactly what you saved in your notebook
    hyperparams = loaded_data.get("model_hyperparameters") 
    
    model = NearestEarthObjClassification(**hyperparams)
    model.load_state_dict(loaded_data["model_state_dict"])
    model.eval() # Set to evaluation mode
except Exception as e:
    print(f"Failed to load PyTorch model: {e}")

def predict_output(user_input: UserInput) -> dict:
    # 1. Extract features and convert to PyTorch Tensor
    features = user_input.to_tensor_list()
    # Shape becomes [1, n_features] indicating batch_size=1
    input_tensor = torch.tensor([features], dtype=torch.float32)

    # 2. Perform inference without tracking gradients (saves memory/time)
    with torch.no_grad():
        logits = model(input_tensor)
        
    # 3. Apply Sigmoid to convert logits into a probability score (0 to 1)
    probability = torch.sigmoid(logits).item()
    
    # 4. Threshold at 0.5 for the boolean class prediction
    predicted_class = bool(probability >= 0.5)

    return {
        "predicted_category": predicted_class,
        "probability": round(probability, 4)
    }