# AI Interaction Tracker: A Simple Tool for Pattern Recognition

After months of working with various AI tools daily, I realized I was losing track of what approaches actually worked. I'd have a breakthrough conversation with Claude one day, then struggle to recreate that success the next. So I built a simple tracker that's become genuinely useful.

## The Basic Tool

```python
import json
import datetime
from pathlib import Path

class AIInteractionTracker:
    def __init__(self, log_file="ai_interactions.json"):
        self.log_file = Path(log_file)
        self.interactions = self._load_data()
    
    def _load_data(self):
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return []
    
    def log_interaction(self, ai_tool, task_type, prompt_strategy, 
                       outcome, notes="", effectiveness=None):
        """Log an AI interaction with key metadata"""
        interaction = {
            "timestamp": datetime.datetime.now().isoformat(),
            "ai_tool": ai_tool,
            "task_type": task_type,
            "prompt_strategy": prompt_strategy,
            "outcome": outcome,  # "success", "partial", "failed"
            "effectiveness": effectiveness,  # 1-5 scale
            "notes": notes
        }
        
        self.interactions.append(interaction)
        self._save_data()
    
    def _save_data(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.interactions, f, indent=2)
    
    def get_patterns(self, task_type=None, days_back=30):
        """Find what's working for specific task types"""
        cutoff = datetime.datetime.now() - datetime.timedelta(days=days_back)
        
        filtered = [i for i in self.interactions 
                   if datetime.datetime.fromisoformat(i["timestamp"]) > cutoff]
        
        if task_type:
            filtered = [i for i in filtered if i["task_type"] == task_type]
        
        # Group by prompt strategy and calculate success rates
        strategies = {}
        for interaction in filtered:
            strategy = interaction["prompt_strategy"]
            if strategy not in strategies:
                strategies[strategy] = {"total": 0, "successful": 0, "notes": []}
            
            strategies[strategy]["total"] += 1
            if interaction["outcome"] == "success":
                strategies[strategy]["successful"] += 1
            if interaction["notes"]:
                strategies[strategy]["notes"].append(interaction["notes"])
        
        # Calculate success rates
        for strategy in strategies:
            total = strategies[strategy]["total"]
            successful = strategies[strategy]["successful"]
            strategies[strategy]["success_rate"] = successful / total if total > 0 else 0
        
        return strategies

# Usage example
tracker = AIInteractionTracker()

# Log interactions as they happen
tracker.log_interaction(
    ai_tool="Claude",
    task_type="code_review",
    prompt_strategy="step_by_step_analysis",
    outcome="success",
    effectiveness=4,
    notes="Worked well when I asked it to review security first, then logic"
)

tracker.log_interaction(
    ai_tool="GPT-4",
    task_type="writing",
    prompt_strategy="examples_first",
    outcome="partial",
    effectiveness=3,
    notes="Good structure but tone was off. Need to be more specific about audience"
)

# Analyze patterns
patterns = tracker.get_patterns(task_type="code_review", days_back=14)
for strategy, data in patterns.items():
    print(f"{strategy}: {data['success_rate']:.1%} success rate ({data['total']} attempts)")
```

## What Actually Works

**The good:** This simple tracker revealed that my "examples first" approach works 80% of the time for writing tasks, but only 40% for technical explanations. That insight alone saved me hours of frustration.

**The limitation:** I initially tried tracking everything automatically, but manual logging works better. It forces me to reflect on

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-06-09*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
