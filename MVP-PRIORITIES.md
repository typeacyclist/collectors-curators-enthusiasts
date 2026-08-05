# CCE / Orchid Enthusiasts MVP Priorities

> **Runtime target:** the Firebase-native serverless stack in ADR-001, confirmed by
> ADR-003 (`docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`).
> The former FastAPI prototype was removed from the active tree on 2026-08-05.
> Its historical implementation evidence remains available through Git history.

## P0 - Capabilities demonstrated by the retired prototype

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

## P0 - Complete contracts and validation foundation

1. Add canonical schemas for command envelopes, identity, tenants, memberships, locations, taxonomy, narratives, AI proposals, media, labels, exports, and the contract registry.
2. Add valid and invalid contract examples.
3. Add AJV compilation with cross-file reference validation.
4. Generate TypeScript types from versioned schemas.
5. Add contract compatibility and unknown-property tests.
6. Add CI for schema validation, type-checking, tests, and secret scanning.

## P0 - Scaffold the Firebase-native MVP

This work replaces the earlier Cloud Run, Cloud SQL, and Alembic deployment plan for the retired prototype.

1. Add npm workspaces and shared TypeScript configuration.
2. Create the React and TypeScript Vite PWA shell.
3. Create the TypeScript Cloud Functions workspace.
4. Configure the Firebase Emulator Suite.
5. Add deny-by-default Firestore and Storage Rules.
6. Add tenant-isolation and role Rules tests before application data access.
7. Configure Firebase Authentication with email/password and Firebase App Check.
8. Add the `OfflineDraftStore` interface and IndexedDB adapter foundation with visible synchronization state.
9. Add callable command foundations with operation-ledger deduplication, `ExpectedVersion` checks, tenant validation, accession allocation, and lifecycle events.
10. Configure Firebase Hosting and `orchid-enthusiasts.com` HTTPS routing after local and emulator validation.

## P1 - First usable Firebase-native vertical slice

1. PCO owner authentication and tenant context.
2. Explicit location hierarchy management.
3. Orchid Create / Read / Update / Archive / Restore.
4. Offline intake draft creation and retryable synchronization.
5. Permanent `ThingUUID` and `LabelID`; server-assigned PCO accession number.
6. Public and authorized QR lookup.
7. Versioned 1 x 4 inch PDF label generation through `LabelService`.
8. Physical-device QA on iPhone and Android.

## P1 - Hardening

1. Enforce App Check, Firebase Authentication, current server-side membership, and role checks on trusted commands.
2. Ensure every tenant, location, orchid, and label change appends an auditable lifecycle event.
3. Represent location changes through event history while retaining explicit current state.
4. Store generated label PDFs in Cloud Storage when retention is required.
5. Add user-friendly validation, conflict, retry, and error states in the PWA.
6. Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts.

## P2 - First CCE experience expansion

1. First-class narratives with create, update, append, remove, and permitted restoration.
2. Mobile photograph capture and upload with original preservation and configured derivatives.
3. AI narrative extraction and one-question-at-a-time completion prompts using Genkit and Vertex AI, limited to `PROPOSE` with human confirmation.
4. “Tell me about this orchid.”
5. Orchid care and repotting guidance.
6. Sharing and similar-orchid discovery.

## P2 - Batch intake and FinOps

1. `BatchIntakeSession` capture and consolidated proposal review.
2. Bounded batch command endpoint with item-level results and safe retry.
3. `PrintQueue` that distinguishes a print request from confirmed physical output.
4. Workflow and FinOps benchmarks measured against representative PCO workflows.
