import os
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

if __name__ == "__main__":
    app_path = PROJECT_ROOT / "app" / "frontend" / "Home.py"
    
    # Configure environment with project root on PYTHONPATH
    env = os.environ.copy()
    current_pypath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{PROJECT_ROOT}{os.pathsep}{current_pypath}" if current_pypath else str(PROJECT_ROOT)
    
    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(app_path),
            "--server.port",
            "8501"
        ],
        cwd=str(PROJECT_ROOT),
        env=env
    )
