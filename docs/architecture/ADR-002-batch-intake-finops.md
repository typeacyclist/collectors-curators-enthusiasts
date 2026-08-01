# ADR-002: Batch Intake, Print Spooling, Edge Processing, and FinOps Controls

- Status: Accepted with corrections
- Scope: CCE platform and Orchid Enthusiasts operational workflows
- Depends on: ADR-001

## Context

CCE must support both careful single-item intake and high-volume collection work such as incoming shipments, relabeling, and mass cataloging. The architecture must increase operational velocity without weakening evidence review, tenant isolation, idempotency, conflict handling, or user control.

## Decision

### Batch capture sessions

Add a `BatchIntakeSession` concept that groups locally captured `DraftThing` records without replacing the existing single-item workflow.

A user may continuously capture photos, label images, narratives, and known locations while offline. Capture must not wait for network acknowledgement or AI completion.

Each draft retains its own:

- `DraftUUID`
- `ThingUUID`
- `LabelID`
- evidence and media references
- sync state
- AI proposal state
- validation state
- command and conflict state

The batch is an orchestration and presentation boundary, not a replacement for item-level identity or audit history.

### Consolidated proposal review

Provide a batch review interface that presents proposed values, evidence, confidence, conflicts, and missing information across multiple drafts.

Bulk acceptance is permitted only when all selected proposals:

- use an allowlisted low-consequence field type
- have no conflicting evidence
- pass deterministic validation
- preserve field-level evidence and confidence
- remain individually attributable to a reviewer and timestamp

Location, privacy, publication, tenant membership, sale or transfer status, archive state, and replacement of a confirmed identity may not be bulk-approved solely because an AI confidence value is high.

Confidence is a review aid, not an authorization policy.

### Batch command orchestration

Add a `BatchCommandRequest` containing multiple independent command envelopes.

Do not process an entire operational batch as one large all-or-nothing Firestore transaction. Large atomic transactions increase contention, retry cost, failure coupling, and platform-limit risk.

The server must:

1. Authenticate and authorize the actor and tenant.
2. Validate the batch envelope and configured item limit.
3. Process each command through the standard transactional operation-ledger handler.
4. Use bounded concurrency and configurable chunk sizes.
5. Return an item-level result for every command.
6. Permit safe retry of failed items by `ClientOperationID`.
7. Never reapply successful operations during a partial retry.

Supported result states include:

- `SUCCEEDED`
- `DUPLICATE_REPLAY`
- `VALIDATION_FAILED`
- `VERSION_CONFLICT`
- `AUTHORIZATION_FAILED`
- `RETRYABLE_ERROR`
- `PERMANENT_ERROR`

A batch may therefore complete partially. The UI must clearly distinguish successful, conflicted, failed, and pending items.

### Print queue and spooling

Extend `LabelService` with a local `PrintQueue`.

A print job references immutable label input data and includes:

- `PrintJobUUID`
- `ThingUUID`
- `LabelID`
- label template and version
- requested quantity
- created timestamp
- print state
- last printed timestamp

The queue may aggregate compatible jobs into:

- a multi-page PDF
- a sheet-label PDF
- a printer-specific batch payload after hardware support is implemented

Queueing a print job does not prove that a physical label was printed. `LABEL_PRINT_REQUESTED` and `LABEL_PRINT_CONFIRMED` must remain distinct events when confirmation is available.

### Edge image processing

Perform client-side image preparation where device capability permits.

Create configurable derivatives rather than permanent fixed dimensions:

- display derivative
- AI full-frame derivative
- optional OCR/label region-of-interest derivative
- thumbnail

The system must preserve processing metadata, including source dimensions, derivative dimensions, encoding, quality profile, orientation correction, crop coordinates when applicable, processing version, and whether the original was retained.

Automatic ROI detection may propose a crop, but the full contextual image remains available when identity or condition analysis requires it.

Media profiles are governed through versioned configuration. Example values such as 1600-pixel display images or 800-pixel OCR crops are initial test profiles, not immutable contracts.

### Taxonomy and canonical metadata cache

Provide a versioned local taxonomy reference cache for deterministic lookup and suggestions.

The cache may include approved genera, species, registered or imported names where licensing permits, aliases, normalized spellings, and source/version metadata.

Lookup order:

1. Exact normalized match.
2. Deterministic alias match.
3. Local fuzzy suggestion requiring user confirmation.
4. AI-assisted interpretation when narrative, OCR ambiguity, or unknown input requires it.
5. External authoritative verification only through an approved source and workflow.

A cache match must not be represented as external verification unless the underlying source and version support that status.

### Local draft recovery

Native applications should support an optional recovery snapshot for unsynchronized drafts using protected application storage or a user-selected export destination.

Recovery snapshots must:

- be explicitly enabled or initiated by the user or tenant policy
- contain only the minimum data required for recovery
- use platform protection or application encryption where sensitive information is included
- record creation time and schema version
- be importable through validated recovery logic
- be deleted or rotated after successful synchronization according to policy

A device-local snapshot reduces the risk of browser-cache loss but does not eliminate loss from device destruction, uninstall, filesystem clearing, forgotten encryption credentials, or inaccessible storage. Documentation must not claim zero risk.

### Tenant isolation

Tenant isolation is mandatory from the first implementation.

- Every canonical document path includes or resolves to an explicit tenant boundary.
- Firestore and Storage Rules validate tenant access.
- Trusted commands validate current server-side membership and role.
- JWT custom claims may provide coarse routing or platform roles but are not the sole source of dynamic tenant membership authorization.
- Batch requests may contain operations for only one tenant.
- Every batch, command, media object, print job, AI request, and export is tenant-scoped.

### FinOps measurements

The architecture accepts edge processing, batching, caching, and bounded AI use as cost controls. It rejects unvalidated percentage savings as contractual architecture facts.

Measure during pilot:

- median capture time per item
- review time per item and per batch
- AI calls per completed Thing
- function invocations and execution time per batch
- uploaded bytes per image profile
- AI input size and cost per accepted proposal
- cache hit rate
- label jobs per print interaction
- retry and conflict rate

Claims such as five-times faster intake, ninety-percent fewer function calls, or sixty-to-seventy-percent lower AI cost remain hypotheses until measured with representative PCO workflows.

## Consequences

### Benefits

- Faster uninterrupted field capture
- Lower print-dialog friction
- Lower avoidable media and AI processing cost
- Item-level retry and auditability
- Reuse of known taxonomy without unnecessary AI calls
- Multi-tenant boundaries established before commercialization

### Costs and risks

- More complex local state and recovery testing
- Partial batch-result handling
- Print queue reconciliation
- Taxonomy cache version and licensing management
- Device-specific image-processing performance
- Additional privacy controls for recovery snapshots

## Delivery priority

### MVP foundation

- `BatchIntakeSession` contract
- batch review presentation model
- `PrintQueue` contract
- configurable image derivative metadata
- strict tenant-scoped batch validation

### Pilot optimization

- bounded batch command endpoint
- safe bulk acceptance for allowlisted fields
- taxonomy cache and fuzzy suggestions
- optional native recovery snapshots
- measured workflow and FinOps benchmarks

### Deferred

- printer-specific direct batch drivers
- fully automatic crop acceptance
- cross-tenant batch administration
- performance or savings guarantees
