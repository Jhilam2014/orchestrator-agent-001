# Universal Enterprise Autonomous Orchestrator Package

This package upgrades the original orchestrator into a workflow-agnostic production-ready agent system.

## Files

- `orchestrator-agent-ready.md` — main upgraded orchestrator instruction
- `schemas/orchestrator-response.schema.json` — strict response schema
- `schemas/workflow.schema.json` — workflow classification and requirement schema
- `schemas/agent.schema.json` — individual generated agent schema
- `schemas/agent-registry.schema.json` — registry for generated agents
- `schemas/execution-topology.schema.json` — execution graph and handoff schema
- `schemas/cost-function.schema.json` — engineering and token cost governance schema
- `schemas/graph.schema.json` — Neo4j/workspace graph schema
- `schemas/openapi-planning.schema.json` — Swagger/OpenAPI planning schema
- `schemas/task.schema.json` — task decomposition schema
- `schemas/observability.schema.json` — observability dashboard schema
- `schemas/memory.schema.json` — architectural memory schema
- `schemas/environment.schema.json` — environment variable planning schema

## Recommended usage

1. Use `orchestrator-agent-ready.md` as the main system/developer instruction for your orchestrator agent.
2. Use `orchestrator-response.schema.json` as the strict JSON output schema when the platform supports response schemas.
3. Store all generated agents in `apps/agentic/agents/`.
4. Store registry files in `apps/agentic/registry/`.
5. Store graph/memory records in Neo4j or JSON fallback during local development.
6. Validate every generated artifact against the schemas before execution.


## Human Agent in Loop

Use `schemas/human-agent-control.schema.json` to record human approval, rejection, modification, or custom agent additions. Use `schemas/custom-agent-request.schema.json` when a user manually defines one or more custom agents before activation.

## Root workspace output rule

When this orchestrator accepts or delivers any work, it must generate operational artifacts under dedicated top-level folders at the workspace root. It must not place generated work files inside `schemas/` or `examples/`.

Use this placement:

- agents -> `agents/`
- workflows -> `workflows/`
- tasks -> `tasks/`
- runtimes -> `runtime/`
- registries -> `registry/`
- graph artifacts -> `graph/`
- topology files -> `topology/`
- final outputs -> `deliverables/`
- human approvals/custom agent changes -> `human-review/`
- traces/cost/token logs -> `observability/`
- generated documentation -> `docs/`
- tests -> `tests/`
- scripts -> `scripts/`
- integrations -> `integrations/`
- persistent memory -> `memory/`

See `ROOT_WORKSPACE_GENERATION_POLICY.md` and `schemas/workspace-generation.schema.json`.

