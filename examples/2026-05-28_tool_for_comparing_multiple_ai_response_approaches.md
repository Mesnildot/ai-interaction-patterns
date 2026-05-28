# Comparing Multiple AI Response Approaches: A Practical Tool

When working with AI daily, I often find myself asking the same question in different ways to see which approach yields better results. Rather than juggling multiple browser tabs or losing track of variations, I built a simple comparison tool that's become essential to my workflow.

## The Core Problem

AI responses can vary dramatically based on:
- Prompt phrasing
- Context length
- Temperature settings
- Model choice

Without systematic comparison, you end up with gut feelings instead of data about what actually works.

## A Simple Comparison Framework

```python
import json
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class AIResponse:
    prompt: str
    response: str
    model: str
    timestamp: str
    quality_score: int  # 1-5 rating you assign
    notes: str = ""
    
class ResponseComparer:
    def __init__(self):
        self.responses = []
        
    def add_response(self, prompt: str, response: str, model: str, 
                    quality_score: int, notes: str = ""):
        """Add a response for comparison"""
        self.responses.append(AIResponse(
            prompt=prompt,
            response=response,
            model=model,
            timestamp=datetime.now().isoformat(),
            quality_score=quality_score,
            notes=notes
        ))
    
    def compare_by_task(self, task_name: str) -> Dict[str, Any]:
        """Compare all responses for a specific task"""
        task_responses = [r for r in self.responses if task_name.lower() in r.prompt.lower()]
        
        if not task_responses:
            return {"error": f"No responses found for task: {task_name}"}
        
        # Sort by quality score
        ranked = sorted(task_responses, key=lambda x: x.quality_score, reverse=True)
        
        return {
            "task": task_name,
            "total_attempts": len(ranked),
            "best_approach": {
                "prompt": ranked[0].prompt,
                "score": ranked[0].quality_score,
                "model": ranked[0].model,
                "notes": ranked[0].notes
            },
            "score_distribution": self._get_score_stats(ranked),
            "all_attempts": [asdict(r) for r in ranked]
        }
    
    def _get_score_stats(self, responses: List[AIResponse]) -> Dict[str, float]:
        scores = [r.quality_score for r in responses]
        return {
            "average": sum(scores) / len(scores),
            "highest": max(scores),
            "lowest": min(scores)
        }
    
    def export_findings(self, filename: str):
        """Save all comparisons for future reference"""
        data = {
            "export_date": datetime.now().isoformat(),
            "total_responses": len(self.responses),
            "responses": [asdict(r) for r in self.responses]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
```

## Real Usage Example

```python
# Initialize comparer
comparer = ResponseComparer()

# Test different code review approaches
comparer.add_response(
    prompt="Review this Python function for bugs",
    response="The function looks good overall...",
    model="gpt-4",
    quality_score=3,
    notes="Generic response, missed edge cases"
)

comparer.add_response(
    prompt="Act as a senior Python developer. Review this function for bugs, security issues, and performance problems. Focus on edge cases:",
    response="Several issues found: 1) No input validation...",
    model="gpt-4", 
    quality_score=5,
    notes="Specific role + explicit areas to check = much better results"
)

# Compare results
results = comparer.compare_by_task("code review")
print(f"Best approach scored {results['best_approach']['score']}/5")
print(f"Winning prompt: {results['best_approach']['prompt']}")
```

## What Actually

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-05-28*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
