# Autonomy-Preserving Prompt Patterns

## The Problem

AI tools can easily slip into being overly directive, pushing you toward specific solutions before you've fully explored the problem space. I've noticed this happens most when I'm tired or rushed—suddenly the AI is making decisions I should be making, and I end up with solutions that don't quite fit.

## Core Pattern: Option Architecture

Instead of asking "What should I do about X?", structure prompts to preserve your decision-making role:

```
"I'm dealing with [situation]. Help me understand:
- What are 3-4 different ways to approach this?
- What would I need to consider for each approach?
- What information am I missing that would help me decide?"
```

This keeps the AI in an advisory role while you stay in the driver's seat.

## Three Practical Approaches

### The Consultant Pattern
Treat the AI like a knowledgeable consultant who provides analysis, not decisions:

*"Act as my strategic advisor. I need to [goal]. What factors should I weigh? What are the potential downsides I might not be seeing?"*

Works well for complex decisions where you need perspective but want to maintain control.

### The Research Assistant Pattern  
When you need information gathering without premature conclusions:

*"I'm researching [topic] to make a decision about [context]. Don't recommend what I should do—instead, help me map out the landscape. What are the key considerations? What do experts disagree about?"*

Particularly useful for unfamiliar domains where you need to understand before deciding.

### The Devil's Advocate Pattern
When you already have a preferred direction but want to stress-test it:

*"I'm leaning toward [approach] for [situation]. Challenge this thinking. What am I potentially overlooking? What would make this approach fail?"*

## What Doesn't Work

**Avoiding the "just tell me" trap**: When pressed for time, it's tempting to ask "What's the best way to...?" This consistently leads to generic advice that misses your specific constraints and preferences.

**The false choice problem**: AI often presents binary options when reality offers more nuance. Always push back with "What other approaches exist?" or "What middle-ground options might work?"

## Real Limitations

This pattern requires more back-and-forth than directive prompting. Sometimes you genuinely need the AI to just pick something reasonable so you can move forward. That's fine—just be intentional about when you're delegating decisions versus when you're preserving your agency.

The key is recognizing the difference between "I need you to decide this" and "I need your help to decide this well."

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-13*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
