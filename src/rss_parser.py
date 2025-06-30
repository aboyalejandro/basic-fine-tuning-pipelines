#!/usr/bin/env python3
"""
Simplified RSS parser for demo
"""

import logging
from typing import List, Dict, Any
import feedparser
from src.content_processor import ContentProcessor
from src.config import SUBSTACK_RSS_URL

logger = logging.getLogger(__name__)


class RSSParser:
    """Simple RSS feed parser for demo."""

    def __init__(self):
        self.content_processor = ContentProcessor()

    def parse_feed(self, rss_url: str = SUBSTACK_RSS_URL) -> List[Dict[str, Any]]:
        """Parse RSS feed and extract essential article data."""
        logger.info(f"Parsing RSS feed: {rss_url}")

        try:
            feed = feedparser.parse(rss_url)
            articles = []

            for entry in feed.entries:
                article = self._process_entry(entry)
                if article:  # Only add if content exists
                    articles.append(article)

            logger.info(f"Successfully parsed {len(articles)} articles")
            return articles

        except Exception as e:
            logger.error(f"Error parsing RSS feed: {str(e)}")
            return []

    def _process_entry(self, entry) -> Dict[str, Any]:
        """Process entry with just essential fields."""
        # Get content
        raw_content = ""
        if hasattr(entry, "content") and entry.content:
            raw_content = entry.content[0].value
        elif hasattr(entry, "summary"):
            raw_content = entry.summary

        # Clean content
        cleaned_content = self.content_processor.clean_html_content(raw_content)

        # Skip if too short
        if len(cleaned_content.split()) < 50:
            return None

        return {
            "title": entry.title,
            "content": cleaned_content,
            "link": entry.link,
        }
