from pathlib import Path
import os
from dotenv import load_dotenv

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# GitHub
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# API
GITHUB_API_URL = "https://api.github.com"

# Directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LOG_DIR = BASE_DIR / "logs"

# Dataset
OUTPUT_FILE = RAW_DATA_DIR / "repositories.csv"

# Search Criteria
SEARCH_QUERY = "language:Python stars:>=50 fork:false archived:false"

# Pagination
PER_PAGE = 100
MAX_REPOSITORIES = 300

# API Rate Limit Safety
REQUEST_DELAY = 1  # seconds