# Script for Structured AI-Assisted Decision Making

After months of using AI for everything from code reviews to strategic planning, I've learned that unstructured conversations lead to circular thinking. Here's a decision-making framework I actually use when the stakes matter.

## The Three-Phase Script

### Phase 1: Frame the Decision
```markdown
**Decision Context:**
- What exactly are we deciding? [One sentence]
- Why does this matter? [Impact/urgency]
- Who's affected? [Stakeholders]
- What's our timeline? [Hard/soft deadlines]

**Current Understanding:**
- What do we know for certain?
- What are we assuming?
- What information is missing?
```

### Phase 2: Generate and Evaluate Options

I start broad, then narrow:

```markdown
**Option Generation:**
AI, help me brainstorm 8-10 approaches to [decision]. 
Include obvious choices AND unconventional ones.
Don't evaluate yet - just list possibilities.

**Structured Evaluation:**
For each viable option, analyze:
- Pros/Cons (be specific)
- Resource requirements (time, money, people)
- Risk level and mitigation strategies
- Alignment with goals/constraints
- Reversibility (can we change course?)
```

**What works:** The AI generates options I wouldn't think of, especially combinations of approaches. But it often suggests impractical ideas, so I filter ruthlessly.

### Phase 3: Stress Test and Commit

This is where most people stop, but the real value comes from challenging the decision:

```markdown
**Red Team Exercise:**
- What could go wrong with our top choice?
- What would someone arguing against this say?
- What evidence would change our minds?
- How would this decision look in 6 months?

**Implementation Reality Check:**
- What's the first concrete step?
- What obstacles will we actually face?
- How will we know if it's working?
```

## Real Example: Code Architecture Decision

Recently used this for choosing between microservices and monolith:

**Frame:** Team of 4, 6-month timeline, customer-facing feature
**Options:** AI suggested 6 approaches, including "modular monolith" I hadn't considered  
**Stress test:** "What if our team doubles?" changed the whole analysis

The process took 45 minutes but saved weeks of second-guessing.

## What Doesn't Work

- **Skip the framing:** AI gives generic advice without context
- **Accept first analysis:** AI is optimistic about implementation difficulty
- **Rush the stress testing:** This catches blind spots that seem obvious in hindsight

## The Honest Truth

This framework slows you down initially. Simple decisions don't need this rigor. But for decisions where you'll live with consequences for months, the structured approach consistently leads to better outcomes and more confidence in the choice.

The AI excels at generating comprehensive option lists and finding logical gaps. It struggles with organizational politics and implementation messiness—that's where your judgment matters most.

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-05-23*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
