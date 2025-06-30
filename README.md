# Substack Fine-Tuning Data Processor

A simplified, modular tool that processes articles from [The Pipe & The Line Substack](https://thepipeandtheline.substack.com) to create training data for OpenAI fine-tuning.

## 🚀 Quick Start with Docker

### 1. Clone and Setup
```bash
git clone <repository-url>
cd finetuning
```

### 2. Environment Variables
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

**⚠️ Required:** OpenAI API key with GPT-4o mini access

*Tip: Copy `.env.example` and update with your actual API key*

### 3. Run with Docker

**Docker Compose**
```bash
# Create output directory
mkdir output

# Build the image
docker build -t substack-finetuner .

# Run the container
docker run --env-file .env -v $(pwd)/output:/app/output substack-finetuner
```


## 📋 What It Does

1. **Parses RSS Feed** → Fetches articles from Substack
2. **Cleans Content** → Removes HTML, extracts text
3. **Generates Instructions** → Uses GPT-4o mini to create custom instruction prompts for each article
4. **Creates Training Data** → Builds instruction-response pairs optimized for fine-tuning
5. **Saves Data** → Outputs `training_data.jsonl`
6. **Fine-tunes Model** → Uploads to OpenAI and creates GPT-4o mini fine-tuning job

## 📄 Output

- **`training_data.jsonl`** - OpenAI fine-tuning format
- **Console logs** - File ID, Job ID, and monitoring link

### Example Output:
```
INFO: Parsed 25 articles
INFO: Generating instructions for article 1/25: Why Modern Data Stacks Are...
INFO: Generating instructions for article 2/25: The Future of Data Engineering...
WARNING: Skipping article 'Short Article Title...' - no instructions generated
INFO: Generated 72 training examples using GPT-4o mini instructions
INFO: 💾 Saved 72 examples to training_data.jsonl
INFO: ✅ File uploaded: file-abc123
INFO: 🚀 Job created: ftjob-xyz789
INFO: 🎉 Success! Monitor at: https://platform.openai.com/finetune/ftjob-xyz789
```

## ⚙️ Configuration

All settings in `src/config.py`:
- `SUBSTACK_RSS_URL` - RSS feed URL
- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `TRAINING_FILE` - Output filename

## 🔧 Customization

### Change RSS Source
Edit `SUBSTACK_RSS_URL` in `src/config.py`

### Modify Prompts  
Update `_get_simple_prompts()` in `src/training_data_generator.py`

### Adjust Content Filtering
Modify word count threshold in `src/rss_parser.py`