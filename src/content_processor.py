#!/usr/bin/env python3
"""
Simplified content processing for demo
"""

import re


class ContentProcessor:
    """Simple content cleaning for demo."""

    def clean_html_content(self, html_content: str) -> str:
        """Basic HTML cleaning."""
        if not html_content:
            return ""

        # Simple HTML tag removal and basic entity cleanup
        text = re.sub(r"<[^>]+>", "", html_content)
        text = text.replace("&nbsp;", " ").replace("&amp;", "&")
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def extract_key_topics(self, content: str) -> list:
        """Simple topic extraction."""
        basic_topics = ["data engineering", "Python", "SQL", "career development"]
        content_lower = content.lower()

        found = [topic for topic in basic_topics if topic in content_lower]
        return found[:2] if found else ["data engineering", "career development"]
