import os
from pathlib import Path
from app import app
from dotenv import load_dotenv

dotenv_path = Path('.')
load_dotenv(dotenv_path)

PORT = os.getenv('PORT')

app.run(port=PORT, debug=True)
