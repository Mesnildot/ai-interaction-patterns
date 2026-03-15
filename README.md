\# AI Interaction Patterns



Practical patterns, prompts, and insights from daily human-AI collaboration.



\## What is this?



A collection of real-world interaction patterns for working effectively with AI tools. Content is auto-generated daily via human-AI interaction (Claude API) based on curated templates reflecting practical experience.



\## Structure



\- \*\*prompts/\*\* - Reusable prompt templates and frameworks

\- \*\*docs/\*\* - Best practices and lessons learned

\- \*\*examples/\*\* - Code utilities for AI workflows

\- \*\*discussions/\*\* - Reflections on human-AI collaboration



\## How it works



A GitHub Action runs daily and:

1\. Picks a random content type and template

2\. Generates practical content via Claude API

3\. Commits the new file to this repository



All content is transparently auto-generated (see footer on each file).



\## Using this repo



Browse any folder. Each file is standalone and useful on its own.



\*\*For practitioners:\*\* Find patterns that work in real AI workflows.



\*\*For researchers:\*\* Observe how interaction patterns affect AI output quality.



\## Setup (if you want to fork and adapt)



\### Prerequisites

\- GitHub account

\- Anthropic API key



\### Steps



1\. Fork this repository



2\. Add your API key in GitHub Secrets:

&#x20;  - Go to repo Settings > Secrets and variables > Actions

&#x20;  - Click "New repository secret"

&#x20;  - Name: `ANTHROPIC\_API\_KEY`

&#x20;  - Value: your key (starts with `sk-ant-...`)



3\. Enable GitHub Actions:

&#x20;  - Go to repo Actions tab

&#x20;  - Click "I understand, enable actions"



4\. The action runs daily at 9h UTC. To test manually:

&#x20;  - Go to Actions tab

&#x20;  - Select "Daily Content Generation"

&#x20;  - Click "Run workflow"



\### Modify templates



Edit `scripts/templates.yaml` to change topics and angles.



\## Transparency



All content in this repository is auto-generated via Claude API based on human-curated templates. Each file includes a footer stating this clearly. This is not human-written content presented as such - it is documented human-AI collaboration.



\## License



MIT - Use, fork, adapt freely.





