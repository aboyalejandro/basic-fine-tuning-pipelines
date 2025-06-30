#!/usr/bin/env python3
"""
Essential configuration for demo
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Essential settings only
SUBSTACK_RSS_URL = "https://thepipeandtheline.substack.com/feed"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Output file - use output directory if it exists (for Docker)
OUTPUT_DIR = "output" if os.path.exists("output") else "."
TRAINING_FILE = os.path.join(OUTPUT_DIR, "training_data.jsonl")
