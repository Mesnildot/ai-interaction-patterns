# Comparing AI Response Approaches: A Daily Driver Tool

When I'm working on complex problems, I often need to see how different AI approaches stack up. Sometimes the first response isn't the best one, or I want to compare structured vs. conversational outputs. Here's a simple comparison tool I built that's become essential to my workflow.

## The Basic Comparison Script

```python
import json
from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class AIResponse:
    approach: str
    prompt: str
    response: str
    timestamp: str
    metrics: Dict[str, Any] = None

class ResponseComparator:
    def __init__(self):
        self.responses = []
        
    def add_response(self, approach: str, prompt: str, response: str, **metrics):
        """Add a response with optional quality metrics"""
        self.responses.append(AIResponse(
            approach=approach,
            prompt=prompt,
            response=response,
            timestamp=datetime.now().isoformat(),
            metrics=metrics or {}
        ))
    
    def compare_side_by_side(self, max_width=80):
        """Display responses in columns for quick visual comparison"""
        if len(self.responses) < 2:
            print("Need at least 2 responses to compare")
            return
            
        # Truncate responses for side-by-side view
        truncated = []
        for resp in self.responses:
            lines = resp.response.split('\n')[:10]  # First 10 lines
            truncated.append([line[:max_width//len(self.responses)] 
                            for line in lines])
        
        print("=" * max_width)
        print(" | ".join([f"{resp.approach:^{max_width//len(self.responses)}}" 
                         for resp in self.responses]))
        print("=" * max_width)
        
        max_lines = max(len(t) for t in truncated)
        for i in range(max_lines):
            row = []
            for j, resp_lines in enumerate(truncated):
                if i < len(resp_lines):
                    row.append(f"{resp_lines[i]:<{max_width//len(self.responses)}}")
                else:
                    row.append(" " * (max_width//len(self.responses)))
            print(" | ".join(row))
    
    def score_responses(self, criteria: List[str]) -> Dict[str, Dict[str, int]]:
        """Interactive scoring for subjective comparison"""
        scores = {}
        for response in self.responses:
            scores[response.approach] = {}
            print(f"\n--- Scoring {response.approach} ---")
            print(f"Response preview: {response.response[:200]}...")
            
            for criterion in criteria:
                while True:
                    try:
                        score = int(input(f"Rate {criterion} (1-5): "))
                        if 1 <= score <= 5:
                            scores[response.approach][criterion] = score
                            break
                        else:
                            print("Please enter a number between 1 and 5")
                    except ValueError:
                        print("Please enter a valid number")
        return scores
    
    def export_comparison(self, filename: str = None):
        """Save comparison for future reference"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ai_comparison_{timestamp}.json"
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'responses': [
                {
                    'approach': r.approach,
                    'prompt': r.prompt,
                    'response': r.response,
                    'metrics': r.metrics
                } for r in self.responses
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Comparison saved to {filename}")
```

## Practical Usage Example

```python
# Real scenario: Comparing different prompting strategies for code review
comparator = ResponseComparator()

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-04*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
