# Quick Scripts to Level Up Your AI Conversations

I've been using AI tools for code, writing, and analysis for over a year. The biggest quality jump came from building simple helper scripts that prep conversations properly. Here are three that actually make a difference.

## The Context Builder

```python
#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def build_context(project_dir=".", include_patterns=None):
    """Build focused context for AI conversations"""
    if include_patterns is None:
        include_patterns = ["*.py", "*.js", "*.md", "*.yml", "*.json"]
    
    context = []
    project_path = Path(project_dir)
    
    # Add project structure first
    context.append("## Project Structure")
    for root, dirs, files in os.walk(project_path):
        # Skip common noise directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
        level = root.replace(str(project_path), '').count(os.sep)
        indent = ' ' * 2 * level
        context.append(f'{indent}{os.path.basename(root)}/')
    
    # Add relevant file contents
    context.append("\n## Key Files")
    for pattern in include_patterns:
        for file_path in project_path.rglob(pattern):
            if file_path.stat().st_size > 50000:  # Skip huge files
                continue
            context.append(f"\n### {file_path}")
            try:
                context.append("```")
                context.append(file_path.read_text()[:5000])  # Truncate long files
                context.append("```")
            except UnicodeDecodeError:
                context.append("(binary file)")
    
    return "\n".join(context)

if __name__ == "__main__":
    project = sys.argv[1] if len(sys.argv) > 1 else "."
    print(build_context(project))
```

This saved me from constantly copying/pasting files. I pipe the output directly into AI conversations: `./context_builder.py | pbcopy` on Mac.

## The Conversation Formatter

```bash
#!/bin/bash
# format_ai_chat.sh - Clean up messy AI conversation logs

input_file=${1:-/dev/stdin}
temp_file=$(mktemp)

# Remove timestamp clutter and format exchanges
sed -E 's/^[0-9]{2}:[0-9]{2}:[0-9]{2}//g' "$input_file" |
sed -E 's/^(Human|Assistant|User|AI):/\n## \1\n/g' |
sed '/^$/N;/^\n$/d' |  # Remove double empty lines
awk 'BEGIN{print "# Conversation Log\n"} {print}' > "$temp_file"

# Add separators between major topics
awk '
/^## Human/ && NR > 1 {print "\n---\n"}
{print}
' "$temp_file"

rm "$temp_file"
```

Real talk: AI conversation logs get messy fast. This script turns chaotic chat exports into readable markdown that I can actually reference later.

## The Quick Prompt Builder

```python
#!/usr/bin/env python3
import argparse

PROMPT_TEMPLATES = {
    "debug": "I'm debugging {issue}. Here's the relevant code:\n\n{code}\n\nThe error is: {error}\n\nWhat I've tried: {attempts}",
    "review": "Please review this {type} for:\n- Logic errors\n- Best practices\n- Performance issues\n\n{code}",
    "explain": "Explain this {language} code like I'm {level}:\n\n{code}",
    "optimize": "How can I optimize this {aspect}?\n\nCurrent approach:\n{code}\n\nConstraints: {constraints}"
}

def build_prompt():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", choices=PROMPT_TEMPLATES.keys())
    parser.add_argument("--interactive", "-

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-05-29*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
