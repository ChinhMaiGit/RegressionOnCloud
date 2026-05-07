# Regression On Cloud

## 📖 About This Project

This project demonstrates how to take a simple machine learning model and turn it into a fully working web service that anyone can use. It uses a basic **Linear Regression** model trained on the California Housing dataset to predict house prices.

The focus is **not** on building the model itself (that part is already done for you). Instead, the project shows the **software development and deployment** steps that real companies use to make machine learning models usable in the real world.

### Business Perspective
Companies often have valuable historical data but need a practical way to let other teams or applications use the predictions. This project shows the complete journey:
- From data → a smart prediction engine
- From prediction engine → a simple web service (API)
- From web service → a reliable, portable application that can run anywhere

Once you understand these deployment steps, you can apply them to any model (Random Forest, XGBoost, neural networks, etc.).

## 🚀 The End-to-End Workflow

Here is the standard industry process this project follows. Each phase includes a simple explanation of **what happens** and **why it matters** for business.

1. **Train the Machine Learning Model**  
   The computer studies historical data and creates a file that contains the “learned” rules for making predictions.  
   **Business intuition**: This turns past information into a reusable tool for faster, more consistent decisions.

2. **Build a REST API**  
   The trained model is placed inside a small web service that can receive requests and send back answers over the internet.  
   **Business intuition**: Other programs or websites can now ask for predictions without needing to understand or install the model.

3. **Containerize the Application with Docker**  
   Everything needed to run the service (code, model, libraries, and settings) is packed into one standardized “box” called a container.  
   **Business intuition**: This box works exactly the same way on any computer, server, or cloud platform — removing the common problem of “it works on my machine but not yours.”

4. **Version Control & Share via GitHub**  
   All files are stored in an organized project on GitHub.  
   **Business intuition**: Teams can collaborate, track changes, and easily share or reuse the work.

The sections below explain **exactly how to perform each step**, with every command described in plain English.

## 🛠️ Prerequisites

You only need four tools. Each one supports a specific part of the workflow:

- **[Python](https://www.python.org/downloads/)** – The general-purpose language used to write the code.
- **[uv](https://github.com/astral-sh/uv)** – A fast, modern tool that manages all the small helper libraries your project needs (think of it as an intelligent shopping list and delivery service for Python tools).
- **[Git](https://git-scm.com/downloads)** – The standard system for tracking changes to your files (like a detailed version history for your project).
- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** – The industry-standard tool that creates and runs the “container box” mentioned in Step 3 above.

## ⚙️ Step-by-Step Implementation

### 1. Clone the Repository (Workflow Step 4)
```bash
git clone https://github.com/ChinhMaiGit/RegressionOnCloud
cd RegressionOnCloud
```
**What this does**: Downloads the complete project folder from GitHub onto your computer and moves you inside it.  
**Why**: This gives you everything you need to follow the rest of the workflow.

### 2. Set Up the Environment
```bash
uv sync
```
**What this does**: `uv` reads the list of required libraries in `pyproject.toml` and installs exactly the right versions into an isolated environment for this project.  
**Why**: It guarantees that everyone who works on the project uses the same tools, so nothing breaks due to version differences.

### 3. Train the Model (Workflow Step 1)
```bash
uv run python train.py
```
**What this does**: 
- `uv run` tells `uv` to use the exact environment we just set up.
- `python train.py` runs the training script.  
**Why**: This creates the file `model.pkl` — the actual prediction engine that will be used by the API.

### 4. Run the API Locally (Workflow Step 2)
```bash
uv run uvicorn app:app --reload
```
**What this does**:
- `uv run` again uses the correct environment.
- `uvicorn` is a fast web server that runs your FastAPI application.
- `app:app` tells uvicorn which file (`app.py`) and which object inside it (`app`) to start.
- `--reload` automatically restarts the server whenever you edit the code (very convenient during development).

The service will be available at `http://localhost:8000`.

**How the API works (no programming background needed)**:  
Think of the API as a restaurant waiter. You send a request (the order) containing house details, and the waiter (API) quickly returns an answer (the predicted price). You do not need to know how the kitchen (model) works — you just communicate through the waiter.

**Useful URLs** (open these in your browser):
- `http://localhost:8000` – Confirms the service is running.
- `http://localhost:8000/health` – Simple health check.
- `http://localhost:8000/docs` – Interactive page where you can test the API without writing code.

### 5. Test a Prediction
On the `/docs` page, click the `/predict` section and try the sample input below:

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

**Expected response**:
```json
{
    "predicted_price": 4.13,
    "unit": "100,000 USD",
    "note": "Multiply by 100,000 to get the actual price in USD"
}
```

This shows the API receiving data and returning a prediction.

### 6. Build and Run with Docker (Workflow Step 3)
```bash
# 1. Build the container
docker build -t house-price-model .

# 2. Run the container
docker run -p 8000:8000 house-price-model
```

**What these commands do**:
- `docker build ...` reads the `Dockerfile` and creates the standardized container (the “box”) that contains everything needed.
- `docker run ...` starts the container and maps port 8000 on your computer to port 8000 inside the box.

**Why Docker?** Once built, this container can be moved to any server or cloud provider and will run exactly the same way — no surprises.

Open `http://localhost:8000` again to confirm the service is now running inside the Docker container.

## 🔢 Communication with the API through Terminal

You can also fetch the data from the API using Terminal: 


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


## 📁 Project Structure

```
RegressionOnCloud/
│
├── app.py              ← Contains the API (Step 2)
├── train.py            ← Trains the model (Step 1)
├── Dockerfile          ← Instructions for building the container (Step 3)
├── pyproject.toml      ← List of required libraries
├── uv.lock             ← Exact versions of libraries
├── .gitignore
├── .dockerignore
└── README.md
```

## 🛠️ Tech Stack

| Tool          | Purpose                                      | Workflow Phase |
|---------------|----------------------------------------------|----------------|
| Python        | Programming language                         | All            |
| Scikit-learn  | Creates the linear regression model          | Step 1         |
| FastAPI       | Builds the web API                           | Step 2         |
| uvicorn       | Runs the web server                          | Step 2         |
| uv            | Manages Python libraries                     | Setup          |
| Docker        | Creates portable containers                  | Step 3         |
| Git           | Version control                              | Step 4         |


