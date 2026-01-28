# 📈 Finsight AI  
## Intelligent Quantitative Trading & Research Engine

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-blue?style=flat)
![Status](https://img.shields.io/badge/status-active-success?style=flat)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)
![DeepLearning](https://img.shields.io/badge/Deep%20Learning-PyTorch-red?style=flat&logo=pytorch&logoColor=white)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![MLOps](https://img.shields.io/badge/MLOps-MLflow%20%7C%20DVC-orange?style=flat)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

</div>

---

## 📌 Overview

**Finsight AI** is a **research-grade quantitative trading and portfolio intelligence platform** designed to bridge the gap between:

> **financial theory → machine learning research → production-grade trading systems**

Unlike traditional backtesting tools or signal generators, Finsight AI emphasizes **risk-first decision making, explainability, regime awareness, and reproducible research**, making it suitable for serious traders, quant researchers, and FinTech builders.

---

## 🎯 Why Finsight AI?

### ❌ The Problem

Most algorithmic trading platforms and GitHub projects:

- Rely on **overfitted historical backtests**
- Ignore **market regimes and tail risk**
- Treat ML models as **black boxes**
- Separate research notebooks from production systems
- Break when moved beyond toy examples

As a result, strategies appear profitable in theory — and fail in real market conditions.

---

### ✅ The Solution

**Finsight AI** is built as a **system**, not a script.

It introduces a modular, MLOps-enabled architecture that:

- Detects **market regimes** before strategy deployment  
- Combines **price action, sentiment, and macro signals**  
- Enforces **realistic execution constraints**  
- Tracks **data, experiments, and models** end-to-end  
- Explains *why* decisions are made — not just *what*  

> **Philosophy**  
> *Returns are meaningless without risk awareness.*

---

## 🧠 System Architecture
```
Streamlit Frontend
│
├── Portfolio Builder
├── Strategy Backtester
├── Risk & Performance Dashboard
│
└── REST / WebSocket API
↓
FastAPI Backend (Async)
│
├── Data Layer
│ ├── Market Data Ingestion
│ ├── News & Sentiment Feeds
│ └── Feature Engineering
│
├── Research Layer
│ ├── Strategy Lab
│ ├── Walk-Forward Validation
│ └── Regime Detection
│
├── Model Layer
│ ├── Time-Series Models
│ ├── NLP Sentiment Models
│ └── Portfolio Optimization
│
├── Execution Simulator
│ ├── Slippage & Fees
│ ├── Latency Modeling
│ └── Risk Constraints
│
└── MLOps Layer
├── MLflow (experiments & models)
├── DVC (data versioning)
└── Evidently AI (monitoring)
```

---

## ✨ Core Capabilities

### 📊 AI-Driven Portfolio Construction
- Mean-Variance & Black–Litterman
- Hierarchical Risk Parity (HRP)
- CVaR & drawdown-constrained optimization

### 🔁 Advanced Backtesting
- Walk-forward analysis
- Purged K-Fold cross-validation
- Strategy stress testing

### 🧠 Market Regime Detection
- Volatility-based regimes
- Trend vs mean-reversion detection
- Strategy switching

### 📰 NLP-Based Sentiment Intelligence
- FinBERT-powered sentiment analysis
- News-driven alpha signals

### ⚠️ Risk-First Trading Logic
- Volatility targeting
- Max drawdown limits
- Kill-switch simulation

### 🔍 Explainable AI
- Feature attribution
- Risk contribution analysis
- Transparent signal rationale

---

## 🛠️ Tech Stack

### Core
- Python 3.10+

### AI / ML
- PyTorch
- Hugging Face Transformers
- FinBERT
- LSTM / Transformer / TFT models
- Scikit-learn

### Application
- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit, Plotly

### MLOps & DevOps
- Docker & Docker Compose
- MLflow
- DVC
- Evidently AI

---

## 📂 Project Structure
```
finsight/
├── backend/
│ ├── app/
│ │ ├── api/
│ │ ├── core/
│ │ ├── models/
│ │ └── services/
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/
│ ├── app/
│ │ ├── pages/
│ │ └── utils/
│ ├── Dockerfile
│ └── requirements.txt
│
├── ml_pipeline/
│ ├── experiments/
│ └── dvc.yaml
│
├── docker-compose.yml
└── README.md
```

---

## 💻 Installation

### Clone Repository
```bash
git clone https://github.com/your-username/finsight-ai.git
cd finsight-ai
```

### Environment Variables
Create .env:
```bash
PROJECT_NAME=Finsight
API_V1_STR=/api/v1
MLFLOW_TRACKING_URI=http://tracking_server:5000
```

### ▶️ Run Locally
```bash
docker-compose up --build
```
### Access
- Dashboard: http://localhost:8501

- API Docs: http://localhost:8000/docs

- MLflow: http://localhost:5000

## 🎮 Hardware & Performance

| Component | Spec           |
| --------- | -------------- |
| GPU       | RTX 4060 (8GB) |
| RAM       | 24 GB          |
| CPU       | i7 / Ryzen     |

> Optimized for consumer GPUs using quantization and batching.

## 🧪 Research Techniques Used

- Regime-aware modeling
- Walk-forward validation
- Multi-factor alpha
- NLP-based sentiment signals
- Risk parity optimization
- MLOps-driven experimentation

## 🗺️ Roadmap

- [ ] Real-time data ingestion
- [ ] Multi-modal alpha models
- [ ] Reinforcement learning for position sizing
- [ ] Paper trading environment
- [ ] Multi-portfolio support

## 🎯 Vision
Finsight AI aims to become an open quantitative research OS for building transparent, risk-aware trading systems grounded in financial reality.

## 🤝 Contributing
Contributions are welcome from researchers, traders, and engineers interested in:

- Quantitative finance
- Time-series ML
- Risk engineering
- MLOps systems

## 📜 License
MIT License

