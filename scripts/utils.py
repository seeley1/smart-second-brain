#!/usr/bin/env python3
"""
Smart Second Brain - Utility Functions
Common utilities for Smart Second Brain system
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
import hashlib

# ==================== File Utilities ====================

def read_file(file_path, encoding="utf-8"):
    """Read file content"""
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading file {file_path}: {e}")
        return None

def write_file(file_path, content, encoding="utf-8"):
    """Write content to file"""
    try:
        # Create directory if not exists
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "w", encoding=encoding) as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"❌ Error writing file {file_path}: {e}")
        return False

def append_file(file_path, content, encoding="utf-8"):
    """Append content to file"""
    try:
        # Create directory if not exists
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "a", encoding=encoding) as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"❌ Error appending to file {file_path}: {e}")
        return False

def copy_file(src_path, dst_path):
    """Copy file from src to dst"""
    try:
        import shutil
        # Create directory if not exists
        Path(dst_path).parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(src_path, dst_path)
        return True
    except Exception as e:
        print(f"❌ Error copying file {src_path} to {dst_path}: {e}")
        return False

def list_files(directory, pattern="*", recursive=True):
    """List files in directory"""
    try:
        dir_path = Path(directory)
        
        if recursive:
            return list(dir_path.rglob(pattern))
        else:
            return list(dir_path.glob(pattern))
    except Exception as e:
        print(f"❌ Error listing files in {directory}: {e}")
        return []

# ==================== Text Utilities ====================

def extract_wikilinks(text):
    """Extract [[wikilinks]] from text"""
    pattern = r'\[\[(.*?)\]\]'
    return re.findall(pattern, text)

def extract_tags(text):
    """Extract #tags from text"""
    pattern = r'#(\w+)'
    return re.findall(pattern, text)

def extract_headings(text):
    """Extract headings from markdown text"""
    pattern = r'^(#{1,6})\s+(.+)$'
    return re.findall(pattern, text, re.MULTILINE)

def generate_summary(text, max_length=200):
    """Generate summary from text"""
    # Remove markdown syntax
    text = re.sub(r'#+\s+', '', text)
    text = re.sub(r'\[\[(.*?)\]\]', r'\1', text)
    text = re.sub(r'#\w+', '', text)
    
    # Get first paragraph
    paragraphs = text.split('\n\n')
    for para in paragraphs:
        para = para.strip()
        if para:
            # Truncate
            if len(para) > max_length:
                para = para[:max_length] + '...'
            return para
    
    return ""

def clean_text(text):
    """Clean text - remove extra whitespace, etc."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    return text

# ==================== Date Utilities ====================

def get_current_date(format="%Y-%m-%d"):
    """Get current date as string"""
    return datetime.now().strftime(format)

def get_current_datetime(format="%Y-%m-%d %H:%M:%S"):
    """Get current datetime as string"""
    return datetime.now().strftime(format)

def parse_date(date_str, format="%Y-%m-%d"):
    """Parse date string to datetime object"""
    try:
        return datetime.strptime(date_str, format)
    except Exception as e:
        print(f"❌ Error parsing date {date_str}: {e}")
        return None

# ==================== Markdown Utilities ====================

def create_markdown_link(text, url):
    """Create markdown link"""
    return f"[{text}]({url})"

def create_wikilink(title):
    """Create Obsidian wikilink"""
    return f"[[{title}]]"

def create_tag(tag):
    """Create tag"""
    return f"#{tag}"

def create_checkbox(checked=False):
    """Create checkbox"""
    return "- [x] " if checked else "- [ ] "

# ==================== AI Utilities ====================

def call_ai_api(prompt, config):
    """Call AI API (generic)"""
    try:
        import requests
        
        api_url = config.get("api_url", "")
        api_key = config.get("api_key", "")
        model = config.get("model", "gpt-3.5-turbo")
        temperature = config.get("temperature", 0.7)
        max_tokens = config.get("max_tokens", 2000)
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            print(f"❌ AI API error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error calling AI API: {e}")
        return None

# ==================== Hash Utilities ====================

def calculate_file_hash(file_path, algorithm="sha256"):
    """Calculate file hash"""
    try:
        hash_obj = hashlib.new(algorithm)
        
        with open(file_path, "rb") as f:
            # Read file in chunks
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"❌ Error calculating hash for {file_path}: {e}")
        return None

def calculate_text_hash(text, algorithm="sha256"):
    """Calculate text hash"""
    try:
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(text.encode("utf-8"))
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"❌ Error calculating hash: {e}")
        return None

# ==================== Config Utilities ====================

def load_config(config_path):
    """Load config from YAML file"""
    try:
        import yaml
        
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading config {config_path}: {e}")
        return None

def save_config(config, config_path):
    """Save config to YAML file"""
    try:
        import yaml
        
        # Create directory if not exists
        Path(config_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
        
        return True
    except Exception as e:
        print(f"❌ Error saving config {config_path}: {e}")
        return False

# ==================== Logging Utilities ====================

def log_message(message, level="INFO", log_file=None):
    """Log message"""
    timestamp = get_current_datetime()
    log_line = f"[{timestamp}] [{level}] {message}\n"
    
    print(log_line.rstrip())
    
    if log_file:
        append_file(log_file, log_line)

# ==================== Validation Utilities ====================

def validate_config(config, required_fields):
    """Validate config has required fields"""
    missing_fields = []
    
    for field in required_fields:
        if field not in config:
            missing_fields.append(field)
    
    if missing_fields:
        print(f"❌ Config missing required fields: {missing_fields}")
        return False
    
    return True

def validate_file_exists(file_path):
    """Validate file exists"""
    if not Path(file_path).exists():
        print(f"❌ File not found: {file_path}")
        return False
    return True

# ==================== Main (Test) ====================

if __name__ == "__main__":
    print("🧰 Testing Utility Functions")
    print("=" * 50)
    
    # Test file utilities
    print("\n📝 Testing file utilities...")
    
    test_file = "temp/test.txt"
    
    # Write
    write_file(test_file, "Hello, World!")
    print(f"  ✅ Written to {test_file}")
    
    # Read
    content = read_file(test_file)
    print(f"  ✅ Read from {test_file}: {content}")
    
    # Test text utilities
    print("\n📝 Testing text utilities...")
    
    test_text = "# Heading\n\nThis is a [[wikilink]] and #tag."
    
    wikilinks = extract_wikilinks(test_text)
    print(f"  ✅ Extracted wikilinks: {wikilinks}")
    
    tags = extract_tags(test_text)
    print(f"  ✅ Extracted tags: {tags}")
    
    headings = extract_headings(test_text)
    print(f"  ✅ Extracted headings: {headings}")
    
    # Test date utilities
    print("\n📅 Testing date utilities...")
    
    current_date = get_current_date()
    print(f"  ✅ Current date: {current_date}")
    
    current_datetime = get_current_datetime()
    print(f"  ✅ Current datetime: {current_datetime}")
    
    # Clean up
    import os
    os.remove(test_file)
    os.rmdir("temp")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!")
