# CCE / Orchid Enthusiasts MVP Priorities

> **Runtime target:** the Firebase-native serverless stack in ADR-001, confirmed by
> ADR-003 (`docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`).
> The `cce-orchid-mvp` FastAPI application is a reference prototype used to validate
> selected vertical-slice behavior. It is not the target runtime and must not be deployed.
> See `docs/CODE-REVIEW.md`.

## P0 - Capabilities demonstrated by the prototype

The prototype demonstrated that the following workflow concepts can operate together. These results are implementation evidence, not completion of the Firebase-native MVP.

| Priority | Work item | Prototype evidence |
|---:|---|---|
| 1 | Mobile-first application shell | Demonstrated |
| 2 | Seed platform administrator and PCO tenant administrator | Demonstrated |
| 3 | Tenant isolation and PCO tenant context | Demonstrated in prototype scope |
| 4 | Explicit Space / Area / Rack / Shelf / Slot locations | Demonstrated |
| 5 | Orchid Create / Read / Update / Archive / Restore | Demonstrated |
| 6 | Permanent ThingUUID, LabelID, and PCO accession number | Demonstrated |
| 7 | QR lookup and 1 x 4 inch PDF label | Demonstrated |
| 8 | iOS / Android responsive layouts | Implemented in prototype; physical-device QA pending |
| 9 | Automated end-to-end test | Demonstrated with prototype tests |

## P0 - Build the Firebase-native MVP

This work replaces the earlier Cloud Run, Cloud SQL, and Alembic deployment plan for the retired prototype.

1. Stand up the Firebase project and Emulator Suite; enable the required GCP APIs.
2. Add CI that runs Security Rules tests, JSON Schema validation of `packages/contracts`, and secret scanning on every pull request.
3. Generate TypeScript types from `packages/contracts` for shared client and function use.
4. Model Firestore under tenant-scoped paths; write tenant-isolation and role Security Rules first, with emulator tests for cross-tenant denial.
5. Configure Firebase Authentication with email/password and Firebase App Check.
6. Build the React and TypeScript PWA shell with an offline draft store and visible synchronization state.
7. Implement callable Cloud Functions for trusted commands—create, update, archive, and restore—with an operation ledger for `ClientOperationID` deduplication, `ExpectedVersion` checks, transactional per-tenant accession allocation, and appended lifecycle events.
8. Port label generation for 1 x 4 inch PDF and QR output, plus public QR lookup.
9. Configure Firebase Hosting and `orchid-enthusiasts.com` HTTPS routing.
10. Complete physical-device QA for create, edit, archive, restore, PDF printing, and QR lookup on iPhone and Android.

## P1 - Hardening after the Firebase-native MVP

1. Enforce write authorization through App Check and Firebase Authentication tokens on every callable command.
2. Ensure every tenant, location, orchid, and label change appends an auditable lifecycle event through the append-oriented event ledger.
3. Represent location changes through event history rather than relying only on in-place state mutation.
4. Store generated label PDFs in Cloud Storage when retention is required.
5. Add user-friendly validation and error states in the PWA.
6. Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts.

## P2 - First CCE experience expansion

1. First-class narratives with create, update, append, and remove.
2. Mobile photograph upload.
3. AI narrative extraction and one-question-at-a-time completion prompts using Genkit and Vertex AI, limited to `PROPOSE` with human confirmation.
4. “Tell me about this orchid.”
5. Orchid care and repotting guidance.
6. Sharing and similar-orchid discovery.

## P2 - Batch intake and FinOps

1. `BatchIntakeSession` capture and consolidated proposal review.
2. Bounded batch command endpoint with item-level results and safe retry.
3. `PrintQueue` that distinguishes a print request from confirmed physical output.
4. Workflow and FinOps benchmarks measured against representative PCO workflows.
