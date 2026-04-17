# Comparing AI Response Approaches: A Practical Tool

When working with AI daily, you quickly realize that the same prompt can yield dramatically different results depending on how you frame it. I built a simple comparison tool after spending too many hours manually testing variations and losing track of what worked.

## The Problem

I was helping a client optimize their customer support responses. One approach used direct instructions, another used few-shot examples, and a third combined both with role-playing. Tracking which approach worked best for different scenarios became a mess of browser tabs and scattered notes.

## A Simple Comparison Framework

Here's the tool I use now - nothing fancy, just systematic:

```python
class AIResponseComparator:
    def __init__(self):
        self.approaches = {}
        self.results = []
    
    def add_approach(self, name, prompt_template, description=""):
        """Add a new prompting approach to compare"""
        self.approaches[name] = {
            'template': prompt_template,
            'description': description,
            'results': []
        }
    
    def test_scenario(self, scenario_name, input_data):
        """Test all approaches against a specific scenario"""
        print(f"\n=== Testing: {scenario_name} ===")
        scenario_results = {'scenario': scenario_name, 'input': input_data}
        
        for approach_name, approach in self.approaches.items():
            # Format the prompt with input data
            formatted_prompt = approach['template'].format(**input_data)
            
            print(f"\n--- {approach_name} ---")
            print(f"Prompt: {formatted_prompt[:100]}...")
            
            # Here you'd call your AI service
            response = self.get_ai_response(formatted_prompt)
            
            result = {
                'approach': approach_name,
                'prompt': formatted_prompt,
                'response': response,
                'length': len(response),
                'evaluation': self.quick_evaluate(response, scenario_name)
            }
            
            approach['results'].append(result)
            scenario_results[approach_name] = result
            
        self.results.append(scenario_results)
        return scenario_results
    
    def get_ai_response(self, prompt):
        # Placeholder - integrate with your AI service
        # Could be OpenAI, Claude, local model, etc.
        return f"AI response to: {prompt[:50]}..."
    
    def quick_evaluate(self, response, scenario):
        """Simple heuristics - replace with your criteria"""
        score = 0
        if len(response) > 50: score += 1  # Not too short
        if len(response) < 500: score += 1  # Not too long
        if any(word in response.lower() for word in ['specific', 'clear', 'help']): 
            score += 1
        return score
    
    def compare_results(self):
        """Generate comparison summary"""
        print("\n" + "="*50)
        print("COMPARISON SUMMARY")
        print("="*50)
        
        for approach_name, approach in self.approaches.items():
            results = approach['results']
            if results:
                avg_length = sum(r['length'] for r in results) / len(results)
                avg_score = sum(r['evaluation'] for r in results) / len(results)
                print(f"\n{approach_name}:")
                print(f"  Avg length: {avg_length:.0f} chars")
                print(f"  Avg score: {avg_score:.1f}/3")
```

## Real Usage Example

Here's how I actually use it:

```python
# Set up the comparison
comparator = AIResponseComparator()

# Add different approaches I want to test
comparator.add_approach(
    "direct_instruction",
    "Answer this customer question directly and professionally: {question}",
    "Straightforward approach"
)

comparator.add_approach(
    "role_playing",
    "You are an expert customer service representative with 10 years experience. "
    "A customer asks: {question}. Respond helpfully and empathetically.",
    "Role-based approach"
)

comparator.add_approach(
    "few_shot",

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-17*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
