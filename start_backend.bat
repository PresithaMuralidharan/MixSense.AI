@echo off
cd /d "%~dp0"
echo Starting MixSense FastAPI Backend on http://localhost:8000 ...
python run_backend.py
pause
