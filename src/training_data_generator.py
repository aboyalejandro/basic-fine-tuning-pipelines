#!/usr/bin/env python3
"""
Enhanced training data generation using GPT-4o mini for instructions
"""

import logging
from typing import List, Dict, Any
from src.content_processor import ContentProcessor
from src.instruction_generator import InstructionGenerator

logger = logging.getLogger(__name__)


class TrainingDataGenerator:
    """Enhanced training data generation using GPT-4o mini."""

    def __init__(self):
        self.content_processor = ContentProcessor()
        self.instruction_generator = InstructionGenerator()

    def generate_training_data(
        self, articles: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Generate training data with GPT-4o mini generated instructions."""
        training_data = []

        for i, article in enumerate(articles):
            if len(article["content"].split()) < 50:  # Skip short articles
                continue

            logger.info(
                f"Generating instructions for article {i+1}/{len(articles)}: {article['title'][:50]}..."
            )

            # Generate custom instructions for this specific article
            instructions = self.instruction_generator.generate_instructions(
                article["title"], article["content"]
            )

            # Skip articles where no instructions were generated
            if not instructions:
                logger.warning(
                    f"Skipping article '{article['title'][:50]}...' - no instructions generated"
                )
                continue

            for instruction in instructions:
                training_data.append(
                    {
                        "messages": [
                            {"role": "user", "content": instruction},
                            {"role": "assistant", "content": article["content"]},
                        ]
                    }
                )

        logger.info(
            f"Generated {len(training_data)} training examples using GPT-4o mini instructions"
        )
        return training_data
