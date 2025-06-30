# Generic Substack Fine-Tuning Data Processor

A modular tool that processes articles from **any Substack** to create high-quality training data for OpenAI fine-tuning. Simply provide your Substack RSS URL and OpenAI API key to generate instruction-response pairs optimized for fine-tuning.

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd finetuning-demo
```

### 2. Environment Variables
Create a `.env` file with your configuration:
```env
# Required: Your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here

# Required: Any Substack RSS feed URL
SUBSTACK_RSS_URL=https://yoursubstack.substack.com/feed

```

**Requirements:**
- OpenAI API key with GPT-4o mini access
- Valid Substack RSS feed URL

### 3. Run with Docker

```bash
# Create output directory
mkdir output

# Build the image
docker build -t substack-finetuner .

# Run the container
docker run --env-file .env -v $(pwd)/output:/app/output substack-finetuner
```

### 4. Run Locally (Alternative)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the processor
python main.py
```

## 📋 What It Does

1. **Parses RSS Feed** → Fetches articles from any Substack
2. **Cleans Content** → Removes HTML, extracts clean text
3. **Generates Instructions** → Uses GPT-4o mini to create diverse instruction prompts for each article
4. **Creates Training Data** → Builds instruction-response pairs in OpenAI format
5. **Saves Data** → Outputs `training_data.jsonl` in proper JSONL format
6. **Fine-tunes Model** → Automatically uploads to OpenAI and creates fine-tuning job

## 🎯 Use Cases

- **Personal Writing Style** - Train a model on your favorite author's style
- **Domain Expertise** - Create domain-specific models (tech, finance, etc.)
- **Content Creation** - Generate content similar to successful newsletters
- **Research** - Analyze writing patterns and generate similar content
- **Business Applications** - Create company-specific content generators

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

### Finding Substack RSS URLs

Most Substacks follow this pattern:
```
https://[substack-name].substack.com/feed
```

For custom domains, try:
```
https://[custom-domain]/feed
```

## 🔧 Customization

### Change Substack Source
Update your `.env` file:
```env
SUBSTACK_RSS_URL=https://newsubstack.substack.com/feed
```

### Modify Instruction Generation
Edit `src/instruction_generator.py` to customize how instructions are generated:
- Adjust prompt templates
- Change instruction diversity
- Modify content targeting

### Adjust Content Filtering
Modify `src/rss_parser.py` to change:
- Minimum article length (default: 50 words)
- Content extraction methods
- Quality filters

### Customize Output Format
Edit `src/file_manager.py` to modify:
- Output file naming
- JSONL formatting
- Additional metadata

## 🔍 Troubleshooting

### Common Issues:

**"No articles found"**
- Check if the RSS URL is valid and accessible
- Verify the Substack has published articles
- Try accessing the URL in a browser

**"No training data generated"**
- Verify your OpenAI API key is valid and has GPT-4o mini access
- Check if articles meet minimum length requirements (50+ words)
- Review API rate limits

**"Fine-tuning blocked by moderation"**
- Some content may violate OpenAI's usage policies
- Review the training data for potentially problematic content
- Consider using different source material

### File Issues:
- Ensure `output/` directory exists for Docker usage
- Check file permissions in the output directory
- Verify sufficient disk space for training data

## 🚀 Advanced Usage

### Batch Processing Multiple Substacks
```bash
# Process different Substacks sequentially
SUBSTACK_RSS_URL=https://first.substack.com/feed python main.py
SUBSTACK_RSS_URL=https://second.substack.com/feed python main.py
```

### Custom Training Data Pipeline
1. **Generate data** from multiple sources
2. **Combine datasets** manually 
3. **Upload combined** dataset to OpenAI
4. **Fine-tune** with larger, diverse dataset

## 📋 Requirements

- Python 3.8+
- OpenAI API access with GPT-4o mini
- Valid Substack RSS feed
- Docker (optional, for containerized usage)

## 🤝 Contributing

Feel free to:
- Add support for other content sources
- Improve instruction generation prompts
- Enhance content filtering
- Add new output formats

## 📄 License

This project is provided as-is for educational and research purposes.