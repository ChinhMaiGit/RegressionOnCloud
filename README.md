# 🏠 House Price Prediction Model

A simple **Linear Regression** model that predicts California house prices,
served through a **FastAPI** REST API and containerized with **Docker**.

---

## 🛠️ Prerequisites

Make sure you have these installed before starting:

- [Python](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) - Python package manager
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

## ⚙️ Installation

### 1. Install Git
```bash
# Windows
winget install --id Git.Git -e --source winget

# Mac
brew install git

# Linux
sudo apt install git
```

### 2. Install uv
```bash
pip install uv
```

### 3. Install Docker
```bash
# Windows
winget install --id Docker.DockerDesktop -e --source winget

# Mac
brew install --cask docker

# Linux
sudo apt install docker-ce
```

---

## 📥 Clone the Repository

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/house-price-model.git

# Navigate into it
cd house-price-model
```

---

## 📦 Set Up the Environment

```bash
# Install all dependencies
uv sync
```

---

## 🧠 Retrain the Model

Since the model file is not included in the repo,
you need to retrain it locally:

```bash
uv run python train.py
```

This will:
- Load the California housing dataset ✅
- Train the linear regression model ✅
- Save the model as `model.pkl` ✅

---

## ▶️ Run the API Locally

```bash
uv run uvicorn app:app --reload
```

Then open these URLs in your browser:

| URL | Description |
|-----|-------------|
| `http://localhost:8000` | API is running check |
| `http://localhost:8000/health` | Health check |
| `http://localhost:8000/docs` | Interactive API documentation |

---

## 🏠 Test a Prediction

Go to `http://localhost:8000/docs` and try this sample input
on the `/predict` endpoint:

```json
{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
}
```

Expected response:
```json
{
    "predicted_price": 4.13,
    "unit": "100,000 USD",
    "note": "Multiply by 100,000 to get the actual price in USD"
}
```

---

## 🐳 Build and Run Docker Image

### 1. Build the image
```bash
docker build -t house-price-model .
```

### 2. Run the container
```bash
docker run -p 8000:8000 house-price-model
```

### 3. Test it
Open `http://localhost:8000` in your browser ✅

---

## 📁 Project Structure

```
house-price-model/
│
├── .gitignore          ← files ignored by git
├── .dockerignore       ← files ignored by docker
├── app.py              ← FastAPI application
├── train.py            ← model training script
├── Dockerfile          ← docker instructions
├── pyproject.toml      ← dependencies
├── uv.lock             ← dependency lock file
└── README.md           ← you are here!
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| Scikit-learn | Linear regression model |
| FastAPI | REST API framework |
| uvicorn | ASGI server |
| uv | Package manager |
| Docker | Containerization |
| Git | Version control |
```

---

## 💾 Save and Push to GitHub

```bash
git add README.md
git commit -m "Add README with full setup instructions"
git push
```