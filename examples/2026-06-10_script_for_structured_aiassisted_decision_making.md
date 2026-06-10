# Structured AI-Assisted Decision Making Script

After months of using AI for everything from code reviews to strategic planning, I've learned that unstructured conversations often lead to circular discussions or missed considerations. Here's a decision framework script I use when facing complex choices.

## The Decision Template Script

I start every major decision conversation with AI using this structured prompt:

```markdown
## Decision Context
- **Decision to make:** [Brief statement]
- **Timeline:** [When decision is needed]
- **Stakeholders affected:** [Who this impacts]
- **Current status quo:** [What happens if we do nothing]

## Known Information
- **Facts we're confident about:** [List key certainties]
- **Assumptions we're making:** [List what we think is true]
- **Key constraints:** [Budget, time, resources, compliance, etc.]

## Options Analysis
For each option, analyze:
1. **Immediate costs/effort**
2. **Long-term implications** 
3. **Risk factors**
4. **Reversibility** (can we undo this?)
5. **Learning opportunity** (what will we discover?)

## Decision Request
Help me think through [specific aspect] and identify blind spots I might be missing.
```

## What Actually Works

**The constraint section is critical.** I used to skip this and get beautiful theoretical advice that ignored our budget realities. Now I'm explicit: "We have $5K and two weeks" changes everything.

**Break down "options analysis" into chunks.** If I dump all options at once, AI tends to give surface-level analysis. Instead, I go deep on 2-3 options first, then compare.

**Ask for blind spots explicitly.** The phrase "what am I not considering?" consistently surfaces angles I miss. Last week it caught that our "quick fix" would create a maintenance nightmare six months out.

## Example in Practice

Recently deciding between three monitoring tools:

```markdown
## Decision Context
- **Decision:** Choose monitoring solution for 12-service architecture
- **Timeline:** Need to decide by Friday for Q1 implementation
- **Stakeholders:** Dev team (8 people), SRE team (3), monthly budget owner
- **Status quo:** Basic logging, lots of manual investigation

## Known Information  
- **Facts:** Current downtime costs ~$2K/hour, team spends 15hrs/week on incidents
- **Assumptions:** New tool will reduce incident time by 50%
- **Constraints:** $800/month budget, must integrate with existing Slack workflow
```

The structured approach revealed that the "enterprise" option I was leaning toward would blow our budget in month three due to data volume pricing.

## What Doesn't Work

**Don't use this for simple decisions.** For "should I refactor this function?", it's overkill. This is for choices that affect multiple people or have lasting consequences.

**Avoid the perfectionism trap.** I sometimes spend more time structuring the decision than needed. Use judgment—not every choice needs the full framework.

**Time pressure reality.** Sometimes you need a quick gut check, not thorough analysis. I keep a shortened version: Context + Constraints + Quick options review.

The real value isn't getting the "right" answer—it's ensuring you've thought through dimensions you'd otherwise skip in the rush to decide.

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-06-10*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
