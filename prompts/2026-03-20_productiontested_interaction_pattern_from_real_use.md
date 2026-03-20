# Production-Tested AI Interaction Pattern: The Layered Refinement Approach

After a year of daily AI collaboration, one pattern consistently delivers better results than the typical "write me X" approach: **layered refinement with explicit checkpoints**.

## How It Works

Instead of asking for the final output immediately, I structure interactions in three distinct layers:

**Layer 1: Scope and Structure**
```
"I need to create a customer onboarding flow. Before we draft anything, 
help me think through: What are the 3-4 essential steps? What's the 
biggest risk of user drop-off? What should we prioritize for clarity vs. speed?"
```

**Layer 2: Draft with Constraints**
```
"Now draft the flow, but keep each step under 50 words and assume users 
are on mobile. Flag anywhere you're making assumptions about our product."
```

**Layer 3: Targeted Polish**
```
"The intro feels generic. Rewrite just that section for SaaS users who've 
been burned by complex tools before. Keep the helpful tone but add more specificity."
```

## What This Prevents

The biggest trap I've learned to avoid: **assumption accumulation**. When you ask for complex output in one shot, the AI makes dozens of micro-assumptions that compound. You end up with something polished but misaligned.

The checkpoint approach forces both you and the AI to surface assumptions early, when they're easier to correct.

## Real Example: Email Campaign

**Bad approach** (my old way):
"Write a welcome email series for new users"

**Layered approach** (what works):
1. "What should a SaaS welcome series accomplish in 3 emails? What's the balance between product education and relationship building?"
2. "Draft email 1, focusing on immediate value. Assume they signed up but haven't logged in yet."
3. "The CTA feels pushy. Soften it while maintaining urgency."

## Limitations and Tradeoffs

This pattern takes 3x longer than one-shot prompting. Sometimes you just need quick content and the extra precision isn't worth it.

It also works better for strategic/creative tasks than pure information retrieval. For "What's the syntax for X?" questions, just ask directly.

The biggest limitation: **you still need domain expertise**. This pattern helps you collaborate more effectively with AI, but garbage questions still produce garbage output, just more efficiently.

## Two Variations That Work

**Time-pressed version**: Combine layers 1-2 into "Here's my context and constraints, give me a draft that flags its own assumptions."

**High-stakes version**: Add a fourth layer asking the AI to critique its own output from a different perspective before you finalize.

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-03-20*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
