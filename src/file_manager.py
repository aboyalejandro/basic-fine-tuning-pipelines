#!/usr/bin/env python3
"""
Simplified file management for demo
"""

import json
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class FileManager:
    """Simple file operations for demo."""

    def save_training_data(
        self, training_data: List[Dict[str, Any]], filename: str = "training_data.jsonl"
    ) -> None:
        """Save training data in JSONL format."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for example in training_data:
                    json.dump(example, f, ensure_ascii=False)
                    f.write("\n")
            logger.info(f"💾 Saved {len(training_data)} examples to {filename}")
        except Exception as e:
            logger.error(f"Error saving training data: {e}")
