# Helper Scripts for Better AI Conversations

After months of daily AI collaboration, I've built small helper scripts that genuinely improve conversation quality. Here are the ones I actually use.

## The Context Bundler

The most useful script packages relevant context automatically:

```python
#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def bundle_context(file_patterns, output_file="context.md"):
    """Gather relevant files for AI conversation context"""
    context = ["# Project Context\n"]
    
    for pattern in file_patterns:
        files = list(Path(".").glob(pattern))
        for file_path in sorted(files):
            if file_path.stat().st_size > 50000:  # Skip huge files
                continue
                
            context.append(f"\n## {file_path}\n")
            try:
                content = file_path.read_text(encoding='utf-8')
                context.append(f"```{file_path.suffix[1:]}\n{content}\n```\n")
            except UnicodeDecodeError:
                context.append("(Binary file - skipped)\n")
    
    Path(output_file).write_text("\n".join(context))
    print(f"Context bundled: {len(files)} files → {output_file}")

if __name__ == "__main__":
    patterns = sys.argv[1:] if len(sys.argv) > 1 else ["*.py", "*.md", "*.yaml"]
    bundle_context(patterns)
```

I run this before complex debugging sessions: `python bundle.py "src/*.py" "*.md"`. The AI gets full project context without me copy-pasting files.

## The Conversation Tracker

Tracking what approaches work prevents repeating failed attempts:

```python
#!/usr/bin/env python3
import json
import datetime
from pathlib import Path

class ConversationLog:
    def __init__(self, log_file="ai_sessions.json"):
        self.log_file = Path(log_file)
        self.sessions = self._load_sessions()
    
    def _load_sessions(self):
        if self.log_file.exists():
            return json.loads(self.log_file.read_text())
        return []
    
    def start_session(self, topic, ai_model="gpt-4"):
        session = {
            "id": len(self.sessions) + 1,
            "topic": topic,
            "model": ai_model,
            "start_time": datetime.datetime.now().isoformat(),
            "approaches": [],
            "outcome": None
        }
        self.sessions.append(session)
        return session["id"]
    
    def log_approach(self, session_id, approach, result):
        session = next(s for s in self.sessions if s["id"] == session_id)
        session["approaches"].append({
            "approach": approach,
            "result": result,
            "timestamp": datetime.datetime.now().isoformat()
        })
        self._save()
    
    def close_session(self, session_id, outcome):
        session = next(s for s in self.sessions if s["id"] == session_id)
        session["outcome"] = outcome
        session["end_time"] = datetime.datetime.now().isoformat()
        self._save()
    
    def _save(self):
        self.log_file.write_text(json.dumps(self.sessions, indent=2))
    
    def search_similar(self, topic_keywords):
        """Find sessions with similar topics"""
        matches = []
        for session in self.sessions:
            topic_lower = session["topic"].lower()
            if any(keyword.lower() in topic_lower for keyword in topic_keywords):
                matches.append({
                    "topic": session["topic"],
                    "successful_approaches": [
                        a["approach"] for a in session["approaches"] 
                        if a["result"] == "success"
                    ],
                    "outcome": session["outcome"]
                })
        return matches

# Usage example
log = ConversationLog()
session_id = log.start_session("Debug React component re-rendering")
log.

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-05-21*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
