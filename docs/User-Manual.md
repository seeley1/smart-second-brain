# Smart Second Brain - User Manual

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Core Concepts](#core-concepts)
3. [Adding Knowledge](#adding-knowledge)
4. [Processing Knowledge](#processing-knowledge)
5. [Generating Output](#generating-output)
6. [Automation Tasks](#automation-tasks)
7. [Knowledge Graph](#knowledge-graph)
8. [Advanced Features](#advanced-features)
9. [Tips and Tricks](#tips-and-tricks)

---

## Getting Started

### First Run

1. **Open Obsidian** and select your Smart Second Brain vault
2. **Check folder structure** - You should see:
   - `00-Raw/`
   - `10-Schema/`
   - `20-Wiki/`
   - `99-Templates/`
3. **Open WorkBuddy** and check automation tasks:
   - Daily Knowledge Sync
   - Obsidian Dialog Sync
   - Knowledge Quality Check
   - Weekly Knowledge Refinement

### First Knowledge Entry

**Method 1: From Douyin**
1. Copy Douyin video link
2. Paste to WorkBuddy
3. AI will auto-parse and save to `00-Raw/抖音笔记/`

**Method 2: From WeChat**
1. Share WeChat article to WorkBuddy
2. AI will auto-extract and save to `00-Raw/公众号文章/`

**Method 3: Manual Input**
1. Create new note in Obsidian
2. Use template `Raw-Layer-Template`
3. Fill in content manually

---

## Core Concepts

### Three-Layer Knowledge Structure

#### 00-Raw (Raw Layer)
- **Purpose**: Store original materials
- **Content**: Unprocessed, raw content
- **Examples**: Douyin video notes, WeChat articles, WeChat Reading notes
- **Action**: Add here first

#### 10-Schema (Schema Layer)
- **Purpose**: Store structured knowledge
- **Content**: Parsed, organized, tagged
- **Examples**: Parsed articles, structured notes, tagged content
- **Action**: AI auto-processes from Raw Layer

#### 20-Wiki (Wiki Layer)
- **Purpose**: Store refined output
- **Content**: Synthesized, actionable knowledge
- **Examples**: Refined articles, how-to guides, output-ready content
- **Action**: AI auto-refines from Schema Layer

### Knowledge Flow

```
Input (Multi-Source) → 00-Raw → 10-Schema → 20-Wiki → Output (Multi-Format)
```

---

## Adding Knowledge

### From Douyin

1. **Copy video link** (e.g., `https://v.douyin.com/xxx/`)
2. **Paste to WorkBuddy**
3. **AI will**:
   - Parse video content
   - Extract key information
   - Generate summary
   - Save to `00-Raw/抖音笔记/`

### From WeChat Official Accounts

1. **Share article** to WorkBuddy
2. **AI will**:
   - Extract article content
   - Remove ads and irrelevant content
   - Generate summary
   - Save to `00-Raw/公众号文章/`

### From WeChat Reading (Weread)

1. **Sync reading notes** via WorkBuddy
2. **AI will**:
   - Import highlights and notes
   - Organize by book
   - Generate reading summary
   - Save to `00-Raw/微信读书/`

### From IMA Knowledge Base

1. **Upload files** to IMA
2. **AI will**:
   - Sync to `10-Schema/ima知识库/`
   - Parse and structure content
   - Add tags and links

### Manual Input

1. **Create new note** in Obsidian
2. **Use template** `Raw-Layer-Template`
3. **Fill in**:
   - Title
   - Source
   - Tags
   - Content
4. **Save to** `00-Raw/` appropriate subfolder

---

## Processing Knowledge

### Automatic Processing

AI will automatically:

1. **Parse content** - Extract key information
2. **Generate summary** - Create concise summary
3. **Add tags** - Auto-tag based on content
4. **Create links** - Link to related notes
5. **Move to Schema Layer** - Move from `00-Raw/` to `10-Schema/`

### Manual Processing

If you want to process manually:

1. **Open note** in `00-Raw/`
2. **Read content**
3. **Add your own summary** (optional)
4. **Add custom tags** (optional)
5. **Move to** `10-Schema/` manually

### Quality Verification

Every day at 22:30, AI will:

1. **Check today's new knowledge**
2. **Verify quality** using three methods:
   - Cross-source validation (至少2个独立来源)
   - Generativity validation (能生成具体行动建议)
   - Exclusivity validation (有明显独特价值)
3. **Generate quality report** in `60-Diary/知识质量验证报告/`
4. **Mark low-quality knowledge** for review

---

## Generating Output

### One-Click Article

1. **Select knowledge nodes** in Obsidian
2. **Right-click** and select "Generate Article"
3. **AI will**:
   - Synthesize knowledge
   - Generate article draft
   - Save to `20-Wiki/输出成品/`
4. **Edit draft** as needed
5. **Publish** to your blog/platform

### One-Click Video

1. **Select knowledge nodes** in Obsidian
2. **Right-click** and select "Generate Video Script"
3. **AI will**:
   - Generate video script
   - Generate voice clone (using your voice)
   - Create video with subtitles
4. **Review video**
5. **Upload** to Douyin/YouTube/TikTok

### One-Click Social Media

1. **Select knowledge nodes** in Obsidian
2. **Right-click** and select "Generate Social Media Post"
3. **AI will**:
   - Generate post content
   - Adapt to platform style (WeChat, Weibo, Douyin)
   - Add hashtags and mentions
4. **Review post**
5. **Publish** to social media

---

## Automation Tasks

### 1. Daily Knowledge Sync

- **Schedule**: Every day at 10:00
- **Action**:
  - Sync from Douyin, WeChat, Weread, IMA
  - Parse and save to `00-Raw/`
- **Notification**: Desktop notification when complete

### 2. Obsidian Dialog Sync

- **Schedule**: Every hour
- **Trigger**: Keywords (knowledge, note, summary)
- **Action**:
  - Sync WorkBuddy conversations to Obsidian
  - Classify by keywords
  - Save to `10-Schema/对话知识/`
- **Notification**: Desktop notification when complete

### 3. Knowledge Quality Check

- **Schedule**: Every day at 22:30
- **Scope**: Today's new knowledge
- **Action**:
  - Verify quality using three methods
  - Generate quality report
  - Mark low-quality knowledge
- **Notification**: Desktop notification when complete

### 4. Weekly Knowledge Refinement

- **Schedule**: Every Sunday at 20:00
- **Scope**: This week's knowledge
- **Action**:
  - Merge related notes
  - Update knowledge links
  - Generate weekly summary
  - Update knowledge graph
- **Notification**: Desktop notification when complete

---

## Knowledge Graph

### What is Knowledge Graph?

Knowledge graph is a **visual representation** of your knowledge network:
- **Nodes**: Knowledge notes
- **Edges**: Links between notes
- **Colors**: Note types (核心, 工具, 概念, etc.)
- **Sizes**: Note importance

### Generating Knowledge Graph

```bash
python scripts/knowledge_graph.py --vault-path "/path/to/your/vault"
```

Output: `output/knowledge_graph.html`

### Using Knowledge Graph

1. **Open** `output/knowledge_graph.html` in browser
2. **Drag nodes** to rearrange layout
3. **Hover over nodes** to see details
4. **Zoom in/out** to adjust view
5. **Click nodes** to open notes (if integrated with Obsidian)

### Customizing Knowledge Graph

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

---

## Advanced Features

### Voice Cloning

**Purpose**: Generate personalized voice for videos

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

### Batch Processing

**Purpose**: Process multiple notes at once

**Usage**:
```bash
python scripts/batch_process.py --input-dir "00-Raw/抖音笔记/" --output-dir "10-Schema/抖音笔记/"
```

### Custom Templates

**Purpose**: Create your own note templates

**How**:
1. Create new template in `99-Templates/`
2. Use Obsidian template syntax: `{{title}}`, `{{date}}`, etc.
3. Use template when creating new notes

### API Integration

**Purpose**: Connect to external APIs (for developers)

**How**:
1. Edit `config/config.yaml` with API details
2. Use `scripts/utils.py` to call APIs
3. Extend functionality as needed

---

## Tips and Tricks

### Tip 1: Use Consistent Tags

- Always use the same tags for similar content
- This makes searching and linking easier
- Example: `#AI`, `#投资`, `#电商`

### Tip 2: Review Weekly Summary

- Every Sunday, review weekly summary
- Identify knowledge gaps
- Plan next week's learning

### Tip 3: Use Knowledge Graph for Inspiration

- Open knowledge graph
- Look for **unconnected nodes** - these are opportunities for new connections
- Look for **dense clusters** - these are your core expertise areas

### Tip 4: Customize Automation Tasks

- Don't like the default schedule? Change it!
- Open WorkBuddy → Automation → Edit task
- Adjust schedule, sources, actions

### Tip 5: Backup Regularly

- Use Git to version control your vault
- Or use Obsidian Sync / iCloud / OneDrive
- Backup to external drive monthly

### Tip 6: Start Small

- Don't try to add ALL knowledge at once
- Start with ONE source (e.g., Douyin)
- Get comfortable, then add more sources

### Tip 7: Use Keyboard Shortcuts

- Obsidian has many shortcuts
- Learn common ones: `Ctrl+N` (new note), `Ctrl+O` (open note), `Ctrl+Shift+F` (search)
- Saves time!

---

## 📞 Support

If you have questions:

1. Check [FAQ.md](FAQ.md)
2. Check [Installation-Guide.md](Installation-Guide.md)
3. Open an issue on GitHub: https://github.com/seeley1/smart-second-brain/issues
4. Contact Seeley: [@seeley1](https://github.com/seeley1)

---

## 📝 Summary

You now know how to:

1. ✅ Add knowledge from multiple sources
2. ✅ Process knowledge automatically/manually
3. ✅ Generate output (articles, videos, social media)
4. ✅ Use automation tasks
5. ✅ Generate and use knowledge graph
6. ✅ Use advanced features (voice clone, batch processing)
7. ✅ Apply tips and tricks

**Next Steps**:

1. Start adding knowledge!
2. Experiment with different features
3. Customize to fit your needs
4. Share with others!

---

*User Manual for Smart Second Brain*
*Created by Seeley, maintained by WorkBuddy AI Agent*
