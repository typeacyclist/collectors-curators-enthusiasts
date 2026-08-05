# Collectors–Curators–Enthusiasts (CCE)

CCE is an AI-native, mobile-first platform for documenting, organizing, managing, understanding, and selectively sharing physical collections. The initial specialty experience is **Orchid Enthusiasts**, validated with the initial tenant **PCO — Park City Orchids and More**.

> **The user tells the story. AI organizes the knowledge. The user remains in control.**

## Repository status

This repository is at the **pre-scaffold foundation stage** for the Firebase-native MVP.

Completed foundation work includes:

- authoritative product-governance and experience requirements
- current Orchid Enthusiasts MVP scope
- accepted architecture decisions for mobile, offline, AI, batching, tenancy, labels, media, and FinOps
- initial language-neutral JSON Schema contracts
- repository and code-review guardrails

The React/TypeScript PWA, Firebase Functions, Security Rules, Emulator Suite, and CI workspaces have not yet been scaffolded.

## Authoritative sources

Use these documents in this order when implementation details conflict:

1. `CCE Solution Governance and Experience Guidelines - AUTHORITATIVE.md`
2. `docs/architecture/ADR-001-ai-native-mobile-offline.md`
3. `docs/architecture/ADR-002-batch-intake-finops.md`
4. `docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`
5. `CCE  Orchid Enthusiasts MVP Definition - WORKING.md`
6. `packages/contracts/schemas/`
7. `AGENTS.md`
8. `MVP-PRIORITIES.md`

`docs/CODE-REVIEW.md` provides the implementation-review checklist. `docs/REPOSITORY-AUDIT-2026-08-05.md` records the repository retirement review.

## Target architecture

```text
React + TypeScript
    Responsive PWA with Capacitor-compatible iOS and Android shells

Firebase Hosting
    Web and PWA delivery

Firebase Authentication + App Check
    Identity and application attestation

Cloud Firestore + Security Rules
    Tenant-scoped operational data and synchronized query views

Cloud Functions for Firebase (TypeScript)
    Trusted commands, operation-ledger deduplication, version checks,
    accession allocation, and lifecycle events

Cloud Storage + Storage Rules
    Original media, derivatives, generated labels, and exports

Genkit + Vertex AI
    Governed READ_ONLY and PROPOSE AI flows
```

FastAPI, Cloud Run as the primary application host, and Cloud SQL/PostgreSQL as the operational database are not part of the MVP target runtime.

## Active repository layout

```text
.
├── AGENTS.md
├── CCE  Orchid Enthusiasts MVP Definition - WORKING.md
├── CCE Solution Governance and Experience Guidelines - AUTHORITATIVE.md
├── MVP-PRIORITIES.md
├── README.md
├── docs/
│   ├── CODE-REVIEW.md
│   ├── REPOSITORY-AUDIT-2026-08-05.md
│   └── architecture/
│       ├── ADR-001-ai-native-mobile-offline.md
│       ├── ADR-002-batch-intake-finops.md
│       └── ADR-003-retire-fastapi-adopt-firebase-native.md
└── packages/
    └── contracts/
        └── schemas/
            ├── batch.schema.json
            └── core.schema.json
```

## Retired implementation

The former `cce-orchid-mvp/` FastAPI prototype and its generated sample-label PDF were removed from the active tree on **2026-08-05**. They remain recoverable through Git history for migration mapping or historical comparison.

Do not restore or extend the retired runtime as production-target code. Reuse business requirements only after mapping them to the accepted JSON Schema contracts, Firebase authorization model, trusted command layer, offline behavior, and AI-governance requirements.

## Next implementation step

Scaffold the Firebase-native foundation:

1. npm workspaces and shared TypeScript configuration
2. React/Vite PWA application shell
3. TypeScript Cloud Functions workspace
4. Firebase Emulator Suite configuration
5. deny-by-default Firestore and Storage Rules with tenant-isolation tests
6. AJV schema validation and generated TypeScript contract types
7. offline draft-store interfaces and IndexedDB adapter foundation
8. CI for type-checking, tests, schema validation, Rules tests, and secret scanning

Feature implementation should follow the sequence in `MVP-PRIORITIES.md`.
