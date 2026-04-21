# Managing LLM Context: A Practical Utility

When you're deep in a coding session with an AI, context gets messy fast. I built this utility after losing track of conversation state one too many times during complex debugging sessions.

## The Problem

LLMs have token limits, but more importantly, they lose track of what's important. I was constantly re-explaining project structure, re-pasting error logs, and watching the AI forget crucial details from 10 messages ago.

## A Simple Context Manager

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class ContextManager:
    def __init__(self, max_tokens: int = 8000):
        self.max_tokens = max_tokens
        self.context_stack = []
        self.pinned_items = {}
        self.session_summary = ""
    
    def add_context(self, content: str, priority: int = 1, tags: List[str] = None):
        """Add context with priority (1=highest, 3=lowest)"""
        item = {
            'content': content,
            'priority': priority,
            'timestamp': datetime.now().isoformat(),
            'tags': tags or [],
            'token_estimate': len(content.split()) * 1.3  # rough estimate
        }
        self.context_stack.append(item)
        return len(self.context_stack) - 1
    
    def pin_context(self, key: str, content: str):
        """Pin critical info that should always be included"""
        self.pinned_items[key] = {
            'content': content,
            'pinned_at': datetime.now().isoformat()
        }
    
    def build_prompt_context(self) -> str:
        """Build optimized context for the current prompt"""
        # Always include pinned items
        context_parts = []
        
        # Add pinned context
        if self.pinned_items:
            context_parts.append("=== PINNED CONTEXT ===")
            for key, item in self.pinned_items.items():
                context_parts.append(f"[{key}]: {item['content']}")
        
        # Add session summary if it exists
        if self.session_summary:
            context_parts.append(f"=== SESSION SUMMARY ===\n{self.session_summary}")
        
        # Sort context by priority and recency, fit within token limit
        sorted_context = sorted(
            self.context_stack, 
            key=lambda x: (x['priority'], -hash(x['timestamp']))
        )
        
        current_tokens = sum(len(part.split()) * 1.3 for part in context_parts)
        
        context_parts.append("=== RECENT CONTEXT ===")
        for item in sorted_context:
            if current_tokens + item['token_estimate'] > self.max_tokens:
                break
            context_parts.append(f"[{', '.join(item['tags'])}] {item['content']}")
            current_tokens += item['token_estimate']
        
        return "\n\n".join(context_parts)
    
    def summarize_session(self, ai_summary: str):
        """Update session summary (ideally with AI help)"""
        self.session_summary = ai_summary
        # Clear old low-priority context
        self.context_stack = [
            item for item in self.context_stack 
            if item['priority'] <= 2 or 
            (datetime.now() - datetime.fromisoformat(item['timestamp'])).seconds < 3600
        ]
```

## Real Usage Patterns

**For debugging sessions:**
```python
ctx = ContextManager()
ctx.pin_context("error", "TypeError: list indices must be integers, not str")
ctx.pin_context("goal", "Fix user authentication flow")
ctx.add_context("Tried changing line 47, still fails", priority=1, tags=["attempt"])
ctx.add_context("Stack trace shows issue in auth.py:23", priority=1, tags=["clue"])
```

**For code reviews:**
```python
ctx.pin_context("files", "main.py, utils.py, config.py")
ctx.add_

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-21*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
