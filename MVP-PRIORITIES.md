# CCE / Orchid Enthusiasts MVP Priorities

> **Runtime target:** the Firebase-native serverless stack in ADR-001, confirmed by
> ADR-003 (`docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`).
> The `cce-orchid-mvp` FastAPI application was a throwaway prototype used to validate
> the vertical slice below; it is reference-only and is not deployed. See
> `docs/CODE-REVIEW.md`.

## P0 - Vertical slice proven by the prototype

The FastAPI prototype validated that this slice hangs together. Each item is carried
forward as a requirement for the native build, not as a shipped feature.

| Priority | Work item | Prototype status |
|---:|---|---|
| 1 | Mobile-first application shell | Validated |
| 2 | Seed platform administrator and PCO tenant administrator | Validated |
| 3 | Tenant isolation and PCO tenant context | Validated |
| 4 | Explicit Space / Area / Rack / Shelf / Slot locations | Validated |
| 5 | Orchid Create / Read / Update / Archive / Restore | Validated |
| 6 | Permanent ThingUUID, LabelID, and PCO accession number | Validated |
| 7 | QR lookup and 1 x 4 inch PDF label | Validated |
| 8 | iOS / Android responsive layouts | Validated; device QA pending |
| 9 | Automated end-to-end test | Validated (prototype pytest) |

## P0 - Build the native MVP (ADR-003)

Replaces the earlier Cloud Run / Cloud SQL / Alembic plan, which targeted the retired prototype.

1. Stand up the Firebase project and Emulator Suite; enable the required GCP APIs.
2. Add CI that runs Security Rules tests, JSON Schema validation of `packages/contracts`, and secret scanning on every pull request.
3. Generate TypeScript types from `packages/contracts` for shared client and function use.
4. Model Firestore under tenant-scoped paths; write tenant-isolation and role Security Rules first, with emulator tests for cross-tenant denial.
5. Configure Firebase Authentication (email/password) and App Check.
6. Build the React / TypeScript PWA shell with an offline draft store and visible synchronization state.
7. Implement callable Cloud Functions for trusted commands (create, update, archive, restore) with an operation ledger (`ClientOperationID` deduplication), `ExpectedVersion` checks, transactional per-tenant accession allocation, and appended lifecycle events.
8. Port label generation (1 x 4 inch PDF and QR) and public QR lookup.
9. Configure Firebase App Hosting and `orchid-enthusiasts.com` HTTPS routing.
10. Device QA: create, edit, archive, restore, PDF printing, and QR lookup on a physical iPhone and Android phone.

## P1 - Hardening after the native MVP

1. Enforce write authorization through App Check and Firebase Auth tokens on every callable command. (Replaces the prototype's CSRF item, which was specific to server-rendered form posts.)
2. Ensure every tenant, location, orchid, and label change appends an auditable lifecycle event through the append-only event ledger.
3. Represent location changes through event history rather than in-place mutation.
4. Store generated label PDFs in Cloud Storage when retention is required.
5. Add user-friendly validation and error states in the PWA.
6. Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts.

## P2 - First CCE experience expansion

1. First-class narratives with create, update, append, and remove.
2. Mobile photograph upload.
3. AI narrative extraction and one-question-at-a-time completion prompts (Genkit / Vertex, PROPOSE-only, human-confirmed).
4. “Tell me about this orchid.”
5. Orchid care and repotting guidance.
6. Sharing and similar-orchid discovery.

## P2 - Batch intake and FinOps (ADR-002)

1. `BatchIntakeSession` capture and consolidated proposal review.
2. Bounded batch command endpoint with item-level results and safe retry.
3. `PrintQueue` that distinguishes a print request from confirmed physical output.
4. Workflow and FinOps benchmarks measured against representative PCO workflows.
