import os
from pathlib import Path
from dotenv import load_dotenv
from flask_migrate import Migrate

from app import app

dotenv_path = Path('.')
load_dotenv(dotenv_path)

PORT = os.getenv('PORT')

if __name__ == '__main__':
    app.run(port=PORT, debug=True)
