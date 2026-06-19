# Smart Second Brain - FAQ (Frequently Asked Questions)

## 📋 Table of Contents

1. [General Questions](#general-questions)
2. [Installation Issues](#installation-issues)
3. [Configuration Issues](#configuration-issues)
4. [Usage Questions](#usage-questions)
5. [Automation Issues](#automation-issues)
6. [Output Issues](#output-issues)
7. [Advanced Topics](#advanced-topics)

---

## General Questions

### Q1: What is Smart Second Brain?

**A**: Smart Second Brain is an **AI-driven knowledge management system** that helps you:
- 📥 **Input**: Collect knowledge from multiple sources (Douyin, WeChat, Weread, IMA)
- 🤖 **Digest**: AI automatically parses, summarizes, and organizes knowledge
- 📤 **Output**: One-click generate articles, videos, and social media content

### Q2: Is Smart Second Brain free?

**A**: Yes! Smart Second Brain is **open-source** (MIT License). You can:
- ✅ Use for free
- ✅ Modify for your needs
- ✅ Distribute to others

However, some **AI APIs may charge** (e.g., GPT-4, Claude), but you can use **free models** (e.g., MiMo).

### Q3: Do I need to know programming?

**A**: **No!** Most features are **no-code**:
- Installing: Use installation script (double-click `install.bat` on Windows)
- Using: Use Obsidian (visual interface) + WorkBuddy (AI assistant)
- Configuring: Edit `config.yaml` (simple text file)

But if you **want to customize**, knowing basic Python/Markdown helps.

### Q4: Can I use Smart Second Brain without Obsidian?

**A**: Currently, **Obsidian is required** (it's the knowledge vault). But we plan to support:
- Logseq (another note-taking app)
- Notion (web-based)
- Pure file system (Markdown files only)

If you don't want to use Obsidian, you can **wait for future versions**.

---

## Installation Issues

### Q5: "Obsidian not found" error

**A**: This means the installation script can't find Obsidian. **Solutions**:

1. **Make sure Obsidian is installed**  
   Download: https://obsidian.md

2. **Add Obsidian to system PATH**  
   - Windows: `Settings → About → Advanced → "Open installer in terminal"`  
   - Mac/Linux: Usually auto-detected

3. **Use manual installation** (see [Installation-Guide.md](Installation-Guide.md))

### Q6: "WorkBuddy not found" error

**A**: This means the installation script can't find WorkBuddy. **Solutions**:

1. **Make sure WorkBuddy is installed**  
   Download: https://www.codebuddy.cn

2. **Start WorkBuddy** before running installation script

3. **Use manual installation** (see [Installation-Guide.md](Installation-Guide.md))

### Q7: "Python not found" error

**A**: This means Python 3.8+ is not installed or not in PATH. **Solutions**:

1. **Install Python**  
   Download: https://www.python.org

2. **Check "Add Python to PATH"** during installation

3. **Verify installation**:  
   ```bash
   python --version
   # Should show Python 3.8+
   ```

### Q8: Installation script hangs/freezes

**A**: This may be due to network issues or permission problems. **Solutions**:

1. **Run as Administrator** (Windows) or `sudo` (Mac/Linux)

2. **Check internet connection** (need to download dependencies)

3. **Use manual installation** (see [Installation-Guide.md](Installation-Guide.md))

---

## Configuration Issues

### Q9: Where is `config.yaml`?

**A**: After installation, `config.yaml` is at:
- **Windows**: `C:\Users\YourName\smart-second-brain\config\config.yaml`
- **Mac/Linux**: `~/smart-second-brain/config/config.yaml`

If it doesn't exist, **copy from example**:
```bash
cp config/config.example.yaml config/config.yaml
```

### Q10: How to get AI API Key?

**A**: Depends on which AI model you use:

#### For MiMo (free-ish):
1. Go to https://platform.moonshot.cn
2. Sign up / Log in
3. Go to "API Keys" → "Create new key"
4. Copy key to `config.yaml`

#### For GPT-4 (paid):
1. Go to https://platform.openai.com
2. Sign up / Log in
3. Go to "API Keys" → "Create new secret key"
4. Copy key to `config.yaml`

#### For Claude (paid):
1. Go to https://console.anthropic.com
2. Sign up / Log in
3. Go to "API Keys" → "Create Key"
4. Copy key to `config.yaml`

### Q11: "API Key invalid" error

**A**: This means your API key is wrong or expired. **Solutions**:

1. **Check key is copied correctly** (no extra spaces)

2. **Check key hasn't expired** (some APIs expire after 1 year)

3. **Regenerate key** (in API provider's website)

4. **Check API has credit** (for paid APIs like GPT-4, make sure you have balance)

### Q12: How to change AI model?

**A**: Edit `config.yaml`:
```yaml
ai:
  model: "gpt-4"  # Options: mimo, gpt-4, claude, gemini
```

Then restart WorkBuddy.

---

## Usage Questions

### Q13: How to add knowledge from Douyin?

**A**: Very easy!

1. **Copy Douyin video link** (e.g., `https://v.douyin.com/xxx/`)
2. **Paste to WorkBuddy**
3. **AI will auto-parse** and save to `00-Raw/抖音笔记/`

### Q14: How to add knowledge from WeChat?

**A**: Two methods:

#### Method 1: Share to WorkBuddy
1. Open WeChat article
2. Click "Share" → "Copy link"
3. Paste link to WorkBuddy
4. AI will auto-extract and save

#### Method 2: Use "WeChat Article Extractor" skill
1. Open WorkBuddy
2. Type: `/wechat-article-extractor`
3. Paste link
4. AI will extract and save

### Q15: How to organize knowledge manually?

**A**: If you don't want AI to auto-organize:

1. **Create new note** in Obsidian
2. **Use template** (`Raw-Layer-Template`, `Schema-Layer-Template`, or `Wiki-Layer-Template`)
3. **Fill in content manually**
4. **Save to appropriate folder** (`00-Raw/`, `10-Schema/`, or `20-Wiki/`)

### Q16: How to search knowledge?

**A**: Obsidian has powerful search:

1. **Quick switcher**: `Ctrl+O` (Windows/Linux) or `Cmd+O` (Mac)
2. **Search in vault**: `Ctrl+Shift+F` (Windows/Linux) or `Cmd+Shift+F` (Mac)
3. **Search by tags**: Click on tag (e.g., `#AI`) to see all notes with that tag
4. **Search by links**: Click on `[[wikilink]]` to jump to that note

---

## Automation Issues

### Q17: Automation tasks not running

**A**: This is the most common issue. **Check these**:

1. **Is WorkBuddy running?**  
   - Check system tray (Windows) or menu bar (Mac) for WorkBuddy icon
   - If not running, start WorkBuddy

2. **Are automation tasks enabled?**  
   - Open WorkBuddy → "Automation" tab
   - Make sure tasks are **enabled** (toggle switch is ON)

3. **Are schedules correct?**  
   - Check cron expressions (e.g., `0 10 * * *` means every day at 10:00)
   - Make sure timezone is correct (`Asia/Shanghai` for China)

4. **Check logs**  
   - Logs are in `60-Diary/第二大脑系统日志/`
   - Open latest log to see errors

### Q18: Automation task runs but does nothing

**A**: This means the task runs, but **no knowledge is found**. **Check these**:

1. **Are sources enabled?**  
   - Open automation config (e.g., `templates/automation/daily-knowledge-sync.json`)
   - Check `"enabled": true` for each source

2. **Are there new knowledge?**  
   - Automation only processes **new knowledge**
   - If no new knowledge, task will do nothing

3. **Check filters**  
   - Some tasks have filters (e.g., only process notes with `#knowledge` tag)
   - Check if your notes match filters

### Q19: How to change automation schedule?

**A**: Edit automation config (JSON file):

```json
"schedule": {
  "type": "cron",
  "expression": "0 20 * * *",  // Every day at 20:00
  "timezone": "Asia/Shanghai"
}
```

Common cron expressions:
- `0 10 * * *` - Every day at 10:00
- `0 * * * *` - Every hour
- `0 20 * * 0` - Every Sunday at 20:00

---

## Output Issues

### Q20: "One-Click Output" not working

**A**: This feature requires **AI API** to be configured. **Check these**:

1. **Is AI API configured?**  
   - Check `config.yaml` has valid `api_key`
   - Check `api_base` is correct

2. **Is AI model available?**  
   - Some models may be offline or deprecated
   - Try switching to another model (e.g., from `gpt-4` to `mimo`)

3. **Check AI API quota**  
   - For paid APIs, make sure you have remaining quota
   - Check API provider's website for usage

### Q21: Generated article is low quality

**A**: AI-generated content may need **human editing**. **Suggestions**:

1. **Edit the draft**  
   - AI generates **first draft**, you need to edit
   - Add your own insights, examples, stories

2. **Improve input quality**  
   - Better input = better output
   - Make sure your knowledge notes are high-quality

3. **Adjust AI temperature**  
   - In `config.yaml`, set `temperature: 0.3` (more conservative) or `temperature: 0.9` (more creative)

### Q22: Voice cloning not working

**A**: Voice cloning requires **reference audio** and **FFmpeg**. **Check these**:

1. **Is FFmpeg installed?**  
   - Run `ffmpeg -version` in terminal
   - If not found, install FFmpeg:
     - Windows: `choco install ffmpeg`
     - Mac: `brew install ffmpeg`
     - Linux: `sudo apt install ffmpeg`

2. **Is reference audio provided?**  
   - In `config.yaml`, set `reference_audio: "/path/to/audio.wav"`
   - Audio should be 10-30 seconds, clear speech

3. **Check voice cloning API**  
   - Make sure `VOXCOMM2_API_KEY` or `MIMO_API_KEY` is set
   - Check API provider's documentation

---

## Advanced Topics

### Q23: Can I customize templates?

**A**: Yes! Templates are **Markdown files** that you can edit:

1. **Open template file** (e.g., `templates/obsidian/Raw-Layer-Template.md`)
2. **Edit with any text editor** (VS Code, Notepad, etc.)
3. **Use Obsidian template syntax**:
   - `{{title}}` - Note title
   - `{{date}}` - Current date
   - `{{content}}` - Note content

### Q24: Can I add custom input sources?

**A**: Yes! You can create **custom skills**:

1. **Create new skill** in `.workbuddy/skills/`
2. **Write skill code** (Python or JavaScript)
3. **Use skill in WorkBuddy** (type `/your-skill-name`)

See [Skill Creator](https://www.codebuddy.cn/docs/skills) for details.

### Q25: Can I use Smart Second Brain on mobile?

**A**: **Partial support**:

- ✅ **Obsidian Mobile**: You can **view** notes on mobile
- ✅ **WorkBuddy Mobile** (if available): You can **add knowledge** on mobile
- ❌ **Automation tasks**: Only run on **desktop** (WorkBuddy desktop required)

We're working on **full mobile support** in future versions.

### Q26: How to contribute to Smart Second Brain?

**A**: Contributions are welcome! Here's how:

1. **Fork repository** on GitHub
2. **Create feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open Pull Request**

Also, you can:
- Report bugs (GitHub Issues)
- Suggest features (GitHub Issues)
- Improve documentation (edit `docs/` files)
- Share your templates (share in Discussions)

---

## 📞 Still Need Help?

If your question isn't answered here:

1. **Check [User-Manual.md](User-Manual.md)** - Detailed usage guide
2. **Check [Installation-Guide.md](Installation-Guide.md)** - Installation help
3. **Open GitHub Issue**: https://github.com/seeley1/smart-second-brain/issues
4. **Contact Seeley**: [@seeley1](https://github.com/seeley1)

---

## 📝 Summary

**Most common issues**:
1. ❌ Automation not running → Check WorkBuddy is running
2. ❌ API Key invalid → Check API key configuration
3. ❌ Output low quality → Edit AI-generated drafts

**Need help?** Don't hesitate to ask! We're here to help 😊

---

*FAQ for Smart Second Brain*
*Created by Seeley, maintained by WorkBuddy AI Agent*
