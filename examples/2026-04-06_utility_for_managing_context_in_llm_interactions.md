# Context Management for LLM Interactions

Managing context across multiple LLM conversations is like maintaining state in a distributed system—it gets messy fast if you don't have good patterns. After building several AI-powered tools, I've learned that explicit context management saves more time than any prompt engineering trick.

## The Basic Context Manager

Here's a lightweight utility I use daily:

```python
class ConversationContext:
    def __init__(self, max_tokens=4000):
        self.messages = []
        self.metadata = {}
        self.max_tokens = max_tokens
        self._token_count = 0
    
    def add_message(self, role, content, metadata=None):
        message = {
            'role': role,
            'content': content,
            'timestamp': time.time(),
            'metadata': metadata or {}
        }
        
        # Rough token estimation (4 chars ≈ 1 token)
        tokens = len(content) // 4
        
        # Truncate old messages if approaching limit
        if self._token_count + tokens > self.max_tokens:
            self._truncate_context()
        
        self.messages.append(message)
        self._token_count += tokens
    
    def _truncate_context(self):
        # Keep system message + recent messages
        system_msgs = [m for m in self.messages if m['role'] == 'system']
        recent_msgs = self.messages[-10:]  # Keep last 10 exchanges
        
        self.messages = system_msgs + recent_msgs
        self._recalculate_tokens()
```

## Smart Context Compression

The real challenge isn't storing context—it's deciding what to keep. I use this pattern for long-running tasks:

```python
def compress_context(self, llm_client):
    """Summarize old context to preserve key information"""
    if len(self.messages) < 20:
        return  # Not worth compressing yet
    
    # Extract middle portion for summarization
    to_compress = self.messages[2:-10]  # Skip system + recent
    
    summary_prompt = f"""
    Summarize this conversation history in 2-3 sentences, 
    focusing on key decisions, findings, or context that 
    might be relevant later:
    
    {self._format_messages(to_compress)}
    """
    
    summary = llm_client.complete(summary_prompt)
    
    # Replace compressed messages with summary
    self.messages = (
        self.messages[:2] +  # System messages
        [{'role': 'assistant', 'content': f"[Context Summary: {summary}]"}] +
        self.messages[-10:]  # Recent messages
    )
```

## Context Branching for Experiments

When testing different approaches, I branch contexts instead of starting over:

```python
def branch(self, branch_name):
    """Create a branch for experimental conversations"""
    branch = ConversationContext(self.max_tokens)
    branch.messages = self.messages.copy()
    branch.metadata = self.metadata.copy()
    branch.metadata['branch'] = branch_name
    branch.metadata['branched_from'] = id(self)
    return branch

def merge_insights(self, branch_context, insight_prompt):
    """Extract learnings from a branch without full history"""
    insights = self.llm_client.complete(f"""
    {insight_prompt}
    
    Branch conversation:
    {branch_context.get_recent_messages(5)}
    """)
    
    self.add_message('assistant', f"[Insights from {branch_context.metadata['branch']}: {insights}]")
```

## What Actually Works

**Token estimation is crucial but imperfect.** The 4-chars-per-token rule gets you close enough for most models, but OpenAI's tiktoken library is worth using for production code.

**Compression works better than truncation.** Simply dropping old messages loses important context. Having the LLM summarize key points preserves more useful information.

**Metadata saves debugging time.** Storing timestamps, token counts, and conversation metadata helps when things go wrong.

## Limitations I've Hit

Context managers don't solve the fundamental problem that LLMs forget. They just make the forgetting more predict

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-06*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
