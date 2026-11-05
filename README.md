# MixSense: Multimodal NLP Intelligence System for Indian Code-Mixed Communication

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red.svg)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2+-orange.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**MixSense** is a multimodal intelligence system that analyzes code-mixed Indian communication across:
- **Tamil + English (Tanglish)**
- **Hindi + English (Hinglish)**
- **Malayalam + English (Manglish)**
- **Native Scripts** (Tamil, Devanagari, Malayalam) & **Romanized/Transliterated Text**

The application accepts **Text**, **Photo**, and **Audio** inputs and processes them all through a unified, shared NLP analysis pipeline.

---

## 🌟 Multimodal Input Architecture

All three input modes converge on the same core NLP intelligence pipeline:

1. **Text Analysis:** Direct input or pasted text with character counts and live model processing.
2. **Photo Analysis:** Drag-and-drop / upload images (JPG, JPEG, PNG, WebP), perform deep-learning OCR extraction, allow user correction of extracted text in an interactive editor, then execute shared NLP.
3. **Audio Analysis:** Record audio via browser microphone or upload audio files (WAV, MP3, M4A, WebM), transcribe speech, extract acoustic wave cues (RMS energy, vocal cadence), allow transcript editing, then execute shared NLP.

---

## 🏛️ 9-Page Application Structure

Every page serves a dedicated application function without marketing or introduction clutter:

- **Page 1: Overview Dashboard (`Home.py`):** Workspace summary with 3 input cards (Text, Photo, Audio), persistent analysis statistics, and recent activity audit.
- **Page 2: Text Analysis (`pages/1_Text_Analysis.py`):** Large text workspace, preset Tanglish/Hinglish/Manglish examples, language selector, token-level color badges, sentiment, 10-class emotion, intent, slang, and sarcasm predictions.
- **Page 3: Photo Analysis (`pages/2_Photo_Analysis.py`):** Image upload, OCR extraction engine status, editable text area for typo correction, and shared NLP results cards.
- **Page 4: Audio Analysis (`pages/3_Audio_Analysis.py`):** Browser microphone recording, audio player, speech transcription, acoustic vs semantic emotion separation, transcript editing, and shared NLP cards.
- **Page 5: Conversation Analysis (`pages/4_Conversation_Analysis.py`):** Multi-turn chat analyzer, emotion trajectory line chart, code-switching shift bars, and turn-by-turn linguistic breakdown.
- **Page 6: Code-Mix Fingerprint (`pages/5_Code_Mix_Fingerprint.py`):** 5D stylistic radar profile, language balance, and experimental sociolinguistic metrics (Translation Loss Score, Adaptation Score, Emotional Switching Index).
- **Page 7: Analysis History (`pages/6_Analysis_History.py`):** Search by text or record ID, multi-faceted filters (mode, sentiment, language), full record inspection modal, and delete records with confirmation.
- **Page 8: Model Analytics (`pages/7_Model_Analytics.py`):** Genuine classification benchmarks (Accuracy, Precision, Recall, Macro-F1), confusion matrix heatmaps, ablation study, and Power BI CSV export.
- **Page 9: Settings (`pages/8_Settings.py`):** Language defaults, theme selection, history retention policy, database purge with confirmation, privacy guarantees, and system diagnostics.

---

## 🚀 Windows & VS Code Local Setup

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13 installed
- Git installed
- *(Optional)* PostgreSQL 15+ if using external database (defaults to SQLite if unconfigured)

### 2. Clone and Setup Environment
Open PowerShell or VS Code Terminal:
```powershell
cd C:\Users\MURALIDHARAN\.gemini\antigravity-ide\scratch\MixSense
pip install -r requirements.txt
```

### 3. Launch Backend & Frontend

**Option A — Dual Terminal Execution:**
- **Terminal 1 (FastAPI Backend on port 8000):**
  ```powershell
  python run_backend.py
  ```
  *Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)*

- **Terminal 2 (Streamlit Frontend on port 8501):**
  ```powershell
  streamlit run app/frontend/Home.py --server.port 8501
  ```
  *Streamlit UI: [http://localhost:8501](http://localhost:8501)*

**Option B — Windows Batch Scripts:**
- Double-click `start_backend.bat`
- Double-click `start_frontend.bat`

---

## 🐳 Containerized Deployment (Docker Compose)

Launch the full stack with PostgreSQL in Docker:
```bash
docker-compose up --build
```
- Streamlit UI: `http://localhost:8501`
- FastAPI OpenAPI Docs: `http://localhost:8000/docs`
- PostgreSQL Port: `localhost:5432`

---

## 📡 REST API Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | Health status and multimodal hardware diagnostics |
| `POST` | `/api/analyze/text` | Full-spectrum NLP analysis for text input with persistence |
| `POST` | `/api/analyze/image` | Multipart image upload for OCR extraction & NLP execution |
| `POST` | `/api/analyze/audio` | Multipart audio upload for speech transcription & acoustics |
| `POST` | `/api/analyze/conversation` | Multi-turn conversational flow and emotion trajectory |
| `GET` | `/api/history` | Paginated and filtered historical analysis records |
| `GET` | `/api/history/{id}` | Detailed analysis record including token and switch arrays |
| `DELETE`| `/api/history/{id}` | Cascade deletion of a single analysis record |
| `GET` | `/api/history-stats` | Summary statistics based on actual stored database records |
| `GET` | `/api/model-performance` | Verified baseline vs transformer model benchmarks |

---

## 🧪 Automated Test Suite

Run the full pytest suite:
```powershell
python -m pytest tests/ -v
```
Tests cover:
- Text preprocessing & character normalization
- Token-level language detection (Tanglish, Hinglish, Manglish)
- Code-switching formulas & transitions
- Sentiment classification & aspect extraction
- 10-class emotion intensity scoring
- Slang & emoji registries
- Intent & sarcasm detection
- Multimodal OCR extraction & audio speech transcription
- Database persistence, filtering, cascade deletion, and stats aggregation
- FastAPI REST endpoints
