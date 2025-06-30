#!/usr/bin/env python3
"""
Simplified main processor for demo
"""

import logging
from src.rss_parser import RSSParser
from src.training_data_generator import TrainingDataGenerator
from src.openai_client import OpenAIClient
from src.file_manager import FileManager
from src.config import TRAINING_FILE

logger = logging.getLogger(__name__)


class SubstackProcessor:
    """Simple processor for demo."""

    def __init__(self):
        self.rss_parser = RSSParser()
        self.training_generator = TrainingDataGenerator()
        self.openai_client = OpenAIClient()
        self.file_manager = FileManager()

    def process_all(self) -> None:
        """Streamlined processing pipeline."""
        logger.info("🚀 Starting demo processing...")

        # Parse articles
        articles = self.rss_parser.parse_feed()
        if not articles:
            logger.error("❌ No articles found")
            return

        # Generate training data
        training_data = self.training_generator.generate_training_data(articles)
        if not training_data:
            logger.error(
                "❌ No training data generated - check OpenAI API key and article processing"
            )
            return

        # Save training data
        self.file_manager.save_training_data(training_data, TRAINING_FILE)

        # Upload to OpenAI if available
        if self.openai_client.is_available():
            file_id, job_id = self.openai_client.upload_and_create_job(TRAINING_FILE)

            if job_id:
                logger.info(
                    f"🎉 Success! Monitor at: https://platform.openai.com/finetune/{job_id}"
                )
        else:
            logger.info("ℹ️  No API key - training data saved locally")

        logger.info("✅ Demo completed!")
