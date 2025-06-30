#!/usr/bin/env python3
"""
Demo: Substack Fine-Tuning Data Processor

Simplified modular version that:
1. Parses RSS feed
2. Cleans content
3. Generates training data
4. Uploads to OpenAI
"""

import logging
from src.substack_processor import SubstackProcessor

# Simple logging setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main():
    """Main execution function."""
    processor = SubstackProcessor()
    processor.process_all()


if __name__ == "__main__":
    main()
