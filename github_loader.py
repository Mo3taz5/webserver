"""
GitHub Repository Loader
Downloads and extracts server code from HuggingFace private dataset
This file is safe to commit to public GitHub repos
"""

import os
import sys
import zipfile
import tempfile
from pathlib import Path

def download_from_dataset():
    """Download latest server code from HuggingFace dataset"""
    try:
        from huggingface_hub import hf_hub_download
        
        # Get credentials from environment
        hf_token = os.getenv("HF_TOKEN")
        dataset_name = os.getenv("DATASET_NAME", "mtaaz/server-code-private")
        
        if not hf_token:
            print("❌ ERROR: HF_TOKEN environment variable not set")
            print("Set it in your deployment platform's environment variables")
            sys.exit(1)
        
        print("=" * 60)
        print("Downloading server code from HuggingFace dataset...")
        print(f"Dataset: {dataset_name}")
        print("=" * 60)
        
        # Download latest.zip from dataset
        zip_path = hf_hub_download(
            repo_id=dataset_name,
            filename="latest.zip",
            repo_type="dataset",
            token=hf_token,
            local_dir=tempfile.gettempdir(),
            local_dir_use_symlinks=False
        )
        
        print(f"✅ Downloaded: {zip_path}")
        
        # Extract to current directory
        print("Extracting files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        print("✅ Extraction complete")
        
        # Clean up
        os.remove(zip_path)
        print("✅ Cleanup complete")
        
        print("=" * 60)
        print("Server code loaded successfully!")
        print("=" * 60)
        
        return True
        
    except ImportError:
        print("❌ ERROR: huggingface_hub not installed")
        print("Run: pip install huggingface_hub")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR: Failed to download from dataset: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_from_dataset()
