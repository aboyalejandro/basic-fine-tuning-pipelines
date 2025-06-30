#!/usr/bin/env python3
"""
Generic Substack Fine-Tuning Data Processor

A modular tool that processes articles from any Substack to create
training data for OpenAI fine-tuning:

1. Parses RSS feed from any Substack
2. Cleans content
3. Generates diverse training examples
4. Uploads to OpenAI for fine-tuning
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
