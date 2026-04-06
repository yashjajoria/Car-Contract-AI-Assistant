# Car Contract AI Assistant 🚗📄

A production-oriented AI system that automates analysis of vehicle lease agreements. It combines OCR, a local Large Language Model (LLaMA 3 via Ollama), and VIN validation to turn unstructured contract documents into structured insights you can act on.

## Why this project 🔍

- Convert scanned or digital lease contracts into readable text (OCR)
- Extract key lease terms and obligations with LLM-assisted analysis
- Flag risky/ambiguous clauses and propose negotiation-friendly improvements
- Validate extracted VINs via the official NHTSA VIN Decoder API

---

## Key Features ✅

- **Document ingestion:** PDF, JPG, PNG
- **OCR pipeline:** `pdfplumber` + `pdf2image` + `pytesseract`
- **Contract intelligence:**
  - Summarization
  - Key info extraction (lease duration, payment terms, obligations)
  - Risky/ambiguous clause detection
  - Suggestions for improvements and negotiation
- **VIN extraction & validation:** NHTSA VIN Decoder API
- **Conversational assistant:** LLaMA 3 via **Ollama** (local LLM)
- **Web UI:** Streamlit-based interface

---

## Tech Stack 🧰

- **Language:** Python
- **UI:** Streamlit
- **LLM Runtime:** Ollama (LLaMA 3)
- **OCR:** pdfplumber, pdf2image, pytesseract
- **External API:** NHTSA VIN Decoder

---

## Project Structure 🗂️

```text
.
├── app.py              # Streamlit UI
├── ocr_pipeline.py     # OCR + document text extraction
├── llm_analysis.py     # Summarization, extraction, risk detection, suggestions
├── chatbot.py          # Conversational assistant (LLaMA 3 via Ollama)
├── vin_api.py          # VIN extraction + NHTSA VIN Decoder integration
└── requirements.txt    # Python dependencies
```

---

## Getting Started ⚙️

### Prerequisites

- **Python 3.10+** recommended
- **Tesseract OCR** installed and available on PATH
- **Ollama** installed and running locally

> Note: Some OCR dependencies (e.g., `pdf2image`) may require system packages such as `poppler`.

### Installation

```bash
# 1) Clone the repository
git clone https://github.com/yashjajoria/Car-Contract-AI-Assistant.git
cd Car-Contract-AI-Assistant

# 2) Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install Python dependencies
pip install -r requirements.txt
```

### Set up Ollama (LLaMA 3)

```bash
# Install Ollama (see official Ollama docs), then pull LLaMA 3
ollama pull llama3

# Ensure Ollama server is running
ollama serve
```

---

## Run the App ▶️

```bash
streamlit run app.py
```

Then open the local URL printed in your terminal (typically `http://localhost:8501`).

---

## How It Works 🧠

- **Step 1 — Upload:** Provide a lease contract (PDF/JPG/PNG)
- **Step 2 — OCR/Text extraction:** Extract text using `pdfplumber` / `pdf2image` + `pytesseract`
- **Step 3 — LLM analysis:** Summarize, extract terms, detect risks, and generate suggestions
- **Step 4 — VIN validation:** Extract VIN and verify details via NHTSA VIN Decoder
- **Step 5 — Chat:** Ask follow-up questions using a local LLaMA 3 chatbot

---

## Project Status 📌

| Area | Status | Notes |
|------|--------|-------|
| OCR pipeline | ✅ Implemented | Handles PDFs and images |
| Contract summarization/extraction | ✅ Implemented | LLM-assisted analysis |
| Risk & ambiguity detection | ✅ Implemented | Flags potentially problematic terms |
| Negotiation suggestions | ✅ Implemented | Improvement recommendations |
| VIN validation (NHTSA) | ✅ Implemented | VIN decode/verification |
| Streamlit UI | ✅ Implemented | End-to-end workflow |
| Tests & CI | 🟡 Planned | Add unit tests and GitHub Actions |
| Deployment | 🟡 Planned | Containerization + hosting options |

---

## Roadmap 🛣️

- Add **unit/integration tests** (OCR, VIN API, LLM prompts)
- Improve **clause-level citation** (link extracted claims to page/line references)
- Add **evaluation harness** for extraction accuracy (golden dataset)
- Provide **configurable risk policy** (thresholds, categories, compliance rules)
- Add **export formats** (JSON, CSV, annotated PDF)
- Support additional LLM backends (optional cloud model integration)
- Package as a Docker image for reproducible deployments

---

## Notes on Safety & Privacy 🔒

- Designed to run with a **local LLM** (Ollama) to keep documents on-device.
- Always validate outputs for legal/financial decisions.

---

## License 📄

Add a license file (e.g., MIT) if you plan to open-source this project.

---

## Contact

For questions or collaboration, open an issue in this repository.