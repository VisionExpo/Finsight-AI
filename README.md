# 📈 ArthaQuant

## Multimodal AI Trading Intelligence & Paper-Trading Research Platform

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-blue?style=flat)
![Status](https://img.shields.io/badge/status-active-success?style=flat)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat\&logo=python\&logoColor=white)
![DeepLearning](https://img.shields.io/badge/Deep%20Learning-PyTorch-red?style=flat\&logo=pytorch\&logoColor=white)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat\&logo=fastapi\&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat\&logo=streamlit\&logoColor=white)
![MLOps](https://img.shields.io/badge/MLOps-W%26B%20%7C%20DVC-orange?style=flat)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat\&logo=docker\&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

</div>

---

## 📌 Overview

**ArthaQuant** is a **research-grade, production-oriented AI trading intelligence platform** designed to demonstrate how **modern quantitative trading systems are architected, evaluated, and monitored** — *safely*, using **paper trading only**.

It bridges the gap between:

> **financial intuition → multimodal machine learning → production-grade AI systems**

Unlike traditional trading bots or notebook-based backtests, ArthaQuant focuses on **system behavior**, **risk awareness**, **model accountability**, and **end-to-end MLOps discipline**.

> ⚠️ ArthaQuant does **not** execute real trades and does **not** provide financial advice.

---

## 🎯 Why ArthaQuant?

### ❌ The Problem

Most algorithmic trading projects and platforms:

* Optimize for **historical backtest performance**
* Ignore **distribution shift and regime change**
* Treat ML models as **static black boxes**
* Separate research code from production systems
* Lack observability once deployed

As a result, models appear strong in isolation — and silently fail in real-world conditions.

---

### ✅ The Philosophy

**ArthaQuant is built as a system, not a strategy.**

It emphasizes:

* **Multimodal intelligence** (price + news sentiment)
* **Probabilistic decision making** (confidence & uncertainty)
* **Realistic execution simulation** (paper trading)
* **Continuous monitoring & drift detection**
* **Auditable, reproducible ML pipelines**

> **Core belief**
> *Predictions are meaningless without accountability and risk context.*

---

## 🧠 System Architecture

```
Streamlit Dashboard
│
├── Predictions & Signals
├── Paper Trading
├── Portfolio & Risk Analytics
├── Drift Monitoring
│
└── REST API (FastAPI)
↓
Backend Services
│
├── Inference Layer
│ ├── Market Transformer
│ ├── FinBERT Sentiment Encoder
│ └── Cross-Attention Fusion Model
│
├── Execution Layer
│ ├── Paper Trading Engine
│ ├── Portfolio State Manager
│ └── Risk Constraints
│
├── Analytics Layer
│ ├── Equity Curve
│ ├── Sharpe & Drawdown
│ └── Performance Reports
│
├── Monitoring Layer
│ ├── Drift Detection (KS-test)
│ └── Retraining Triggers
│
└── MLOps & Infra
    ├── Weights & Biases (experiments & artifacts)
    ├── DVC (data & model versioning)
    ├── Audit Logs (decision traceability)
    └── Docker / CI
```

---

## 🧬 Machine Learning Design

### 📈 Market Intelligence (Price Model)

* Transformer-based time-series model
* Learns temporal dependencies in OHLCV + indicators
* Outputs:

  * Probability of upward movement
  * Expected return
  * Uncertainty estimate

---

### 📰 Event Intelligence (Sentiment Model)

* FinBERT (financial domain-specific NLP)
* Processes news and textual signals
* Produces dense semantic embeddings (not naive labels)

---

### 🔗 Multimodal Fusion (Core Alpha)

* **Cross-attention architecture**
* Price embeddings act as **queries**
* Sentiment embeddings act as **context**
* Avoids naive feature concatenation
* Aligns with current multimodal financial ML research

---

## 📊 Trading Logic (Paper Trading Only)

ArthaQuant uses **probabilistic execution**, not rule-based BUY/SELL signals.

```
If P(up) > threshold and uncertainty < limit:
    Execute BUY (paper)
Else if P(down) > threshold:
    Execute SELL (paper)
Else:
    HOLD
```

Includes:

* Capital-aware position sizing
* Slippage & transaction cost simulation
* Cool-down and exposure constraints

📌 No real money. No broker integration.

---

## 💼 Paper Trading Engine

* Simulates realistic order execution
* Shared logic between:

  * Backtesting
  * Live paper trading
* Deterministic and replayable
* Portfolio tracks:

  * Cash
  * Positions
  * Trade history
  * PnL

---

## 📉 Portfolio Analytics

Risk-aware evaluation using:

* Equity curve
* Sharpe ratio
* Maximum drawdown
* Total return

Focus is on **risk behavior**, not profit claims.

---

## 🚨 Drift Detection & Model Health

ArthaQuant continuously monitors:

* Prediction distributions
* Confidence decay
* Regime shifts

Uses **statistical drift detection (KS-test)**.

Drift does **not** immediately redeploy models.
Instead, it triggers:

1. Evaluation
2. Controlled retraining
3. Validation
4. Gated model promotion

---

## 🔁 Automated Retraining (Safe & Auditable)

* Drift → retraining pipeline
* Retraining is:

  * Asynchronous
  * Versioned
  * Fully tracked
* Models are promoted **only if they outperform baselines**

This prevents silent degradation.

---

## 🧾 Audit Logs & Observability

Every critical event is logged:

* Predictions
* Paper trades
* Drift detection
* Retraining triggers

Audit logs are:

* Append-only
* Time-stamped
* Model-version aware

This enables **full decision traceability**.

---

## 🖥️ Dashboard (Streamlit)

Interactive UI for:

* Predictions
* Paper trading
* Portfolio state
* Risk analytics
* Drift monitoring

The frontend contains **no business logic** — it consumes APIs only.

---

## 🛠️ Tech Stack

### Core

* Python 3.10+

### AI / ML

* PyTorch
* Hugging Face Transformers
* FinBERT
* Transformer-based time-series models

### Application

* **Backend:** FastAPI, Uvicorn
* **Frontend:** Streamlit, Plotly

### MLOps & Infra

* Weights & Biases (experiments & artifacts)
* DVC (data & model versioning)
* Docker & Docker Compose
* Redis (infra support)

---

## 🔐 Safety, Ethics & Scope

* ✅ Paper trading only
* ❌ No real capital
* ❌ No broker integration
* ❌ No investment advice
* ❌ No profit guarantees
* ✅ Transparent evaluation
* ✅ Full auditability

ArthaQuant is designed for **education, research, and system demonstration**.

---

## 🗺️ Roadmap (Conservative by Design)

* Stress testing under extreme regimes
* Explainability research
* Robustness benchmarking

Not planned:

* Live trading
* Broker APIs
* Retail financial advice

---

## 👤 Who This Is For

* Recruiters evaluating **senior ML / AI engineers**
* Investors assessing **technical depth**
* Engineers interested in **real MLOps systems**
* Researchers exploring **multimodal financial ML**

---

## 🏁 Final Note

ArthaQuant is not about “beating the market”.

It is about demonstrating:

* How **real AI systems** are built
* How risk is managed
* How models are monitored
* How engineering discipline meets research

That is the real differentiator.

---

## 📜 License

MIT License
> If you like this project, ⭐ star the repo and join the journey.

<div align="center">
<sub>Built with ❤️ by Vishal Gorule</sub>
</div>
