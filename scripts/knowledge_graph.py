#!/usr/bin/env python3
"""
Smart Second Brain - Knowledge Graph Generator
Generate interactive knowledge graph using D3.js
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict
import re

# Default colors
COLORS = {
    "核心": "#FF6B6B",  # Red
    "工具": "#4ECDC4",  # Teal
    "概念": "#45B7D1",  # Blue
    "主题": "#96CEB4",  # Green
    "人物": "#FECA57",  # Yellow
    "方法": "#FF9FF3",  # Pink
    "项目": "#54A0FF",  # Light blue
    "默认": "#D1D8E0"   # Gray
}

# Default sizes
SIZES = {
    "核心": 25,
    "工具": 18,
    "概念": 18,
    "主题": 20,
    "人物": 15,
    "方法": 16,
    "项目": 22,
    "默认": 15
}

def extract_wikilinks(content):
    """Extract [[wikilinks]] from content"""
    pattern = r'\[\[(.*?)\]\]'
    return re.findall(pattern, content)

def parse_obsidian_vault(vault_path):
    """Parse Obsidian vault and extract knowledge graph data"""
    print(f"📂 Parsing Obsidian vault: {vault_path}")
    
    vault_path = Path(vault_path)
    if not vault_path.exists():
        print(f"  ❌ Vault path not found: {vault_path}")
        return None
    
    # Data structures
    nodes = []
    edges = []
    node_ids = {}
    node_idx = 0
    
    # First pass: collect all notes (nodes)
    print("  📊 Collecting notes...")
    for md_file in vault_path.rglob("*.md"):
        # Skip hidden folders
        if any(part.startswith(".") for part in md_file.parts):
            continue
        
        # Read file
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"  ⚠️ Error reading {md_file}: {e}")
            continue
        
        # Extract title (from filename or first heading)
        title = md_file.stem
        heading_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if heading_match:
            title = heading_match.group(1).strip()
        
        # Extract tags
        tags = re.findall(r'#(\w+)', content)
        
        # Determine node type
        node_type = "默认"
        if "核心" in tags or "Core" in tags:
            node_type = "核心"
        elif "工具" in tags or "Tool" in tags:
            node_type = "工具"
        elif "概念" in tags or "Concept" in tags:
            node_type = "概念"
        elif "主题" in tags or "Topic" in tags:
            node_type = "主题"
        elif "人物" in tags or "Person" in tags:
            node_type = "人物"
        elif "方法" in tags or "Method" in tags:
            node_type = "方法"
        elif "项目" in tags or "Project" in tags:
            node_type = "项目"
        
        # Add node
        nodes.append({
            "id": title,
            "type": node_type,
            "category": tags[0] if tags else "未分类",
            "size": SIZES.get(node_type, 15),
            "color": COLORS.get(node_type, COLORS["默认"]),
            "file_path": str(md_file.relative_to(vault_path)),
            "tags": tags
        })
        
        node_ids[title] = node_idx
        node_idx += 1
    
    print(f"  ✅ Collected {len(nodes)} notes")
    
    # Second pass: extract links (edges)
    print("  🔗 Extracting links...")
    edge_count = 0
    for md_file in vault_path.rglob("*.md"):
        # Skip hidden folders
        if any(part.startswith(".") for part in md_file.parts):
            continue
        
        # Read file
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue
        
        # Get source node
        source_title = md_file.stem
        heading_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if heading_match:
            source_title = heading_match.group(1).strip()
        
        # Extract wikilinks
        links = extract_wikilinks(content)
        
        # Add edges
        for link in links:
            if source_title in node_ids and link in node_ids:
                edges.append({
                    "source": source_title,
                    "target": link,
                    "relation": "link"
                })
                edge_count += 1
    
    print(f"  ✅ Extracted {edge_count} links")
    
    return {
        "nodes": nodes,
        "edges": edges
    }

def generate_d3_html(graph_data, output_path, title="Knowledge Graph"):
    """Generate D3.js HTML file"""
    print(f"📊 Generating D3.js knowledge graph...")
    
    # Create output directory
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Convert to JSON
    graph_json = json.dumps(graph_data, ensure_ascii=False, indent=2)
    
    # HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            overflow: hidden;
        }}
        
        #container {{
            width: 100%;
            height: 100%;
            position: relative;
        }}
        
        #graph {{
            width: 100%;
            height: 100%;
        }}
        
        .node {{
            cursor: pointer;
        }}
        
        .node-text {{
            font-size: 12px;
            fill: #333;
            text-anchor: middle;
            pointer-events: none;
            font-weight: 500;
        }}
        
        .link {{
            stroke: #999;
            stroke-opacity: 0.4;
            stroke-width: 1.5px;
        }}
        
        .tooltip {{
            position: absolute;
            padding: 12px 16px;
            background: rgba(0, 0, 0, 0.9);
            color: white;
            border-radius: 8px;
            font-size: 13px;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s;
            max-width: 300px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        
        .tooltip strong {{
            display: block;
            margin-bottom: 6px;
            font-size: 14px;
            color: #FFD700;
        }}
        
        .tooltip .tags {{
            margin-top: 6px;
            font-size: 11px;
            color: #AAA;
        }}
        
        #controls {{
            position: absolute;
            top: 20px;
            left: 20px;
            background: white;
            padding: 16px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            font-size: 13px;
        }}
        
        #controls h3 {{
            margin-bottom: 12px;
            color: #333;
        }}
        
        .control-group {{
            margin-bottom: 12px;
        }}
        
        .control-group label {{
            display: block;
            margin-bottom: 4px;
            color: #666;
        }}
        
        .control-group input {{
            width: 100%;
        }}
        
        button {{
            padding: 8px 16px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
            margin-right: 8px;
        }}
        
        button:hover {{
            background: #764ba2;
        }}
        
        #legend {{
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: white;
            padding: 16px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            font-size: 12px;
        }}
        
        #legend h4 {{
            margin-bottom: 8px;
            color: #333;
        }}
        
        .legend-item {{
            display: flex;
            align-items: center;
            margin-bottom: 4px;
        }}
        
        .legend-color {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }}
    </style>
</head>
<body>
    <div id="container">
        <svg id="graph"></svg>
        
        <div id="controls">
            <h3>📊 Knowledge Graph Controls</h3>
            
            <div class="control-group">
                <label>🔗 Link Distance: <span id="distance-value">100</span></label>
                <input type="range" id="distance" min="50" max="200" value="100">
            </div>
            
            <div class="control-group">
                <label>🧲 Charge Strength: <span id="charge-value">-300</span></label>
                <input type="range" id="charge" min="-500" max="-100" value="-300">
            </div>
            
            <div>
                <button onclick="resetLayout()">🔄 Reset Layout</button>
                <button onclick="centerGraph()">🎯 Center Graph</button>
            </div>
        </div>
        
        <div id="legend">
            <h4>🏷️ Node Types</h4>
            <div class="legend-item">
                <div class="legend-color" style="background: #FF6B6B;"></div>
                <span>核心 (Core)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #4ECDC4;"></div>
                <span>工具 (Tool)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #45B7D1;"></div>
                <span>概念 (Concept)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #96CEB4;"></div>
                <span>主题 (Topic)</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #FECA57;"></div>
                <span>人物 (Person)</span>
            </div>
        </div>
    </div>
    
    <div class="tooltip" id="tooltip"></div>
    
    <script>
        // Graph data
        const graphData = {graph_json};
        
        // Set up SVG
        const width = window.innerWidth;
        const height = window.innerHeight;
        
        const svg = d3.select("#graph")
            .attr("width", width)
            .attr("height", height);
        
        // Create tooltip
        const tooltip = d3.select("#tooltip");
        
        // Create simulation
        let simulation = d3.forceSimulation(graphData.nodes)
            .force("link", d3.forceLink(graphData.edges)
                .id(d => d.id)
                .distance(100)
            )
            .force("charge", d3.forceManyBody()
                .strength(-300)
            )
            .force("center", d3.forceCenter(width / 2, height / 2))
            .force("collision", d3.forceCollide()
                .radius(d => d.size + 10)
            );
        
        // Create links
        const link = svg.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(graphData.edges)
            .enter()
            .append("line")
            .attr("class", "link");
        
        // Create nodes
        const node = svg.append("g")
            .attr("class", "nodes")
            .selectAll("g")
            .data(graphData.nodes)
            .enter()
            .append("g")
            .attr("class", "node")
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended)
            );
        
        // Add circles to nodes
        node.append("circle")
            .attr("r", d => d.size)
            .attr("fill", d => d.color)
            .attr("stroke", "#FFF")
            .attr("stroke-width", 2);
        
        // Add text to nodes
        node.append("text")
            .attr("class", "node-text")
            .attr("dy", d => d.size + 12)
            .text(d => d.id);
        
        // Add tooltip events
        node.on("mouseover", function(event, d) {{
            tooltip.transition()
                .duration(200)
                .style("opacity", 1);
            
            tooltip.html(`
                <strong>${{d.id}}</strong>
                <div>Type: ${{d.type}}</div>
                <div>Category: ${{d.category}}</div>
                <div class="tags">Tags: ${{d.tags ? d.tags.join(", ") : "None"}}</div>
            `)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 28) + "px");
        }})
        .on("mouseout", function() {{
            tooltip.transition()
                .duration(500)
                .style("opacity", 0);
        }});
        
        // Update positions on simulation tick
        simulation.on("tick", () => {{
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);
            
            node
                .attr("transform", d => `translate(${{d.x}}, ${{d.y}})`);
        }});
        
        // Drag functions
        function dragstarted(event, d) {{
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }}
        
        function dragged(event, d) {{
            d.fx = event.x;
            d.fy = event.y;
        }}
        
        function dragended(event, d) {{
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }}
        
        // Control functions
        function resetLayout() {{
            simulation.force("center", d3.forceCenter(width / 2, height / 2));
            simulation.alpha(1).restart();
        }}
        
        function centerGraph() {{
            simulation.force("center", d3.forceCenter(width / 2, height / 2));
            simulation.alpha(0.5).restart();
        }}
        
        // Update simulation on control change
        d3.select("#distance").on("input", function() {{
            const value = this.value;
            d3.select("#distance-value").text(value);
            simulation.force("link").distance(Number(value));
            simulation.alpha(0.5).restart();
        }});
        
        d3.select("#charge").on("input", function() {{
            const value = this.value;
            d3.select("#charge-value").text(value);
            simulation.force("charge").strength(Number(value));
            simulation.alpha(0.5).restart();
        }});
        
        // Handle window resize
        window.addEventListener("resize", () => {{
            const newWidth = window.innerWidth;
            const newHeight = window.innerHeight;
            
            svg.attr("width", newWidth)
               .attr("height", newHeight);
            
            simulation.force("center", d3.forceCenter(newWidth / 2, newHeight / 2));
            simulation.alpha(0.5).restart();
        }});
    </script>
</body>
</html>"""
    
    # Write HTML file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"  ✅ Generated: {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Knowledge Graph Generator")
    parser.add_argument("--vault-path", required=True, help="Path to Obsidian vault")
    parser.add_argument("--output", default="output/knowledge_graph.html", help="Output HTML file path")
    parser.add_argument("--title", default="Smart Second Brain - Knowledge Graph", help="Title for the graph")
    
    args = parser.parse_args()
    
    print("🧠 Smart Second Brain - Knowledge Graph Generator")
    print("=" * 60)
    
    # Parse vault
    graph_data = parse_obsidian_vault(args.vault_path)
    if not graph_data:
        print("❌ Failed to parse vault")
        return
    
    # Generate HTML
    output_path = generate_d3_html(graph_data, args.output, args.title)
    
    print("\n" + "=" * 60)
    print("✅ Knowledge graph generation complete!")
    print(f"\n📊 Graph statistics:")
    print(f"  - Nodes: {len(graph_data['nodes'])}")
    print(f"  - Edges: {len(graph_data['edges'])}")
    print(f"\n📂 Output file: {output_path}")
    print(f"\n🌐 Open in browser to view the knowledge graph!")

if __name__ == "__main__":
    main()
