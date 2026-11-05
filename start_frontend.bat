@echo off
cd /d "%~dp0"
echo Starting MixSense Streamlit Dashboard on http://localhost:8501 ...
python run_frontend.py
pause
