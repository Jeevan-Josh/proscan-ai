# ProScan-AI

ProScan-AI

Project overview
- This repository contains a small Python web app and support files. Use the `requirements.txt` in the root and the `ATS/` folder for the app code and templates.

Repository layout
- `main.py` — project entry (if present)
- `requirements.txt` — Python dependencies
- `ATS/` — application package (contains `app.py`, `templates/`, and `ATS.html`)
- `templates/` — top-level HTML templates used by the project
- `uploads/` — file upload storage

Quick start
1. Create and activate a virtual environment (Python 3.8+):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app (example entry points):

```powershell
python main.py
# or
python -m ATS.app
```

Notes
- Adjust commands above to match your environment and the actual entry point you use.
- If git commit fails due to missing user configuration, set local git user.name and user.email.

License
- Add a license file if you plan to make this public.
