import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# ── Load Model ─────────────────────────────────────────
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# ── Define App ─────────────────────────────────────────
app = FastAPI(
    title="House Price Prediction API",
    description="Predicts California house prices using Linear Regression",
    version="1.0.0"
)

# ── Define Input Format ────────────────────────────────
class HouseFeatures(BaseModel):
    MedInc: float        # Median income
    HouseAge: float      # House age
    AveRooms: float      # Average rooms
    AveBedrms: float     # Average bedrooms
    Population: float    # Population
    AveOccup: float      # Average occupancy
    Latitude: float      # Latitude
    Longitude: float     # Longitude

# ── Endpoints ──────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "House Price Prediction API is running! 🏠"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(features: HouseFeatures):
    # Convert input to array
    data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]])
    
    # Make prediction
    prediction = model.predict(data)
    
    return {
        "predicted_price": round(float(prediction[0]), 2),
        "unit": "100,000 USD",
        "note": "Multiply by 100,000 to get the actual price in USD"
    }