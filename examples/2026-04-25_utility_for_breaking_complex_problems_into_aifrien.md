# Breaking Down Complex Problems for AI: A Practical Chunking Utility

Working with AI daily, I've learned that the biggest barrier isn't the AI's capability—it's how you frame the problem. A 500-line function refactor request gets mediocre results, but breaking it into logical 50-line chunks with clear context? Game changer.

## The Problem Chunker

Here's a utility I built after too many failed "please fix everything" prompts:

```python
class ProblemChunker:
    def __init__(self, max_context_size=2000):
        self.max_context_size = max_context_size
        self.chunks = []
        
    def add_context(self, label, content, priority="medium"):
        """Add contextual information with priority weighting"""
        return {
            "label": label,
            "content": content,
            "priority": priority,
            "size": len(content)
        }
    
    def chunk_by_dependency(self, tasks):
        """Break tasks into dependency-aware chunks"""
        independent = [t for t in tasks if not t.get('depends_on')]
        dependent = [t for t in tasks if t.get('depends_on')]
        
        chunks = []
        # Start with independent tasks
        if independent:
            chunks.append({
                "type": "foundation",
                "tasks": independent,
                "note": "These can be tackled first - no dependencies"
            })
        
        # Group dependent tasks by what they depend on
        dep_groups = {}
        for task in dependent:
            dep = task['depends_on']
            if dep not in dep_groups:
                dep_groups[dep] = []
            dep_groups[dep].append(task)
        
        for dep, tasks in dep_groups.items():
            chunks.append({
                "type": "dependent",
                "depends_on": dep,
                "tasks": tasks,
                "note": f"Complete after: {dep}"
            })
            
        return chunks

    def chunk_codebase(self, files, focus_area):
        """Break down code changes by impact radius"""
        core_files = [f for f in files if focus_area in f['path']]
        related_files = [f for f in files if f not in core_files 
                        and any(imp in f.get('imports', []) for imp in [focus_area])]
        edge_files = [f for f in files if f not in core_files + related_files]
        
        return [
            {"scope": "core", "files": core_files, 
             "approach": "Detailed analysis - this is where the main changes happen"},
            {"scope": "related", "files": related_files,
             "approach": "Impact assessment - what breaks if core changes?"},  
            {"scope": "edge", "files": edge_files,
             "approach": "Light review - likely just import/type updates"}
        ]
```

## Real Usage Patterns

**For debugging sessions:**
```python
chunker = ProblemChunker()

# Instead of "fix my broken app"
bug_chunks = chunker.chunk_by_dependency([
    {"task": "Reproduce error", "type": "investigation"},
    {"task": "Check database connections", "depends_on": "Reproduce error"},
    {"task": "Fix connection pooling", "depends_on": "Check database connections"},
    {"task": "Add monitoring", "depends_on": "Fix connection pooling"}
])
```

**For feature development:**
```python
# Break down "add user authentication" 
auth_chunks = chunker.chunk_codebase(
    files=get_relevant_files(),
    focus_area="auth"
)
```

## What Actually Works

**The 3-chunk rule**: Most complex problems break into exactly 3 meaningful chunks. More than that and you lose coherence. Fewer and you're not really chunking.

**Dependency-first thinking**: Always start with "what has to happen before what else?" The AI handles sequential logic much better than parallel complexity.

**Context budgeting**: I reserve 30% of my prompt space for context, 50% for the specific chunk, 20% for examples and constraints.

## Honest Limitations

This approach adds overhead—sometimes significantly. For truly novel

---
*Auto-generated content via human-AI interaction (Claude API) - 2026-04-25*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
