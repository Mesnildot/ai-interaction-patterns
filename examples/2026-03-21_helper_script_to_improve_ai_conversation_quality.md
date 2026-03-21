# Helper Script: AI Conversation Quality Booster

After months of daily AI collaboration, I noticed my conversations getting stale. I was asking lazy questions, not building on previous insights, and missing opportunities for deeper exploration. So I built a simple helper script that runs in my terminal to nudge me toward better interactions.

## The Quality Checker Script

```python
#!/usr/bin/env python3
import sys
import re
from datetime import datetime

class ConversationHelper:
    def __init__(self):
        self.quality_flags = {
            'vague': ['help me', 'make this better', 'what should i do'],
            'context_missing': ['this', 'it', 'that thing', 'the code'],
            'binary': ['is this good', 'should i', 'which is better'],
            'open_ended': ['explore', 'alternatives', 'approaches', 'consider']
        }
    
    def analyze_prompt(self, text):
        text_lower = text.lower()
        issues = []
        strengths = []
        
        # Check for vague language
        if any(phrase in text_lower for phrase in self.quality_flags['vague']):
            issues.append("🚨 Vague request - be more specific about what you want")
        
        # Check for missing context
        if any(phrase in text_lower for phrase in self.quality_flags['context_missing']):
            issues.append("📝 Missing context - define 'this' and 'it'")
        
        # Check for binary questions
        if any(phrase in text_lower for phrase in self.quality_flags['binary']):
            issues.append("🤔 Binary question - consider asking 'what are the tradeoffs?'")
        
        # Check for good patterns
        if any(phrase in text_lower for phrase in self.quality_flags['open_ended']):
            strengths.append("✅ Open-ended exploration")
        
        if len(text) > 100:
            strengths.append("✅ Good detail level")
            
        return issues, strengths
    
    def suggest_improvements(self, text):
        suggestions = []
        
        if "help me" in text.lower():
            suggestions.append("Try: 'I'm working on X and struggling with Y. Here's what I've tried...'")
        
        if len(text.split()) < 10:
            suggestions.append("Add more context: your goal, constraints, what you've already considered")
        
        if not any(char in text for char in '?'):
            suggestions.append("End with a specific question to guide the response")
        
        return suggestions

def main():
    helper = ConversationHelper()
    
    if len(sys.argv) < 2:
        print("Usage: ./ai_helper.py 'your prompt here'")
        print("Or: ./ai_helper.py --interactive")
        return
    
    if sys.argv[1] == '--interactive':
        print("🤖 AI Conversation Helper - Interactive Mode")
        print("Paste your prompt (press Enter twice to analyze):\n")
        
        lines = []
        while True:
            try:
                line = input()
                if line == '' and lines:
                    break
                lines.append(line)
            except KeyboardInterrupt:
                return
        
        prompt = '\n'.join(lines)
    else:
        prompt = ' '.join(sys.argv[1:])
    
    print(f"\n📊 ANALYZING: {prompt[:50]}{'...' if len(prompt) > 50 else ''}")
    print("-" * 50)
    
    issues, strengths = helper.analyze_prompt(prompt)
    
    if strengths:
        print("💪 STRENGTHS:")
        for strength in strengths:
            print(f"  {strength}")
        print()
    
    if issues:
        print("🔧 IMPROVEMENT AREAS:")
        for issue in issues:
            print(f"  {issue}")
        print()
        
        suggestions = helper.suggest_improvements(prompt)
        if suggestions:
            print("💡 SPECIFIC SUGGESTIONS:")
            for suggestion in suggestions:
                print(f"  

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-03-21*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
