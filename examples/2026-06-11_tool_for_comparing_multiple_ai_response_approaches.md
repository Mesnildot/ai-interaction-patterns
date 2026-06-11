# Comparing AI Response Approaches: A Practical Tool

When working with multiple AI models or testing different prompting strategies, manually comparing outputs gets messy fast. I've been using a simple comparison tool that's saved me hours of copying, pasting, and losing track of which approach worked best.

## The Reality of AI Response Testing

Here's what I've learned: you need to test at least 3-4 different approaches to find what actually works. Maybe it's different models (GPT-4 vs Claude), different prompt structures, or various temperature settings. Without a systematic way to compare, you'll end up with browser tabs everywhere and no clear winner.

## A Simple Comparison Script

```python
import json
from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class AIResponse:
    approach_name: str
    prompt: str
    response: str
    model: str
    timestamp: str
    metadata: Dict[str, Any] = None

class AIResponseComparer:
    def __init__(self):
        self.responses = []
        
    def add_response(self, approach_name: str, prompt: str, 
                    response: str, model: str, **metadata):
        """Add a response to compare"""
        ai_response = AIResponse(
            approach_name=approach_name,
            prompt=prompt,
            response=response,
            model=model,
            timestamp=datetime.now().isoformat(),
            metadata=metadata
        )
        self.responses.append(ai_response)
        
    def compare_lengths(self):
        """Quick length comparison - often tells you a lot"""
        print("Response Lengths:")
        for resp in self.responses:
            print(f"{resp.approach_name}: {len(resp.response)} chars")
            
    def side_by_side(self, max_width=50):
        """Display responses side by side"""
        if len(self.responses) < 2:
            print("Need at least 2 responses to compare")
            return
            
        # Truncate for readability
        truncated = []
        for resp in self.responses:
            lines = resp.response.split('\n')[:10]  # First 10 lines
            truncated.append([line[:max_width] for line in lines])
            
        max_lines = max(len(t) for t in truncated)
        
        # Print headers
        header = " | ".join(f"{resp.approach_name[:max_width]:<{max_width}}" 
                           for resp in self.responses)
        print(header)
        print("-" * len(header))
        
        # Print content side by side
        for i in range(max_lines):
            row = []
            for j, resp_lines in enumerate(truncated):
                if i < len(resp_lines):
                    row.append(f"{resp_lines[i]:<{max_width}}")
                else:
                    row.append(" " * max_width)
            print(" | ".join(row))
            
    def export_comparison(self, filename: str):
        """Export all responses for detailed analysis"""
        export_data = {
            'comparison_date': datetime.now().isoformat(),
            'responses': [
                {
                    'approach': resp.approach_name,
                    'model': resp.model,
                    'prompt': resp.prompt,
                    'response': resp.response,
                    'timestamp': resp.timestamp,
                    'metadata': resp.metadata
                }
                for resp in self.responses
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        print(f"Comparison exported to {filename}")

# Usage example
if __name__ == "__main__":
    comparer = AIResponseComparer()
    
    # Add different approaches
    comparer.add_response(
        "Direct Ask",
        "Explain machine learning",
        "Machine learning is a subset of AI...",
        "gpt-4",
        temperature=0.7
    )
    
    comparer.add_response(
        "Step-by-step",
        "Explain machine learning step by step with examples",

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-06-11*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
