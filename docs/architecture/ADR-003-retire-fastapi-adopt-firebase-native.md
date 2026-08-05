# ADR-003: Retire FastAPI and Cloud SQL; Adopt the Firebase-Native Runtime

- Status: Accepted
- Scope: CCE platform and Orchid Enthusiasts MVP runtime and deployment architecture
- Depends on: ADR-001 and ADR-002
- Supersedes: the legacy FastAPI, Cloud Run, and Cloud SQL hosting plan retained in repository history

## Context

The original MVP implementation plan used a FastAPI application deployed to Cloud Run with Cloud SQL for PostgreSQL. That design supported a conventional request/response web application, but it did not align well with the current CCE requirements for:

- mobile-first and intermittent-connectivity workflows
- local draft preservation and synchronization
- direct Firebase Authentication and App Check integration
- Firestore Security Rules for tenant-scoped query access
- trusted command handling with transactional operation-ledger controls
- governed Genkit and Vertex AI orchestration
- one React and TypeScript application prepared for PWA and Capacitor delivery
- lower operational overhead during MVP validation

ADR-001 established the target architecture. ADR-002 extended that architecture with batch intake, print spooling, edge media processing, local recovery controls, and FinOps measurements. This ADR formally retires the prior runtime so product documents do not describe two competing deployment models.

## Decision

Use the Firebase-native serverless runtime as the authoritative MVP architecture.

### Client and delivery

- React and TypeScript
- Responsive Progressive Web Application
- Firebase Hosting
- Capacitor-compatible iOS and Android shells without separate native application codebases

### Identity and application protection

- Firebase Authentication
- Firebase App Check
- Server-side membership and role validation for trusted commands

### Operational data and synchronization

- Cloud Firestore
- Firestore Security Rules
- Firebase offline SDK capabilities where appropriate
- Application-managed `OfflineDraftStore` for required offline intake behavior
- Transactional command handlers for canonical writes

### Media and generated assets

- Cloud Storage
- Tenant-scoped object paths and Storage Rules
- Preserved originals according to tenant policy
- Configurable display, AI, OCR-region, and thumbnail derivatives

### Trusted server operations

- Cloud Functions written in TypeScript
- Command/query separation
- Transactional operation-ledger deduplication
- Expected-version conflict detection
- Server-assigned accession numbers
- Append-oriented lifecycle events

### Governed AI

- Genkit and Vertex AI
- AI permissions limited to read and propose
- Strict schemas, provenance, confidence, and evidence references
- Deterministic validation and required user confirmation for consequential changes

## Retired runtime

The following are not part of the target MVP runtime:

- FastAPI as the primary application API
- Cloud Run as the primary application host
- Cloud SQL or PostgreSQL as the operational database
- server-rendered or Python-specific domain contracts
- direct database CRUD from the user interface

Legacy code and documentation may remain temporarily as reference material, but they must be clearly marked as archived or retired. New implementation work must not extend the retired runtime unless a later ADR explicitly reverses this decision.

## Migration rules

1. Preserve business requirements and user workflows independently of the retired implementation.
2. Translate canonical records and commands into language-neutral JSON Schema contracts.
3. Keep `ThingUUID`, `LabelID`, and tenant identity stable during any data migration.
4. Preserve narratives, original evidence, audit history, and lifecycle events.
5. Do not migrate secrets, obsolete session data, generated build output, or environment-specific credentials.
6. Validate tenant isolation before importing any production or pilot data.
7. Treat the prior PostgreSQL schema as a source mapping, not as the new Firestore document model.
8. Remove or archive deployment files that could accidentally deploy the retired runtime after equivalent Firebase capabilities exist.

## Documentation authority

- Product and experience scope: `CCE  Orchid Enthusiasts MVP Definition - WORKING.md`
- Governing product standard: `CCE Solution Governance and Experience Guidelines - AUTHORITATIVE.md`
- Core runtime and offline architecture: ADR-001
- Batch and FinOps controls: ADR-002
- Runtime retirement and migration boundary: ADR-003
- Review background and migration checklist: `docs/CODE-REVIEW.md`

When documents conflict, the authoritative governance document and accepted ADRs control implementation details. Product requirements remain valid unless an ADR changes only the technical mechanism used to deliver them.

## Consequences

### Benefits

- One coherent target runtime
- Better alignment with offline mobile intake
- Direct tenant-aware Firebase authorization controls
- Reduced MVP infrastructure and deployment complexity
- Shared TypeScript contracts across client and trusted functions
- Native integration with Genkit, Vertex AI, App Check, and Firebase emulators

### Costs and risks

- Existing FastAPI and PostgreSQL code cannot be treated as production-ready target code
- Firestore data modeling and query design require deliberate contract work
- Security Rules and emulator tests become mandatory
- Offline drafts, retries, conflicts, and partial batch outcomes require explicit application state
- Some administrative or reporting workflows may later require derived projections or export pipelines

## Validation

This decision is implemented when:

1. Product documents no longer present Cloud Run and Cloud SQL as the active MVP architecture.
2. New contracts are language-neutral and shared by the React client and TypeScript functions.
3. Firebase emulator tests cover authentication, tenant isolation, commands, retries, and conflicts.
4. The PWA supports required offline intake and synchronized canonical commit.
5. Legacy deployment assets are archived or clearly marked non-authoritative.
