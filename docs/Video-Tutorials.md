# Smart Second Brain - Video Tutorials

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Tutorial 1: Installation](#tutorial-1-installation)
3. [Tutorial 2: Adding Knowledge](#tutorial-2-adding-knowledge)
4. [Tutorial 3: Processing Knowledge](#tutorial-3-processing-knowledge)
5. [Tutorial 4: Generating Output](#tutorial-4-generating-output)
6. [Tutorial 5: Automation Tasks](#tutorial-5-automation-tasks)
7. [Tutorial 6: Knowledge Graph](#tutorial-6-knowledge-graph)
8. [Tutorial 7: Advanced Features](#tutorial-7-advanced-features)
9. [Next Steps](#next-steps)

---

## Introduction

Welcome to **Smart Second Brain** video tutorials! 🎥

These tutorials will guide you through:
- 🛠️ Installing and configuring Smart Second Brain
- 📥 Adding knowledge from multiple sources
- 🤖 Processing knowledge automatically
- 📤 Generating output (articles, videos, social media)
- ⚙️ Using automation tasks
- 📊 Visualizing knowledge with knowledge graph
- 🚀 Using advanced features

### 📺 Video List

| # | Tutorial | Duration | Difficulty |
|---|-----------|----------|------------|
| 1 | Installation | 10 min | ⭐ |
| 2 | Adding Knowledge | 15 min | ⭐⭐ |
| 3 | Processing Knowledge | 20 min | ⭐⭐ |
| 4 | Generating Output | 25 min | ⭐⭐⭐ |
| 5 | Automation Tasks | 15 min | ⭐⭐ |
| 6 | Knowledge Graph | 10 min | ⭐⭐ |
| 7 | Advanced Features | 20 min | ⭐⭐⭐ |

---

## Tutorial 1: Installation

### 🎯 What You'll Learn

- Install Obsidian
- Install WorkBuddy
- Install Smart Second Brain
- Configure basic settings

### 📝 Steps

#### Step 1: Install Obsidian

1. Go to https://obsidian.md
2. Download Obsidian for your OS (Windows/Mac/Linux)
3. Install Obsidian
4. Open Obsidian
5. Create new vault: `SmartSecondBrain`

#### Step 2: Install WorkBuddy

1. Go to https://www.codebuddy.cn
2. Download WorkBuddy for your OS
3. Install WorkBuddy
4. Open WorkBuddy
5. Complete initial setup

#### Step 3: Install Smart Second Brain

**Windows:**
```bash
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain
install.bat
```

**Mac/Linux:**
```bash
git clone https://github.com/seeley1/smart-second-brain.git
cd smart-second-brain
bash install.sh
```

#### Step 4: Configure

1. Open `config/config.yaml`
2. Set `vault_path: "/path/to/your/vault"`
3. Set `ai.api_key: "your-api-key"`
4. Save file

### ✅ Checkpoint

After this tutorial, you should have:
- ✅ Obsidian installed and vault created
- ✅ WorkBuddy installed and running
- ✅ Smart Second Brain installed
- ✅ Basic configuration done

### 📤 Next Tutorial

→ [Tutorial 2: Adding Knowledge](#tutorial-2-adding-knowledge)

---

## Tutorial 2: Adding Knowledge

### 🎯 What You'll Learn

- Add knowledge from Douyin
- Add knowledge from WeChat
- Add knowledge from WeChat Reading
- Add knowledge manually

### 📝 Steps

#### Method 1: From Douyin

1. Copy Douyin video link (e.g., `https://v.douyin.com/xxx/`)
2. Paste to WorkBuddy
3. AI will auto-parse and save to `00-Raw/抖音笔记/`

#### Method 2: From WeChat

1. Open WeChat article
2. Click "Share" → "Copy link"
3. Paste link to WorkBuddy
4. AI will auto-extract and save to `00-Raw/公众号文章/`

#### Method 3: From WeChat Reading (Weread)

1. Open WeChat Reading
2. Select book
3. Click "Share" → "Sync to WorkBuddy"
4. AI will auto-import and save to `00-Raw/微信读书/`

#### Method 4: Manual Input

1. Open Obsidian
2. Create new note
3. Use template: `Raw-Layer-Template`
4. Fill in content manually
5. Save to `00-Raw/`

### ✅ Checkpoint

After this tutorial, you should be able to:
- ✅ Add knowledge from Douyin
- ✅ Add knowledge from WeChat
- ✅ Add knowledge from WeChat Reading
- ✅ Add knowledge manually

### 📤 Next Tutorial

→ [Tutorial 3: Processing Knowledge](#tutorial-3-processing-knowledge)

---

## Tutorial 3: Processing Knowledge

### 🎯 What You'll Learn

- Understand three-layer knowledge structure
- Process knowledge automatically (AI)
- Process knowledge manually
- Verify knowledge quality

### 📝 Steps

#### Understand Three-Layer Structure

```
00-Raw (Raw Layer) → 10-Schema (Schema Layer) → 20-Wiki (Wiki Layer)
```

- **00-Raw**: Original materials (unprocessed)
- **10-Schema**: Structured knowledge (parsed)
- **20-Wiki**: Refined output (actionable)

#### Automatic Processing (AI)

AI will automatically:

1. **Parse content** - Extract key information
2. **Generate summary** - Create concise summary
3. **Add tags** - Auto-tag based on content
4. **Create links** - Link to related notes
5. **Move to Schema Layer** - Move from `00-Raw/` to `10-Schema/`

#### Manual Processing

If you want to process manually:

1. Open note in `00-Raw/`
2. Read content
3. Add your own summary (optional)
4. Add custom tags (optional)
5. Move to `10-Schema/` manually

#### Verify Knowledge Quality

Every day at 22:30, AI will:

1. **Check today's new knowledge**
2. **Verify quality** using three methods:
   - Cross-source validation (至少2个独立来源)
   - Generativity validation (能生成具体行动建议)
   - Exclusivity validation (有明显独特价值)
3. **Generate quality report** in `60-Diary/知识质量验证报告/`
4. **Mark low-quality knowledge** for review

### ✅ Checkpoint

After this tutorial, you should understand:
- ✅ Three-layer knowledge structure
- ✅ Automatic processing (AI)
- ✅ Manual processing
- ✅ Knowledge quality verification

### 📤 Next Tutorial

→ [Tutorial 4: Generating Output](#tutorial-4-generating-output)

---

## Tutorial 4: Generating Output

### 🎯 What You'll Learn

- Generate articles (one-click)
- Generate videos (one-click)
- Generate social media content (one-click)

### 📝 Steps

#### Generate Articles (One-Click)

1. **Select knowledge nodes** in Obsidian
2. **Right-click** and select "Generate Article"
3. **AI will**:
   - Synthesize knowledge
   - Generate article draft
   - Save to `20-Wiki/输出成品/`
4. **Edit draft** as needed
5. **Publish** to your blog/platform

#### Generate Videos (One-Click)

1. **Select knowledge nodes** in Obsidian
2. **Right-click** and select "Generate Video Script"
3. **AI will**:
   - Generate video script
   - Generate voice clone (using your voice)
   - Create video with subtitles
4. **Review video**
5. **Upload** to Douyin/YouTube/TikTok

#### Generate Social Media Content (One-Click)

1. **Select knowledge nodes** in Obsidian
2. **Right-click** and select "Generate Social Media Post"
3. **AI will**:
   - Generate post content
   - Adapt to platform style (WeChat, Weibo, Douyin)
   - Add hashtags and mentions
4. **Review post**
5. **Publish** to social media

### ✅ Checkpoint

After this tutorial, you should be able to:
- ✅ Generate articles (one-click)
- ✅ Generate videos (one-click)
- ✅ Generate social media content (one-click)

### 📤 Next Tutorial

→ [Tutorial 5: Automation Tasks](#tutorial-5-automation-tasks)

---

## Tutorial 5: Automation Tasks

### 🎯 What You'll Learn

- Understand 4 automation tasks
- Configure automation tasks
- Run automation tasks manually
- Check automation logs

### 📝 Steps

#### 4 Automation Tasks

1. **Daily Knowledge Sync** (每天10:00)
   - Auto-sync from multiple sources
   - Save to `00-Raw/`

2. **Obsidian Dialog Sync** (每小时)
   - Sync WorkBuddy conversations to Obsidian
   - Save to `10-Schema/对话知识/`

3. **Knowledge Quality Check** (每天22:30)
   - Verify today's new knowledge
   - Generate quality report

4. **Weekly Knowledge Refinement** (每周日20:00)
   - Refine this week's knowledge
   - Generate weekly summary

#### Configure Automation Tasks

1. Open WorkBuddy
2. Go to "Automation" tab
3. Click on task name (e.g., "Daily Knowledge Sync")
4. Edit settings:
   - Schedule (cron expression)
   - Sources (enable/disable)
   - Actions (enable/disable)
5. Click "Save"

#### Run Automation Tasks Manually

1. Open WorkBuddy
2. Go to "Automation" tab
3. Find task (e.g., "Daily Knowledge Sync")
4. Click "Run" button
5. Wait for task to complete
6. Check results in Obsidian

#### Check Automation Logs

1. Open Obsidian
2. Go to `60-Diary/第二大脑系统日志/`
3. Open latest log file (e.g., `2026-06-19-系统执行第XX次.md`)
4. Check log content for errors

### ✅ Checkpoint

After this tutorial, you should be able to:
- ✅ Understand 4 automation tasks
- ✅ Configure automation tasks
- ✅ Run automation tasks manually
- ✅ Check automation logs

### 📤 Next Tutorial

→ [Tutorial 6: Knowledge Graph](#tutorial-6-knowledge-graph)

---

## Tutorial 6: Knowledge Graph

### 🎯 What You'll Learn

- Understand knowledge graph
- Generate knowledge graph
- Use knowledge graph (interactive)
- Customize knowledge graph

### 📝 Steps

#### Understand Knowledge Graph

Knowledge graph is a **visual representation** of your knowledge network:
- **Nodes**: Knowledge notes
- **Edges**: Links between notes
- **Colors**: Note types (核心, 工具, 概念, etc.)
- **Sizes**: Note importance

#### Generate Knowledge Graph

```bash
python scripts/knowledge_graph.py --vault-path "/path/to/your/vault"
```

Output: `output/knowledge_graph.html`

#### Use Knowledge Graph (Interactive)

1. **Open** `output/knowledge_graph.html` in browser
2. **Drag nodes** to rearrange layout
3. **Hover over nodes** to see details
4. **Zoom in/out** to adjust view
5. **Click nodes** to open notes (if integrated with Obsidian)

#### Customize Knowledge Graph

Edit `config/config.yaml`:

```yaml
knowledge_graph:
  enabled: true
  output_path: "output/knowledge_graph.html"
  visualization:
    layout: "force-directed"
    node_size: 20
    edge_thickness: 2
  colors:
    core_node: "#FF6B6B"
    tool_node: "#4ECDC4"
    concept_node: "#45B7D1"
```

### ✅ Checkpoint

After this tutorial, you should be able to:
- ✅ Understand knowledge graph
- ✅ Generate knowledge graph
- ✅ Use knowledge graph (interactive)
- ✅ Customize knowledge graph

### 📤 Next Tutorial

→ [Tutorial 7: Advanced Features](#tutorial-7-advanced-features)

---

## Tutorial 7: Advanced Features

### 🎯 What You'll Learn

- Use voice cloning
- Use batch processing
- Create custom templates
- Integrate with external APIs

### 📝 Steps

#### Use Voice Cloning

**Setup**:
1. Record reference audio (10-30 seconds)
2. Save to `assets/voice/reference.wav`
3. Configure in `config/config.yaml`:
   ```yaml
   voice_clone:
     enabled: true
     engine: "mimo"
     reference_audio: "assets/voice/reference.wav"
   ```

**Usage**:
- When generating video, AI will auto-clone your voice
- Output: MP3 audio file

#### Use Batch Processing

**Purpose**: Process multiple notes at once

**Usage**:
```bash
python scripts/batch_process.py --input-dir "00-Raw/抖音笔记/" --output-dir "10-Schema/抖音笔记/"
```

#### Create Custom Templates

**Purpose**: Create your own note templates

**How**:
1. Create new template in `99-Templates/`
2. Use Obsidian template syntax: `{{title}}`, `{{date}}`, etc.
3. Use template when creating new notes

#### Integrate with External APIs

**Purpose**: Connect to external APIs (for developers)

**How**:
1. Edit `config/config.yaml` with API details
2. Use `scripts/utils.py` to call APIs
3. Extend functionality as needed

### ✅ Checkpoint

After this tutorial, you should be able to:
- ✅ Use voice cloning
- ✅ Use batch processing
- ✅ Create custom templates
- ✅ Integrate with external APIs (for developers)

---

## Next Steps

### 🎓 What's Next?

After completing all tutorials, you should:

1. **Practice** - Add knowledge daily
2. **Experiment** - Try different features
3. **Customize** - Adapt to your needs
4. **Share** - Share with others!

### 📚 Additional Resources

- [README.md](../README.md) - Project introduction
- [Installation-Guide.md](Installation-Guide.md) - Detailed installation
- [User-Manual.md](User-Manual.md) - Detailed usage
- [FAQ.md](FAQ.md) - Frequently asked questions

### 📞 Support

If you need help:

1. Check [FAQ.md](FAQ.md)
2. Open GitHub issue: https://github.com/seeley1/smart-second-brain/issues
3. Contact Seeley: [@seeley1](https://github.com/seeley1)

---

## 📝 Summary

You've completed all **Smart Second Brain** video tutorials! 🎉

You now know how to:
- ✅ Install and configure Smart Second Brain
- ✅ Add knowledge from multiple sources
- ✅ Process knowledge automatically
- ✅ Generate output (articles, videos, social media)
- ✅ Use automation tasks
- ✅ Visualize knowledge with knowledge graph
- ✅ Use advanced features

**Happy knowledge building!** 🧠💡

---

*Video Tutorials for Smart Second Brain*
*Created by Seeley, maintained by WorkBuddy AI Agent*
