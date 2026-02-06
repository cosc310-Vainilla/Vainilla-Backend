
## Prerequisitesgit switch 
Make sure you have the following installed:

- Python **3.10 or higher**
- `pip`
- `git`

---

## Setup Instructions
### 1. Clone the repository

```bash
git clone https://github.com/cosc310-vainilla/Vainilla-Backend.git
cd Vainilla-Backend


2. Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

On Windows:
.venv\Scripts\activate


3. Install dependencies
pip install -r requirements.txt
Running the Application

From the root of the project, run:
uvicorn backend.app.main:app --reload

API Documentation
Once the server is running, open your browser and go to:
http://127.0.0.1:8000/docs

Notes:
The current implementation uses a CSV file as the data source (no database yet).
This structure is intentionally simple and designed for coursework and incremental extension.
The backend follows a clean separation of concerns to support future scaling.