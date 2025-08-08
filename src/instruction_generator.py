#!/usr/bin/env python3
"""
GPT-4o mini powered instruction generation for any content type
"""

import logging
from typing import List
from openai import OpenAI
from src.config import OPENAI_API_KEY

logger = logging.getLogger(__name__)


class InstructionGenerator:
    """Generate diverse instructions using GPT-4o mini for any content type."""

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def generate_instructions(
        self, article_title: str, article_content: str
    ) -> List[str]:
        """Generate diverse instruction prompts for an article using GPT-4o mini."""
        if not self.client:
            logger.error("No OpenAI API key found - cannot generate instructions")
            return []

        try:
            # Extract key topics from the article
            content_preview = (
                article_content[:500] + "..."
                if len(article_content) > 500
                else article_content
            )

            prompt = f"""
Based on this article titled "{article_title}":

{content_preview}

Generate 3 diverse instruction prompts that would lead someone to write content similar to this article. Each instruction should:
- Be specific and actionable
- Target different aspects (explanation, analysis, practical advice)
- Match the style and domain of the original content
- Be 10-20 words long

Return only the 3 instructions, one per line, without numbering or bullet points.
"""

            response = self.client.chat.completions.create(
                model="gpt-5-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                reasoning_effort="low",
            )

            instructions = response.choices[0].message.content.strip().split("\n")
            instructions = [inst.strip() for inst in instructions if inst.strip()]

            # Return up to 3 instructions, or empty list if none generated
            if len(instructions) >= 3:
                return instructions[:3]
            elif len(instructions) > 0:
                logger.warning(
                    f"Generated only {len(instructions)} instructions for '{article_title[:50]}...'"
                )
                return instructions
            else:
                logger.error(f"No instructions generated for '{article_title[:50]}...'")
                return []

        except Exception as e:
            logger.error(
                f"Error generating instructions for '{article_title[:50]}...': {e}"
            )
            return []

    def is_available(self) -> bool:
        """Check if instruction generation is available."""
        return self.client is not None
