# HANDOFF: Job Hunter Agent

> Read this first in every new session. Update it at the end of every step.

**Last updated:** 2026-10-18 · **Current step:** 2 (Hello LangGraph), not started

## Goal
A LangGraph agent for Fahad (AI/ML + backend/frontend dev) that finds freelance, contract and
remote-job leads, writes personalised outreach, and creates Gmail drafts with the right CV attached.
He reviews everything and sends it himself.

## Decisions made
- **LLM:** Claude via `langchain-anthropic`. Use `claude-haiku-5-5` for cheap work (classifying)
  and `claude-sonnet-5-5` for writing messages. Haiku 5.5 thinks by default, so use `effort="low"`,
  give it `max_tokens` >= 1024 and read `reply.text`, not `reply.content`.
- **LinkedIn: the safe route (user agreed).** No bot login, scraping or auto-connect/DM, because of
  the ban risk. The agent finds leads through public web search and job APIs (Remotive, RemoteOK, etc.)
  plus post URLs/text the user pastes in. It writes connection notes and DMs, and the user sends them.
- **Gmail:** official Gmail API, OAuth, **drafts only, never send**. Attach the right CV.
- **Job applications:** the agent finds and ranks jobs and writes cover letters. The user submits.
- **Interviews:** Google Calendar events or a booking link (later step).
- **Budget:** hard stop at **$3/day**, with every run's tokens and cost logged.
- **Memory:** a context file the agent reads at the start and updates at the end of each session.
- **Tracing:** LangSmith project `job-hunter-agent` (`LANGSMITH_TRACING=true` in `.env`).

## How we work (user preferences)
- The user is a **Python beginner** and is learning. Take tiny steps, one at a time.
- Before each step, briefly explain **what / why / how / prerequisites to know**. Keep it short.
- Split the work: give the user short tasks (accounts, keys, running commands), and they send screenshots.
  Do the code yourself in small pieces. Wait for confirmation before moving on.
- Ask questions when something is unclear.
- The user handles git (repo: github.com/fahadtariqaziz/job-hunter-agent). Don't commit unless asked.

## Project layout
```
job-hunter-agent/
  .env.example / .env (gitignored)   API keys
  pyproject.toml, uv.lock            uv project, Python 3.13
  src/job_hunter_agent/
    check_setup.py                   step 1: key + Claude + LangSmith check
```
Run anything with: `uv run python src/job_hunter_agent/<file>.py`

## Roadmap
1. [x] Setup: uv, deps (langgraph, langchain-anthropic, langsmith, python-dotenv), `.env`, LangSmith trace confirmed
2. [ ] Hello LangGraph: State + 2 nodes + edges; print the graph (ASCII + Mermaid PNG)
3. [ ] LangSmith: view a graph run as a tree of nodes; add run names/tags
4. [ ] Cost tracker: callback logs tokens and $ to `data/usage.jsonl`; refuse to run past $3/day
5. [ ] Memory: `data/context.md` loaded at start and summarised at end (yesterday / last week)
6. [ ] CV loader: user adds 2 PDFs to `cvs/`; parse them into `data/profile.json`
7. [ ] Lead finder: web search + job APIs + pasted posts, then classify (AI/ML | backend/frontend | skip)
8. [ ] Writer: connection note, DM and email text per lead (Sonnet)
9. [ ] Gmail drafts with the CV attached (OAuth `credentials.json` / `token.json`, gitignored)
10. [ ] Human-in-the-loop approval with LangGraph `interrupt` + a checkpointer
11. [ ] Job ranking + cover letters; interview scheduling through Google Calendar

## Log
- **2026-10-18:** Step 1 done. Project created and keys working. The first trace showed up in LangSmith.
  Fixed `check_setup.py`: Haiku 5.5 spent all 50 `max_tokens` on thinking and returned no text.
