# Regression On Cloud

## 📖 About This Project

This project is designed for **educational purposes** to demonstrate how to build
and deploy a complete machine learning pipeline from scratch. It is a great
starting point for anyone who wants to learn how to:

- 🧠 **Build a Machine Learning Model** - Train a simple Linear Regression model
  using Python and Scikit-learn on the California Housing dataset
- 🔌 **Build a REST API** - Wrap the model with FastAPI to create a clean and
  interactive API that others can use to make predictions
- 🐳 **Containerize with Docker** - Package the entire application into a Docker
  image so it can run consistently on any machine
- 🐙 **Deploy to GitHub** - Manage and share the project using Git and GitHub
  so others can clone, run, and build on top of it



## 🎯 What You Will Learn

By following this project, you will learn:

| Topic | What You Learn |
|-------|---------------|
| **Python** | Writing clean and structured Python code |
| **Scikit-learn** | Loading datasets, training and evaluating ML models |
| **FastAPI** | Building REST APIs with automatic documentation |
| **Docker** | Writing Dockerfiles and building container images |
| **Git & GitHub** | Version control and code sharing |
| **uv** | Modern Python package management |



## 💡 Why This Project?

Most machine learning tutorials stop at **training the model**. This project
goes beyond that and shows you the **full pipeline** that is used in the
real world:

```
Train Model → Save Model → Build API → Containerize → Deploy
```

Once you understand this pipeline with a simple **Linear Regression** model,
you can swap it with any other model such as:
- 🌲 Random Forest
- 📈 XGBoost
- 🧠 Neural Networks

The **Docker, API and GitHub** steps will remain exactly the same!



## 👥 Who Is This For?

This project is perfect for:
- 🎓 **Students** learning machine learning and software engineering
- 👨‍💻 **Developers** transitioning into machine learning
- 📊 **Data Scientists** who want to learn how to deploy their models
- 🤓 **Curious minds** who want to understand the full ML pipeline



## ⚠️ Disclaimer

The California Housing dataset used in this project is a well known
educational dataset. The predictions made by this model are for
**learning purposes only** and should not be used for real world
house price predictions.




## 🛠️ Prerequisites

Make sure you have these installed before starting:

- [Python](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) - Python package manager
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)



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



## 📥 Clone the Repository

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/PROJECT_NAME

# Navigate into it
cd PROJECT_NAME
```

Change `YOUR_USERNAME` and `PROJECT_NAME` to your corresponding github name and chosen project name, for this repo, the full link is:

`https://github.com/ChinhMaiGit/RegressionOnCloud`

## 📦 Set Up the Environment

```bash
# Install all dependencies
uv sync
```



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


## 🔢 Communication with the API through terminal

Here are a few ways to fetch data from the API using the terminal:



## 🔍 GET Requests

### Check if API is Running
```bash
# Windows (PowerShell)
Invoke-WebRequest -Uri "http://localhost:8000" -Method GET

# Mac/Linux
curl http://localhost:8000
```

### Health Check
```bash
# Windows (PowerShell)
Invoke-WebRequest -Uri "http://localhost:8000/health" -Method GET

# Mac/Linux
curl http://localhost:8000/health
```



## 🏠 POST Request - Get a Prediction

### 🪟 Windows (PowerShell)
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/predict" `
  -Method POST `
  -Headers @{"Content-Type" = "application/json"} `
  -Body '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'
```

### 🍎 Mac / 🐧 Linux
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'
```



## ✅ Expected Response

```json
{
    "predicted_price": 4.13,
    "unit": "100,000 USD",
    "note": "Multiply by 100,000 to get the actual price in USD"
}
```



## 💡 Bonus - Pretty Print the Response

### 🪟 Windows (PowerShell)
```powershell
# Install Python json tool if needed
Invoke-WebRequest -Uri "http://localhost:8000/predict" `
  -Method POST `
  -Headers @{"Content-Type" = "application/json"} `
  -Body '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
  }' | ConvertFrom-Json
```

### 🍎 Mac / 🐧 Linux
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
  }' | python -m json.tool
```

