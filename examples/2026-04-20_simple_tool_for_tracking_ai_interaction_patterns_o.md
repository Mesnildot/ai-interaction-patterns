# Tracking AI Interaction Patterns: A Simple Logger

After months of daily AI work, I realized I was losing track of what actually worked. Which prompts got good results? What patterns led to frustration? I built a simple tracker that's become surprisingly valuable.

## The Basic Logger

```python
import json
from datetime import datetime
from pathlib import Path

class AIInteractionLogger:
    def __init__(self, log_file="ai_interactions.json"):
        self.log_file = Path(log_file)
        self.interactions = self._load_existing()
    
    def _load_existing(self):
        if self.log_file.exists():
            return json.loads(self.log_file.read_text())
        return []
    
    def log_interaction(self, ai_tool, task_type, prompt_strategy, 
                       outcome, notes="", iterations=1):
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "ai_tool": ai_tool,
            "task_type": task_type,
            "prompt_strategy": prompt_strategy,
            "outcome": outcome,  # "success", "partial", "failed"
            "iterations": iterations,
            "notes": notes
        }
        
        self.interactions.append(interaction)
        self._save()
    
    def _save(self):
        self.log_file.write_text(json.dumps(self.interactions, indent=2))
    
    def get_success_patterns(self, task_type=None):
        filtered = self.interactions
        if task_type:
            filtered = [i for i in filtered if i["task_type"] == task_type]
        
        successful = [i for i in filtered if i["outcome"] == "success"]
        
        # Group by prompt strategy
        patterns = {}
        for interaction in successful:
            strategy = interaction["prompt_strategy"]
            if strategy not in patterns:
                patterns[strategy] = {"count": 0, "avg_iterations": 0}
            
            patterns[strategy]["count"] += 1
            patterns[strategy]["avg_iterations"] += interaction["iterations"]
        
        # Calculate averages
        for strategy in patterns:
            count = patterns[strategy]["count"]
            patterns[strategy]["avg_iterations"] /= count
        
        return patterns
```

## Quick Command-Line Interface

```python
import argparse

def main():
    logger = AIInteractionLogger()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", action="store_true")
    parser.add_argument("--analyze", action="store_true")
    parser.add_argument("--tool", default="chatgpt")
    parser.add_argument("--task")
    parser.add_argument("--strategy")
    parser.add_argument("--outcome", choices=["success", "partial", "failed"])
    parser.add_argument("--notes", default="")
    parser.add_argument("--iterations", type=int, default=1)
    
    args = parser.parse_args()
    
    if args.log:
        logger.log_interaction(
            args.tool, args.task, args.strategy, 
            args.outcome, args.notes, args.iterations
        )
        print("Logged interaction")
    
    elif args.analyze:
        patterns = logger.get_success_patterns(args.task)
        print(f"\nSuccess patterns for {args.task or 'all tasks'}:")
        for strategy, data in sorted(patterns.items(), 
                                   key=lambda x: x[1]["count"], 
                                   reverse=True):
            print(f"  {strategy}: {data['count']} successes, "
                  f"avg {data['avg_iterations']:.1f} iterations")

if __name__ == "__main__":
    main()
```

## Usage Examples

```bash
# Log a successful code generation
python ai_logger.py --log --task "code_generation" \
    --strategy "step_by_step_with_context" --outcome success \
    --iterations 2 --notes "Worked after adding specific requirements"

# Log a failed writing attempt
python ai_logger.py --log --task "technical_writing" \
    --

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-20*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
