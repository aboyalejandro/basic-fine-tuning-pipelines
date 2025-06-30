#!/usr/bin/env python3
"""
Simplified OpenAI client for demo
"""

import logging
from openai import OpenAI
from src.config import OPENAI_API_KEY

logger = logging.getLogger(__name__)


class OpenAIClient:
    """Simple OpenAI client for demo."""

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def upload_and_create_job(self, file_path: str) -> tuple:
        """Upload file and create fine-tuning job in one step."""
        if not self.client:
            logger.warning("No OpenAI API key found")
            return None, None

        try:
            # Upload file
            logger.info("Uploading training data...")
            with open(file_path, "rb") as f:
                file_response = self.client.files.create(file=f, purpose="fine-tune")

            file_id = file_response.id
            logger.info(f"✅ File uploaded: {file_id}")

            # Create job
            logger.info("Creating fine-tuning job...")
            job_response = self.client.fine_tuning.jobs.create(
                training_file=file_id, model="gpt-4.1-mini-2025-04-14"
            )

            job_id = job_response.id
            logger.info(f"🚀 Job created: {job_id}")

            return file_id, job_id

        except Exception as e:
            logger.error(f"OpenAI operation failed: {e}")
            return None, None

    def is_available(self) -> bool:
        """Check if client is ready."""
        return self.client is not None
