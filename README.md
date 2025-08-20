# Fine-Tuning Pipeline For Your Substack Articles

A modular tool that processes articles from **any Substack** to create high-quality training data for OpenAI fine-tuning. Simply provide your Substack RSS URL and OpenAI API key to generate instruction-response pairs optimized for fine-tuning.

### This repo was created for [The Pipe & The Line](https://thepipeandtheline.substack.com/). 

## 🚀 Quick Start

### Environment Variables
Copy `.env.example` and rename it to  `.env` file with your configuration:
```env
# Required: Your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
SUBSTACK_RSS_URL=https://yoursubstack.substack.com/feed

```

**Requirements:**
- OpenAI API key with GPT-5 mini access
- Valid Substack RSS feed URL

### Run with Docker

```bash

# Build the image
docker build -t substack-finetuner .

# Run the container
docker run --env-file .env -v $(pwd)/output:/app/output substack-finetuner
```


## 📋 What It Does

1. **Parses RSS Feed** → Fetches articles from any Substack
2. **Cleans Content** → Removes HTML, extracts clean text
3. **Generates Instructions** → Uses GPT-5 mini to create diverse instruction prompts for each article
4. **Creates Training Data** → Builds instruction-response pairs in OpenAI format
5. **Saves Data** → Outputs `training_data.jsonl` in proper JSONL format
6. **Fine-tunes Model** → Automatically uploads to OpenAI and creates fine-tuning job
