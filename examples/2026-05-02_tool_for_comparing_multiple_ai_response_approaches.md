# Comparing AI Response Approaches: A Practical Tool

When you're working with AI daily, you quickly realize that getting the *right* response often means trying multiple approaches. I built a simple comparison tool after spending too many hours manually juggling different prompts and losing track of what worked.

## The Reality Check

Most AI tools give you one shot, one answer. But experienced practitioners know that slight prompt variations can yield dramatically different results. The challenge isn't just generating responses—it's systematically comparing them without losing your mind.

## A Practical Comparison Script

Here's a Python tool I use daily that actually saves time:

```python
import json
import time
from datetime import datetime

class AIResponseComparer:
    def __init__(self):
        self.comparisons = []
    
    def add_approach(self, name, prompt, response, model="gpt-4", notes=""):
        """Add a response approach to compare"""
        approach = {
            "name": name,
            "prompt": prompt,
            "response": response,
            "model": model,
            "timestamp": datetime.now().isoformat(),
            "notes": notes,
            "rating": None
        }
        self.comparisons.append(approach)
        return len(self.comparisons) - 1
    
    def rate_response(self, index, rating, criteria="overall"):
        """Rate a response 1-5 with optional criteria"""
        if 0 <= index < len(self.comparisons):
            if "ratings" not in self.comparisons[index]:
                self.comparisons[index]["ratings"] = {}
            self.comparisons[index]["ratings"][criteria] = rating
    
    def compare_side_by_side(self, indices=None):
        """Display responses side by side for easy comparison"""
        if indices is None:
            indices = list(range(len(self.comparisons)))
        
        print("\n" + "="*80)
        print("AI RESPONSE COMPARISON")
        print("="*80)
        
        for i, idx in enumerate(indices):
            if idx >= len(self.comparisons):
                continue
                
            comp = self.comparisons[idx]
            print(f"\nAPPROACH {idx + 1}: {comp['name']}")
            print("-" * 40)
            print(f"Model: {comp['model']}")
            print(f"Prompt: {comp['prompt'][:100]}{'...' if len(comp['prompt']) > 100 else ''}")
            print(f"\nResponse:\n{comp['response']}\n")
            
            if comp.get('ratings'):
                ratings_str = ", ".join([f"{k}: {v}/5" for k, v in comp['ratings'].items()])
                print(f"Ratings: {ratings_str}")
            
            if comp.get('notes'):
                print(f"Notes: {comp['notes']}")
    
    def export_comparison(self, filename=None):
        """Export to JSON for later analysis"""
        if filename is None:
            filename = f"ai_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.comparisons, f, indent=2)
        print(f"Exported to {filename}")

# Real usage example
comparer = AIResponseComparer()

# Testing different prompt approaches for code review
comparer.add_approach(
    name="Direct Ask",
    prompt="Review this Python code for bugs",
    response="The code looks good overall...",
    notes="Too generic, missed edge cases"
)

comparer.add_approach(
    name="Structured Review",
    prompt="Review this Python code. Check for: 1) Logic errors 2) Edge cases 3) Performance issues 4) Security concerns",
    response="Logic errors: None found. Edge cases: Missing null check on line 15...",
    notes="Much more thorough and actionable"
)

comparer.rate_response(0, 2, "usefulness")
comparer.rate_response(1, 4, "usefulness")

comparer.compare_side_by_side()
```

## What Actually Works

**Multiple quick iterations beat one "perfect" prompt.

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-05-02*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
