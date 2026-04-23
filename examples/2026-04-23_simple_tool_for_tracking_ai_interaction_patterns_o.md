# Tracking AI Interaction Patterns: A Simple Daily Logger

After months of bouncing between ChatGPT, Claude, and various coding assistants, I realized I had no clear picture of what was actually working. So I built a dead-simple interaction tracker that's been running for six months now.

## The Basic Logger

```python
import json
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional, List
from pathlib import Path

@dataclass
class AIInteraction:
    timestamp: str
    ai_tool: str  # "gpt4", "claude", "copilot", etc.
    task_type: str  # "code", "writing", "analysis", "brainstorm"
    quality_rating: int  # 1-5 scale
    iterations: int  # how many back-and-forth exchanges
    success: bool  # did you get what you needed?
    notes: Optional[str] = None

class InteractionTracker:
    def __init__(self, log_file: str = "ai_interactions.json"):
        self.log_file = Path(log_file)
        self.interactions = self._load_data()
    
    def _load_data(self) -> List[AIInteraction]:
        if not self.log_file.exists():
            return []
        
        with open(self.log_file, 'r') as f:
            data = json.load(f)
            return [AIInteraction(**item) for item in data]
    
    def log_interaction(self, ai_tool: str, task_type: str, 
                       quality_rating: int, iterations: int, 
                       success: bool, notes: str = None):
        interaction = AIInteraction(
            timestamp=datetime.now().isoformat(),
            ai_tool=ai_tool,
            task_type=task_type,
            quality_rating=quality_rating,
            iterations=iterations,
            success=success,
            notes=notes
        )
        
        self.interactions.append(interaction)
        self._save_data()
        print(f"✓ Logged {ai_tool} interaction for {task_type}")
    
    def _save_data(self):
        data = [asdict(interaction) for interaction in self.interactions]
        with open(self.log_file, 'w') as f:
            json.dump(data, f, indent=2)
```

## Quick Analysis Tools

```python
def analyze_patterns(self):
    if not self.interactions:
        return "No data yet!"
    
    # Success rates by tool
    tools = {}
    for interaction in self.interactions:
        tool = interaction.ai_tool
        if tool not in tools:
            tools[tool] = {'total': 0, 'success': 0, 'avg_quality': 0}
        
        tools[tool]['total'] += 1
        if interaction.success:
            tools[tool]['success'] += 1
        tools[tool]['avg_quality'] += interaction.quality_rating
    
    print("\n📊 Success Rates by Tool:")
    for tool, stats in tools.items():
        success_rate = (stats['success'] / stats['total']) * 100
        avg_quality = stats['avg_quality'] / stats['total']
        print(f"{tool}: {success_rate:.1f}% success, {avg_quality:.1f}/5 quality")
    
    # Task patterns
    task_success = {}
    for interaction in self.interactions:
        task = interaction.task_type
        if task not in task_success:
            task_success[task] = []
        task_success[task].append(interaction.success)
    
    print("\n📝 Task Success Patterns:")
    for task, results in task_success.items():
        success_rate = (sum(results) / len(results)) * 100
        print(f"{task}: {success_rate:.1f}% ({len(results)} attempts)")

# Usage
tracker = InteractionTracker()

# Log an interaction (I do this right after each AI session)
tracker.log_interaction(
    ai_tool="claude",
    task_type="code",
    quality_rating=4,
    iterations=3,

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-23*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
