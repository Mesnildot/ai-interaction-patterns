# Comparing AI Response Approaches: A Practical Tool

When working with AI daily, you quickly realize that prompt variations can produce wildly different results. I built this simple comparison tool after spending too many hours manually testing different approaches in separate chat windows.

## The Problem

You're working on a task - maybe writing documentation, analyzing data, or debugging code. You have three different prompt strategies in mind, but testing them one by one is tedious and you lose track of which approach worked best.

## A Simple Comparison Framework

Here's a Python tool I use regularly:

```python
import asyncio
import time
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class PromptVariant:
    name: str
    prompt: str
    context: str = ""
    
@dataclass
class ResponseComparison:
    variant_name: str
    response: str
    response_time: float
    tokens_used: int = 0
    rating: int = 0  # User rating 1-5
    notes: str = ""

class AIResponseComparer:
    def __init__(self, ai_client):
        self.client = ai_client
        self.results: List[ResponseComparison] = []
    
    async def test_variants(self, variants: List[PromptVariant], task_context: str = ""):
        """Test multiple prompt variants concurrently"""
        tasks = []
        for variant in variants:
            full_prompt = f"{task_context}\n\n{variant.context}\n\n{variant.prompt}"
            tasks.append(self._get_response(variant.name, full_prompt))
        
        self.results = await asyncio.gather(*tasks)
        return self.results
    
    async def _get_response(self, name: str, prompt: str) -> ResponseComparison:
        start_time = time.time()
        
        # Replace with your AI client call
        response = await self.client.generate(prompt)
        
        return ResponseComparison(
            variant_name=name,
            response=response.text,
            response_time=time.time() - start_time,
            tokens_used=response.usage.total_tokens if hasattr(response, 'usage') else 0
        )
    
    def display_comparison(self):
        """Print side-by-side comparison"""
        print("=" * 80)
        print("AI RESPONSE COMPARISON")
        print("=" * 80)
        
        for i, result in enumerate(self.results, 1):
            print(f"\n--- VARIANT {i}: {result.variant_name} ---")
            print(f"Response time: {result.response_time:.2f}s")
            print(f"Tokens: {result.tokens_used}")
            print(f"Rating: {result.rating}/5")
            print(f"Response:\n{result.response}\n")
            if result.notes:
                print(f"Notes: {result.notes}\n")
    
    def rate_response(self, variant_name: str, rating: int, notes: str = ""):
        """Add user rating and notes"""
        for result in self.results:
            if result.variant_name == variant_name:
                result.rating = rating
                result.notes = notes
                break
```

## Real Usage Example

Here's how I used it yesterday for documentation writing:

```python
# Testing different approaches for API documentation
variants = [
    PromptVariant(
        name="Technical",
        prompt="Write technical API documentation for this endpoint:",
        context="Target audience: experienced developers"
    ),
    PromptVariant(
        name="Beginner-friendly",
        prompt="Explain this API endpoint in simple terms with examples:",
        context="Target audience: new developers, include common pitfalls"
    ),
    PromptVariant(
        name="Problem-focused",
        prompt="Document this API by showing what problems it solves:",
        context="Start with use cases, then show implementation"
    )
]

comparer = AIResponseComparer(my_ai_client)
await comparer.test_variants(variants, "Endpoint: GET /users/{id}/preferences")

# Rate the results after reviewing
comparer.rate_response("Beginner-

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-06-07*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
