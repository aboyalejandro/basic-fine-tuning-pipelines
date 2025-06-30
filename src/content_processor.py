#!/usr/bin/env python3
"""
Generic content processing for any Substack
"""

import re


class ContentProcessor:
    """Generic content cleaning for any content type."""

    def clean_html_content(self, html_content: str) -> str:
        """Basic HTML cleaning and text extraction."""
        if not html_content:
            return ""

        # Remove HTML tags and clean up entities
        text = re.sub(r"<[^>]+>", "", html_content)
        text = text.replace("&nbsp;", " ").replace("&amp;", "&")
        text = text.replace("&lt;", "<").replace("&gt;", ">")
        text = text.replace("&quot;", '"').replace("&#39;", "'")
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def extract_key_topics(self, content: str) -> list:
        """Basic topic extraction - can be customized for specific domains."""
        # Generic topics that work across many content types
        basic_topics = ["technology", "business", "writing", "analysis", "insights"]
        content_lower = content.lower()

        found = [topic for topic in basic_topics if topic in content_lower]
        return found[:2] if found else ["writing", "analysis"]
