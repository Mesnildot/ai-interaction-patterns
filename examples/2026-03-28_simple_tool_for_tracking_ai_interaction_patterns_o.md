# Simple AI Interaction Pattern Tracker

After months of jumping between different AI tools, I realized I was making the same mistakes repeatedly. I'd rediscover good prompts by accident, forget which models worked best for specific tasks, and waste time on approaches I'd already proven ineffective.

Here's a dead-simple tracker I built to capture patterns that actually matter:

## Basic Python Implementation

```python
import json
import datetime
from pathlib import Path

class AITracker:
    def __init__(self, log_file="ai_interactions.json"):
        self.log_file = Path(log_file)
        self.data = self._load_data()
    
    def _load_data(self):
        if self.log_file.exists():
            return json.loads(self.log_file.read_text())
        return {"sessions": []}
    
    def log_interaction(self, tool, task_type, prompt_snippet, outcome, notes=""):
        """Log a single AI interaction with context"""
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "tool": tool,  # "claude", "gpt4", "copilot", etc.
            "task_type": task_type,  # "code_review", "debugging", "writing"
            "prompt_snippet": prompt_snippet[:100] + "...",  # First 100 chars
            "outcome": outcome,  # "success", "partial", "failure"
            "notes": notes
        }
        
        self.data["sessions"].append(entry)
        self._save_data()
    
    def _save_data(self):
        self.log_file.write_text(json.dumps(self.data, indent=2))
    
    def get_patterns(self, days=30):
        """Find patterns in recent interactions"""
        cutoff = datetime.datetime.now() - datetime.timedelta(days=days)
        recent = [s for s in self.data["sessions"] 
                 if datetime.datetime.fromisoformat(s["timestamp"]) > cutoff]
        
        # Success rates by tool
        tool_stats = {}
        for session in recent:
            tool = session["tool"]
            if tool not in tool_stats:
                tool_stats[tool] = {"success": 0, "total": 0}
            tool_stats[tool]["total"] += 1
            if session["outcome"] == "success":
                tool_stats[tool]["success"] += 1
        
        for tool, stats in tool_stats.items():
            rate = stats["success"] / stats["total"] if stats["total"] > 0 else 0
            print(f"{tool}: {rate:.1%} success rate ({stats['total']} attempts)")
```

## Usage Example

```python
tracker = AITracker()

# After each significant AI interaction
tracker.log_interaction(
    tool="claude",
    task_type="code_review", 
    prompt_snippet="Review this Python function for edge cases...",
    outcome="success",
    notes="Good at catching off-by-one errors, missed performance issue"
)

# Weekly pattern review
tracker.get_patterns(days=7)
```

## What Actually Gets Tracked

I focus on three things that move the needle:

1. **Tool effectiveness by task type** - Claude crushes code analysis but GPT-4 handles creative writing better
2. **Prompt patterns that consistently work** - "Act as [specific role]" vs "Help me with [vague request]"  
3. **Common failure modes** - When does the AI completely miss the point?

## Limitations & Reality Checks

This is deliberately minimal. It won't automatically parse your conversations or generate fancy charts. You have to manually log interactions, which means you'll only capture maybe 20% of them. That's fine - the act of consciously reflecting on what worked is half the value.

The real insight comes from reviewing patterns weekly. I discovered I was using the wrong tool for technical documentation (switched from GPT-4 to Claude, huge improvement) and that my debugging prompts were way too vague.

Start simple. Track for two weeks. The patterns that matter will become obvious.

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-03-28*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
