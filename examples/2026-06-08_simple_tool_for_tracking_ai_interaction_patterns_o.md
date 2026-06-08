# Tracking Your AI Interaction Patterns: A Simple Logger

After six months of working with various AI tools daily, I realized I was losing track of what actually worked. Which prompts got me better code reviews? What reasoning chains helped with complex problems? I built this simple tracker to capture patterns over time.

## The Basic Logger

```python
import json
import datetime
from pathlib import Path

class AIInteractionLogger:
    def __init__(self, log_file="ai_interactions.json"):
        self.log_file = Path(log_file)
        self.interactions = self._load_existing()
    
    def _load_existing(self):
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return []
    
    def log_interaction(self, tool, task_type, approach, outcome, notes=""):
        interaction = {
            "timestamp": datetime.datetime.now().isoformat(),
            "tool": tool,  # "claude", "gpt4", "copilot"
            "task_type": task_type,  # "code_review", "debugging", "writing"
            "approach": approach,  # brief description of your method
            "outcome": outcome,  # "success", "partial", "failed"
            "notes": notes,
            "session_id": f"{datetime.date.today()}_{len(self.interactions)}"
        }
        
        self.interactions.append(interaction)
        self._save()
        return interaction
    
    def _save(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.interactions, f, indent=2)
    
    def get_success_patterns(self, task_type=None):
        """Find approaches that work consistently"""
        successful = [i for i in self.interactions 
                     if i['outcome'] == 'success']
        
        if task_type:
            successful = [i for i in successful 
                         if i['task_type'] == task_type]
        
        # Group by approach
        patterns = {}
        for interaction in successful:
            approach = interaction['approach']
            if approach not in patterns:
                patterns[approach] = []
            patterns[approach].append(interaction)
        
        return {k: v for k, v in patterns.items() if len(v) >= 2}
```

## Usage in Practice

```python
# Initialize once
logger = AIInteractionLogger()

# Log after each significant AI interaction
logger.log_interaction(
    tool="claude",
    task_type="code_review",
    approach="Ask for specific focus areas first, then general review",
    outcome="success",
    notes="Got much more targeted feedback when I specified what to look for"
)

logger.log_interaction(
    tool="gpt4",
    task_type="debugging",
    approach="Share error + relevant code + what I already tried",
    outcome="success",
    notes="Including failed attempts saved 3 back-and-forth messages"
)

# Find what's working
patterns = logger.get_success_patterns("code_review")
for approach, examples in patterns.items():
    print(f"Approach: {approach}")
    print(f"Success count: {len(examples)}")
    print("---")
```

## Simple Analysis Helper

```python
def analyze_patterns(self, days=30):
    """Quick analysis of recent patterns"""
    cutoff = datetime.datetime.now() - datetime.timedelta(days=days)
    recent = [i for i in self.interactions 
              if datetime.datetime.fromisoformat(i['timestamp']) > cutoff]
    
    success_rate = len([i for i in recent if i['outcome'] == 'success']) / len(recent)
    
    tool_performance = {}
    for interaction in recent:
        tool = interaction['tool']
        if tool not in tool_performance:
            tool_performance[tool] = {'total': 0, 'success': 0}
        
        tool_performance[tool]['total'] += 1
        if interaction['outcome'] == 'success':
            tool_performance[tool]['success'] += 1
    
    return {
        'overall_success

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-06-08*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
