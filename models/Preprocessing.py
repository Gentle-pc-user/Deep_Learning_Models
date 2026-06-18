# save_optimized_model.py  (or Preprocessing.py)

import torch
import torch.nn as nn
from pathlib import Path

class HousingMLP(nn.Module):
    def __init__(self, n_features, n_hidden1=128, n_hidden2=256, n_hidden3=104):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_features, n_hidden1),
            nn.ReLU(),
            nn.Linear(n_hidden1, n_hidden2),
            nn.ReLU(),
            nn.Linear(n_hidden2, n_hidden3),
            nn.ReLU(),
            nn.Linear(n_hidden3, 1)
        )
    
    def forward(self, X):
        return self.net(X)


def load_and_optimize_model(model_path='housing_mlp_best.pt'):
    # Load saved data
    loaded_data = torch.load(model_path, weights_only=True)
    
    hyperparams = loaded_data["model_hyperparameters"]
    model = HousingMLP(**hyperparams)
    model.load_state_dict(loaded_data["model_state_dict"])
    model.eval()
    
    print("✅ Model loaded successfully from state_dict")
    
    # ============== CREATE DIRECTORY ==============
    save_dir = Path("model")
    save_dir.mkdir(parents=True, exist_ok=True)   # ← This fixes the error
    
    # ============== COMPILE WITH TORCHSCRIPT ==============
    print("🔄 Compiling with TorchScript...")
    scripted_model = torch.jit.script(model)
    
    # Save optimized model
    scripted_path = save_dir / "housing_mlp_scripted.pt"
    scripted_model.save(str(scripted_path))
    print(f"✅ TorchScript model saved to: {scripted_path}")
    
    # Save hyperparameters
    hyperparams_path = save_dir / "hyperparams.pt"
    torch.save(hyperparams, hyperparams_path)
    print(f"✅ Hyperparameters saved to: {hyperparams_path}")
    
    return scripted_model


if __name__ == "__main__":
    load_and_optimize_model()