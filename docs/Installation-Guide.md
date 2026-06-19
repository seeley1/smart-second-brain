# Smart Second Brain - Installation Guide

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Installation](#quick-installation)
3. [Manual Installation](#manual-installation)
4. [Configuration](#configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

1. **Obsidian** (v1.0+)
   - Download: https://obsidian.md
   - Purpose: Knowledge vault

2. **WorkBuddy** (v2.0+)
   - Download: https://www.codebuddy.cn
   - Purpose: AI assistant platform

3. **Python** (v3.8+)
   - Download: https://www.python.org
   - Purpose: Run scripts

4. **Git** (v2.0+)
   - Download: https://git-scm.com
   - Purpose: Version control

### Optional Software

1. **FFmpeg** (for voice cloning)
   - Windows: `choco install ffmpeg`
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

2. **VS Code** (for editing)
   - Download: https://code.visualstudio.com
   - Purpose: Edit config files

---

## Quick Installation

### Windows

```bash
# Clone repository
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain

# Run installation script
install.bat
```

### Linux / macOS

```bash
# Clone repository
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain

# Run installation script
bash install.sh
```

### What the Installation Script Does

1. ✅ Checks prerequisites (Python, Git, Obsidian, WorkBuddy)
2. ✅ Creates Obsidian vault structure
3. ✅ Copies templates to Obsidian
4. ✅ Creates configuration file
5. ✅ Sets up automation tasks
6. ✅ Verifies installation

---

## Manual Installation

If the quick installation script doesn't work, follow these steps:

### Step 1: Clone Repository

```bash
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain
```

### Step 2: Create Obsidian Vault

1. Open Obsidian
2. Click "Open another vault"
3. Click "Create new vault"
4. Name: `SmartSecondBrain`
5. Location: Choose a location

### Step 3: Copy Templates

```bash
# Copy templates to Obsidian vault
cp -r templates/obsidian/* "/path/to/your/vault/.obsidian/templates/"
```

### Step 4: Configure WorkBuddy Automation

1. Open WorkBuddy
2. Go to "Automation" tab
3. Click "Import Automation"
4. Select files from `templates/automation/`:
   - `daily-knowledge-sync.json`
   - `obsidian-dialog-sync.json`
   - `knowledge-quality-check.json`
   - `weekly-refinement.json`

### Step 5: Create Configuration File

```bash
# Copy example config
cp config/config.example.yaml config/config.yaml

# Edit config.yaml with your settings
# (Use VS Code or any text editor)
```

### Step 6: Initialize Vault Structure

```bash
# Run initialization script
python scripts/init_vault.py --vault-path "/path/to/your/vault"
```

---

## Configuration

### Edit config.yaml

Open `config/config.yaml` and edit the following:

```yaml
# Path to your Obsidian vault (REQUIRED)
vault_path: "/path/to/your/obsidian/vault"

# AI Configuration
ai:
  model: "mimo"  # Options: mimo, gpt-4, claude, gemini
  api_key: "your-api-key-here"
  api_base: "https://api.example.com/v1/chat/completions"
```

### Configure Automation Tasks

#### 1. Daily Knowledge Sync

- **Schedule**: Every day at 10:00
- **Sources**: Douyin, WeChat, Weread, IMA
- **Action**: Auto-sync to Raw Layer

#### 2. Obsidian Dialog Sync

- **Schedule**: Every hour
- **Trigger**: Keywords (knowledge, note, summary)
- **Action**: Auto-sync WorkBuddy conversations

#### 3. Knowledge Quality Check

- **Schedule**: Every day at 22:30
- **Scope**: Today's new knowledge
- **Action**: Verify and validate quality

#### 4. Weekly Knowledge Refinement

- **Schedule**: Every Sunday at 20:00
- **Scope**: This week's knowledge
- **Action**: Refine and optimize

---

## Verification

### Verify Installation

```bash
# Run verification script
python scripts/verify_installation.py
```

### Expected Output

```
🧠 Smart Second Brain - Verification
==================================================

✅ Obsidian vault found: /path/to/vault
✅ Templates found: 3
✅ Automation tasks found: 4
✅ Config file found: config/config.yaml
✅ Scripts found: 4

==================================================
✅ All checks passed! Smart Second Brain is ready to use.
```

### Test Usage

#### Test 1: Add a Note

1. Paste a Douyin video link to WorkBuddy
2. Check if note is auto-saved to `00-Raw/抖音笔记/`

#### Test 2: Run Automation

1. Open WorkBuddy
2. Go to "Automation" tab
3. Click "Run" on "Daily Knowledge Sync"
4. Check if knowledge is synced

#### Test 3: Generate Knowledge Graph

```bash
python scripts/knowledge_graph.py --vault-path "/path/to/vault"
```

Open `output/knowledge_graph.html` in browser.

---

## Troubleshooting

### Issue 1: "Obsidian not found"

**Solution**:
- Make sure Obsidian is installed
- Check if Obsidian is in system PATH
- Try reinstalling Obsidian

### Issue 2: "WorkBuddy not found"

**Solution**:
- Make sure WorkBuddy is installed
- Check if WorkBuddy is running
- Try reinstalling WorkBuddy

### Issue 3: "Python not found"

**Solution**:
- Make sure Python 3.8+ is installed
- Check if Python is in system PATH
- Try `python3` instead of `python`

### Issue 4: "Git not found"

**Solution**:
- Make sure Git is installed
- Check if Git is in system PATH
- Try reinstalling Git

### Issue 5: "Automation tasks not running"

**Solution**:
- Check if WorkBuddy is running
- Check automation config in WorkBuddy
- Check logs in `60-Diary/第二大脑系统日志/`

### Issue 6: "Voice cloning not working"

**Solution**:
- Make sure FFmpeg is installed
- Check if reference audio file exists
- Check API keys for voice cloning

### Issue 7: "Knowledge graph not generating"

**Solution**:
- Check if Obsidian vault path is correct
- Check if vault has markdown files
- Check browser console for errors

---

## 📞 Support

If you still have issues:

1. Check [FAQ.md](FAQ.md)
2. Check [User-Manual.md](User-Manual.md)
3. Open an issue on GitHub: https://github.com/seeley1/smart-second-brain/issues
4. Contact Seeley: [@seeley1](https://github.com/seeley1)

---

## 📝 Summary

After installation, you should have:

1. ✅ Obsidian vault with three-layer structure
2. ✅ WorkBuddy automation tasks configured
3. ✅ Configuration file created and edited
4. ✅ Scripts ready to use

**Next Steps**:

1. Read [User-Manual.md](User-Manual.md) to learn how to use
2. Try the example notes in `examples/`
3. Customize templates and config to fit your needs
4. Start building your second brain!

---

*Installation Guide for Smart Second Brain*
*Created by Seeley, maintained by WorkBuddy AI Agent*
