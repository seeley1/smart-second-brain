# 🧠 Smart Second Brain

<p align="center">
  <strong>AI-Driven Knowledge Management System</strong><br>
  Multi-Source Input → Automatic Digestion → One-Click Output
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## ✨ Features

### 🔥 Core Features

- **📥 Multi-Source Input** - WeChat, Douyin, WeChat Reading, IMA Knowledge Base, and more
- **🤖 Automatic Digestion** - AI-powered content parsing, summarization, and knowledge extraction
- **📤 One-Click Output** - Generate articles, videos, and social media content instantly
- **🧠 Intelligent Organization** - Three-layer knowledge structure (Raw → Schema → Wiki)
- **🔗 Knowledge Graph** - Visualize connections between your knowledge nodes
- **✅ Quality Verification** - Automated knowledge quality checks and validation

### 🚀 Advanced Features

- **Multi-Device Sync** - Access your second brain from anywhere
- **AI Agent Integration** - WorkBuddy AI agents for automated workflows
- **Voice Cloning** - Create personalized voice content (Chinese optimized)
- **Video Generation** - Auto-generate videos from knowledge content
- **Custom Templates** - Flexible note templates for different use cases

---

## 🏗️ Architecture

```
Smart Second Brain
│
├── 📥 Input Layer (Multi-Source)
│   ├── WeChat Articles
│   ├── Douyin Videos
│   ├── WeChat Reading Notes
│   ├── IMA Knowledge Base
│   └── Manual Input
│
├── 🤖 Digestion Layer (AI Processing)
│   ├── Content Parsing
│   ├── Knowledge Extraction
│   ├── Auto-Tagging
│   ├── Summary Generation
│   └── Quality Verification
│
├── 🗂️ Storage Layer (Three-Layer Structure)
│   ├── Raw Layer (00-Raw) - Original materials
│   ├── Schema Layer (10-Schema) - Structured knowledge
│   └── Wiki Layer (20-Wiki) - Refined output
│
└── 📤 Output Layer (One-Click)
    ├── Articles & Blogs
    ├── Social Media Content
    ├── Video Scripts
    └── Knowledge Sharing
```

---

## 🚀 Quick Start

### Prerequisites

- **Obsidian** (knowledge vault)
- **WorkBuddy** (AI assistant platform)
- **Python 3.8+** (for scripts)

### Installation

#### Option 1: One-Click Install (Recommended)

**Windows:**
```bash
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain
install.bat
```

**Linux/macOS:**
```bash
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain
bash install.sh
```

#### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/seeley1/smart-second-brain.git
   cd smart-second-brain
   ```

2. **Copy templates to your Obsidian vault**
   ```bash
   cp -r templates/obsidian/* "/path/to/your/vault/.obsidian/templates/"
   ```

3. **Configure WorkBuddy automations**
   - Open WorkBuddy
   - Import automation tasks from `templates/automation/`
   - Configure your API keys in `config/config.yaml`

4. **Initialize your vault structure**
   ```bash
   python scripts/init_vault.py --vault-path "/path/to/your/vault"
   ```

### Configuration

1. Copy the example config:
   ```bash
   cp config/config.example.yaml config/config.yaml
   ```

2. Edit `config/config.yaml` with your settings:
   ```yaml
   vault_path: "/path/to/your/vault"
   workbuddy_api_key: "your-api-key"
   ai_model: "mimo"  # or "gpt-4", "claude"
   voice_clone_enabled: true
   ```

---

## 📚 Documentation

### Core Concepts

#### Three-Layer Knowledge Structure

1. **Raw Layer (00-Raw)** - Original materials
   - Douyin video notes
   - WeChat article extracts
   - Reading highlights

2. **Schema Layer (10-Schema)** - Structured knowledge
   - Parsed content with metadata
   - Tagged and categorized
   - Cross-referenced

3. **Wiki Layer (20-Wiki)** - Refined output
   - Synthesized knowledge
   - Actionable insights
   - Ready for output

#### Automation Tasks

The system includes 4 automated tasks:

1. **Daily Knowledge Sync** - Auto-sync from multiple sources
2. **Obsidian Dialog Sync** - Sync WorkBuddy conversations to Obsidian
3. **Knowledge Quality Check** - Verify and validate knowledge
4. **Weekly Knowledge Refinement** - Summarize and refine weekly

### Usage Guide

#### Adding Knowledge

**From Douyin:**
```
Paste Douyin video link → Auto-parse → Save to Raw Layer
```

**From WeChat:**
```
Share article to WorkBuddy → Auto-extract → Save to Raw Layer
```

**From WeChat Reading:**
```
Sync reading notes → Auto-import → Save to Raw Layer
```

#### Digesting Knowledge

AI automatically:
- Parses content
- Extracts key points
- Generates summaries
- Adds tags and links
- Moves from Raw → Schema layer

#### Outputting Content

**One-Click Article:**
```
Select knowledge nodes → Click "Generate Article" → Get draft
```

**One-Click Video:**
```
Select knowledge nodes → Click "Generate Video" → Get video script + audio
```

**One-Click Social Media:**
```
Select knowledge nodes → Click "Generate Post" → Get social media content
```

---

## 🛠️ Project Structure

```
smart-second-brain/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── config/
│   ├── config.example.yaml      # Config template
│   └── config.yaml              # Your config (don't commit)
├── templates/
│   ├── obsidian/               # Obsidian note templates
│   │   ├── Raw-Layer-Template.md
│   │   ├── Schema-Layer-Template.md
│   │   └── Wiki-Layer-Template.md
│   └── automation/              # WorkBuddy automation configs
│       ├── daily-knowledge-sync.json
│       ├── obsidian-dialog-sync.json
│       ├── knowledge-quality-check.json
│       └── weekly-refinement.json
├── docs/
│   ├── 第二大脑管理规范.md      # Management guide (Chinese)
│   ├── Installation-Guide.md
│   ├── User-Manual.md
│   ├── FAQ.md
│   └── Video-Tutorials.md
├── scripts/
│   ├── init_vault.py           # Initialize vault structure
│   ├── dual_voiceclone_tool.py # Voice cloning tool
│   ├── knowledge_graph.py      # Knowledge graph generator
│   └── utils.py                # Utility functions
├── examples/
│   ├── example-notes/          # Example notes
│   └── example-knowledge-graph.html
└── .workbuddy/
    └── skills/                 # WorkBuddy skills
        ├── douyin-to-obsidian/
        ├── obsidian-sync/
        └── knowledge-integration/
```

---

## 🎯 Use Cases

### For Content Creators
- Auto-generate article drafts from collected knowledge
- Create video scripts with AI-generated voice
- Manage content calendar with knowledge tags

### For Researchers
- Collect and organize research materials
- Auto-generate literature reviews
- Visualize knowledge connections

### For Students
- Organize study notes automatically
- Generate revision materials
- Connect concepts across subjects

### For Professionals
- Build personal knowledge base
- Auto-summarize meetings and articles
- Generate reports and presentations

---

## 🔧 Advanced Configuration

### Customizing AI Models

Edit `config/config.yaml`:
```yaml
ai:
  model: "mimo"  # Options: mimo, gpt-4, claude, gemini
  temperature: 0.7
  max_tokens: 2000
```

### Adding Custom Sources

Create a new skill in `.workbuddy/skills/`:
```python
# my-custom-source.py
def parse_content(url):
    # Your parsing logic
    pass
```

### Customizing Output Templates

Edit templates in `templates/obsidian/`:
- Modify `Raw-Layer-Template.md` for input format
- Modify `Schema-Layer-Template.md` for digestion format
- Modify `Wiki-Layer-Template.md` for output format

---

## 🐛 Troubleshooting

### Common Issues

**Issue: Automation tasks not running**
- Check WorkBuddy is running
- Verify automation config in WorkBuddy settings
- Check logs in `vault/60-Diary/第二大脑系统日志/`

**Issue: Voice cloning not working**
- Ensure `dual_voiceclone_tool.py` is configured
- Check reference audio file exists
- Verify ffmpeg is installed

**Issue: Knowledge graph not generating**
- Check browser supports D3.js
- Verify `knowledge_graph.html` is in output folder
- Open browser console for errors

More issues? Check [FAQ.md](docs/FAQ.md)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain
pip install -r requirements.txt  # (to be created)
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

## 📧 Contact

Seeley - [@seeley1](https://github.com/seeley1)

Project Link: [https://github.com/seeley1/smart-second-brain](https://github.com/seeley1/smart-second-brain)

---

## 🙏 Acknowledgments

- [WorkBuddy](https://www.codebuddy.cn) - AI assistant platform
- [Obsidian](https://obsidian.md) - Knowledge base
- [D3.js](https://d3js.org/) - Knowledge graph visualization
- All contributors and users of this project

---

<p align="center">
  Built with ❤️ for knowledge workers everywhere
</p>
