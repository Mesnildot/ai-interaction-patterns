# Helper Script to Improve AI Conversation Quality

After months of daily AI collaboration, I've learned that conversation quality often comes down to consistency and context management. Here's a Python script I use to structure better AI interactions.

## The Problem

Most AI conversations deteriorate because we lose track of context, ask vague questions, or don't maintain consistent formatting. I found myself constantly retyping similar prompts and losing valuable conversation threads.

## The Solution

```python
#!/usr/bin/env python3
"""
AI Conversation Helper
Helps structure and track AI conversations for better results
"""

import json
import datetime
from pathlib import Path

class AIConversationHelper:
    def __init__(self, project_name="default"):
        self.project_name = project_name
        self.context_file = Path(f"ai_context_{project_name}.json")
        self.load_context()
    
    def load_context(self):
        if self.context_file.exists():
            with open(self.context_file, 'r') as f:
                self.context = json.load(f)
        else:
            self.context = {
                "project_background": "",
                "key_decisions": [],
                "current_focus": "",
                "constraints": [],
                "conversation_history": []
            }
    
    def save_context(self):
        with open(self.context_file, 'w') as f:
            json.dump(self.context, f, indent=2)
    
    def format_prompt(self, question, include_context=True, prompt_type="general"):
        """Format a structured prompt for better AI responses"""
        
        templates = {
            "code_review": """
Context: {context}
Current Focus: {focus}

Code Review Request:
{question}

Please provide:
1. Specific issues found
2. Suggestions with examples
3. Alternative approaches if applicable

Constraints: {constraints}
""",
            "debugging": """
Context: {context}
Problem: {question}

Environment:
- Current Focus: {focus}
- Known Constraints: {constraints}

Please help me:
1. Identify the root cause
2. Suggest 2-3 potential solutions
3. Highlight any assumptions I should verify
""",
            "general": """
Context: {context}
Current Focus: {focus}

Question: {question}

Please consider these constraints: {constraints}
"""
        }
        
        template = templates.get(prompt_type, templates["general"])
        
        formatted_prompt = template.format(
            context=self.context["project_background"],
            focus=self.context["current_focus"],
            question=question,
            constraints="; ".join(self.context["constraints"])
        )
        
        # Log the conversation
        self.context["conversation_history"].append({
            "timestamp": datetime.datetime.now().isoformat(),
            "prompt_type": prompt_type,
            "question": question
        })
        
        self.save_context()
        return formatted_prompt
    
    def update_context(self, **kwargs):
        """Update context with new information"""
        for key, value in kwargs.items():
            if key in self.context:
                if isinstance(self.context[key], list):
                    if isinstance(value, list):
                        self.context[key].extend(value)
                    else:
                        self.context[key].append(value)
                else:
                    self.context[key] = value
        self.save_context()
    
    def get_conversation_summary(self):
        """Get recent conversation patterns for analysis"""
        recent = self.context["conversation_history"][-10:]
        types = [conv["prompt_type"] for conv in recent]
        return {
            "recent_count": len(recent),
            "prompt_types": list(set(types)),
            "last_focus": self.context["current_focus"]
        }

# Usage examples
if __name__ == "__main__":
    # Initialize for a specific project
    helper = AIConversationHelper("web_scraper_project")
    
    # Set up context once
    helper.update_context(
        project_background="Building a Python web scraper for e-commerce sites",
        current_focus="

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-03-16*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
