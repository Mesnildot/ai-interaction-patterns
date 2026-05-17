# Managing Context in LLM Interactions

Working with AI tools daily means constantly juggling context - what the AI remembers, what it forgets, and how to maintain coherent conversations across sessions. Here's a practical utility I've developed after countless frustrating "wait, what were we talking about?" moments.

## Basic Context Manager

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class ContextManager:
    def __init__(self, max_context_length: int = 8000):
        self.max_length = max_context_length
        self.conversation_history: List[Dict] = []
        self.pinned_context: Dict = {}
        self.session_metadata = {}
    
    def add_exchange(self, user_input: str, ai_response: str, 
                    importance: int = 1):
        """Add a user-AI exchange with importance weighting"""
        exchange = {
            'timestamp': datetime.now().isoformat(),
            'user': user_input,
            'assistant': ai_response,
            'importance': importance,
            'tokens': len(user_input + ai_response) // 4  # rough estimate
        }
        self.conversation_history.append(exchange)
        self._trim_context()
    
    def pin_context(self, key: str, value: str):
        """Pin important context that should persist"""
        self.pinned_context[key] = {
            'content': value,
            'created': datetime.now().isoformat()
        }
    
    def get_context_summary(self) -> str:
        """Generate a context summary for new conversations"""
        summary = []
        
        # Add pinned context first
        if self.pinned_context:
            summary.append("PINNED CONTEXT:")
            for key, data in self.pinned_context.items():
                summary.append(f"- {key}: {data['content']}")
            summary.append("")
        
        # Add recent important exchanges
        recent_important = [
            ex for ex in self.conversation_history[-10:] 
            if ex['importance'] > 1
        ]
        
        if recent_important:
            summary.append("RECENT CONTEXT:")
            for exchange in recent_important:
                summary.append(f"Q: {exchange['user'][:100]}...")
                summary.append(f"A: {exchange['assistant'][:150]}...")
                summary.append("")
        
        return "\n".join(summary)
    
    def _trim_context(self):
        """Keep context under token limit, preserving important exchanges"""
        total_tokens = sum(ex['tokens'] for ex in self.conversation_history)
        
        while total_tokens > self.max_length and len(self.conversation_history) > 5:
            # Remove least important, oldest exchanges first
            self.conversation_history.sort(
                key=lambda x: (x['importance'], x['timestamp'])
            )
            removed = self.conversation_history.pop(0)
            total_tokens -= removed['tokens']
```

## Practical Usage Patterns

```python
# Initialize for a coding project
context = ContextManager()
context.pin_context("project", "Building a Python web scraper for job listings")
context.pin_context("tech_stack", "Python, BeautifulSoup, SQLite, FastAPI")

# Mark important exchanges
context.add_exchange(
    "How should I handle rate limiting?", 
    "Use exponential backoff with random jitter...",
    importance=3  # High importance - architectural decision
)

# Regular exchanges get default importance
context.add_exchange(
    "What's the syntax for SQLite INSERT?",
    "INSERT INTO table_name (col1, col2) VALUES (?, ?)",
    importance=1
)

# When starting a new session or tool
context_prompt = f"""
{context.get_context_summary()}

CURRENT TASK: Continue working on the web scraper, focusing on error handling.
"""
```

## What Works and What Doesn't

**Works well:**
- Pinning project context prevents having to re-explain everything
- Importance weighting keeps architectural decisions while dropping syntax questions
- Token estimation (rough as it is) prevents context bloat

**Limitations I've

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-05-17*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
