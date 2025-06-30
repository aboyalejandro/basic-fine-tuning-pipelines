#!/usr/bin/env python3
"""
Configuration for Substack Fine-Tuning Data Processor
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Substack configuration - configurable via environment variables
SUBSTACK_RSS_URL = os.getenv("SUBSTACK_RSS_URL", "https://example.substack.com/feed")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Output configuration
OUTPUT_DIR = "output" if os.path.exists("output") else "."
TRAINING_FILE = os.path.join(OUTPUT_DIR, "training_data.jsonl")
