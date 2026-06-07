# Root Workspace Generation Policy

This orchestrator must generate all work-acceptance, execution, agent, workflow, runtime, and delivery artifacts under dedicated top-level folders at the root of the workspace.

## Mandatory rule

When accepting, executing, or delivering any work, the orchestrator MUST NOT place generated operational artifacts inside existing package/support folders such as:

- `schemas/`
- `examples/`
- `.git/`
- dependency folders such as `node_modules/`, `.venv/`, `venv/`, `dist/`, `build/`, `.next/`
- any unrelated existing application folder unless the request explicitly targets that application folder

Schemas remain only for reusable JSON Schema contracts. Examples remain only for sample files. Runtime-generated agents, workflows, logs, delivery outputs, topology files, and review records must be created under the root-level folders listed below.

## Required top-level folders

```plaintext
workspace-root/
├── agents/
├── workflows/
├── tasks/
├── runtime/
├── registry/
├── graph/
├── topology/
├── deliverables/
├── human-review/
├── observability/
├── docs/
├── configs/
├── tests/
├── scripts/
├── integrations/
├── memory/
├── schemas/
└── examples/
```

## Placement map

| Artifact type | Required root folder |
|---|---|
| AI-generated agent instructions | `agents/generated/` |
| Human-custom agents | `agents/custom/` |
| Human controller agents | `agents/human/` |
| Agent runtime definitions | `runtime/agents/` |
| OpenAI registration payloads | `runtime/openai/` |
| Workflow manifests | `workflows/` |
| Task breakdowns | `tasks/` |
| Agent registry state | `registry/agents/` |
| Workflow registry state | `registry/workflows/` |
| Neo4j graph manifests | `graph/` |
| Execution topology | `topology/execution/` |
| Infrastructure topology | `topology/infrastructure/` |
| Data/API topology | `topology/data/`, `topology/api/` |
| Human review requests | `human-review/requests/` |
| Human decisions/audit records | `human-review/decisions/` |
| Final delivery outputs | `deliverables/` |
| Validation reports | `deliverables/validation/` |
| Cost/token/trace logs | `observability/` |
| Generated documentation | `docs/` |
| Runtime configs | `configs/` |
| Tests | `tests/` |
| Utility scripts | `scripts/` |
| Integration specs | `integrations/` |
| Architectural memory | `memory/` |

## Acceptance and delivery behavior

For every accepted work item, the orchestrator must create or update:

1. `workflows/<workflow-id>.workflow.json`
2. `tasks/<workflow-id>.tasks.json`
3. `topology/execution/<workflow-id>.topology.json`
4. `registry/workflows/<workflow-id>.registry.json`
5. `deliverables/<workflow-id>/delivery-manifest.json`
6. `observability/<workflow-id>/execution-trace.json`
7. `human-review/<workflow-id>/approval-state.json` when human approval is required
8. agent files under `agents/` only when agent creation is justified

## Existing-folder protection

Before writing any file, the orchestrator must classify the file into an artifact category and resolve its destination from the placement map. If no category matches, create a new top-level category folder instead of writing into `schemas/` or `examples/`.
