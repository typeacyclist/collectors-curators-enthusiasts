# CCE Architecture Code Review Guide

## Purpose

This document explains the architectural transition from the original FastAPI, Cloud Run, and Cloud SQL implementation plan to the accepted Firebase-native CCE runtime. It provides reviewers with a consistent checklist for determining whether new code follows the current product, security, mobile, offline, AI-governance, and tenant-isolation requirements.

## Governing documents

Review changes against these sources in order:

1. `CCE Solution Governance and Experience Guidelines - AUTHORITATIVE.md`
2. `docs/architecture/ADR-001-ai-native-mobile-offline.md`
3. `docs/architecture/ADR-002-batch-intake-finops.md`
4. `docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`
5. `CCE  Orchid Enthusiasts MVP Definition - WORKING.md`
6. JSON Schema contracts under `packages/contracts/schemas/`
7. `AGENTS.md`

The MVP definition governs product and experience scope. The accepted ADRs govern technical mechanisms where the former hosting plan conflicts with the current architecture.

## Retired implementation assumptions

Reject new production-target work that assumes:

- FastAPI is the primary application API
- Cloud Run is the primary host
- Cloud SQL or PostgreSQL is the operational database
- Python models are the canonical cross-layer contracts
- the client can perform unrestricted direct canonical writes
- a server connection is always available during orchid intake
- tenant identity can be inferred from a record identifier
- AI output may directly modify canonical records

Legacy files may remain temporarily for reference or migration mapping, but they must be marked non-authoritative and must not be extended as the target runtime.

## Current runtime expectations

Changes should align with:

- React and TypeScript
- mobile-first PWA delivery through Firebase Hosting
- Capacitor-compatible iOS and Android shells
- Firebase Authentication and App Check
- Cloud Firestore and Security Rules
- Cloud Storage and Storage Rules
- TypeScript Cloud Functions for trusted commands
- Genkit and Vertex AI for governed AI flows
- language-neutral JSON Schema contracts

## Review checklist

### Mobile and accessibility

- Every required workflow works at mobile widths beginning near 320 pixels.
- No required interaction depends on hover, right-click, or desktop-only layout.
- Touch targets, focus handling, contrast, loading states, and error states are explicit.
- Browser back navigation and application suspension do not silently lose active work.
- Dense tabular views become cards, stacked rows, or another usable mobile presentation.

### Offline and synchronization

- Essential orchid intake can begin and continue without connectivity.
- Drafts persist through application suspension and accidental navigation.
- Sync state is visible and supports retry.
- Reconnect, application resume, manual sync, and pending-work review can trigger synchronization.
- Browser background sync is not the only recovery mechanism.
- Unsupported offline actions are visibly pending or unavailable rather than appearing successful.

### Identity and commands

- `ThingUUID`, `LabelID`, and `AccessionNumber` remain separate concepts.
- Identifiers are never treated as authorization credentials.
- Canonical commands contain `ClientOperationID`, tenant identity, Thing identity, actor identity, command type, payload, and expected version where applicable.
- Trusted command handlers use transactional ledger deduplication and version checks.
- Duplicate replay returns the original result rather than repeating the operation.
- Conflicts produce reviewable outcomes rather than last-write-wins replacement.

### Tenant isolation

- Every query, command, batch, storage path, print job, AI request, and export resolves an explicit tenant boundary.
- Firestore and Storage Rules validate access.
- Trusted commands validate current server-side membership and role.
- JWT custom claims are not the sole authority for dynamic tenant membership.
- Batch requests contain operations for one tenant only.
- Tests attempt cross-tenant reads and writes and verify denial.

### AI governance

- Narratives, OCR, labels, images, and documents are treated as untrusted evidence.
- AI permissions are limited to read and propose.
- Structured output is validated against strict schemas and unexpected keys are rejected.
- Proposals preserve evidence references, confidence, uncertainty, and model/prompt/schema versions.
- Consequential changes require deterministic authorization, validation, and user confirmation.
- AI confidence alone does not permit bulk changes to identity, location, privacy, publication, transfer, sale, archive, or tenant access.

### Batch workflows

- A batch is an orchestration boundary, not a replacement for item-level identity or auditability.
- Large batches are not implemented as one all-or-nothing Firestore transaction.
- Commands use bounded concurrency and item-level transactional handling.
- Partial success, conflicts, retryable failures, and permanent failures are distinguishable.
- Failed items can be retried without replaying successful items.
- Bulk review is limited to allowlisted low-consequence fields without evidence conflicts.

### Media and FinOps

- Original evidence is preserved according to tenant policy.
- Configurable display, AI, OCR-region, and thumbnail derivatives are supported where appropriate.
- Processing metadata records dimensions, encoding, crop, orientation correction, profile, and processing version.
- Example image sizes are configuration values, not permanent architecture contracts.
- Quotas, rate limits, duplicate detection, caching, and model routing are applied server-side where needed.
- Claimed speed or cost reductions are measured pilot outcomes, not unverified guarantees.

### Labels and printing

- Label behavior is accessed through `LabelService`.
- Print requests use a queue and can aggregate compatible jobs into PDF or later printer-specific payloads.
- Queueing or generating a PDF does not prove physical printing.
- Print request and print confirmation remain separate when confirmation is available.
- QR routes remain stable when records are renamed, moved, transferred, or archived.

### Data and contract quality

- Canonical shapes are defined in versioned JSON Schema.
- Unknown properties are rejected where contracts require closed objects.
- Valid and invalid examples are maintained.
- Cross-file references resolve during automated validation.
- Taxonomy concepts remain separate and preserve the name as entered.
- Cached or fuzzy taxonomy matches are not described as external verification without an approved source.

## Migration review

When translating legacy FastAPI or PostgreSQL behavior:

1. Identify the business requirement independently of the old framework.
2. Map the behavior to a current JSON Schema contract.
3. Determine whether it is a query, trusted command, background process, or local draft operation.
4. Preserve stable identifiers, narratives, evidence, lifecycle history, and tenant boundaries.
5. Replace database-specific assumptions with Firestore-aware access patterns.
6. Add emulator and tenant-isolation tests before considering the migration complete.
7. Archive obsolete deployment files after equivalent Firebase behavior is verified.

## Required validation before merge

Run the applicable checks:

- TypeScript compilation
- unit tests
- JSON Schema compilation and examples
- Firebase Emulator tests
- Firestore and Storage Security Rules tests
- tenant-isolation tests
- idempotency and version-conflict tests
- partial batch success and retry tests
- print queue reconciliation tests
- mobile viewport and accessibility tests
- AI golden-set and adversarial evidence tests
- secret scanning

Documentation-only changes should still be checked for conflicting architecture statements, broken file references, and terminology inconsistent with the accepted ADRs.
