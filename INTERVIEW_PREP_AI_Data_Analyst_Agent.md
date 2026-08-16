# Interview Prep — AI Data Analyst & Knowledge Agent

> How to use this file: fill in each section **as you build it**, not at the end.
> Each answer should be specific to what you actually built — real numbers,
> real trade-offs, real bugs you hit — not generic textbook explanations.
> When you hit a checkpoint on the build plan, come back here and fill in
> the matching section while it's fresh.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` done, ready to answer

---

## 1. ARCHITECTURE

- [ ] Explain complete architecture
- [ ] Explain every major component
- [ ] Explain why each technology was selected

**Notes / draft answers:**

_(Fill in after Day 1, revisit after Day 17 once the full system is built —
this is the "walk me through your project" answer, practice saying it out
loud in under 2 minutes)_

```
Draft answer:


```

**Why each technology (fill in per component as you build it):**

| Component | Chosen | Why | Alternative considered |
|---|---|---|---|
| Backend framework | FastAPI | | Flask, Django |
| DB | PostgreSQL | | MySQL, SQLite |
| LLM runtime | Ollama (local) | | OpenAI/Anthropic API |
| Orchestration | LangGraph | | plain Python, CrewAI, AutoGen |
| Vector store | ChromaDB / FAISS | | Qdrant, Pinecone |
| Frontend | React | | Streamlit, Next.js |
| Viz | Plotly | | Matplotlib, D3 |

---

## 2. LLM

- [ ] Explain tokens/context
- [ ] Explain prompting
- [ ] Explain structured output
- [ ] Explain tool calling
- [ ] Explain temperature/model selection

**Fill in during Day 3-4.**

```
Tokens/context — what model, what context window, did you hit limits:


Prompting approach — system vs user messages, how schema/glossary
gets injected:


Structured output — how you enforce JSON output from the LLM, what
you do when it fails to parse:


Tool calling — did you use native tool calling or prompt-based
routing? why:


Temperature/model choice — what temperature for SQL gen vs answer
gen, and why they might differ:

```

---

## 3. TEXT-TO-SQL

- [ ] How SQL is generated
- [ ] How schema is provided
- [ ] How SQL is validated
- [ ] How SQL errors are corrected
- [ ] How destructive queries are blocked

**Fill in during Day 4-6.**

```
Generation approach:


Schema injection — full schema every time vs selective? why (tie to
your RAG decision — you chose NOT to do schema RAG, be ready to
justify at your table count):


Validation — what library/approach (regex? sqlparse? AST?), what's
the allow-list:


Error correction loop — max retries, what gets sent back to the LLM
on failure, an example of a real failure you saw and how it recovered:


Destructive query blocking — exact mechanism, what happens if the
LLM tries DROP/DELETE anyway:

```

---

## 4. RAG

- [ ] Chunking
- [ ] Embeddings
- [ ] Vector database
- [ ] Similarity search
- [ ] Top-K
- [ ] Grounding
- [ ] Source attribution
- [ ] No-context behavior

**Fill in during Day 7-8.**

```
Chunking strategy — size, overlap, why (fixed-size vs semantic
chunking, and why you picked one):


Embedding model — which one, dimension size, local vs hosted:


Vector DB — ChromaDB or FAISS, final decision and why (in-memory vs
persistent, scale considerations):


Similarity search — cosine/dot product/euclidean, why:


Top-K — what K, how you picked it, did you test different values:


Grounding — how you force the LLM to only use retrieved context:


Source attribution — how sources get surfaced in the UI:


No-context behavior — exact prompt/logic for "I don't know," a real
example question that triggered it:

```

---

## 5. AGENTS

- [ ] LangGraph state
- [ ] Nodes
- [ ] Edges
- [ ] Routing
- [ ] Retry workflow
- [ ] Why single-agent

**Fill in during Day 9-11.**

```
State object — what's in it, why each field is there:


Nodes — list them, one line each on what they do:


Edges — which are conditional, what determines the branch:


Routing — how intent classification works (SQL/RAG/HYBRID), accuracy
you saw on your test set:


Retry workflow — where retries happen (SQL gen, SQL execution), max
counts, what happens after max retries exhausted:


Why single-agent, not multi-agent — this is a common interview
question, have a sharp answer (complexity/latency/debuggability
trade-off vs a multi-agent system):

```

---

## 6. SECURITY

- [ ] Read-only DB
- [ ] SQL injection
- [ ] Prompt injection
- [ ] Query limits
- [ ] Timeouts
- [ ] Secrets

**Fill in during Day 5 and Day 15.**

```
Read-only DB user — how it's configured, what permissions it
actually has (be specific — GRANT SELECT ON which schemas):


SQL injection — how you prevent it given the SQL itself is
LLM-generated (this is a good one to think through carefully — the
validator IS your injection defense here, since there's no
user-supplied SQL string being concatenated):


Prompt injection — what happens if a user asks a question designed
to make the LLM ignore its instructions or leak schema/prompts, did
you test this:


Query limits — LIMIT enforcement, row caps, timeout values:


Timeouts — SQL execution timeout, LLM call timeout:


Secrets — where API keys/DB creds live, what's in .env vs .env.example:

```

---

## 7. EVALUATION

- [ ] Dataset
- [ ] SQL accuracy
- [ ] RAG quality
- [ ] Routing accuracy
- [ ] Hybrid evaluation
- [ ] Regression testing

**Fill in during Day 14-15 — use your REAL numbers here, not placeholders.**

```
Dataset — how many questions, how split across SQL/RAG/hybrid/
invalid/ambiguous:


SQL accuracy — your actual execution accuracy % and result accuracy %:


RAG quality — retrieval precision, groundedness check results,
false "I don't know" rate:


Routing accuracy — % of questions correctly classified SQL/RAG/HYBRID,
what the router got wrong and why:


Hybrid evaluation — how you evaluated a compound answer as
correct/incorrect:


Regression testing — show an actual before/after: did a prompt
change you made improve or regress accuracy? what was the change?

```

---

## 8. ENGINEERING

- [ ] FastAPI
- [ ] PostgreSQL
- [ ] React
- [ ] Docker
- [ ] CI/CD
- [ ] Logging
- [ ] Observability
- [ ] Error handling

**Fill in during Day 13, 16, 17.**

```
FastAPI — endpoint design, Pydantic validation approach:


PostgreSQL — schema design decisions, indexes if any:


React — state management approach, how streaming/loading states work:


Docker — what's containerized, what's not (Ollama running on host?),
why:


CI/CD — what GitHub Actions actually checks, what would block a merge:


Logging — what gets logged, structured format, what's deliberately
excluded (secrets):


Observability — what you can see in a trace, example trace with
real latency numbers:


Error handling — what happens on DB down, LLM timeout, malformed
request — walk through 2-3 real failure paths:

```

---

## 9. SYSTEM DESIGN

- [ ] Scalability
- [ ] Latency
- [ ] Cost
- [ ] Reliability
- [ ] Failure scenarios
- [ ] Trade-offs
- [ ] Limitations

**Fill in on Day 17, after the full system exists — this needs hindsight.**

```
Scalability — honest answer: this is a single-node demo. What would
break first under load (Ollama serial inference is the likely
bottleneck)? What would you change for real scale (hosted LLM API,
connection pooling, async SQL execution, persistent/sharded vector
store)?


Latency — your actual measured end-to-end latency (from Day 16
tracing), which node is slowest, why:


Cost — $0 for local Ollama inference during dev; what would this
cost per request on a hosted API at your typical token counts —
do the math for a real number:


Reliability — what happens if Postgres is down, if Ollama is down,
if the vector store is corrupted — did you test any of these:


Failure scenarios — 2-3 concrete ways this system could give a wrong
answer confidently (e.g. router misclassifies, SQL is valid but
semantically wrong, RAG retrieves the wrong policy doc) — and what
you'd add to catch each:


Trade-offs made (have these ready, they show judgment):
  - Single-agent LangGraph vs multi-agent — why:
  - Rule-based chart selection vs LLM-based — why:
  - FAISS/ChromaDB vs Qdrant/Pinecone — why:
  - Local Ollama vs hosted API — why:
  - Manual regression log vs MLflow — why:


Limitations (say these proactively, don't wait to be asked):
  -
  -
  -

```

---

## Quick-fire prep (do this the night before an interview)

- [ ] Can you draw the full architecture diagram from memory on a whiteboard?
- [ ] Can you explain the LangGraph flow for a SQL question, a RAG
      question, and a HYBRID question, start to end, without looking
      at code?
- [ ] Do you have 2-3 real bugs you hit and fixed, with specifics?
- [ ] Do you have your actual eval numbers memorized (not "pretty good,"
      an actual percentage)?
- [ ] Can you explain one thing you'd do differently if you rebuilt this?
