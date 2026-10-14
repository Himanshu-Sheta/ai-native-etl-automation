# 🤖 AI-Native ETL Automation Platform

[![Python](https://img.shields.io/badge/Python-FastAPI-009688?logo=python&logoColor=white)](https://fastapi.tiangolo.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-Client_SDK-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

An enterprise-ready **AI-Native Data Pipeline Engine** featuring **Python FastAPI** backend services and a typed **TypeScript Client SDK**. Designed for automated ingestion, schema transformation, statistical anomaly detection, and LLM-assisted data harmonization.

---

## 🏗️ Architecture

```text
┌────────────────────────────┐
│   TypeScript Client SDK    │  -> Client Applications / React / Next.js
└─────────────┬──────────────┘
              │ (REST / JSON)
              ▼
┌────────────────────────────┐
│   FastAPI Gateway          │  -> Pydantic Request Validation & Auth
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│  Pandas Transformation Core│  -> Data Normalization, Type Casting
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│  Statistical & Anomaly     │  -> IQR Outlier Flagging & Rule Enforcement
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│  AI Semantic Synthesis     │  -> Structured Reasoning Summary & Imputation
└────────────────────────────┘
```

---

## ⚡ Tech Stack

* **Backend:** Python 3.10+, FastAPI, Pydantic v2, Pandas, NumPy, Scikit-learn
* **Frontend / Client SDK:** TypeScript 5.0+, Fetch API, ES2022
* **Testing:** Pytest, TypeScript Compiler (`tsc`)

---

## 🚀 Getting Started

### 1. Run Python Backend
```bash
pip install -r requirements.txt
uvicorn backend.server:app --reload --port 8000
```
Interactive Swagger API documentation will be available at: `http://localhost:8000/docs`.

### 2. Build TypeScript SDK
```bash
npm install
npm run build
```

---

## 👨‍💻 Author
**Himanshu Sheta**  
M.Sc. Applied Computer Science — Technische Hochschule Deggendorf  
LinkedIn: [linkedin.com/in/himanshu-sheta](https://www.linkedin.com/in/himanshu-sheta)
