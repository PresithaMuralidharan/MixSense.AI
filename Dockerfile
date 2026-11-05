# Multi-stage lightweight Python runtime for MixSense
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies including audio and OCR libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
    tesseract-ocr \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose FastAPI (8000) and Streamlit (8501) ports
EXPOSE 8000 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8000/api/health || exit 1

# Default command: launch both backend and frontend
CMD ["sh", "-c", "uvicorn app.backend.main:app --host 0.0.0.0 --port 8000 & streamlit run app/frontend/Home.py --server.port 8501 --server.address 0.0.0.0"]
