# Generic Substack Fine-Tuning Data Processor

A modular tool that processes articles from **any Substack** to create high-quality training data for OpenAI fine-tuning. Simply provide your Substack RSS URL and OpenAI API key to generate instruction-response pairs optimized for fine-tuning.

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd finetuning-demo
```

### 2. Environment Variables
Copy `.env.example` and rename it to  `.env` file with your configuration:
```env
# Required: Your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
SUBSTACK_RSS_URL=https://yoursubstack.substack.com/feed

```

**Requirements:**
- OpenAI API key with GPT-4o mini access
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
3. **Generates Instructions** → Uses GPT-4o mini to create diverse instruction prompts for each article
4. **Creates Training Data** → Builds instruction-response pairs in OpenAI format
5. **Saves Data** → Outputs `training_data.jsonl` in proper JSONL format
6. **Fine-tunes Model** → Automatically uploads to OpenAI and creates fine-tuning job

## 📄 Output

The tool generates:
- **`training_data.jsonl`** - OpenAI fine-tuning format with instruction-response pairs
- **Console logs** - Processing status, file IDs, and job monitoring links

### Example Output:
```
INFO: 🚀 Starting Substack processing...
INFO: Parsing RSS feed: https://yoursubstack.substack.com/feed
INFO: Successfully parsed 25 articles
INFO: Generating instructions for article 1/25: Why AI Will Transform...
INFO: Generated 75 training examples using GPT-4o mini instructions
INFO: 💾 Saved 75 examples to training_data.jsonl
INFO: 📤 Uploading training data to OpenAI...
INFO: ✅ File uploaded: file-abc123
INFO: 🚀 Job created: ftjob-xyz789
INFO: 🎉 Success! Monitor at: https://platform.openai.com/finetune/ftjob-xyz789
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ Yes | `sk-...` |
| `SUBSTACK_RSS_URL` | Substack RSS feed URL | ✅ Yes | `https://example.substack.com/feed` |