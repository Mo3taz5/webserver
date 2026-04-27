# Mo3taz Cloud Save API

This repository contains a loader that downloads the actual server code from a private HuggingFace dataset.

## Why This Approach?

- **Security**: Keeps sensitive code and credentials private
- **Version Control**: Single source of truth in HuggingFace dataset
- **Easy Updates**: Update dataset, restart server - no git commits needed
- **Public Repo**: Can share this loader publicly without exposing code

## Deployment

### Environment Variables Required

```bash
HF_TOKEN=your_huggingface_token_here
DATASET_NAME=mtaaz/server-code-private  # Optional, defaults to this
```

### How It Works

1. `github_loader.py` downloads `latest.zip` from HuggingFace dataset
2. Extracts all server files to current directory
3. Runs the actual `startup.sh` from extracted files

### Local Development

```bash
# Set environment variables
export HF_TOKEN=your_token_here

# Install minimal requirements
pip install -r github_requirements.txt

# Download and start
python github_loader.py
bash startup.sh
```

### Deployment Platforms

#### Render / Railway / Fly.io

1. Fork this repo
2. Connect to your deployment platform
3. Set `HF_TOKEN` environment variable
4. Set start command: `bash github_startup.sh`

#### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy loader files
COPY github_loader.py github_startup.sh github_requirements.txt ./

# Install minimal requirements
RUN pip install -r github_requirements.txt

# Set environment variables (or use docker-compose)
ENV HF_TOKEN=your_token_here
ENV DATASET_NAME=mtaaz/server-code-private

# Download code and start
CMD ["bash", "github_startup.sh"]
```

## Updating Server Code

1. Update code locally in `translation-server/` directory
2. Run `python upload_server_to_dataset.py` (uploads to HuggingFace dataset)
3. Restart your deployment (it will download the latest code automatically)

## Support

For issues or questions, contact the development team.
