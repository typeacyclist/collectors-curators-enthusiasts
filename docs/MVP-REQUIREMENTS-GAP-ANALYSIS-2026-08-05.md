# CCE / Orchid Enthusiasts MVP — Requirements Gap Analysis

- **Date:** 2026-08-05
- **Scope:** every tracked document in the repository at the pre-scaffold foundation stage
- **Purpose:** identify requirements that are **missing**, **underspecified**, or **contradictory** across the documentation set, before Firebase-native scaffolding begins
- **Status of this document:** resolved 2026-08-05 — 71 of 75 findings resolved in the documents and contracts listed in the Resolution log below; 4 findings (5, 6, 13, 59) await a product decision. Detail sections below record the original analysis.

## Documents reviewed

1. `README.md`
2. `MVP-PRIORITIES.md`
3. `CCE  Orchid Enthusiasts MVP Definition - WORKING.md`
4. `CCE Solution Governance and Experience Guidelines - AUTHORITATIVE.md`
5. `AGENTS.md`
6. `docs/CODE-REVIEW.md`
7. `docs/REPOSITORY-AUDIT-2026-08-05.md`
8. `docs/architecture/ADR-001-ai-native-mobile-offline.md`
9. `docs/architecture/ADR-002-batch-intake-finops.md`
10. `docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`
11. `packages/contracts/schemas/core.schema.json`
12. `packages/contracts/schemas/batch.schema.json`

## Method

Six independent specialist reviews swept the full documentation set — product/UX journeys, orchid-domain fitness, contracts-vs-features consistency, security/privacy/compliance, operations/launch readiness, and non-functional requirements/testability. Raw findings (96) were consolidated (75 distinct gaps), and every candidate was then **adversarially verified**: a separate fact-checking pass attempted to refute each finding by locating documentation that already covers it. Findings the docs already resolve were to be discarded; **none were refuted**. Verification verdicts:

- **Missing** — no meaningful coverage found anywhere in the documentation set.
- **Partially covered** — the topic is named or partially addressed, but a real gap remains (a doc saying "add X later" without defining X counts as partial at best).

Findings that fall inside the schema list `MVP-PRIORITIES.md` already acknowledges as to-be-added are marked **(acknowledged schema gap)** — they are included only where a concrete unresolved design question goes beyond the acknowledgement.

Priorities: **P0** = must resolve before or at MVP launch · **P1** = resolve during pilot hardening · **P2** = post-pilot, but record the decision now.

## Result summary

**75 verified gaps** — 24 P0, 42 P1, 9 P2; 30 fully missing, 45 partially covered.

## Executive summary

The documentation set is unusually strong on **how to build safely** — AI governance, tenant isolation, offline command semantics, idempotency, batch processing, and privacy principles are specified in depth and were deliberately not re-litigated here. The verified gaps cluster in eight themes:

### 1. The launch path has more holes than the product does

The docs describe the running product well but not how it comes to exist or stays alive: there is no production bootstrap for the PCO tenant under deny-by-default Rules (#8 — a genuine bootstrap paradox), no dev/staging/prod environment strategy (#3), no deployment/rollback pipeline (CI covers checks only, #2), no email-sending capability anywhere in the architecture despite invitations, password reset, and notifications all needing it (#35), no error/crash reporting (#32), and no support or feedback channel for the pilot (#38).

### 2. Account and tenancy lifecycle is one screen deep

The screens list has Sign in and Create account and nothing else: no password reset, email verification, or MFA (#1) for a persona explicitly defined as older and nontechnical; a stranger who creates an account on the public site lands in an undefined tenant-less dead end (#6); member invitation is named but has no workflow (#51); session lifetime and revocation for removed members are unspecified (#60); the Owner role "manages subscription" but no subscription exists anywhere (#34); and the deletion rights the governance doc promises have no workflow or propagation spec (#46).

### 3. Contract–product drift has already started, pre-scaffold

The two schemas that exist already disagree with the product docs: the `thingEvent` enum cannot express transfer, sale, status, sharing, print confirmation, or the MVP's own history vocabulary (#12); the Thing/DraftThing contracts have no fields for the orchid data the Update workflow requires (#11); Collections — a core concept — are absent even from the acknowledged to-be-added schema list (#9); `DRAFT` exists as a status in the schema but in no product document (#29); and the MVP's own Update field list collapses species/grex and cultivar/clone, contradicting ADR-001's taxonomy separation (#21).

### 4. Six confirmed cross-document contradictions

Verification confirmed genuine conflicts, with quotes, in: voice input mechanism — device-keyboard dictation vs platform transcription with audio deletion (#13); similar-orchid discovery — MVP Release 5 scope vs ADR-001 "post-MVP" (#59); the event vocabulary (#12); the taxonomy field collapse (#21); exact-timestamp `EffectiveAt` vs the no-false-precision rule for backdated events (#30); and the `DRAFT` status (#29). The documented precedence rules do not cleanly resolve the first two because they are scope conflicts, not mechanism conflicts.

### 5. Architecture decisions the scaffold needs are unrecorded

Full-text narrative search is a headline MVP feature and Firestore cannot do it natively — no search-service decision is recorded (#5). There is no Firestore data-model/index design even though the documented dashboard and search queries cannot be answered from the current contracts (#16). Offline intake depends on a locally available location tree, collection list, and template that nothing says will be cached (#17), and offline draft storage has no quota/eviction/loss behavior (#18).

### 6. The privacy/legal surface is behind the governance ambition

No Terms of Service or Privacy Policy pages (#4); EXIF/GPS stripping for shared photos is implied but never required — a direct exact-location leak vector the governance doc otherwise defends against (#19); no Vertex AI data-governance terms (model-training exclusion, residency, AI log retention) (#26); no content moderation or takedown path for PUBLIC sharing (#28); telemetry vs privacy-by-design is unresolved (#36); and append-only lifecycle events have no PII redaction mechanism, which collides with deletion rights (#47).

### 7. Success is defined but nothing measures it

Section 24's targets ("under two minutes", "without training") and ADR-002's FinOps metrics have no measurement mechanism (#15, #39); there are no performance budgets beyond the two-minute figure (#7); FinOps is measurement-only with no billing budgets or spend caps to prevent runaway pilot cost (#14); the mandated AI golden-set merge gate has no data, owner, or thresholds (#42); and pilot exit criteria beyond the UX checklist are undefined (#54).

### 8. Orchid-domain depth the pilot customer will hit in week one

Care guidance is promised with no knowledge source or accuracy requirement (#43); a Quarantine area/status/collection all exist but no quarantine or pest/disease workflow is defined (#31); the Oakland Acquisition scenario needs an acquisition-lot concept batch intake doesn't have (#49); `DIVIDED` has no parent/child lineage (#37); and "For Sale" gives a buyer no way to contact PCO while default privacy hides contact info (#61).

### If only ten findings get attention, make it these

| Finding | Why first |
|---|---|
| #8 Production bootstrap | Nothing in the P1 vertical slice is acceptable without it; improvised console writes would poison the audit trail from day one |
| #1 Password reset / verification | Locked-out Owner = lost business records; target persona makes this near-certain |
| #6 Non-PCO sign-up dead end | Public site + Create account + no defined outcome = worst possible first impression |
| #4 ToS / Privacy Policy | Public launch with accounts, photos, minors possible, and AI processing — a legal blocker |
| #5 Search architecture decision | Headline feature; impossible on Firestore natively; retrofitting changes the data model |
| #16 Firestore data model | Deny-by-default Rules and dashboards both depend on it; expensive to change later |
| #12 / #11 Event enum + orchid fields | Every feature built on the current contracts inherits the drift |
| #13 Voice input contradiction | Determines whether an entire transcription/audio-deletion subsystem exists in MVP |
| #17+#18 Offline reference data + quota | "Field-ready offline intake" silently fails in the greenhouse without both |
| #15 Success-metric telemetry | Without it the pilot cannot prove or disprove the MVP thesis it exists to test |

## Resolution log (2026-08-05)

Shorthand: **MVP Def** = `CCE  Orchid Enthusiasts MVP Definition - WORKING.md` · **core** / **batch** = the JSON schemas · **ACCT** = `docs/requirements/ACCOUNT-TENANT-LIFECYCLE.md` · **OPS** = `docs/requirements/OPERATIONS-LAUNCH-READINESS.md` · **PRIV** = `docs/requirements/PRIVACY-LEGAL-COMPLIANCE.md` · **MEAS** = `docs/requirements/MEASUREMENT-ACCEPTANCE-NFR.md` · **ORCH** = `docs/requirements/ORCHID-DOMAIN-REQUIREMENTS.md`

| # | Resolution |
|---:|---|
| 1 | Resolved — MVP Def screens list (reset, verification, account settings) + ACCT §1 |
| 2 | Resolved — OPS §2 (CI deploy pipeline, rollback) |
| 3 | Resolved — OPS §1 (dev/staging/prod projects) |
| 4 | Resolved — MVP Def screens list + PRIV §1 (ToS, Privacy Policy, acceptance gate) |
| 5 | **Decision pending** — search architecture (client-side index vs managed service vs defer full-text) |
| 6 | **Decision pending** — public sign-up model; interim guard in ACCT §2 |
| 7 | Resolved — MEAS §2 (performance budgets) |
| 8 | Resolved — OPS §3 (scripted idempotent bootstrap) + MVP-PRIORITIES P0 scaffold item 11 |
| 9 | Resolved — core `collection` def (copy-at-creation semantics) + MVP Def §5 (Archived collection removed) |
| 10 | Resolved — batch `commandType` taxonomy + `commandEnvelope` + consequence classes |
| 11 | Resolved — core `orchidTemplateData` + `TemplateData` on thing/draftThing |
| 12 | Resolved — core `EventType` enum aligned; MVP Def §12 mapping note |
| 13 | **Decision pending** — voice mechanism (device dictation vs platform transcription) |
| 14 | Resolved — MEAS §4 ($100 provisional budget, alerts, quotas) |
| 15 | Resolved — MEAS §1 (instrumentation map) + MVP-PRIORITIES P1 hardening item 7 |
| 16 | Resolved — MVP-PRIORITIES P0 contracts item 7 (data-model design work item before Rules) |
| 17 | Resolved — MVP Def connectivity (offline reference data) + AGENTS.md offline rules |
| 18 | Resolved — MVP Def connectivity (quota behavior) + AGENTS.md offline rules |
| 19 | Resolved — AGENTS.md media rule + PRIV §2 (EXIF/GPS stripping, acceptance test) |
| 20 | Resolved — MVP Def §9 "Scan states for every viewer" |
| 21 | Resolved — MVP Def Update fields separated + core taxonomy fields |
| 22 | Resolved — core `aiProposal` / `aiProposalClaim` contracts |
| 23 | Resolved — MVP Def §21 allocation rules + core AccessionNumber comment |
| 24 | Resolved — ACCT §3 (role-to-command matrix, platform admin, elevated deletion) |
| 25 | Resolved — PRIV §5 (SHARED_LINK = separate revocable token, `/s/{ShareToken}`) |
| 26 | Resolved — PRIV §3 (no-training terms, region pinning, AI log retention) |
| 27 | Resolved — MEAS §3 (scale envelope) |
| 28 | Resolved — PRIV §5 (report action, unpublish power, takedown contact) |
| 29 | Resolved — core `thingStatus` DRAFT removed |
| 30 | Resolved — core `EffectiveAtPrecision` + MVP Def §12 note |
| 31 | Resolved — ORCH §2 (quarantine workflow) |
| 32 | Resolved — OPS §5 (scrubbed error/crash reporting) |
| 33 | Resolved — OPS §13 (incident response, 72-hour breach notification) |
| 34 | Resolved — deferred; ACCT §4 + MVP Def §25 |
| 35 | Resolved — OPS §4 (transactional email, SPF/DKIM/DMARC) |
| 36 | Resolved — PRIV §6 (first-party content-free telemetry policy) |
| 37 | Resolved — core `RelatedThingUUIDs` + ORCH §3 (division lineage) |
| 38 | Resolved — OPS §10 (help entry, support email, feedback form) |
| 39 | Resolved — MEAS §6 (usability protocol) |
| 40 | Resolved — PRIV §5 (rate limiting, non-enumerability, uniform generic page) |
| 41 | Resolved — MEAS §7 (WCAG 2.1 AA + test method) |
| 42 | Resolved — MEAS §5 (golden set: owner, contents, thresholds, CI gate) |
| 43 | Resolved — ORCH §1 (curated versioned care knowledge base) |
| 44 | Resolved — OPS §8 (pinned models, reviewed prompt changes) |
| 45 | Resolved — MEAS §9 (support floor + physical-device QA set) |
| 46 | Resolved — PRIV §4 (deletion workflows, propagation, grace period) |
| 47 | Resolved — PRIV §4 + core `REDACTED`/`REDACT_EVENT` tombstone mechanism |
| 48 | Resolved — OPS §9 (domain continuity) |
| 49 | Resolved — batch `batchIntakeSession.SharedDefaults` + ORCH §4 |
| 50 | Resolved — MEAS §11 (synthetic stock, 300 DPI, 30-day greenhouse scan test) |
| 51 | Resolved — ACCT §5 + MVP-PRIORITIES P1 hardening item 8 |
| 52 | Resolved — OPS §6 (alert signals, thresholds, recipients) |
| 53 | Resolved — ACCT §6 (in-app-only notification surface) |
| 54 | Resolved — MEAS §12 (pilot exit criteria) |
| 55 | Resolved — MVP-PRIORITIES P1 hardening item 9 (tenant JSON/CSV export) |
| 56 | Resolved — free text retained; deferral recorded in MVP Def §25 + ORCH §5 |
| 57 | Resolved — MEAS §8 (AI never blocks intake; async fallback) |
| 58 | Resolved — OPS §7 (PITR, media versioning, RPO/RTO, restore tests) |
| 59 | **Decision pending** — similarity scope (deterministic matching in Release 5 vs move post-MVP) |
| 60 | Resolved — ACCT §7 (sessions, revocation ≤1 h, sign-out safeguards) |
| 61 | Resolved — MVP Def §17 (tenant public contact method) + ORCH §6 |
| 62 | Resolved — core DraftThing.Narrative mapping comment (first timeline entry) |
| 63 | Resolved — core `labelTemplate` contract (allowlisted fields, privacy review) |
| 64 | Resolved — core/batch `labelId` (opaque 8–36 char; short codes preferred) |
| 65 | Resolved — MEAS §10 (standard-user conflict screen) |
| 66 | Resolved — ORCH §6 (listing, transfer, post-transfer QR) |
| 67 | Resolved — deferred; MVP Def §25 (reminders/tasks) |
| 68 | Resolved — ORCH §7 (ISO 4217, UTC + precision, metric-when-structured) |
| 69 | Resolved — PRIV §1 (18+ minimum age) |
| 70 | Resolved — deferred; MVP Def §25 + ORCH §8 (EnvironmentNotes accommodation) |
| 71 | Resolved — ORCH §9 (first-run card, defined empty states) |
| 72 | Resolved — OPS §11 (pilot SLO 99.5%, support expectations) |
| 73 | Resolved — deferred; MVP Def §25 + ORCH §10 |
| 74 | Resolved — ORCH §11 (BLOOM_* canonical, "Flowered" mapping) |
| 75 | Resolved — OPS §12 (workload identity, Secret Manager, rotation) |


## P0 — must resolve before or at MVP launch

These gaps block scaffolding decisions, block launch, or would be materially more expensive to fix after implementation starts.

| # | Finding | Area | Verdict |
|---:|---|---|---|
| 1 | [Password reset, email verification, and MFA absent from MVP screens and all requirements](#1-password-reset-email-verification-and-mfa-absent-from-mvp-screens-and-all-requirements) | `authentication` | Missing |
| 2 | [Deployment pipeline and rollback are unspecified (CI covers checks only)](#2-deployment-pipeline-and-rollback-are-unspecified-ci-covers-checks-only) | `deployment` | Missing |
| 3 | [No dev/staging/prod Firebase environment strategy](#3-no-devstagingprod-firebase-environment-strategy) | `environment-strategy` | Missing |
| 4 | [Terms of Service and Privacy Policy pages absent from MVP screens and all requirements](#4-terms-of-service-and-privacy-policy-pages-absent-from-mvp-screens-and-all-requirements) | `legal-compliance` | Missing |
| 5 | [Full-text narrative search has no recorded architecture decision on Firestore](#5-full-text-narrative-search-has-no-recorded-architecture-decision-on-firestore) | `missing-decision` | Missing |
| 6 | [Self-serve sign-up on orchid-enthusiasts.com leads to an undefined dead end for non-PCO users](#6-self-serve-sign-up-on-orchid-enthusiastscom-leads-to-an-undefined-dead-end-for-non-pco-users) | `onboarding-tenancy` | Missing |
| 7 | [No performance budgets beyond the two-minute record target](#7-no-performance-budgets-beyond-the-two-minute-record-target) | `performance` | Missing |
| 8 | [Production bootstrap of platform admin and PCO tenant is undefined in the Firebase-native plan](#8-production-bootstrap-of-platform-admin-and-pco-tenant-is-undefined-in-the-firebase-native-plan) | `tenant-lifecycle` | Missing |
| 9 | [Collections contract is missing and absent from the acknowledged to-be-added schema list](#9-collections-contract-is-missing-and-absent-from-the-acknowledged-to-be-added-schema-list) | `contract-gap` | Partially covered |
| 10 | [Command envelope and command-type taxonomy cannot express the MVP command set or ADR-002's authorization rules](#10-command-envelope-and-command-type-taxonomy-cannot-express-the-mvp-command-set-or-adr-002s-authorization-rules) | `contract-gap` | Partially covered |
| 11 | [Core Thing/DraftThing contracts have no place for required orchid fields (genus, grex, cultivar, acquisition, notes, temporary name)](#11-core-thingdraftthing-contracts-have-no-place-for-required-orchid-fields-genus-grex-cultivar-acquisition-notes-temporary-name) | `contract-gap` | Partially covered |
| 12 | [thingEvent EventType enum contradicts the MVP, governance, and ADR-002 event vocabulary (transfer, sale, status, sharing, print confirm, naming)](#12-thingevent-eventtype-enum-contradicts-the-mvp-governance-and-adr-002-event-vocabulary-transfer-sale-status-sharing-print-confirm-naming) | `contract-mismatch` | Partially covered |
| 13 | [Voice input mechanism contradictory: device-keyboard dictation vs platform transcription with audio deletion](#13-voice-input-mechanism-contradictory-device-keyboard-dictation-vs-platform-transcription-with-audio-deletion) | `contradiction` | Partially covered |
| 14 | [No billing budgets, Vertex AI spend caps, or numeric quota values — FinOps guardrails are measurement-only](#14-no-billing-budgets-vertex-ai-spend-caps-or-numeric-quota-values--finops-guardrails-are-measurement-only) | `finops` | Partially covered |
| 15 | [Section 24 success targets and ADR-002 FinOps metrics have no measurement mechanism](#15-section-24-success-targets-and-adr-002-finops-metrics-have-no-measurement-mechanism) | `measurement-telemetry` | Partially covered |
| 16 | [No Firestore data-model, index, or projection design despite queries the contracts cannot answer](#16-no-firestore-data-model-index-or-projection-design-despite-queries-the-contracts-cannot-answer) | `missing-requirement` | Partially covered |
| 17 | [Offline intake depends on locally available location tree, collection list, and template — availability never specified](#17-offline-intake-depends-on-locally-available-location-tree-collection-list-and-template--availability-never-specified) | `missing-requirement` | Partially covered |
| 18 | [Offline draft storage quota, eviction, and loss behavior undefined for the PWA](#18-offline-draft-storage-quota-eviction-and-loss-behavior-undefined-for-the-pwa) | `offline-resilience` | Partially covered |
| 19 | [EXIF/GPS stripping for shared and public photos is not explicitly required](#19-exifgps-stripping-for-shared-and-public-photos-is-not-explicitly-required) | `privacy` | Partially covered |
| 20 | [Unauthorized and pre-activation QR scans of a private orchid have no defined view](#20-unauthorized-and-pre-activation-qr-scans-of-a-private-orchid-have-no-defined-view) | `privacy-sharing` | Partially covered |
| 21 | [Orchid Update fields collapse species/grex and cultivar/clone, contradicting ADR-001 taxonomy separation](#21-orchid-update-fields-collapse-speciesgrex-and-cultivarclone-contradicting-adr-001-taxonomy-separation) | `taxonomy` | Partially covered |
| 22 | [AI proposal contract: confirmation command exists but the proposal object, lifecycle, and versioning are undefined](#22-ai-proposal-contract-confirmation-command-exists-but-the-proposal-object-lifecycle-and-versioning-are-undefined) | `underspecified` | Partially covered |
| 23 | [Accession-number allocation is named everywhere but specified nowhere (year reset, padding, concurrency, gaps)](#23-accession-number-allocation-is-named-everywhere-but-specified-nowhere-year-reset-padding-concurrency-gaps) | `underspecified` | Partially covered |
| 24 | [Role and membership model is prose-only: no role-to-command matrix, undefined platform administrator, undefined 'elevated permission' for deletion](#24-role-and-membership-model-is-prose-only-no-role-to-command-matrix-undefined-platform-administrator-undefined-elevated-permission-for-deletion) | `underspecified` | Partially covered |

### 1. Password reset, email verification, and MFA absent from MVP screens and all requirements

**Priority:** P0 · **Verdict:** Missing · **Area:** `authentication` · **Lenses:** Product/UX, Security/Privacy/Compliance

MVP Definition Section 19 lists only five public/account screens (home, Sign in, Create account, Shared orchid page, QR orchid page) with no Forgot Password screen, no email-verification step, and no account/profile settings screen for changing password or email. MVP-PRIORITIES P0 scaffold item 7 specifies only 'Firebase Authentication with email/password and Firebase App Check.' Repo-wide searches confirm 'password reset', 'forgot', 'email verification', password strength policy, and MFA appear nowhere in the 12 documents. ADR-003's Identity section and AGENTS.md cover server-side membership checks but nothing about credential lifecycle. Unverified emails also enable throwaway accounts once PLATFORM sharing opens, and email-based recovery is unsafe without verified ownership; whether emails are verified also gates invitation trust and shared-orchid attribution.

**Why it matters:** The explicit target persona is an older or nontechnical collector (MVP Definition Section 1; Governance Sections 2 and 16) — the population most likely to forget a password. The PCO Owner account controls the entire commercial tenant (members, sharing, financial data, subscription per Section 3); with email/password as the only configured auth method and no recovery path, a locked-out Owner permanently loses access to the business records, and there is no acceptance criterion to build against.

**Suggested requirement:** Add 'Forgot password' to the MVP public screens list with Firebase Auth email-based reset (customized sender/domain) reachable from Sign in; require email verification before tenant creation or membership-invitation acceptance (or record an explicit deferral decision); add an authenticated Account screen supporting change password/email; define a minimum password policy; offer optional TOTP/SMS MFA to Owner accounts at pilot hardening. Acceptance test: a PCO Owner who forgets their password recovers access on a phone without support intervention.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched: MVP Definition Sections 19/21/24, MVP-PRIORITIES P0 item 7, ADR-003 Identity section, AGENTS.md, Governance 11.7 and 16

Confirmed by repo-wide grep: 'password' appears only in MVP-PRIORITIES P0 item 7 ('Configure Firebase Authentication with email/password and Firebase App Check'). No forgot-password, reset, email-verification, password-policy, or MFA/TOTP text anywhere. Section 19's public screen list (home, Sign in, Create account, Shared orchid page, QR orchid page) has no recovery or account-settings screen; Section 21 tenant settings covers only tenant-level items. Governance 11.7 mentions account deletion requests but nothing about credential lifecycle. No coverage found.

</details>

### 2. Deployment pipeline and rollback are unspecified (CI covers checks only)

**Priority:** P0 · **Verdict:** Missing · **Area:** `deployment` · **Lenses:** Operations/Launch

CI is specified strictly for verification (README step 8; MVP-PRIORITIES P0 contracts item 6; the merge-gate lists in AGENTS.md and docs/CODE-REVIEW.md). No document specifies how Hosting, Cloud Functions, Firestore Security Rules, indexes, or Storage Rules reach production — CD from main vs manual firebase deploy — who is authorized to deploy, or any rollback procedure for a bad Hosting release, Functions revision, or Rules push. MVP-PRIORITIES P0 scaffold item 10 covers only initial Hosting/domain configuration, not an ongoing release mechanism.

**Why it matters:** Deny-by-default Rules are the sole enforcement of tenant isolation for direct Firestore/Storage access. A Rules deploy takes effect globally and instantly: an unreviewed manual deploy can silently expose PCO data or lock out all users, and with no documented rollback the outage persists while the team improvises. All of AGENTS.md's merge gates are worthless if the artifact that ships is not the artifact that passed them.

**Suggested requirement:** All production deploys (Hosting, Functions, Firestore/Storage Rules, indexes) run through a CI/CD pipeline from main only after required checks pass; manual production deploys are prohibited. Each release records the deployed commit/tag, and the runbook documents one-step rollback per artifact type (Hosting version rollback; redeploy of the previous tagged Functions and Rules).

<details>
<summary>Verification evidence</summary>

**Checked:** Searched README.md (Next implementation step 8; step 10 area), MVP-PRIORITIES.md (P0 contracts item 6; P0 scaffold item 10; P1 Hardening item 6), AGENTS.md 'Required validation', docs/CODE-REVIEW.md 'Required validation before merge', all three ADRs; repo-wide grep for deploy/rollback/pipeline.

Every CI reference is a pre-merge verification gate (type-check, tests, schema validation, Rules tests, secret scanning). P0 scaffold item 10 only covers initial 'Firebase Hosting and orchid-enthusiasts.com HTTPS routing after local and emulator validation'. P1 Hardening item 6 covers Firestore backups/backup-restore verification/Cloud Monitoring alerts — operational recovery, not release mechanics. No document specifies how Hosting, Functions, Rules, or indexes reach production, who may deploy, CD-vs-manual, or any rollback procedure. Grep for deploy/rollback confirms only retired-runtime and audit references.

</details>

### 3. No dev/staging/prod Firebase environment strategy

**Priority:** P0 · **Verdict:** Missing · **Area:** `environment-strategy` · **Lenses:** Operations/Launch

README's 'Next implementation step' and MVP-PRIORITIES P0 scaffold specify the Firebase Emulator Suite for local validation, then jump directly to configuring Hosting and orchid-enthusiasts.com. No document defines how many Firebase/GCP projects exist, whether a staging project sits between emulator and the production domain, which project holds pilot data, or how configuration (App Check site keys, Auth providers, Vertex AI access, Rules, indexes) is promoted between environments. App Check attestation, real Auth flows, IAM, and Vertex AI cannot be fully exercised in the emulator, so the implied emulator-to-prod path has no integration-validation stage.

**Why it matters:** PCO pilot data is real customer data. Without an environment boundary, every Rules change, Functions deploy, and AI-flow experiment is tested against the only project containing the records the pilot is judged on — a single mistake can corrupt or expose PCO's collection. Offline/sync and tenant-isolation behavior differs between emulator and real Firebase services.

**Suggested requirement:** Operate at least two Firebase/GCP projects (e.g. cce-staging, cce-prod). Rules, indexes, Functions, and Hosting configuration are promoted staging-to-prod with no direct-to-prod changes; App Check, Authentication, and Vertex AI integration must be verified in staging before any production deploy; production credentials are never used for development or testing.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched: README 'Next implementation step', MVP-PRIORITIES P0 scaffold items 4 and 10, ADR-003 'Migration rules' and 'Validation', AGENTS.md 'Required validation'

Grep for staging/environment/promotion finds no environment strategy. The documented path is Emulator Suite for local validation (README step 4; MVP-PRIORITIES P0 item 4) then 'Configure Firebase Hosting and orchid-enthusiasts.com HTTPS routing after local and emulator validation' (P0 item 10) — no intermediate staging project, no project count, no config-promotion process, no statement of which project holds pilot data. Closest adjacent text is ADR-003 migration rule 6 ('Validate tenant isolation before importing any production or pilot data') and rule 5 on not migrating environment-specific credentials, neither of which defines environments. No coverage found.

</details>

### 4. Terms of Service and Privacy Policy pages absent from MVP screens and all requirements

**Priority:** P0 · **Verdict:** Missing · **Area:** `legal-compliance` · **Lenses:** Security/Privacy/Compliance

MVP Definition Section 19's complete public/account screen list contains no Terms of Service, Privacy Policy, or legal/consent screen. Across the full 12-document set (including Governance Sections 11 and 20), the strings 'Terms of Service' and 'Privacy Policy' never occur, and Governance 20.4's release criteria require privacy defaults but never published legal documents or recorded user acceptance.

**Why it matters:** MVP success criteria begin with account creation by an untrained PCO user, and Release 5 makes user content public. Collecting narratives containing names, purchase prices, and locations without a published privacy notice and terms exposes CCE and PCO to state privacy-law violations, and Capacitor app-store distribution (required by ADR-001) will be rejected without a privacy policy URL. There is no basis for the user consent that AI processing of personal stories relies on.

**Suggested requirement:** Add Terms of Service and Privacy Policy to the public screens list; require affirmative, versioned acceptance at account creation (stored with user record, timestamp, document version), links in the footer of every public/shared/QR page, and re-acceptance on material change. Block production sign-up until both documents are published.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched: MVP Definition Section 19 screens list; Governance Sections 11 and 20; repo-wide grep for 'terms of service', 'privacy policy', 'consent', 'legal'

Grep confirms neither 'Terms of Service' nor 'Privacy Policy' occurs in any of the 12 documents. The only adjacent hits are Governance 7.2 ('permanent removal is required for privacy, legal, or account-deletion purposes') and 11.7 (export and deletion requests), which concern data handling, not published legal documents or recorded acceptance. Governance 20.4's release criteria require privacy defaults and private-data exclusion but never a legal notice or consent capture. Section 19's public screen list has no legal pages. No coverage found.

</details>

### 5. Full-text narrative search has no recorded architecture decision on Firestore

**Priority:** P0 · **Verdict:** Missing · **Area:** `missing-decision` · **Lenses:** Contracts/Architecture, NFR/Quality

MVP Definition Section 16 requires basic search over display name, accession number, narrative text, source, and tag/label text (examples: 'Bought from Andy', 'Needs TLC') plus AI-assisted natural-language search, shipping in Release 2. Firestore — the operational store per ADR-001/ADR-003 — has no native full-text search, and no document (ADR-001/002/003, README target architecture, MVP-PRIORITIES) records a search mechanism: no external index (Algolia/Typesense/Elasticsearch), Vertex AI Search, derived index, or client-side index decision, and no search latency, freshness, or tenant-isolation requirement for any external index. Governance 11.5 additionally requires that search never expose private tenant information, so any index must be tenant-scoped and sharing-aware, affecting the sync pipeline (index updates on narrative/sharing changes) and cost model.

**Why it matters:** Story-based searches are a headline MVP capability and the payoff of the narrative-first design. Without a decision, Release 2 cannot be built as specified; discovering mid-build that the database cannot serve the requirement forces an unplanned external dependency with new tenant-isolation obligations, or a scope cut to the pilot's showcase feature. Retrofitting a sharing-aware index after data exists is significantly harder.

**Suggested requirement:** Add an ADR selecting the MVP search mechanism (tenant-partitioned external index fed by Cloud Functions triggers, a client-side index over synced tenant documents up to the declared scale envelope, or an explicitly reduced prefix/field-search scope), specifying indexed fields, tenant isolation and per-Thing sharing enforcement at query time, propagation of narrative edits/removals and sharing downgrades, p90 search response <= 2 s at pilot scale, freshness (results include records synced within the prior minute), and cross-tenant leakage tests for any external index.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched: ADR-001/002/003, README 'Target architecture', MVP-PRIORITIES, MVP Definition Section 16, Governance 11.5

Grep for index/Algolia/Typesense/Elasticsearch/full-text returns nothing. MVP Section 16 defines the search product requirement (narrative text, source, tag text, AI natural-language search) and Governance 11.5 requires search never expose private tenant information, but no document selects a mechanism, index, freshness, latency, or tenant-isolation requirement for search. Closest adjacent text is ADR-003's cost note that 'Some administrative or reporting workflows may later require derived projections or export pipelines', which does not address search. The decision the finding demands is genuinely unrecorded.

</details>

### 6. Self-serve sign-up on orchid-enthusiasts.com leads to an undefined dead end for non-PCO users

**Priority:** P0 · **Verdict:** Missing · **Area:** `onboarding-tenancy` · **Lenses:** Product/UX

The MVP ships a public Create account screen (MVP Definition Section 19; Hosting in MVP-PRIORITIES P0 item 10), but every downstream journey assumes PCO membership ('Create account → Open PCO tenant', Section 24; mobile acceptance criteria start 'Sign in as PCO tenant administrator'). No document states what a stranger who creates an account receives: no self-serve tenant-creation flow exists, no tenant-less landing state is defined, and sign-up is not restricted/invite-only. Meanwhile PLATFORM sharing ('Visible to platform members', Section 17; Governance 8.4) and similar-orchid discovery (Section 18) presuppose non-PCO platform members with some surface to view platform-shared orchids — no such browsing screen is in the screens list.

**Why it matters:** At launch, real strangers will find the public site, create accounts, and hit an undefined state — the worst first impression for the community the PLATFORM/similarity features depend on. It is a product-scope decision with tenancy, security-rules, and quota implications engineering cannot infer.

**Suggested requirement:** Decide and document the non-member account experience: either restrict Create Account to invited/allowlisted users until multi-tenant self-serve is ready, or define a self-serve 'create your collection' tenant-provisioning flow plus the tenant-less landing state. Separately specify where platform members view PLATFORM-shared orchids, or explicitly defer PLATFORM sharing from Release 5.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched: MVP Definition Sections 3, 17-19, 24, 26; Governance 8.4 and 12; ADR-001 Similarity; MVP-PRIORITIES P0 item 10

Create account is a public screen (Section 19) and the success criteria assume 'Create account → Open PCO tenant' (Section 24), but no document defines what a non-PCO account holder sees, restricts sign-up to invitees, or defines self-serve tenant creation. Section 3's 'The initial MVP may begin with one Owner account and add invitations later in the release' addresses PCO membership only, not strangers. No browsing surface for PLATFORM-shared orchids appears in the screens list (only 'Shared orchid page'). Mitigating adjacent fact: ADR-001 states 'Embeddings and similarity are post-MVP', which softens the similarity-surface aspect but not the core undefined post-signup state.

</details>

### 7. No performance budgets beyond the two-minute record target

**Priority:** P0 · **Verdict:** Missing · **Area:** `performance` · **Lenses:** NFR/Quality

The only quantified performance target in the documentation set is 'A basic record can be created in under two minutes' (MVP Section 24). No budgets exist for: initial PWA load on a mid-range phone over cellular; QR scan-to-record-open time; Step 4 AI-interpretation latency during intake; 'Tell me about this orchid' response latency; search response time; label PDF generation; or trusted-command round trip (ADR-001 lists command-function latency as a cost with no budget). ADR-002's FinOps measurements are explicitly post-hoc, not acceptance thresholds, and 'slow cellular connections' has no reference network profile to test against.

**Why it matters:** Intake is performed standing in a greenhouse by older, nontechnical users on cellular connections. An unbounded AI step or a slow scan-to-open silently blows the two-minute target, and QA has no objective basis to accept or reject a build. Every latency-sensitive step in the flagship workflow is currently unmeasurable.

**Suggested requirement:** Adopt a performance budget table measured on a reference mid-range Android and iPhone over a throttled 4G profile: cold PWA load <= 5 s / warm <= 2 s; QR scan to record view <= 3 s; intake AI interpretation p90 <= 10 s with visible progress; 'Tell me about this orchid' p90 <= 8 s; search p90 <= 2 s at pilot scale; single-label PDF <= 3 s; trusted-command commit p90 <= 2 s. Make these part of release acceptance and pilot monitoring.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched MVP Definition Section 24 (Operational targets), 'Connectivity and session behavior' ('Slow cellular connections'), Mobile interface requirements ('Visible loading and save status'), ADR-001 Consequences ('Command-function latency for canonical writes'), ADR-002 FinOps measurements; repo-wide grep for latency/seconds/p90/response time.

The only quantified performance figure in the entire documentation set is Section 24's 'A basic record can be created in under two minutes', which the finding already excludes. Everything else is qualitative: 'slow cellular connections' has no reference network profile, ADR-001 names command latency as a cost with no budget, and ADR-002's metrics are post-hoc pilot measurements, not acceptance thresholds. No budget exists for PWA load, QR scan-to-open, AI interpretation, search, label PDF, or command round trip. Grep confirms no other latency or timing values anywhere.

</details>

### 8. Production bootstrap of platform admin and PCO tenant is undefined in the Firebase-native plan

**Priority:** P0 · **Verdict:** Missing · **Area:** `tenant-lifecycle` · **Lenses:** Product/UX, Operations/Launch

MVP-PRIORITIES lists 'Seed platform administrator and PCO tenant administrator' only as retired-prototype evidence; docs/REPOSITORY-AUDIT-2026-08-05.md confirms the seeding code (app/seed.py) was removed 2026-08-05 and AGENTS.md forbids restoring it. The Firebase-native scaffold list (P0 items 1-10), README's 'Next implementation step', and ADR-001's implementation order contain no tenant-provisioning or bootstrap step, yet the P1 vertical slice begins at 'PCO owner authentication and tenant context', presupposing the tenant document, Owner membership, and tenant settings (accession format PCO-{YEAR}-{SEQUENCE}, timezone America/Denver, currency USD per MVP Definition Sections 3 and 21) already exist behind deny-by-default Rules. MVP Definition Sections 4-5 'recommend' initial locations and collections without stating whether they are pre-seeded or Owner-created. No document defines who runs provisioning, how the real Owner's Firebase Auth account links to the Owner membership, whether the procedure is idempotent, whether it emits the lifecycle events AGENTS.md requires, or what a 'platform administrator' is in the Firebase-native runtime.

**Why it matters:** This is a hard launch blocker with a bootstrap paradox by design: under deny-by-default Rules with trusted-command-only canonical writes, no member exists to create the first membership. Nothing in the P1 vertical slice can be accepted without a provisioned tenant, and improvised console writes would bypass the operation ledger and lifecycle-event guarantees, poisoning the audit trail from day one.

**Suggested requirement:** Add a P0/P1 work item defining a scripted, idempotent, audited bootstrap procedure (Admin SDK script or one-time privileged callable restricted to a platform-admin claim) that creates the platform administrator, PCO tenant document, Owner membership bound to a named Firebase Auth account, tenant settings, and the Section 4-5 recommended locations/collections, initializes the accession sequence, and emits standard lifecycle events — validated in staging before production; prohibit direct console mutation of canonical documents. Document the platform-administrator role and Owner enrollment.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched: MVP-PRIORITIES (all sections), README 'Next implementation step', ADR-001 Implementation order, ADR-003, MVP Definition Sections 3-5 and Release 1

The only 'seed' reference is MVP-PRIORITIES P0 prototype-evidence row 2 ('Seed platform administrator and PCO tenant administrator | Demonstrated'), which the audit confirms was removed with app/seed.py and which AGENTS.md forbids restoring. The Firebase scaffold list (P0 items 1-10), README's next steps, and ADR-001's implementation order contain no provisioning/bootstrap step, yet P1 item 1 starts at 'PCO owner authentication and tenant context'. Release 1 lists 'PCO tenant' as a deliverable and Section 3 defines its settings, but no document defines who provisions it, how the Owner's Auth account is bound, idempotency, or lifecycle-event emission. No Firebase-native definition of 'platform administrator' exists beyond AGENTS.md's passing 'coarse platform roles' mention.

</details>

### 9. Collections contract is missing and absent from the acknowledged to-be-added schema list

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `contract-gap` · **Lenses:** Contracts/Architecture

MVP Definition Section 5 defines collection behavior (name, description, status, sharing default, default location) and Release 1 ships collections; core.schema.json makes CollectionUUID required on both thing and draftThing. But there is no collection schema, and MVP-PRIORITIES P0-contracts item 1's schema list omits collections — the gap is unacknowledged. Underspecified semantics compound it: whether a collection's Default Location/Default Sharing are copied at Thing creation or dynamically inherited (Section 5's example implies copy, never stated), and how the recommended 'Archived Orchids' collection interacts with the ARCHIVED status — two overlapping mechanisms for the same concept.

**Why it matters:** Every orchid record requires a CollectionUUID from day one; without the contract, CREATE_THING validation, Rules, and the intake collection picker cannot be built. The Archived-collection-vs-ARCHIVED-status overlap will confuse PCO users and produce inconsistent dashboard counts if not resolved deliberately.

**Suggested requirement:** Add collection to the to-be-added schema list and define it (CollectionUUID, TenantUUID, name, description, status, DefaultSharingLevel, DefaultLocationUUID, timestamps, Version); state that defaults are applied once at Thing creation and thereafter owned by the Thing; and remove 'Archived Orchids' from the recommended collections or document that archive is exclusively a status.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 5 'Collection behavior'; MVP-PRIORITIES P0-contracts item 1; core.schema.json (CollectionUUID required); Governance 8.6

Verified: the P0-contracts to-be-added list ('command envelopes, identity, tenants, memberships, locations, taxonomy, narratives, AI proposals, media, labels, exports, and the contract registry') indeed omits collections while core.schema.json requires CollectionUUID on both thing and draftThing — the schema gap is real and unacknowledged. Partial coverage: Section 5 defines collection behavior at product level (name, description, status, sharing default, default location) and Governance 8.2 requires explicit collection assignment. Unresolved as claimed: whether Default Location/Sharing are copied or inherited is never stated, and the recommended 'Archived Orchids' collection sits unreconciled against Governance 8.6's 'Archive is a status, not deletion.'

</details>

### 10. Command envelope and command-type taxonomy cannot express the MVP command set or ADR-002's authorization rules

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `contract-gap` · **Lenses:** Contracts/Architecture · **(acknowledged schema gap)**

ADR-001 names trusted commands for creation, movement, archive/restore, confirmation, and accession allocation; MVP-PRIORITIES P1 requires Archive/Restore. But the only existing command contract, batchOperation in batch.schema.json, enumerates just CREATE_THING, UPDATE_METADATA, RECORD_EVENT, CONFIRM_AI_PROPOSAL, QUEUE_LABEL_PRINT with a fully open Payload. There is no ARCHIVE/RESTORE, CHANGE_LOCATION, status-change, sharing-change, or transfer command type, and no statement of whether those flow through generic types. If consequential changes share a generic command type with open payloads, ADR-002's rule that they 'may not be bulk-approved' and AGENTS.md's role-permission checks cannot be enforced at the envelope level, because the server cannot classify consequence from the type alone. There is also no schema for the single (non-batch) callable command despite ADR-001 defining its required fields. The command-envelope schema is acknowledged as to-be-added; these design contradictions go beyond that acknowledgement.

**Why it matters:** The trusted command layer is P0 scaffold work and the enforcement point for role authorization, bulk-approval allowlists, and confirmation requirements; five types with open payloads make the governance model unimplementable and untestable in the planned Rules/emulator tests.

**Suggested requirement:** Define the canonical command taxonomy as distinct typed commands with closed per-command payload schemas (CREATE_THING, UPDATE_TEMPLATE_DATA, CHANGE_LOCATION, CHANGE_STATUS, CHANGE_SHARING, CHANGE_COLLECTION, RECORD_TRANSFER, ARCHIVE_THING, RESTORE_THING, RECORD_EVENT, CONFIRM_AI_PROPOSAL, QUEUE_LABEL_PRINT), a standalone command-envelope schema matching ADR-001's required fields, and a consequence classification per type driving role checks and the ADR-002 bulk-approval exclusion list.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 'Command/query separation'; MVP-PRIORITIES P0-contracts item 1 ('command envelopes'); ADR-002 'Consolidated proposal review'; batch.schema.json batchOperation

Covered: ADR-001 defines the envelope's required fields (ClientOperationID, TenantUUID, ThingUUID, ExpectedVersion, command type and payload), the handler transaction steps, and the command families ('creation, movement, archive/restore, confirmation, and accession allocation'); the command-envelope schema is explicitly on the P0-contracts to-be-added list. Verified gaps: batchOperation's enum (CREATE_THING, UPDATE_METADATA, RECORD_EVENT, CONFIRM_AI_PROPOSAL, QUEUE_LABEL_PRINT) has no ARCHIVE/RESTORE, CHANGE_LOCATION, status/sharing/transfer types despite P1 requiring Archive/Restore; Payload is an open object; and no document defines a consequence classification per type, so ADR-002's 'may not be bulk-approved' exclusions have no envelope-level hook. The acknowledged to-be-added schema does not resolve the taxonomy/classification design.

</details>

### 11. Core Thing/DraftThing contracts have no place for required orchid fields (genus, grex, cultivar, acquisition, notes, temporary name)

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `contract-gap` · **Lenses:** Contracts/Architecture

The MVP Definition's Update section requires editing Genus, 'Species or grex', 'Cultivar or clone', optional notes, and acquisition information; Section 6 requires an orchid display name or temporary name; ADR-001's Taxonomy section mandates separate epithets with name-as-entered preservation. But core.schema.json defines thing and draftThing with additionalProperties: false and contains none of these fields, no acquisition sub-object, and no template-data extension container (only TemplateID/TemplateVersion strings). draftThing has no DisplayName property, so an offline intake draft cannot hold the temporary name the Create workflow requires. The acknowledged to-be-added taxonomy schema does not resolve this: the closed thing object provides no attachment point for it.

**Why it matters:** Every Release 2 workflow (add orchid, edit orchid, AI summary, label content) depends on where template-specific structured data lives. Whether it is an open extension object validated per TemplateVersion, a sibling document, or a subcollection changes the Firestore document model, Security Rules, and command payloads. Building the scaffold against the current closed contract guarantees rework.

**Suggested requirement:** Extend core.schema.json so thing and draftThing carry a versioned template-data extension point (e.g. a TemplateData object whose schema is selected by TemplateID+TemplateVersion, kept additionalProperties: false per template version), add DisplayName/temporary-name capture to draftThing, and define the orchid template schema covering genus, species epithet, grex, clonal/cultivar epithet, acquisition (source, date, price+currency), and notes.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES 'P0 - Complete contracts and validation foundation' item 1; docs/REPOSITORY-AUDIT-2026-08-05.md schemas review

Verified: thing and draftThing are additionalProperties:false with no taxonomy, acquisition, or notes fields, and draftThing has no DisplayName property. Partial coverage exists: MVP-PRIORITIES item 1 schedules 'taxonomy' and 'narratives' schemas, and the audit states the schemas 'are incomplete for Phase 0 ... must be extended rather than replaced', signalling intended extension of these closed objects. Genuinely missing: any design for where template-specific data attaches (extension object vs sibling document vs subcollection), the temporary-name/DisplayName capture on draftThing, and an acquisition structure — 'add taxonomy later' without defining the attachment point leaves the core gap unresolved.

</details>

### 12. thingEvent EventType enum contradicts the MVP, governance, and ADR-002 event vocabulary (transfer, sale, status, sharing, print confirm, naming)

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `contract-mismatch` · **Lenses:** Contracts/Architecture, Orchid domain, NFR/Quality, Product/UX

core.schema.json's closed thingEvent.EventType enum conflicts with every product-level event requirement. (1) MVP Definition Section 12 lists MOVED, FLOWERED, PHOTOGRAPHED, LISTED_FOR_SALE, TRANSFERRED; the enum renames MOVED to LOCATION_CHANGED, splits FLOWERED into BLOOM_STARTED/BLOOM_ENDED, and omits PHOTOGRAPHED, LISTED_FOR_SALE, and TRANSFERRED entirely, with no recorded mapping or deliberate-omission note. (2) Governance Section 18 requires understandable histories for status changes, sharing changes, narrative changes, transfers, and sales, and Governance 8.5 requires sale/transfer to remain in the historical record with recipient/type/date/price — but the enum has no STATUS_CHANGED, SHARING_CHANGED, COLLECTION_CHANGED, or NARRATIVE_CREATED/UPDATED/REMOVED/RESTORED types, even though thingStatus includes FOR_SALE and TRANSFERRED (states reachable with no conforming way to record the mandated event). (3) A single LABEL_PRINTED event conflates request with confirmed output, contradicting ADR-002 ('LABEL_PRINT_REQUESTED and LABEL_PRINT_CONFIRMED must remain distinct events'), AGENTS.md, and docs/CODE-REVIEW.md — while batch.schema.json's printJob correctly has PRINT_REQUESTED/PRINT_CONFIRMED, so the two contracts disagree. (4) thingEvent requires ThingUUID, so tenant-level and location-entity changes have no event contract, making MVP-PRIORITIES P1-Hardening item 2 ('every tenant, location, orchid, and label change appends an auditable lifecycle event') unimplementable. (5) StructuredDetails is an open object with no per-EventType schema, in tension with the closed-contract policy in docs/CODE-REVIEW.md.

**Why it matters:** Selling or transferring a plant is the moment provenance matters most to a nursery, sharing changes are the highest-privacy-risk consequential action, and the very first status or sharing change cannot satisfy the mandatory audit-event rule without an unversioned schema hack. A single LABEL_PRINTED event means history asserts labels were printed when only a PDF was generated, making the 'Labels Not Yet Printed' dashboard tile unreliable. History is a headline MVP capability, and contract/Rules tests cannot cover events that have no type.

**Suggested requirement:** Publish one authoritative event-type table reconciling MVP Section 12 and core.schema.json: add TRANSFERRED (sale as a transfer subtype carrying recipient/type/date/price/currency per Governance 8.5), LISTED_FOR_SALE, STATUS_CHANGED, SHARING_CHANGED, COLLECTION_CHANGED, PHOTOGRAPHED, NARRATIVE_CREATED/UPDATED/REMOVED/RESTORED, and LABEL_PRINT_REQUESTED/LABEL_PRINT_CONFIRMED (retiring LABEL_PRINTED, aligned with printJob states); document the MOVED→LOCATION_CHANGED mapping and how a single user-reported 'flowered' statement maps to BLOOM_STARTED/BLOOM_ENDED (including open-ended blooms); define closed per-EventType StructuredDetails schemas; and add a separate tenant-scoped entity-event contract (no required ThingUUID) covering tenant, location, and label-template changes.

<details>
<summary>Verification evidence</summary>

**Checked:** core.schema.json thingEvent.EventType vs MVP Definition Section 12, Governance Sections 8.5/18, ADR-002 'Print queue and spooling', batch.schema.json printJob, MVP-PRIORITIES P1-Hardening item 2

Conflicts verified against the actual enum (CREATED, ACQUIRED, LOCATION_CHANGED, REPOTTED, BLOOM_STARTED, BLOOM_ENDED, TREATED, INSPECTED, FERTILIZED, WATERED, DIVIDED, IDENTIFICATION_CHANGED, LABEL_PRINTED, ARCHIVED, RESTORED, GENERAL_NOTE): MVP Section 12's MOVED, FLOWERED, PHOTOGRAPHED, LISTED_FOR_SALE, TRANSFERRED have no enum counterparts or recorded mapping; Governance 18/8.5 mandate histories for status, sharing, narrative, transfer, and sale changes with no corresponding types even though thingStatus includes FOR_SALE and TRANSFERRED; single LABEL_PRINTED vs ADR-002's 'LABEL_PRINT_REQUESTED and LABEL_PRINT_CONFIRMED must remain distinct events when confirmation is available' (note the qualifier) while printJob has separate PRINT_REQUESTED/PRINT_CONFIRMED states; ThingUUID is required so P1-Hardening's tenant/location-change events have no contract; StructuredDetails is an open object. Partial credit only because the enum covers most care/lifecycle events and the audit generically states schemas 'are incomplete ... must be extended rather than replaced' — but events are not in the P0-contracts to-be-added list, so the reconciliation is unacknowledged.

</details>

### 13. Voice input mechanism contradictory: device-keyboard dictation vs platform transcription with audio deletion

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `contradiction` · **Lenses:** Product/UX, Contracts/Architecture, Security/Privacy/Compliance, NFR/Quality

The MVP Definition's mobile Create requirements specify 'Voice-to-text using the device keyboard' (OS dictation; audio never reaches CCE). But Section 7 Step 3 says 'Voice input is transcribed. Only the transcript is retained', Section 22 requires 'Voice audio deleted after transcription', Section 23 lists 'Transcribe voice' as an MVP AI capability, Release 2 includes 'Voice transcription', and Governance 5.2/9.1/11.4 describe a CCE-side pipeline ('CCE transcribes → ... Temporary voice recording is deleted') with transcript review. These are different products: platform transcription requires audio capture UI, upload, a speech-to-text service (absent from ADR-001's service list), a retention/deletion pipeline with a deadline ('after transcription' could mean seconds or weeks), backup/provider-log exclusion, and an offline story — while device dictation requires none of that and renders the audio-deletion privacy rules vacuous and untestable. Additionally, core.schema.json mediaReference.Kind permits only PHOTO, DOCUMENT, LABEL_IMAGE — no AUDIO kind — so a voice note recorded offline cannot be stored in a draft for later transcription, in tension with 'Essential intake must work without connectivity' (AGENTS.md). No document states which mechanism is the MVP.

**Why it matters:** Voice is the marquee accessibility feature and primary input path for the older-collector persona and greenhouse intake, and appears in the MVP success criteria ('Speak or type story'). The two readings differ by an entire subsystem with cost, privacy, and offline implications (device dictation works offline; server transcription does not). Release 2 cannot be scoped, the 'Voice audio deleted after transcription' launch-acceptance rule cannot be verified, and the schema gap silently forecloses offline voice intake in the product's signature scenario.

**Suggested requirement:** Record an explicit decision: either (a) MVP voice input is device-keyboard dictation only — CCE never receives audio, the audio-deletion rules are noted as applying only when platform transcription is introduced, and platform transcription via a governed Genkit flow is a named post-MVP enhancement; or (b) add to ADR-001/MVP-PRIORITIES a transcription service with audio clips stored in a dedicated tenant-scoped Storage path, hard-deleted within 24 hours of successful transcription with an audited deletion event, excluded from backups, provider configured for zero retention, mediaReference gaining Kind=AUDIO for LOCAL_ONLY offline capture, and an emulator test asserting post-transcription deletion.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition mobile Create requirements vs Section 7/22/23 and Release 2; Governance 5.2/9.1/11.4; core.schema.json mediaReference.Kind; ADR-001 service list

Conflict confirmed. MVP mobile Create requires 'Voice-to-text using the device keyboard' (OS dictation, no audio to CCE), while Governance 5.2 specifies 'User speaks → CCE transcribes → ... Temporary voice recording is deleted', MVP Section 22 requires 'Voice audio deleted after transcription' as an MVP privacy control, Section 23 lists 'Transcribe voice' as an MVP AI capability, and Release 2 ships 'Voice transcription'. These describe different subsystems and no document records which is the MVP mechanism. Verified: ADR-001's Google Cloud service list has no speech-to-text service, and mediaReference.Kind permits only PHOTO, DOCUMENT, LABEL_IMAGE (no AUDIO), so offline audio capture has no contract. Voice privacy intent is well covered; the mechanism decision, retention deadline, and audio contract are not.

</details>

### 14. No billing budgets, Vertex AI spend caps, or numeric quota values — FinOps guardrails are measurement-only

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `finops` · **Lenses:** Operations/Launch, NFR/Quality

ADR-002 defines only what to MEASURE during pilot; AGENTS.md ('application-level quotas, rate limits...') and ADR-001 ('Enforce request-size, image-count, rate, and tenant-usage limits server-side') name application-level limits but assign no numeric values. Beyond draftThing.Media maxItems 20, no value exists anywhere for: maximum upload size per photo, photos per orchid after sync, per-tenant storage quota, AI calls per user/tenant per day, or request rate limits. No document requires a GCP Billing budget with alert thresholds, Vertex AI quotas or a hard spend ceiling, or defined behavior when a limit trips (degrade AI features vs hard stop). Deny-by-default Storage Rules (P0 scaffold item 5) and callable-command validation cannot be written or tested against unvalued limits; the media/label schemas' to-be-added acknowledgement covers schema shape, not policy values.

**Why it matters:** Serverless plus generative AI is the exact profile where a client retry loop, an abused public endpoint, or a prompt bug can burn a pilot budget in a weekend — faster than monthly billing review catches it. Unbounded uploads from modern 48 MP phone cameras are the largest single cost lever. PCO is a single small-nursery tenant; an uncontrolled four-figure Vertex AI bill could end the pilot commercially regardless of product success, and each developer otherwise invents quota behavior ad hoc.

**Suggested requirement:** Before any production Vertex AI traffic: create a GCP billing budget with alerts at 50/80/100% routed to a monitored channel; set an explicit monthly Vertex AI spend ceiling. Publish an initial versioned quota configuration (per ADR-002's pattern): original photo <= 15 MB, capture-profile derivative <= 4 MB, <= 50 photos per orchid, pilot tenant storage soft cap 50 GB with 80% alert, <= 200 AI interpretation calls per tenant/day (with per-user daily caps), enforced by Storage Rules and callable validation with tests; define graceful degradation when quotas trip (AI features pause with a friendly message; core CRUD, QR lookup, and labels unaffected).

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md Media and FinOps ('Use application-level quotas, rate limits, duplicate detection, caching, and model routing'); ADR-001 Media processing ('Enforce request-size, image-count, rate, and tenant-usage limits server-side'); docs/CODE-REVIEW.md Media and FinOps; batch.schema.json (Operations maxItems 50, printJob Quantity max 1000); core.schema.json (draftThing.Media maxItems 20, Narrative maxLength 20000).

Quotas and rate limits are mandated in principle in three documents, and a few structural bounds exist in schemas (50 ops/batch, 20 media/draft, 1000 labels/job, 20k-char narrative). But the finding's core claims hold: no numeric value anywhere for upload size, photos per orchid post-sync, per-tenant storage, AI calls per user/tenant/day, or request rates; no GCP billing budget or alert thresholds; no Vertex AI spend ceiling; no defined behavior when a limit trips. Grep for budget/spend/billing returns nothing. The title's 'measurement-only' slightly overstates (quotas are required, just unvalued), hence partial rather than missing.

</details>

### 15. Section 24 success targets and ADR-002 FinOps metrics have no measurement mechanism

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `measurement-telemetry` · **Lenses:** Operations/Launch

MVP Definition Section 24 sets measurable targets ('basic record in under two minutes', workflow completed 'without training') and ADR-002's FinOps section mandates pilot measurements (median capture time per item, review time, AI calls per completed Thing, function invocations, uploaded bytes per image profile, cache hit rate, label jobs per print interaction, retry and conflict rate); MVP-PRIORITIES P2 item 4 repeats the benchmark requirement. Yet no document requires the instrumentation to produce these numbers: no analytics/telemetry tool selection, no client-side timing-event requirement, no server-side per-tenant counter or logging convention for AI calls and invocations, and no definition of how 'without training' is observed. ADR-002 explicitly demotes all savings claims to 'hypotheses until measured' — but the capability to measure is itself unrequired.

**Why it matters:** The pilot's entire verdict rests on these numbers. Without instrumentation at launch, baseline data is unrecoverable, Section 24 acceptance becomes anecdote, and ADR-002's cost hypotheses (5x intake, 60-70% AI cost reduction) can never be confirmed or falsified against representative PCO workflows as the ADR requires.

**Suggested requirement:** Before pilot launch, implement a documented measurement plan: client timing events for intake start/save, label print, QR scan, and AI question answer/skip; server-side structured metrics keyed by TenantUUID and flow for Vertex AI calls, Function invocations, and uploaded bytes; and a written mapping of every Section 24 target and every ADR-002 metric to its concrete data source, owner, and review cadence.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-002 'FinOps measurements' ('Measure during pilot:' + nine-metric list); MVP-PRIORITIES.md P2 Batch item 4 ('Workflow and FinOps benchmarks measured against representative PCO workflows'); P1 Hardening item 6 (Cloud Monitoring alerts); AGENTS.md Media and FinOps ('hypotheses until measured').

The WHAT is well specified: ADR-002 enumerates the exact metrics, MVP-PRIORITIES schedules benchmarking as a P2 work item, and AGENTS.md/CODE-REVIEW make measurement mandatory before claiming savings. Still missing: any instrumentation requirement — no analytics/telemetry tool, no client timing-event spec, no per-tenant server-side counter or logging convention, no mapping of Section 24 targets (e.g. 'under two minutes', 'without training') to a concrete data source or observation method. Cloud Monitoring alerts (P1 Hardening 6) are infrastructure alerting, not product/FinOps metric capture. The mandate to measure exists; the capability to measure is unspecified.

</details>

### 16. No Firestore data-model, index, or projection design despite queries the contracts cannot answer

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `missing-requirement` · **Lenses:** Contracts/Architecture

ADR-003 itself flags 'Firestore data modeling and query design require deliberate contract work', but no document defines collection paths, composite indexes, counters, or read projections. Concrete unanswerable requirements: the PCO dashboard (MVP Section 20) needs 'Labels Not Yet Printed' and 'Orchids Needing Review' — no contract carries a label-print state or needs-review flag, and Firestore cannot join thing against events or print jobs at query time; dashboard counts need aggregation or counter design. Public/shared pages and unauthenticated QR views must show a field subset (Governance 11.2/11.3; MVP 17 excludes exact location and price), but Firestore Rules grant document-level, not field-level, read access — implying denormalized public-projection documents no contract or doc mentions.

**Why it matters:** These are not implementation details: they dictate which denormalized fields must be added to canonical contracts, which projection documents Rules must expose to unauthenticated QR scanners, and which writes each trusted command must fan out. Discovering this after Rules and contracts ship forces migrations of pilot data.

**Suggested requirement:** Produce a Firestore data-model design doc or ADR defining document paths per tenant, the shared/public projection documents used for QR and shared-link views, denormalized query fields on thing (label-print state, identification-review state), dashboard counter strategy, and required composite indexes for the Section 16/20 queries — then reflect the new fields in the JSON Schema contracts.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-003 'Costs and risks' ('Firestore data modeling and query design require deliberate contract work'); ADR-001 'Google Cloud services' and 'Similarity'

The need is acknowledged but never defined: ADR-003 flags Firestore data modeling as pending deliberate contract work and notes some workflows 'may later require derived projections'; ADR-001 mentions 'synchronized query views' and that only 'approved public/platform projections' are similarity-eligible, confirming projection documents are intended. But no document defines collection paths, composite indexes, counter/aggregation strategy for the Section 20 dashboard tiles ('Labels Not Yet Printed', 'Orchids Needing Review' — no contract carries either state), or the public-projection documents needed because Rules cannot do field-level reads. Acknowledgement without definition; the design gap is real.

</details>

### 17. Offline intake depends on locally available location tree, collection list, and template — availability never specified

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `missing-requirement` · **Lenses:** Contracts/Architecture

ADR-001's offline-first intake requires creating a local DraftThing with 'an explicit known location' and continuing without connectivity, and core.schema.json makes CollectionUUID, TemplateID, and TemplateVersion required on draftThing at creation. Governance 8.1 forbids silently creating undefined locations, so the offline selector must present real tenant locations. Yet no document requires the location hierarchy, collection list, or template definitions to be cached offline: ADR-002 specifies a taxonomy reference cache only, and ADR-003 mentions 'Firebase offline SDK capabilities where appropriate' without a pre-warming or staleness requirement (the SDK cache only holds previously-read documents). Also unspecified: behavior when a cached location was archived/renamed while offline and the sync-time command references it.

**Why it matters:** The exact scenario ADR-001 was written for — PCO intake in a greenhouse with intermittent connectivity — fails if the location tree or collection list is not locally available (a fresh session, evicted cache, or first offline launch shows an empty selector and blocks draft creation). Stale-reference conflict handling determines whether the P1 'user-friendly conflict' hardening item is designable.

**Suggested requirement:** Require that the tenant's location hierarchy, collections, and active template versions are proactively synchronized to durable local storage (alongside the OfflineDraftStore) whenever connectivity exists, with a defined staleness indicator and a defined sync-time resolution flow when a draft references a location or collection that changed while offline.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 'Offline-first intake'; ADR-002 'Taxonomy and canonical metadata cache'; ADR-003 'Operational data and synchronization'; AGENTS.md 'Offline and synchronization'

The capability is required implicitly: ADR-001 mandates that a user can 'create a local DraftThing ... select an explicit known location, and continue without connectivity', AGENTS.md requires 'Essential intake must work without connectivity', and Governance 8.1 forbids silently creating undefined locations — together these entail an offline-available location/collection/template set. But no document requires proactive caching of that reference data: ADR-002's versioned local cache covers taxonomy reference only, and ADR-003 offers 'Firebase offline SDK capabilities where appropriate' with no pre-warm or staleness requirement. Stale-reference resolution at sync time is covered only generically (P1-Hardening item 5 'user-friendly validation, conflict, retry, and error states'; CODE-REVIEW 'Conflicts produce reviewable outcomes'), never for the archived/renamed-location case.

</details>

### 18. Offline draft storage quota, eviction, and loss behavior undefined for the PWA

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `offline-resilience` · **Lenses:** NFR/Quality

Offline creation is mandatory (MVP 'Connectivity and session behavior'; ADR-001 'Offline-first intake'; AGENTS.md). A draft may carry up to 20 media items, but no document specifies an IndexedDB/origin storage budget, how many unsynced drafts and photos the PWA must retain, whether persistent storage (navigator.storage.persist) is requested, behavior when quota is exhausted mid-capture, or user warnings as local storage fills. ADR-002's local draft recovery snapshots apply only to 'Native applications', leaving the PWA — the actual MVP delivery vehicle — with no stated mitigation for browser storage eviction (iOS Safari can evict origin storage under pressure or non-use).

**Why it matters:** PCO's core scenario is capturing photos and narratives offline in a greenhouse. Silent browser eviction or an unhandled mid-capture quota failure destroys unrecoverable field data — fatal to trust for the older, nontechnical pilot user the MVP must convince.

**Suggested requirement:** The PWA must request persistent storage before first offline intake, support a stated minimum offline capacity (proposed: >= 50 unsynced drafts / 200 photos at the configured capture profile), surface remaining capacity below 20%, refuse new capture with a plain-language message rather than failing silently at quota, and have a tested, documented behavior for browser-initiated eviction of unsynced drafts.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES.md P0 scaffold item 8 (OfflineDraftStore + IndexedDB adapter with visible sync state); docs/CODE-REVIEW.md Offline ('Drafts persist through application suspension and accidental navigation'); ADR-002 'Local draft recovery' ('Native applications should support an optional recovery snapshot…'; 'A device-local snapshot reduces the risk of browser-cache loss but does not eliminate loss…'); AGENTS.md Offline and synchronization.

The docs mandate an IndexedDB draft store, draft persistence across suspension/navigation, and visible sync state, and ADR-002 explicitly acknowledges browser-cache loss risk — but its recovery-snapshot mitigation is scoped to 'Native applications' only, confirming the finding's PWA gap. Nowhere is there an origin-storage budget, a navigator.storage.persist requirement, a minimum unsynced-draft/photo capacity, quota-exhaustion behavior mid-capture, capacity warnings, or defined handling of browser-initiated eviction. The risk is acknowledged; the required behaviors are not specified.

</details>

### 19. EXIF/GPS stripping for shared and public photos is not explicitly required

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `privacy` · **Lenses:** Security/Privacy/Compliance

ADR-001 says derivatives are created 'correcting orientation and removing unnecessary metadata' — 'unnecessary' is undefined, the requirement applies to derivative creation (not what is publicly served), and originals are preserved with all metadata. Governance 11.6 and MVP Sections 17/22 address location fields only, never photo-embedded GPS. batch.schema.json mediaProcessingMetadata has no field recording metadata removal, and docs/CODE-REVIEW.md's media checklist omits EXIF verification.

**Why it matters:** Phone photos carry GPS coordinates of PCO's greenhouse or a collector's home. Release 5 publishes photos on PUBLIC/PLATFORM/SHARED_LINK pages; serving any variant retaining EXIF GPS directly defeats the 'exact locations private by default' promise (a listed MVP privacy rule) and creates real theft risk for valuable collections held by older users. This is the class of leak Governance 20.3 calls 'privacy leakage', with no testable requirement enforcing it.

**Suggested requirement:** Require that every image variant served on a non-private surface (PUBLIC, PLATFORM, SHARED_LINK, QR page) has all EXIF/XMP/IPTC metadata — explicitly including GPS, timestamps, device serial numbers — stripped server-side or verified stripped; originals with full metadata are never directly reachable from a shared page. Add a MetadataStripped flag to mediaProcessingMetadata and an automated EXIF-leak test to the CODE-REVIEW media checklist.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 'Media processing' ('correcting orientation and removing unnecessary metadata'); Governance 11.6; batch.schema.json mediaProcessingMetadata; docs/CODE-REVIEW.md 'Media and FinOps'

One gesture toward the requirement exists: ADR-001's derivative pipeline includes 'removing unnecessary metadata', and Governance 11.6 protects exact locations as data fields. But 'unnecessary' is undefined, the removal applies at derivative creation with no requirement that only stripped variants are served on PUBLIC/PLATFORM/SHARED_LINK/QR surfaces, originals are preserved with metadata intact, mediaProcessingMetadata has no field recording metadata removal (verified — fields cover dimensions, encoding, crop, ROI, retention only), and the CODE-REVIEW media checklist has no EXIF verification item. No testable requirement prevents serving GPS-bearing images publicly.

</details>

### 20. Unauthorized and pre-activation QR scans of a private orchid have no defined view

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `privacy-sharing` · **Lenses:** Product/UX

The MVP Definition says only 'When the user is not authorized, the page displays only the permitted public or limited view.' For a PRIVATE orchid (the default, Section 17), the 'permitted limited view' is never defined: 404, generic private page, sign-in prompt, tenant name, display name? Whether the page may even confirm a record exists is unstated, though Governance Section 11 mandates minimum necessary disclosure. ADR-001 says a QR generated before synchronization is 'pending activation and does not grant access' — but no document defines what a pending-activation scan displays. There is also no requirement that an authorized member scanning while signed out is returned to /p/{LabelID} after sign-in.

**Why it matters:** QR lookup ships in the P1 vertical slice and labels are permanent physical artifacts on plants PCO sells, transfers, and displays — strangers WILL scan them. An over-permissive default leaks private data; an undefined one cannot be built or accepted. This is the single most privacy-sensitive screen in the MVP with one ambiguous sentence of specification.

**Suggested requirement:** Specify the unauthenticated QR page per sharing level: PRIVATE returns a neutral page revealing at most 'This label belongs to a private collection' with a sign-in link (no display name, tenant, or existence-confirming metadata); SHARED_LINK/PUBLIC render the approved public projection; pending-activation LabelIDs render the same neutral page. Require sign-in to deep-link back to /p/{LabelID}, and add Rules tests asserting the private projection excludes location, price, and internal notes.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition 'Mobile QR scanning'; Governance Sections 11.2 and 13; ADR-001 'Three-tier identity'

Principles exist: 'When the user is not authorized, the page displays only the permitted public or limited view' (MVP Definition); 'Labels should not expose private information unless explicitly configured' (Governance 13); minimum necessary disclosure (Governance 11.2); 'A QR generated before synchronization is pending activation and does not grant access' (ADR-001). Genuinely missing: the concrete content of the unauthenticated view for a PRIVATE orchid (404 vs neutral page, whether record existence is confirmed), what a pending-activation scan renders, and any sign-in-then-return-to-/p/{LabelID} requirement. The buildable specification does not exist.

</details>

### 21. Orchid Update fields collapse species/grex and cultivar/clone, contradicting ADR-001 taxonomy separation

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `taxonomy` · **Lenses:** Orchid domain · **(acknowledged schema gap)**

ADR-001 explicitly requires keeping botanical concepts separate ('Do not combine species epithet, grex, clonal epithet, or cultivar epithet') and defines a nameType classifier plus optional hybridOrigin. But the MVP Definition's Update capability lists the editable identity fields as 'Genus / Species or grex / Cultivar or clone' — a flat model merging species epithet with grex and cultivar with clonal name. No document defines the actual separated orchid template field set (genus, species epithet, grex, clonal/cultivar epithet, nameType, hybridOrigin, parentage). MVP-PRIORITIES acknowledges a taxonomy schema is still to be added; this finding is the specific unresolved design contradiction that schema must resolve.

**Why it matters:** A grex (a hybrid's registered cross name, e.g. Cymbidium Golden Elf) is categorically different from a species epithet — conflating them means the system cannot distinguish a natural species from a man-made hybrid, cannot drive correct labels ('Golden Elf' should not italicize like a species), cannot support parentage or grex registration, and cannot power correct similarity matching. This is the most fundamental orchid identity distinction and the two authoritative docs disagree on the model.

**Suggested requirement:** Define the orchid taxonomy contract with separate fields — Genus, specificEpithet, grex, cultivarEpithet (clonal name), nameType (SPECIES | HYBRID/GREX | INTERGENERIC), optional hybridOrigin/parentage — matching ADR-001; correct the MVP Update field list to expose these as distinct inputs (with a simple mode that preserves the entered name verbatim), and preserve name-as-entered plus verification status separately from classification.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 'Taxonomy' and 'Corrections to client feedback' item 1; ADR-003 'Documentation authority'; MVP Definition 'Update' capability; MVP-PRIORITIES P0-contracts item 1

The surface conflict is real: MVP Update lists 'Species or grex' and 'Cultivar or clone' as merged fields while ADR-001 mandates 'Do not combine species epithet, grex, clonal epithet, or cultivar epithet'. However, the docs substantially resolve which side wins: ADR-003 states 'When documents conflict, the authoritative governance document and accepted ADRs control implementation details', and ADR-001 already names the accepted taxonomy contract's nameType and optional hybridOrigin. The separated data model is therefore decided; what remains missing is the actual taxonomy schema (acknowledged as to-be-added in MVP-PRIORITIES item 1 without definition) and correction of the MVP field list.

</details>

### 22. AI proposal contract: confirmation command exists but the proposal object, lifecycle, and versioning are undefined

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `underspecified` · **Lenses:** Contracts/Architecture · **(acknowledged schema gap)**

batch.schema.json already ships CONFIRM_AI_PROPOSAL with an open Payload object — contradicting ADR-001 ('Strict output schemas with unexpected keys rejected') and AGENTS.md ('Reject unexpected keys and malformed outputs'). Nothing defines: proposal identity (ProposalUUID) and storage location (Firestore vs draft-local — syncState includes WAITING_FOR_AI/AI_REVIEW_REQUIRED, implying pre-sync proposals); field-level claim granularity and partial acceptance (Section 7's review offers 'Change Something'); invalidation when the canonical Version advances past the proposal's version metadata; the shape of mandated provenance fields (model, prompt, schema, template, knowledge versions per AGENTS.md; evidence references, confidence, uncertainty per ADR-001); or how a confirmed proposal maps onto thingEvent beyond the AI_CONFIRMED SourceType. The AI-proposals schema is acknowledged as to-be-added; these design questions go further.

**Why it matters:** AI interpretation is the primary intake experience and an MVP success criterion ('Review AI summary'). The proposal contract is the boundary that makes 'AI proposes, human confirms' auditable; an open confirmation payload is exactly the hole prompt-injection controls are meant to close.

**Suggested requirement:** Specify the AI proposal contract before AI flow work: ProposalUUID, tenant/thing/draft scoping, per-field claims each carrying value, evidence references, source type, confidence, and uncertainty text; required model/prompt/schema/template version metadata; a validity window bound to the Thing Version (stale proposals require re-review); a closed CONFIRM_AI_PROPOSAL payload referencing ProposalUUID plus accepted claim IDs and per-claim user edits; and the deterministic mapping from accepted claims to commands and lifecycle events.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES P0-contracts item 1 ('AI proposals'); ADR-001 'AI permissions'; AGENTS.md 'AI development'; docs/CODE-REVIEW.md 'AI governance'

Prose partially specifies proposal content: 'Proposed claims include evidence references, confidence, uncertainty, and version metadata' (ADR-001); 'Record model, prompt, schema, template, and knowledge versions' (AGENTS.md); 'Proposals preserve evidence references, confidence, uncertainty, and model/prompt/schema versions' (CODE-REVIEW). The AI-proposals schema is acknowledged on the to-be-added list. Verified missing: CONFIRM_AI_PROPOSAL's Payload is an open object (contradicting 'Strict output schemas with unexpected keys rejected'), and no document defines ProposalUUID/storage location, field-level claim granularity or partial acceptance mapping to 'Change Something', staleness/invalidation against Thing Version, or the mapping from accepted claims to commands and events.

</details>

### 23. Accession-number allocation is named everywhere but specified nowhere (year reset, padding, concurrency, gaps)

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `underspecified` · **Lenses:** Contracts/Architecture · **(acknowledged schema gap)**

MVP Definition Section 21 recommends PCO-{YEAR}-{SEQUENCE} (example PCO-2026-0001) as a tenant setting; ADR-001 says AccessionNumber is a 'tenant sequence assigned by trusted server logic during canonical commit'; MVP-PRIORITIES schedules the allocator. Unspecified: whether SEQUENCE resets per calendar year and in which time zone the year boundary falls (PCO is America/Denver); zero-padding width and overflow beyond 9999; whether allocation may leave gaps on failed commits; uniqueness scope (tenant-wide vs per-year); what happens to existing numbers if the format setting is edited; and how a sequential counter is allocated safely under Firestore transaction contention when ADR-002 batch intake commits up to 50 CREATE_THING operations concurrently. The identity schema is acknowledged as to-be-added, but the allocation behavior spec is beyond that acknowledgement.

**Why it matters:** Accession numbers are printed on permanent physical labels and cannot be reissued after PCO labels its plants; a wrong guess on reset/padding is effectively irreversible. Contention behavior determines whether batch intake — ADR-002's headline workflow — serializes on a single counter document.

**Suggested requirement:** Write an accession-allocation spec: per-tenant, per-calendar-year sequence in the tenant time zone, 4-digit zero-padded with defined overflow (grow digits, never wrap), allocated inside the canonical-commit transaction via a per-tenant-per-year counter document with documented contention/retry behavior under batch load, gaps permitted and never reused, and format-setting changes applying only to future allocations.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 'Three-tier identity' and command list; MVP Definition Section 21; MVP-PRIORITIES P0 item 9

Covered: allocation ownership and timing ('AccessionNumber: tenant sequence assigned by trusted server logic during canonical commit', ADR-001), the recommended tenant-configurable format PCO-{YEAR}-{SEQUENCE} with example PCO-2026-0001 (MVP Section 21), tenant timezone America/Denver (Section 3), and its placement in the scaffold ('accession allocation', MVP-PRIORITIES P0 item 9). Missing exactly as claimed: no document specifies year reset semantics or timezone boundary, padding width/overflow, gap policy on failed commits, uniqueness scope, behavior when the format setting changes, or counter contention under ADR-002's 50-operation concurrent batch commits.

</details>

### 24. Role and membership model is prose-only: no role-to-command matrix, undefined platform administrator, undefined 'elevated permission' for deletion

**Priority:** P0 · **Verdict:** Partially covered · **Area:** `underspecified` · **Lenses:** Contracts/Architecture · **(acknowledged schema gap)**

MVP Definition Section 3 defines Owner/Editor/Viewer capabilities in prose, but no document maps roles to the trusted-command set that MVP-PRIORITIES P0 item 6 must test ('tenant-isolation and role Rules tests before application data access'). The MVP Delete section requires permanent deletion to need 'an additional confirmation and elevated permission' without naming the role or whether it is tenant-level or platform-level. MVP-PRIORITIES P0 seeds a 'platform administrator' and AGENTS.md references 'coarse platform roles' in JWT claims, but no document defines any platform-role model, its powers over tenant data, or its audit treatment. Membership lifecycle states (invited/active/suspended/removed) are likewise undefined. Tenant/membership schemas are acknowledged as to-be-added; these design questions exceed schema shape.

**Why it matters:** Deny-by-default Rules and role tests are scheduled before any application data access; they cannot be written against prose. Whether a platform administrator can read PCO's private tenant data is a privacy-governance question (Governance Section 11) that must be answered before the first seed accounts exist.

**Suggested requirement:** Publish an authorization matrix: enumerated tenant roles (OWNER, EDITOR, VIEWER) and platform roles (PLATFORM_ADMIN) mapped to every command type and query surface; define permanent-deletion authority (proposed: tenant Owner request plus platform-admin execution, both audited); define membership states and transitions in the membership schema.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 3 'Initial member roles' and 'Delete or archive'; MVP-PRIORITIES P0-contracts item 1 ('tenants, memberships'); AGENTS.md 'Tenant authorization'

Covered: Section 3 enumerates Owner/Editor/Viewer capabilities in prose; membership and tenant schemas are on the acknowledged to-be-added list; AGENTS.md requires server-side membership/role validation and notes JWT claims 'may support coarse platform roles'. Verified missing: no role-to-command mapping exists to write the P0 item 6 role Rules tests against; the Delete section's 'additional confirmation and elevated permission' never names a role or level; no document defines the platform-role model, its powers over tenant data, or audit treatment in the Firebase-native runtime; membership lifecycle states (invited/suspended/removed) appear nowhere. Section 3's 'add invitations later in the release' is deferral without definition.

</details>

## P1 — resolve during pilot hardening

These gaps will surface during the PCO pilot; each needs an owner and a decision before a paid pilot or second tenant.

| # | Finding | Area | Verdict |
|---:|---|---|---|
| 25 | [SHARED_LINK semantics are undefined relative to the permanent QR URL](#25-sharedlink-semantics-are-undefined-relative-to-the-permanent-qr-url) | `access-control` | Missing |
| 26 | [No Vertex AI data-governance terms: model-training exclusion, data residency, and AI log retention undefined](#26-no-vertex-ai-data-governance-terms-model-training-exclusion-data-residency-and-ai-log-retention-undefined) | `ai-data-governance` | Missing |
| 27 | [Expected PCO scale, load, and collection-size design envelope are undocumented](#27-expected-pco-scale-load-and-collection-size-design-envelope-are-undocumented) | `capacity-planning` | Missing |
| 28 | [No content-moderation, reporting, or copyright-takedown requirements for PUBLIC/PLATFORM sharing](#28-no-content-moderation-reporting-or-copyright-takedown-requirements-for-publicplatform-sharing) | `content-moderation` | Missing |
| 29 | [thingStatus DRAFT exists in the schema but in no product document](#29-thingstatus-draft-exists-in-the-schema-but-in-no-product-document) | `contract-mismatch` | Missing |
| 30 | [Exact-timestamp EffectiveAt contradicts the no-false-precision rule for backdated events](#30-exact-timestamp-effectiveat-contradicts-the-no-false-precision-rule-for-backdated-events) | `data-semantics` | Missing |
| 31 | [Quarantine area/status/collection exist but no quarantine or pest/disease workflow is defined](#31-quarantine-areastatuscollection-exist-but-no-quarantine-or-pestdisease-workflow-is-defined) | `domain-workflow` | Missing |
| 32 | [No error or crash reporting for the PWA](#32-no-error-or-crash-reporting-for-the-pwa) | `error-reporting` | Missing |
| 33 | [No incident-response or breach-notification requirement anywhere in the documentation set](#33-no-incident-response-or-breach-notification-requirement-anywhere-in-the-documentation-set) | `incident-response` | Missing |
| 34 | [Owner 'Manage subscription' has no subscription, plan, or billing requirement anywhere](#34-owner-manage-subscription-has-no-subscription-plan-or-billing-requirement-anywhere) | `monetization` | Missing |
| 35 | [No email-sending capability specified anywhere in the architecture](#35-no-email-sending-capability-specified-anywhere-in-the-architecture) | `platform-infrastructure` | Missing |
| 36 | [Telemetry vs. privacy-by-design policy is unresolved](#36-telemetry-vs-privacy-by-design-policy-is-unresolved) | `privacy` | Missing |
| 37 | [DIVIDED event has no parent/child plant lineage linkage](#37-divided-event-has-no-parentchild-plant-lineage-linkage) | `provenance` | Missing |
| 38 | [No help, support, or feedback channel anywhere in the product or pilot plan](#38-no-help-support-or-feedback-channel-anywhere-in-the-product-or-pilot-plan) | `support` | Missing |
| 39 | ['Without training' MVP success criterion has no measurement protocol](#39-without-training-mvp-success-criterion-has-no-measurement-protocol) | `testability` | Missing |
| 40 | [No abuse controls for the unauthenticated public QR endpoint (rate limiting, enumeration, scraping, App Check)](#40-no-abuse-controls-for-the-unauthenticated-public-qr-endpoint-rate-limiting-enumeration-scraping-app-check) | `abuse-prevention` | Partially covered |
| 41 | [Accessibility requirement has no standard, assistive-technology scope, or test method](#41-accessibility-requirement-has-no-standard-assistive-technology-scope-or-test-method) | `accessibility` | Partially covered |
| 42 | [Golden-set evaluation data has no owner, source, size, or pass thresholds — the mandated merge gate is unenforceable](#42-golden-set-evaluation-data-has-no-owner-source-size-or-pass-thresholds--the-mandated-merge-gate-is-unenforceable) | `ai-evaluation` | Partially covered |
| 43 | [Orchid care/repotting guidance promised, but no knowledge source, curation, or accuracy requirement defined](#43-orchid-carerepotting-guidance-promised-but-no-knowledge-source-curation-or-accuracy-requirement-defined) | `ai-guidance` | Partially covered |
| 44 | [Vertex AI model selection, version pinning, and prompt-change operations undefined](#44-vertex-ai-model-selection-version-pinning-and-prompt-change-operations-undefined) | `ai-operations` | Partially covered |
| 45 | [Supported browser/OS versions and the physical-device QA matrix are unspecified](#45-supported-browseros-versions-and-the-physical-device-qa-matrix-are-unspecified) | `compatibility` | Partially covered |
| 46 | [Account and tenant deletion promised by governance but has no workflow, propagation spec, or retention schedule](#46-account-and-tenant-deletion-promised-by-governance-but-has-no-workflow-propagation-spec-or-retention-schedule) | `compliance-account-lifecycle` | Partially covered |
| 47 | [PII embedded in append-only lifecycle events has no redaction or tombstone mechanism](#47-pii-embedded-in-append-only-lifecycle-events-has-no-redaction-or-tombstone-mechanism) | `data-lifecycle` | Partially covered |
| 48 | [Domain continuity for the permanent QR URL space is unaddressed](#48-domain-continuity-for-the-permanent-qr-url-space-is-unaddressed) | `domain-email` | Partially covered |
| 49 | [Oakland Acquisition modeled as a Collection, not an acquisition lot; batch intake cannot apply shared source/location/quarantine](#49-oakland-acquisition-modeled-as-a-collection-not-an-acquisition-lot-batch-intake-cannot-apply-shared-sourcelocationquarantine) | `domain-workflow` | Partially covered |
| 50 | [Label physical durability and QR print quality for greenhouse conditions are unspecified and untestable](#50-label-physical-durability-and-qr-print-quality-for-greenhouse-conditions-are-unspecified-and-untestable) | `labels` | Partially covered |
| 51 | [Member invitation flow is named but has no workflow, screen, release slot, or acceptance criteria](#51-member-invitation-flow-is-named-but-has-no-workflow-screen-release-slot-or-acceptance-criteria) | `membership` | Partially covered |
| 52 | [Cloud Monitoring alerts named with no signals, thresholds, or recipients](#52-cloud-monitoring-alerts-named-with-no-signals-thresholds-or-recipients) | `monitoring-alerting` | Partially covered |
| 53 | [No notification mechanism for asynchronous events ('We found similar orchids', sync failures)](#53-no-notification-mechanism-for-asynchronous-events-we-found-similar-orchids-sync-failures) | `notifications` | Partially covered |
| 54 | [Pilot exit criteria beyond the section 24 UX checklist are undefined](#54-pilot-exit-criteria-beyond-the-section-24-ux-checklist-are-undefined) | `pilot-governance` | Partially covered |
| 55 | [Tenant JSON/CSV export is a paid-pilot precondition in ADR-001 but has no work item, screen, or release anywhere](#55-tenant-jsoncsv-export-is-a-paid-pilot-precondition-in-adr-001-but-has-no-work-item-screen-or-release-anywhere) | `portability` | Partially covered |
| 56 | [Acquisition/source is unstructured free text; no reusable vendor entity or acquisition record](#56-acquisitionsource-is-unstructured-free-text-no-reusable-vendor-entity-or-acquisition-record) | `provenance` | Partially covered |
| 57 | [AI latency and unavailability behavior in interactive intake is undefined](#57-ai-latency-and-unavailability-behavior-in-interactive-intake-is-undefined) | `reliability` | Partially covered |
| 58 | [Backup requirement omits Cloud Storage media and lacks RPO/RTO, cadence, retention, and restore-test scope](#58-backup-requirement-omits-cloud-storage-media-and-lacks-rporto-cadence-retention-and-restore-test-scope) | `resilience-backup` | Partially covered |
| 59 | [Similar-orchid discovery: MVP Release 5 scope directly conflicts with ADR-001 'post-MVP'](#59-similar-orchid-discovery-mvp-release-5-scope-directly-conflicts-with-adr-001-post-mvp) | `scope-contradiction` | Partially covered |
| 60 | [Auth session lifetime, sign-out, and revocation propagation unspecified (offline re-auth, shared devices, removed members)](#60-auth-session-lifetime-sign-out-and-revocation-propagation-unspecified-offline-re-auth-shared-devices-removed-members) | `session-management` | Partially covered |
| 61 | ['For Sale' has no defined buyer-contact mechanism, and default privacy excludes contact info](#61-for-sale-has-no-defined-buyer-contact-mechanism-and-default-privacy-excludes-contact-info) | `sharing-sales` | Partially covered |
| 62 | [DraftThing's single Narrative string has no defined mapping to the first-class multi-entry narrative timeline](#62-draftthings-single-narrative-string-has-no-defined-mapping-to-the-first-class-multi-entry-narrative-timeline) | `underspecified` | Partially covered |
| 63 | [Label template contract: printJob references templates that have no contract, and the privacy/physical/reprint-history requirements are undefined](#63-label-template-contract-printjob-references-templates-that-have-no-contract-and-the-privacyphysicalreprint-history-requirements-are-undefined) | `underspecified` | Partially covered |
| 64 | [LabelID locked to UUID format produces a dense ~69-character QR URL on a 1x4 inch label; ADR-001 only requires 'opaque'](#64-labelid-locked-to-uuid-format-produces-a-dense-69-character-qr-url-on-a-1x4-inch-label-adr-001-only-requires-opaque) | `underspecified` | Partially covered |
| 65 | [Standard-user conflict-resolution UX is undefined](#65-standard-user-conflict-resolution-ux-is-undefined) | `usability` | Partially covered |
| 66 | [Sale/transfer statuses exist but the listing/transfer journey and post-transfer QR behavior are missing](#66-saletransfer-statuses-exist-but-the-listingtransfer-journey-and-post-transfer-qr-behavior-are-missing) | `workflow-contract-gap` | Partially covered |

### 25. SHARED_LINK semantics are undefined relative to the permanent QR URL

**Priority:** P1 · **Verdict:** Missing · **Area:** `access-control` · **Lenses:** Security/Privacy/Compliance

SHARED_LINK is a first-class sharing level (core.schema.json sharingLevel; Governance 8.4; MVP Section 17), but no document defines what the shared link actually is. The only URL specified anywhere is the permanent QR route /p/{LabelID}, printed on every physical label and valid through all lifecycle changes. Unresolved: whether SHARED_LINK reuses the LabelID URL or mints a separate token; token entropy; expiry; and revocation semantics — Governance 11.7 requires users can 'Remove public listings', but revoking a share that rides the LabelID would conflict with the label/QR-permanence guarantee (Governance 13).

**Why it matters:** LabelIDs leak physically: every visitor, buyer, or greenhouse photo exposes them. If SHARED_LINK grants access via the same identifier, a one-time share becomes irrevocable-in-practice for anyone who ever captured the label — silently violating the revocation promise older users will rely on. This must be decided before Firestore/Storage Rules and the public route are designed, not retrofitted.

**Suggested requirement:** Specify SHARED_LINK as a distinct, independently revocable ShareToken (>=128-bit random, optional expiry) resolving to a defined field projection; /p/{LabelID} for a non-public thing shows at most a neutral 'private record' page regardless of any active share tokens. Add ShareToken to the contracts backlog and revocation tests to the Rules test plan.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched core.schema.json sharingLevel enum, MVP Definition Sections 17 and 19, Governance 8.4 and 11.7, ADR-001, docs/CODE-REVIEW.md

Confirmed missing. SHARED_LINK appears only as an enum value (core.schema.json), a one-line option in MVP Section 17, and 'Available through a shared link' in Governance 8.4; MVP Section 19 lists 'Shared orchid page' and 'QR orchid page' as separate screens but defines neither. No document states whether the shared link reuses /p/{LabelID} (the only URL specified anywhere) or mints a separate token, and nothing addresses token entropy, expiry, or how Governance 11.7's revocation ('Remove public listings') coexists with Governance 13's QR permanence. Greps for token, expiry, and revocation found only embedding deactivation in ADR-001. Mere enum/screen-list mentions are the finding's premise, not coverage.

</details>

### 26. No Vertex AI data-governance terms: model-training exclusion, data residency, and AI log retention undefined

**Priority:** P1 · **Verdict:** Missing · **Area:** `ai-data-governance` · **Lenses:** Security/Privacy/Compliance

Genkit/Vertex AI is the mandated AI runtime (ADR-001, ADR-003, README, AGENTS.md), but no document addresses the model-provider side: nothing requires that tenant narratives, photos, and transcripts sent to Vertex AI are excluded from provider model training or abuse-monitoring retention; no GCP region/data-residency requirement exists anywhere; and no retention limit is set for CCE's own AI request/response logs, which AGENTS.md implicitly grows by requiring provenance recording.

**Why it matters:** Narratives are the richest PII in the system (seller names like 'Andy', prices, locations, personal memories). The authoritative 'Private by default' posture is hollow if that content is retained or used for training outside CCE's control. Region choice must be made when the first Genkit flow is configured — before P2 AI features — and affects latency for the Utah pilot and any future EU expansion. This is also information a Privacy Policy must accurately state.

**Suggested requirement:** Add an AI data-governance requirement: Vertex AI configured with training-use disabled/zero-retention options as available; all Firestore, Storage, and Vertex AI resources pinned to a named US region (e.g. us-central1) recorded in an ADR; CCE-side AI request/response logs tenant-scoped, retained max 90 days, and included in deletion propagation.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched ADR-001 (Prompt-injection controls: 'Data minimization'), ADR-003, AGENTS.md 'AI development', Governance 11.5 (AI privacy), README; greps for residency, region, training, retention

Confirmed missing. Genkit/Vertex AI is mandated in ADR-001/ADR-003/README/AGENTS.md, and ADR-001 requires data minimization in AI flows, but no document addresses the provider side: nothing excludes tenant content from provider model training or abuse-monitoring retention, no GCP region/data-residency requirement exists anywhere (grep for 'region' hits only OCR-region derivatives), and no retention limit applies to CCE's own AI request/response logs even though AGENTS.md requires recording model/prompt/schema/knowledge versions. Governance 11.5 covers exposure to other members, not the model provider.

</details>

### 27. Expected PCO scale, load, and collection-size design envelope are undocumented

**Priority:** P1 · **Verdict:** Missing · **Area:** `capacity-planning` · **Lenses:** Operations/Launch, NFR/Quality

No document records how many orchids, photos, members, or labels PCO currently has or expects (ADR-002 says only 'high-volume collection work such as incoming shipments' with no numbers), and no per-tenant collection-size assumption exists for the dashboard, search, or orchid list. Meanwhile hard limits are baked into contracts with no stated workload justification: batch.schema.json caps a BatchCommandRequest at 50 operations and printJob Quantity at 1000; core.schema.json caps Media at 20 per draft and Narrative at 20000 characters — these bound requests, not collection size. There is no storage or cost forecast for the preserve-originals media policy, ADR-003 concedes Firestore query design 'requires deliberate contract work' without a scale target, and ADR-002's benchmarks require 'representative PCO workflows' whose representativeness is undefined without real numbers.

**Why it matters:** List pagination, the search strategy, and dashboard aggregation (count queries vs maintained counters) differ fundamentally at 200 versus 10,000 plants, and choosing wrong is expensive to retrofit on Firestore. Without a workload profile, nobody can validate whether a 50-operation batch fits a real PCO shipment, forecast the Cloud Storage bill, set FinOps quotas, or justify any test dataset size; every 'representative workload' claim is unanchored.

**Suggested requirement:** Document a PCO workload profile before scaffold decisions freeze: current collection size, expected additions per month, typical shipment/batch size, photos per orchid and average photo size, member count and expected concurrent users. Declare a design envelope (proposed: 5,000 active orchids per tenant) within which list, search, and dashboard views must meet the performance budgets; validate existing contract limits (50-op batch, 20 media/draft) against it; produce a first-year storage and AI cost estimate; seed and maintain a test dataset at envelope scale for emulator and performance tests.

<details>
<summary>Verification evidence</summary>

Searched all 12 documents. No document records PCO's collection size, member count, photos per orchid, shipment size, or any per-tenant scale assumption. ADR-002 says only 'high-volume collection work such as incoming shipments' and its FinOps section lists metrics to measure during pilot (capture time, AI calls, retry rate) without any workload profile anchoring them; 'representative PCO workflows' is never quantified. The contract limits (batch.schema.json: 50 operations, printJob Quantity 1000; core.schema.json: 20 media per draft, 20000-char narrative) carry no stated workload justification. No storage or cost forecast exists for the preserve-originals policy, and ADR-003 ('Firestore data modeling and query design require deliberate contract work') names the risk without a scale target. The MVP's only performance number is the two-minute basic-record target (Section 24), which is not a scale envelope.

</details>

### 28. No content-moderation, reporting, or copyright-takedown requirements for PUBLIC/PLATFORM sharing

**Priority:** P1 · **Verdict:** Missing · **Area:** `content-moderation` · **Lenses:** Security/Privacy/Compliance

MVP Sections 17-18 and Release 5 put PUBLIC/PLATFORM sharing and cross-member similar-orchid discovery in MVP scope. Governance 12 provides block/decline controls for connection requests only. Across all 12 documents there is no requirement for reporting abusive/spam/infringing shared pages, no moderation workflow or platform takedown authority, no DMCA/copyright process, and no prohibited-content policy; Governance 20.3 tests AI outputs, not user-published content.

**Why it matters:** Once Release 5 ships, CCE hosts user-generated public content and becomes responsible for it: DMCA safe harbor requires a registered agent and a takedown process before infringement occurs, and public pages carrying spam or abuse under the orchid-enthusiasts.com brand damage the trust the pilot depends on. There is no defined platform authority to unpublish a page — governance gives only the owner that control (11.7).

**Suggested requirement:** Before Release 5: add a 'Report this page' action on every PUBLIC/PLATFORM/SHARED_LINK page; define a platform-admin takedown capability (unpublish without deleting tenant data, with audit event and owner notification); publish an acceptable-use policy; establish a DMCA agent and takedown/counter-notice workflow.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched all 12 documents; closest content is Governance 12 (block/decline for connection requests) and Governance 11.7 (owner's 'Remove public listings')

Confirmed missing. Grep across the repository for DMCA, takedown, moderation, abuse, acceptable use, and infringement returned zero matches. Governance 12's block/decline controls apply only to member connection requests; Governance 11.7 gives only the owner the ability to remove public listings; Governance 20.3 tests AI outputs, not user-published content. No reporting action, platform takedown authority, prohibited-content policy, or copyright process exists anywhere, despite Release 5 putting PUBLIC/PLATFORM sharing in MVP scope.

</details>

### 29. thingStatus DRAFT exists in the schema but in no product document

**Priority:** P1 · **Verdict:** Missing · **Area:** `contract-mismatch` · **Lenses:** Contracts/Architecture

core.schema.json thingStatus enumerates DRAFT alongside the statuses MVP Section 6 defines (ACTIVE default, QUARANTINE, FOR_SALE, RESERVED, TRANSFERRED, ARCHIVED) — DRAFT appears in no product or governance document. Its semantics are undefined: pre-sync drafts are modeled by the separate draftThing contract with syncState, so it is unclear whether a canonical Thing can ever be DRAFT, whether DRAFT is the server-side state for ADR-001's 'QR pending activation' window, whether DRAFT things appear in search, dashboard counts, and the orchid list, and what transition rules apply.

**Why it matters:** Status drives Rules visibility, dashboard counts, and QR lookup behavior. An undefined status invites divergent implementations (one developer using DRAFT for unsynced intake, another for incomplete records), and PCO users would see an unexplained status in the UI.

**Suggested requirement:** Either remove DRAFT from thingStatus (drafts are exclusively draftThing records) or define it in the MVP Definition: visibility in search/dashboards/QR lookup, the transition to ACTIVE, and whether accession numbers are assigned while DRAFT.

<details>
<summary>Verification evidence</summary>

**Checked:** packages/contracts/schemas/core.schema.json $defs.thingStatus (line 20) vs MVP Definition Section 6 ('Default orchid status ACTIVE' plus QUARANTINE, FOR_SALE, RESERVED, TRANSFERRED, ARCHIVED)

Confirmed mismatch. core.schema.json enumerates DRAFT in thingStatus, but MVP Section 6 lists only ACTIVE (default), QUARANTINE, FOR_SALE, RESERVED, TRANSFERRED, ARCHIVED. Searched the MVP Definition, Governance, all three ADRs, AGENTS.md, MVP-PRIORITIES, CODE-REVIEW, and the audit: 'draft' appears only for DraftThing/OfflineDraftStore (a separate contract with its own syncState) and ADR-001's 'pending activation' QR window, never as a canonical Thing status. No document defines DRAFT semantics, visibility, transitions, or accession behavior.

</details>

### 30. Exact-timestamp EffectiveAt contradicts the no-false-precision rule for backdated events

**Priority:** P1 · **Verdict:** Missing · **Area:** `data-semantics` · **Lenses:** NFR/Quality

core.schema.json thingEvent requires EffectiveAt as an RFC 3339 date-time, yet Governance 10.4 forbids inferring exact dates from vague statements and the intake flow explicitly solicits vague dates ('About when did you acquire it?', Section 7 Step 5). There is no representation for approximate or partial dates (year-only, 'spring 2024'), so any backdated ACQUIRED or REPOTTED event must fabricate a precise timestamp. Separately, the tenant Default Time Zone America/Denver is never connected to event semantics: no document says whether EffectiveAt is entered and displayed in tenant time or device time, or how a date-only statement converts to a timestamp.

**Why it matters:** Acquisition and care history are core provenance for collectors. Storing invented precision directly violates the authoritative confidence-awareness rules the platform is marketed on, and ambiguous timezone handling will scramble displayed history dates (an evening event appearing on the next day).

**Suggested requirement:** Extend thingEvent with EffectiveAtPrecision (EXACT, DAY, MONTH, YEAR, APPROXIMATE) or an approximate-date structure, and specify: event dates are entered and displayed in the tenant time zone; a day-precision event stores 12:00 tenant-local time with precision DAY; the UI renders only the precision actually known.

<details>
<summary>Verification evidence</summary>

**Checked:** core.schema.json thingEvent (EffectiveAt required, format date-time) vs Governance 10.4; MVP Section 7 Step 5

Conflict CONFIRMED. core.schema.json thingEvent requires 'EffectiveAt' as an RFC 3339 date-time ('EffectiveAt': {'$ref': '#/$defs/timestamp'}, timestamp = 'format': 'date-time') on every event including ACQUIRED and REPOTTED, while Governance 10.4 states 'CCE should not infer: Exact dates from vague statements' and 9.6 requires preserving uncertainty ('Likely from the 1980s'). The intake flow explicitly solicits vague dates ('About when did you acquire it?', Section 7 Step 5). No approximate/partial-date representation exists anywhere — StructuredDetails is an untyped 'type': 'object' with no specification. The tenant Default Time Zone America/Denver (MVP Section 3) is never connected to event entry or display semantics in any document. Searched all docs and both schemas for precision, partial-date, or timezone-semantics coverage; none found.

</details>

### 31. Quarantine area/status/collection exist but no quarantine or pest/disease workflow is defined

**Priority:** P1 · **Verdict:** Missing · **Area:** `domain-workflow` · **Lenses:** Orchid domain

Quarantine appears as a location (Section 4), a collection (Section 5), a Thing status (Section 6 and core.schema.json), and a dashboard tile (Section 20). The only related events are generic TREATED and INSPECTED. No document defines a quarantine workflow: no entry trigger, minimum/target duration, inspection cadence, release criteria/approval to move to the main growing area, or any structured pest/disease observation record (scale, mealybug, mites, thrips, rot, or virus such as CymMV/ORSV) that Section 14's 'What may be wrong with it?' implies.

**Why it matters:** For a working nursery, quarantine is a biosecurity process, not just a shelf. Newly acquired plants (the Oakland Acquisition scenario) must be isolated, inspected on a schedule, and cleared before joining the collection, or a single infested import can spread pests/virus to the entire greenhouse. A Quarantine bucket with no rules, watch-list, or gated release gives a false sense of a managed process while the actual biosecurity decision is undefined and unauditable.

**Suggested requirement:** Define a quarantine workflow: entering QUARANTINE records a start date and target release date; require at least one INSPECTED event with a structured pest/disease observation (type, severity, affected part) before a governed, confirmed release transition out of QUARANTINE; add a structured condition/pest observation schema reused by TREATED/INSPECTED and by diagnosis guidance; surface overdue-inspection quarantine plants on the dashboard.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched MVP Sections 4 (Quarantine Area), 5 (Quarantine collection), 6 (QUARANTINE status), 12 (TREATED/INSPECTED events), 14 ('What may be wrong with it?'), 20 ('Orchids in Quarantine' tile), 23 (status changes need confirmation); core.schema.json thingStatus/thingEvent; Governance 8.3 (statuses explicit, confirmed).

Only the nouns exist: a quarantine location, collection, status, and dashboard count, plus generic TREATED/INSPECTED events and a generic diagnosis-guidance question. No document defines any quarantine process — no entry trigger, duration, inspection cadence, release criteria or gated exit transition, and no structured pest/disease observation model anywhere (StructuredDetails is an untyped object). The requirement judged is the workflow, and it has no coverage in any document.

</details>

### 32. No error or crash reporting for the PWA

**Priority:** P1 · **Verdict:** Missing · **Area:** `error-reporting` · **Lenses:** Operations/Launch

MVP-PRIORITIES P1 Hardening item 5 requires user-friendly error states — user-facing display only. No document requires client-side error/crash aggregation (Crashlytics/Sentry-class), reporting of unhandled exceptions on mobile Safari/Chrome, or surfacing drafts stuck in SYNC_ERROR to the team. core.schema.json defines SyncState SYNC_ERROR and LastErrorCode on DraftThing, but nothing routes those signals anywhere; Cloud Functions errors are unmentioned outside the vague 'Cloud Monitoring alerts' line.

**Why it matters:** Target users are older, nontechnical collectors who will not file bug reports. ADR-001 itself lists 'local draft and synchronization complexity' as a cost — and a silent client-side sync failure is lost orchid data, the exact failure mode the offline design exists to prevent. Without error reporting, the team's first sign of a broken intake flow is a pilot user quietly giving up.

**Suggested requirement:** Integrate a client error-reporting service before pilot launch: unhandled exceptions, failed command submissions, and drafts remaining in SYNC_ERROR beyond a threshold (e.g. 24h) are reported to a monitored dashboard with tenant/user/operation identifiers but no narrative or media content; top errors reviewed weekly during the pilot.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched MVP-PRIORITIES P1 Hardening items 5-6, AGENTS.md 'Offline and synchronization', core.schema.json (SYNC_ERROR, LastErrorCode), docs/CODE-REVIEW.md offline checklist; greps for crash, Crashlytics, Sentry

Confirmed missing. The only related items are user-facing: P1 Hardening item 5 (user-friendly validation/conflict/retry/error states), visible sync state with manual retry (AGENTS.md, ADR-001), and the schema's SYNC_ERROR/LastErrorCode fields — none of which route failures to the team. 'Cloud Monitoring alerts' (P1 item 6) is server-side and undefined. Greps for crash/Crashlytics/Sentry returned nothing. No requirement exists for client-side error/crash aggregation, unhandled-exception reporting, or surfacing stuck SYNC_ERROR drafts to a monitored dashboard.

</details>

### 33. No incident-response or breach-notification requirement anywhere in the documentation set

**Priority:** P1 · **Verdict:** Missing · **Area:** `incident-response` · **Lenses:** Security/Privacy/Compliance

Across all 12 documents, the closest items are 'Cloud Monitoring alerts' (MVP-PRIORITIES P1 Hardening item 6) and secret scanning in CI. There is no incident classification, no response roles or runbook requirement, no commitment to notify affected tenants/users after a breach, no notification timeline, and no requirement to log/preserve forensic evidence during an incident.

**Why it matters:** CCE will hold personal narratives, purchase prices, and location data for a commercial tenant. Utah (PCO's jurisdiction) and every other US state have breach-notification statutes with deadlines; discovering obligations mid-incident during a pilot with a real nursery is the worst time. A one-page requirement now is cheap; its absence also blocks any credible Privacy Policy statement about breach handling.

**Suggested requirement:** Add a pilot-grade incident-response requirement: severity definitions, a named responder, a documented runbook (revoke credentials, preserve logs, assess scope), tenant/user notification within 72 hours of confirming a breach affecting their data, and a post-incident review recorded in docs/. Reference it from Governance 20.4's release criteria.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched all 12 documents; closest content is MVP-PRIORITIES P1 Hardening item 6 ('Cloud Monitoring alerts') and CI secret scanning (AGENTS.md, docs/CODE-REVIEW.md)

Confirmed missing. Grep for incident, breach, notification, forensic, and runbook returned zero matches across the repository. No incident classification, response roles, runbook, tenant/user breach-notification commitment, timeline, or evidence-preservation requirement exists in any document. Governance 20.4's release criteria do not reference incident handling.

</details>

### 34. Owner 'Manage subscription' has no subscription, plan, or billing requirement anywhere

**Priority:** P1 · **Verdict:** Missing · **Area:** `monetization` · **Lenses:** Product/UX

The Owner role includes 'Manage subscription and tenant settings' (Section 3), and ADR-001 references a 'paid pilot'. Yet no document defines a subscription: no plan/tier model, no billing provider, no subscription screen (Section 21's nine tenant settings omit it), no schema mention, no release slot. The Out of Scope list defers 'E-commerce checkout' and 'Payment processing', which in context concern orchid sales, leaving it ambiguous whether platform billing is also deferred. What happens to tenant data/access when a paid pilot subscription lapses is undefined.

**Why it matters:** A role capability referencing a nonexistent object cannot be built or tested, and the paid pilot ADR-001 anticipates has no commercial mechanics. Ambiguity between 'payment processing is out of scope' and 'Owner manages subscription' invites contradictory implementation assumptions during pilot hardening.

**Suggested requirement:** Either strike 'Manage subscription' from the MVP Owner role and record that billing is post-MVP (paid pilot handled by manual agreement), or add a P1 requirement defining the pilot commercial model: plan record on the tenant, billing provider decision, a read-only subscription status panel in Tenant Settings, and a documented grace/lapse policy that never deletes tenant data.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched MVP Definition Section 3 (Owner: 'Manage subscription and tenant settings'), Section 21 (nine tenant settings, no subscription), Section 25 Out of Scope ('E-commerce checkout', 'Payment processing'), ADR-001 Portability ('paid pilot'); repo-wide grep for subscription/billing/plan/payment/tier.

The Owner capability line is the sole mention of a subscription in the entire documentation set. No plan/tier model, billing provider, subscription screen or setting, schema concept, release slot, or lapse policy exists anywhere. The Out of Scope 'Payment processing' entry sits in a list about orchid commerce (checkout, shipping, accounting) and never states whether platform billing is deferred, so the ambiguity the finding describes is real and unresolved. A dangling role capability with zero defining requirements is a genuine gap.

</details>

### 35. No email-sending capability specified anywhere in the architecture

**Priority:** P1 · **Verdict:** Missing · **Area:** `platform-infrastructure` · **Lenses:** Product/UX, Operations/Launch

A repo-wide search shows 'email' appears only in MVP-PRIORITIES item 7 ('Firebase Authentication with email/password'). The README target-architecture diagram, ADR-001's Google Cloud services list, and ADR-003's runtime definition contain no transactional email service (no Trigger Email extension, SendGrid, Mailgun, SES, or equivalent), no sender-domain/deliverability requirement (SPF/DKIM/DMARC) for orchid-enthusiasts.com, and no email templates — default Firebase Auth mail comes from a generic firebaseapp.com sender. Yet at least three specified or implied journeys need outbound email: member invitations (Section 3), password reset (implied by email/password auth from day one), and email-channel notifications. Even the choice of Firebase Auth built-in templates is nowhere recorded.

**Why it matters:** Email is a cross-cutting dependency with lead time (domain authentication, deliverability, template review for a non-technical audience). A password-reset email from an unrecognized sender that lands in spam is a lockout and a trust failure for exactly the older users the MVP must win, and discovering mid-build that the architecture has no way to send an invitation will stall membership work and tempt insecure shortcuts.

**Suggested requirement:** Add an architecture decision selecting the MVP email mechanism: Firebase Auth built-in templates for reset/verification on a verified orchid-enthusiasts.com sender domain with SPF/DKIM configured before the first pilot user is onboarded, plus a designated transactional email service (e.g. the Firebase Trigger Email extension) for invitations and notifications, with tenant-scoped, audited send events.

<details>
<summary>Verification evidence</summary>

**Checked:** Repo-wide grep for email/SMTP/SendGrid/Mailgun/SES/SPF/DKIM/DMARC returns exactly one hit: MVP-PRIORITIES.md item 7 'Configure Firebase Authentication with email/password and Firebase App Check'. Checked README target architecture, ADR-001 Google Cloud services list, ADR-003 runtime definition.

No transactional email service, extension, sender-domain/deliverability requirement, or template appears in any document. Even the implicit day-one need (password reset for email/password auth) has no stated mechanism or sender-domain decision, and invitation/notification journeys have no email channel. The finding's absence claim is fully verified.

</details>

### 36. Telemetry vs. privacy-by-design policy is unresolved

**Priority:** P1 · **Verdict:** Missing · **Area:** `privacy` · **Lenses:** Operations/Launch

Governance mandates privacy-by-design (Section 11: private by default, minimum necessary disclosure, 11.5 AI privacy) and AGENTS.md mandates data minimization in AI flows, but no document states what product/usage telemetry may be collected, whether third-party analytics SDKs (e.g. Google Analytics for Firebase) are permitted in the PWA, whether narratives, photos, prices, or location names may appear in logs, traces, error reports, or Vertex AI request logging, what retention applies to telemetry, or whether pilot users are told they are being measured. Since measuring Section 24 and ADR-002 requires telemetry, the two requirement sets collide with no stated policy.

**Why it matters:** PCO narratives contain exactly the data Governance 11.2 classifies as private — purchase prices, seller names, exact locations. Accidental capture of that content in an analytics pipeline or default Vertex AI logging would violate the platform's own authoritative standard and undermine the trust proposition the pilot exists to validate with older, privacy-sensitive collectors.

**Suggested requirement:** Adopt a telemetry data policy before instrumentation is built: telemetry events carry identifiers, timings, counts, and error codes only — never narrative text, media, prices, or location names; Vertex AI production request/response logging is disabled or redacted; telemetry retention is bounded (e.g. 90 days); pilot users receive a plain-language notice that usage timing and errors are measured.

<details>
<summary>Verification evidence</summary>

**Checked:** Searched Governance 11 and 11.5, AGENTS.md, ADR-001 (data minimization is scoped to AI extraction flows), ADR-002 FinOps measurements, MVP Definition Section 24; greps for telemetry and analytics

Confirmed missing. Greps for telemetry and analytics returned zero matches. ADR-002 mandates measuring pilot metrics (capture time, AI calls, retry rates) and MVP-PRIORITIES P2 requires FinOps benchmarks, so measurement is required — yet no document states what usage telemetry may be collected, whether third-party analytics SDKs are permitted, whether narratives/prices/locations may appear in logs or Vertex AI request logging, what retention applies, or whether pilot users are notified. ADR-001's 'data minimization' applies to AI extraction flow inputs, not product telemetry. The collision between required measurement and privacy-by-design has no stated policy.

</details>

### 37. DIVIDED event has no parent/child plant lineage linkage

**Priority:** P1 · **Verdict:** Missing · **Area:** `provenance` · **Lenses:** Orchid domain

Both MVP Section 12 and core.schema.json define a DIVIDED event, and Governance 4.1 names 'parentage' as an orchid-specific concept. But neither thing/thingIdentity nor any event carries a parent/child ThingUUID relationship — no ParentThingUUID, DerivedFromThingUUID, or lineage field. A division that creates new plants (each needing its own ThingUUID, LabelID, and accession number per ADR-001) has no defined way to link offspring back to the divided parent.

**Why it matters:** Every division IS the same clone as the parent (all divisions of Golden Elf 'Sundust' share clonal identity, provenance, and any award). Losing the parent link severs clonal identity, provenance, and value from the new plants and prevents a nursery from tracking how many divisions of a valuable stock plant exist or answering 'where did this come from?'. Division is a primary propagation method and explicitly an MVP event, so the gap is directly in scope.

**Suggested requirement:** Add an optional lineage linkage to the Thing/identity contract (e.g. OriginThingUUID plus OriginKind = DIVISION | KEIKI | SEEDLING) that a DIVIDED/propagation event populates when creating child Things, so a division inherits and displays its parent's clonal identity and provenance while retaining its own permanent identity and accession number.

<details>
<summary>Verification evidence</summary>

**Checked:** core.schema.json thingEvent enum (DIVIDED) and thing/thingIdentity definitions (no parent/origin field); MVP Section 12 (DIVIDED); Governance 4.1 ('Orchids add grex, clone, parentage, flowering, and culture'); MVP-PRIORITIES P0 contracts item 1 (schema list omits lineage); REPOSITORY-AUDIT (schemas 'incomplete for Phase 0'). Grep for parentage/lineage/keiki/division.

Verified: no ParentThingUUID, OriginThingUUID, or any lineage field exists in thing, thingIdentity, or thingEvent, and no document describes linking a division's offspring to its parent. The only adjacent text is Governance 4.1's single word 'parentage' in a template-examples list — undefined, and in context about botanical/breeding parentage rather than Thing-to-Thing division linkage — plus a generic acknowledgment that schemas are incomplete, whose P0 extension list (identity, tenants, taxonomy, etc.) does not include lineage. That does not address the linkage requirement.

</details>

### 38. No help, support, or feedback channel anywhere in the product or pilot plan

**Priority:** P1 · **Verdict:** Missing · **Area:** `support` · **Lenses:** Product/UX, Operations/Launch

A repo-wide search finds no help screen, support contact, FAQ, tutorial, or feedback mechanism in any document — not in the MVP screens list (Section 19), dashboard actions (Section 20), Tenant Administration (Section 21), or MVP-PRIORITIES. This despite the success criterion that 'a PCO user can complete this workflow without training' (Section 24) and Governance Section 16's whole section on accessibility for users of varying technical confidence. There is no support address, no response-time expectation, and no triage process for the pilot: when the workflow fails for a non-technical user — a stuck sync, a mis-scanned QR, a confusing AI proposal — there is no defined path to a human or to guidance.

**Why it matters:** For older, non-technical PCO users, no support affordance converts every confusion into abandoned data or an out-of-band phone call the team never learns about. An older collector who hits a sync error does not file a ticket — they stop using the app, and the pilot fails silently with no diagnostic signal. A feedback channel is also the primary instrument for validating the MVP hypotheses ADR-002 insists must be measured, and the 'without training' verdict depends on hearing exactly where users get stuck.

**Suggested requirement:** Before pilot launch: a persistent, large-target 'Help / Send Feedback' entry in plain language opening a short guide for the core journey plus a contact/feedback action that captures the user's description and app-state context (screen, sync state, app version); a monitored support address with a stated response target (e.g. next business day, America/Denver); and a weekly pilot feedback review that feeds the issue tracker, with a named owner for triage.

<details>
<summary>Verification evidence</summary>

**Checked:** Repo-wide grep for help/support/feedback/FAQ/tutorial: only ADR-001's 'Corrections to client feedback' heading (design feedback, not a user channel), Governance 'AI should help users', and Section 24's 'without training'. Checked MVP Section 19 screens, Section 20 dashboard actions, Section 21 settings, Governance Section 16, MVP-PRIORITIES all tiers.

No help screen, guide, support contact, response-time expectation, feedback mechanism, or pilot triage process appears in any document. Governance Section 16 mandates accessibility qualities (plain language, easy correction) and Section 24 sets the 'without training' bar, but neither provides any path to human assistance or a feedback instrument. The absence claim is fully verified.

</details>

### 39. 'Without training' MVP success criterion has no measurement protocol

**Priority:** P1 · **Verdict:** Missing · **Area:** `testability` · **Lenses:** NFR/Quality

MVP Section 24 makes the overall success gate 'a PCO user can complete this workflow without training', and Governance 20.4 requires that standard users can complete the workflow without understanding the backend. Neither defines a protocol: no participant profile (age or technical familiarity matching the declared older-collector audience), no sample size, no task-completion or assistance thresholds, and no time bounds other than the two-minute basic-record target.

**Why it matters:** This criterion is the definition of MVP success itself. Without a protocol it degenerates into a founder-assisted demo, and the simplicity claims made for older, nontechnical collectors are never actually validated against that population before the pilot bets on them.

**Suggested requirement:** MVP acceptance includes a moderated usability test with at least 5 first-time participants aged 55+ from the target demographic: >= 80% complete the full Section 24 workflow with zero facilitator interventions, each producing a basic record in under two minutes; every failure is triaged as a blocking or waived issue with recorded rationale.

<details>
<summary>Verification evidence</summary>

The criterion itself is stated twice — MVP Section 24 ('The MVP is successful when a PCO user can complete this workflow without training') and Governance 20.4 ('Standard users can complete the workflow without understanding the backend') — but the requirement under review is a measurement protocol, and none exists: no participant profile, sample size, assistance/completion thresholds, or moderation method appears anywhere. The only measurable bound is 'A basic record can be created in under two minutes' (Section 24 operational targets). Grep for 'usability test', participant counts, and demographic criteria returned nothing; Governance 20.3 tests AI behavior, not human task completion.

</details>

### 40. No abuse controls for the unauthenticated public QR endpoint (rate limiting, enumeration, scraping, App Check)

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `abuse-prevention` · **Lenses:** Security/Privacy/Compliance

The public QR route https://orchid-enthusiasts.com/p/{LabelID} and 'Public and authorized QR lookup' (MVP-PRIORITIES P1 item 6) are the only unauthenticated data-serving surfaces, yet every abuse-control requirement in the docs is scoped elsewhere: App Check enforcement is 'on trusted commands' (P1 Hardening item 1); rate/usage limits appear only under Media processing (ADR-001) and FinOps (AGENTS.md, docs/CODE-REVIEW.md). No document specifies rate limiting, bot/scraper controls, caching, or monitoring for /p/{LabelID}, and none precisely defines what an unauthenticated scan of a PRIVATE orchid's QR reveals.

**Why it matters:** Each anonymous hit triggers billable Firestore reads/Function invocations, so an unthrottled public endpoint is a direct FinOps and denial-of-wallet exposure. LabelIDs are UUIDs (low enumeration risk) but leak physically: anyone photographing PCO's sales bench harvests valid IDs. Scraping of PLATFORM/PUBLIC pages also undermines Governance 11.5's promise that private tenant information is not exposed.

**Suggested requirement:** Specify the public QR/shared-page endpoint as a hardened surface: per-IP and global rate limits with CDN caching, 404-indistinguishable responses for unknown vs pending-activation vs private LabelIDs (defining exactly which fields a PRIVATE thing exposes — recommend none), App Check where client-mediated, abuse monitoring alerts, and a scraping/robots policy. Add these to the P1 Hardening list alongside trusted-command enforcement.

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md 'Media and FinOps' ('Use application-level quotas, rate limits, duplicate detection, caching, and model routing'); docs/CODE-REVIEW.md Media and FinOps ('Quotas, rate limits ... applied server-side where needed'); ADR-001 Media processing; MVP-PRIORITIES P1 Hardening item 1 (App Check on trusted commands); MVP Definition 'Mobile QR scanning' ('When the user is not authorized, the page displays only the permitted public or limited view')

Generic mandates exist: AGENTS.md and CODE-REVIEW.md require application-level quotas, rate limits, and caching server-side (scoped under Media/FinOps, 'where needed'), and the MVP defines that unauthorized scans see 'only the permitted public or limited view', with Section 17/22 excluding location/price/contact from public views. But no document applies any abuse control to the /p/{LabelID} route specifically: App Check enforcement is scoped to trusted commands only, no rate-limit/caching/monitoring/bot requirement names the public QR or shared-page surface, and no document defines exactly what an unauthenticated scan of a PRIVATE thing's QR returns (the 'permitted public view' of a PRIVATE record is undefined).

</details>

### 41. Accessibility requirement has no standard, assistive-technology scope, or test method

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `accessibility` · **Lenses:** NFR/Quality

Governance Section 16 lists qualitative properties (large readable text, clear action labels, limited choices) and 20.4 requires 'Accessibility has been reviewed' before release; AGENTS.md and docs/CODE-REVIEW.md require 'mobile viewport and accessibility tests'. No document names a conformance target (WCAG version and level), minimum text sizes or contrast ratios, screen-reader or OS text-scaling support, or the review method that would make 'reviewed' a pass/fail gate.

**Why it matters:** The declared primary users are older, less technical collectors with 'varying technical confidence, vision, dexterity'. Without a measurable bar, accessibility review is subjective, regressions cannot block CI, and the population the product is explicitly designed for is the one most likely to be excluded by an unmeasured deficiency.

**Suggested requirement:** Required MVP workflows conform to WCAG 2.2 AA; body text >= 16 px CSS with correct behavior at 200% OS text scaling; touch targets >= 44x44 px; contrast >= 4.5:1. Verification per release: automated checks (axe or equivalent) in CI plus a manual screen-reader pass (VoiceOver on iOS, TalkBack on Android) of the intake, scan, and label workflows.

<details>
<summary>Verification evidence</summary>

**Checked:** Governance Section 16 (Accessibility and ease of use); Governance 20.4 ('Accessibility has been reviewed'); MVP Definition Mobile interface requirements ('Large readable text', 'High contrast', 'Minimum touch-target size appropriate for mobile use'); AGENTS.md and docs/CODE-REVIEW.md ('mobile viewport and accessibility tests')

Qualitative accessibility requirements are substantive and repeated: Governance 16 lists large readable text, clear action labels, limited choices, voice input, plain-language confirmations; the MVP requires high contrast and appropriate touch targets; accessibility tests are on both required-validation lists; AGENTS.md forbids silently weakening accessibility requirements. Genuinely missing: no conformance target (WCAG appears nowhere), no numeric text-size/contrast/touch-target thresholds, no screen-reader (VoiceOver/TalkBack absent from the set) or OS text-scaling requirement, and no defined method that makes 'Accessibility has been reviewed' a pass/fail gate.

</details>

### 42. Golden-set evaluation data has no owner, source, size, or pass thresholds — the mandated merge gate is unenforceable

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `ai-evaluation` · **Lenses:** Operations/Launch, NFR/Quality

AGENTS.md mandates 'AI golden-set evaluations' and docs/CODE-REVIEW.md mandates 'AI golden-set and adversarial evidence tests' as merge gates; ADR-001 requires adversarial evaluation cases for prompt injection; Governance 20.3 lists ten AI failure modes to test. But no document defines who creates the golden set, what it is built from (synthetic narratives? real PCO narratives — which triggers the Governance 11 question of tenant data in test fixtures?), how many cases, orchid-specific composition, or any quantitative threshold: no target extraction accuracy for explicit facts (the '$34.44 from Andy' canonical example), no schema-validity rate, no injection-resistance criterion, no measurable test of Section 24's 'AI clearly distinguishes user statements from inference', and no versioning/extension process when misbehavior appears in pilot. A mandatory merge gate references an artifact no requirement produces.

**Why it matters:** Without a defined dataset and thresholds the gate is either silently skipped — leaving Governance 20.3's AI review (false certainty, privacy leakage, failure to preserve uncertainty) untested — or trivially 'passes', so regressions in flagship AI extraction quality or successful prompt injections could ship to the pilot undetected. The MVP's core promise of accurate, uncertainty-preserving extraction is only enforceable through this evaluation asset.

**Suggested requirement:** Before the first AI feature merges: a named owner curates a versioned in-repo golden set of >= 100 orchid intake narrative/OCR cases (synthetic plus consented, anonymized PCO examples), including >= 20 adversarial/prompt-injection cases and >= 10 conflicting-evidence cases, with expected structured outputs and uncertainty markers; CI gates at >= 95% schema-valid outputs, >= 90% exact extraction of explicit facts, zero AI inference labeled as a user statement, and zero successful injections; every pilot AI defect adds a regression case.

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md 'Required validation' ('AI golden-set evaluations'); docs/CODE-REVIEW.md 'Required validation before merge' ('AI golden-set and adversarial evidence tests'); ADR-001 Prompt-injection controls ('Adversarial evaluation cases'); Governance 20.3 (ten AI failure modes to test)

The gate and its qualitative targets are mandated in four places: AGENTS.md and CODE-REVIEW.md require golden-set/adversarial evaluations before merge, ADR-001 requires adversarial evaluation cases, and Governance 20.3 enumerates the failure modes to test (false certainty, privacy leakage, failure to preserve uncertainty, etc.). But no document defines the artifact itself: no owner, no data source (synthetic vs real PCO narratives and the resulting tenant-data question), no case count or composition, no quantitative pass thresholds (extraction accuracy, schema-validity rate, injection resistance), and no versioning/extension process. The mandated gate references an evaluation asset that no requirement produces — mandate without definition is PARTIALLY_COVERED at best.

</details>

### 43. Orchid care/repotting guidance promised, but no knowledge source, curation, or accuracy requirement defined

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `ai-guidance` · **Lenses:** Orchid domain

The MVP promises orchid care as a core deliverable: Section 2 lists 'Orchid care and repotting guidance', Section 10 offers '[Care Instructions]' and '[How Should I Repot It?]', Section 14 commits to answering best-care, potting, and 'What may be wrong with it?' questions; MVP-PRIORITIES lists it as P2. Governance Section 17 sets safety rules and 9.7 requires distinguishing known/assumed/recommendation/confidence. AGENTS.md says to record 'knowledge versions' — implying a knowledge artifact — but NO document defines where the horticultural facts come from: no curated culture knowledge base, no genus-specific culture data model, no citation/sourcing requirement, and no accuracy/golden-set requirement specific to care answers.

**Why it matters:** Orchid culture is genus-specific and often opposite between genera (Phalaenopsis: warm, low light, evenly moist; Cymbidium: cool nights, high light; Masdevallia: cold, constant moisture). If care guidance is generated from an LLM's unsourced parametric knowledge, plausible-but-wrong advice (wrong temperature class, watering, repotting season) will kill plants and destroy trust with exactly the older, non-technical PCO users the MVP targets. This is the highest-value orchid-specific promise in the MVP and it currently has no grounding.

**Suggested requirement:** Define an explicit, versioned orchid culture knowledge source (curated per-genus/section culture profiles covering temperature class, light, water, humidity, medium, repotting season) that care/repotting guidance MUST cite; require every care answer to reference the knowledge version and fall back to 'insufficient context, consult a specialist' rather than inferring culture from visual similarity or genus guesses; add a care-guidance golden evaluation set and an accuracy acceptance bar before the P2 guidance feature ships.

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md AI development ('Record model, prompt, schema, template, and knowledge versions'; 'AI golden-set evaluations' in Required validation); docs/CODE-REVIEW.md ('AI golden-set and adversarial evidence tests'); Governance 4.5 (specialty sites provide 'Domain-specific knowledge'); Governance 20.2 (templates define 'Guidance boundaries'); Governance 9.7 and 17 (guidance structure and safety, 'A plant treatment should not be recommended without sufficient context'); MVP Section 14 (inputs and required answer structure).

Partial scaffolding exists: 'knowledge versions' implies a versioned knowledge artifact, golden-set evaluations are a mandatory merge gate (generically), specialty sites are assigned 'domain-specific knowledge', and guidance answers must separate known/assumed/recommendation/confidence. But no document defines WHAT the horticultural knowledge source is — no curated per-genus culture knowledge base, no culture data model, no citation/grounding requirement tying care answers to a source rather than LLM parametric knowledge, and no care-guidance-specific accuracy bar or golden set before the P2 feature ships. The grounding gap the finding identifies is real.

</details>

### 44. Vertex AI model selection, version pinning, and prompt-change operations undefined

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `ai-operations` · **Lenses:** Operations/Launch

AGENTS.md requires recording model/prompt/schema/template/knowledge versions and ADR-001 requires proposals to carry version metadata — recording provenance is covered. But no document selects a model or criteria for choosing one, requires pinning flows to explicit model versions rather than floating aliases, defines the response when Google deprecates a Vertex AI model version mid-pilot, or defines where prompts live, how prompt changes are reviewed, released, and rolled back, or what re-evaluation gates a model/prompt change before production.

**Why it matters:** An unpinned model alias can change extraction behavior under PCO users with zero code change, silently breaking the Section 9/23 guarantees (preserve uncertainty, never present inference as fact) that were validated on the prior model. A forced model retirement with no upgrade playbook is an outage risk for 'Tell me about this orchid' — the MVP's flagship interaction.

**Suggested requirement:** AI flows pin explicit Vertex AI model versions in versioned configuration; any model or prompt change must pass the golden-set and adversarial evaluations before production rollout and ships/rolls back through the same CD pipeline as code; maintain a deprecation watch on announced Vertex AI model retirements with a tested migration path.

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md 'AI development' ('Record model, prompt, schema, template, and knowledge versions') and 'Required validation' (AI golden-set evaluations); ADR-001 AI permissions (proposals include version metadata); docs/CODE-REVIEW.md required validation ('AI golden-set and adversarial evidence tests')

Provenance recording is covered (AGENTS.md, ADR-001, CODE-REVIEW proposals must carry model/prompt/schema versions), and the merge-time golden-set/adversarial gates would nominally apply to prompt changes shipped through code review. What remains missing, as claimed: no document selects a model or criteria for choosing one, requires pinning flows to explicit model versions rather than floating aliases, defines a response to a Vertex AI model deprecation mid-pilot, or specifies where prompts live and how prompt/model changes are released, re-evaluated, and rolled back. ADR-002's 'model routing' is a FinOps cost lever, not a version-management policy.

</details>

### 45. Supported browser/OS versions and the physical-device QA matrix are unspecified

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `compatibility` · **Lenses:** NFR/Quality

The MVP Definition requires support for 'current mobile Safari and Chrome browsers' without defining 'current' (no minimum iOS or Android versions; desktop browsers only implicit). MVP-PRIORITIES names 'Physical-device QA on iPhone and Android' but no device or OS list exists in any document. The in-application QR scanner and direct camera capture depend on camera APIs whose behavior differs in installed-PWA context on iOS, and no document records these platform constraints or a minimum-version decision.

**Why it matters:** Older collectors disproportionately carry older phones and OS versions. Without a version floor, 'works on iPhone and Android' is untestable, and a camera-API failure on the pilot user's actual device gets discovered in the greenhouse instead of in QA.

**Suggested requirement:** Publish a support matrix (proposed: iOS Safari on iOS >= 16; Android Chrome within the last two major releases; latest desktop Chrome, Safari, Edge), require physical-device QA on at least one roughly three-year-old device per platform plus the actual phone models used by PCO staff, and document known PWA camera-API limitations per platform with fallbacks (e.g. file-input capture).

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition, Supported approach ('The implementation must support current mobile Safari and Chrome browsers') and Mobile acceptance criteria; MVP-PRIORITIES P1 item 8 ('Physical-device QA on iPhone and Android')

Browser support is stated ('current mobile Safari and Chrome browsers') and physical-device QA on iPhone and Android is required, with the mobile acceptance criteria requiring the full workflow on both an iPhone and an Android phone. Genuinely missing: 'current' is never defined — no minimum iOS or Android version, no desktop browser list (desktop is only implicit in 'Desktop browser' in the one-application diagram and PDF requirements), no device/OS QA matrix, and no documentation of PWA camera-API constraints for the in-application QR scanner and direct camera capture. Grep for version numbers and per-platform camera limitations returned nothing.

</details>

### 46. Account and tenant deletion promised by governance but has no workflow, propagation spec, or retention schedule

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `compliance-account-lifecycle` · **Lenses:** Product/UX, Security/Privacy/Compliance

Governance 11.7 requires users be able to 'Request account or tenant deletion', and Governance 7.2 anticipates permanent removal 'for privacy, legal, or account-deletion purposes' as the exception to durable audit history. No other document operationalizes this: no screen, command, schema concept, or release entry covers account or tenant deletion, and nothing defines what deletion covers — Firebase Auth accounts, Firestore Things/events/operation ledger, Cloud Storage originals and derivatives, generated label PDFs and exports, Firestore backups, Genkit/Vertex AI request logs, similarity embeddings (ADR-001 requires removal when discoverability is revoked, but only for embeddings), lifecycle events referencing the deleted user's RecordedByUserUUID, or content the tenant shared publicly. No completion SLA or per-category data-retention schedule exists, and the tension between append-oriented history (AGENTS.md) and true deletion is unresolved.

**Why it matters:** This is a stated user-control commitment in the authoritative document and a likely legal obligation under US state privacy laws once real consumer accounts exist on a public domain. The architecture is deliberately append-oriented with backups — deletion that was never designed cannot later be honestly claimed. Design implications (how audit events reference actors, storage layout for erasable media) are far cheaper to decide before the Firestore document model hardens; if PCO churns or a platform member invokes the right, there are currently no acceptance criteria for fulfilling it.

**Suggested requirement:** Add a data-lifecycle requirement defining deletion semantics: user-initiated account deletion (auth record removal, personal data anonymized to an opaque actor ID in retained audit events); Owner-initiated tenant deletion with export-first prompt and cooling-off period; cascade rules for media, embeddings, exports, AI logs, and shared pages, completed or irreversibly anonymized within 30 days; backups containing the data expire within a defined retention window (max 90 days); the deletion command itself audited with non-personal identifiers; a support-mediated request path for the MVP period before self-serve UI; and a published per-category retention schedule (drafts, media, AI logs, exports, audit events).

<details>
<summary>Verification evidence</summary>

**Checked:** Governance 11.7 ('Request account or tenant deletion'); Governance 7.2 ('unless permanent removal is required for privacy, legal, or account-deletion purposes'); MVP Definition 'Delete or archive' (permanent deletion of erroneous records requires additional confirmation and elevated permission — Thing-level only). Grep for deletion/retention across all docs.

The commitment is documented (11.7) and the audit-history exception for account deletion is anticipated (7.2), and Thing-level permanent deletion has a stated control — but nothing operationalizes account or tenant deletion: no screen, command, schema concept, or release entry; no cascade definition across Auth records, Firestore, Storage media, labels, exports, backups, AI logs, or embeddings (ADR-001's removal covers embeddings on discoverability revocation only); no completion SLA or per-category retention schedule; and the append-oriented-history vs true-deletion tension is unaddressed. A stated promise with zero defined mechanics is exactly the 'X promised without defining X' pattern.

</details>

### 47. PII embedded in append-only lifecycle events has no redaction or tombstone mechanism

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `data-lifecycle` · **Lenses:** Security/Privacy/Compliance

core.schema.json thingEvent copies free-text Narrative (20k chars), PriorState, ResultingState, and RecordedByUserUUID into every event, and SupersedesEventUUID supersedes but does not remove content. ADR-001 mandates corrections via superseding events rather than erasure; AGENTS.md requires append-oriented history; Governance 18 requires audit histories with no retention limit. Yet Governance 7.2 explicitly reserves 'permanent removal... for privacy, legal, or account-deletion purposes'. No document or schema defines how permanent removal works against the append-only event model — no redaction event type, tombstoning of Narrative/PriorState payloads, or user-UUID anonymization exists.

**Why it matters:** This is a concrete unresolved design conflict between two authoritative requirements (immutable history vs permanent privacy removal), and it must be resolved while the thingEvent contract is still being finalized: once events replicate into backups and exports with embedded narrative text, honoring a 7.2 removal or account deletion becomes practically impossible. Audit-log retention is also unbounded, which no privacy notice can honestly describe.

**Suggested requirement:** Extend the event contract with a REDACTED mechanism: a privileged redaction command that overwrites Narrative/PriorState/ResultingState payloads of targeted events with a tombstone (retaining EventUUID, type, timestamps for chain integrity), plus user-UUID anonymization on account deletion; define an audit-event retention ceiling (e.g. life of tenant + 90 days). Record the design in an ADR.

<details>
<summary>Verification evidence</summary>

**Checked:** Governance 7.2: 'Previous versions should remain in the audit history unless permanent removal is required for privacy, legal, or account-deletion purposes'; ADR-001 Lifecycle history: 'Corrections create superseding or corrective events rather than erasing history'; core.schema.json thingEvent (SupersedesEventUUID, Narrative, PriorState/ResultingState)

The tension is real and the mechanism is undefined. Governance 7.2 itself carves out the permanent-removal exception ('unless permanent removal is required for privacy, legal, or account-deletion purposes') and 11.7 requires honoring account/tenant deletion — so the removal REQUIREMENT is stated, meaning this is not wholly missing. But ADR-001's model ('superseding or corrective events rather than erasing history') and the thingEvent contract (SupersedesEventUUID only; free-text Narrative and PriorState/ResultingState embedded per event) provide no redaction event type, payload tombstoning, or user-UUID anonymization, and Governance 18's audit histories carry no retention ceiling. How the stated exception is executed against the append-only contract is defined nowhere.

</details>

### 48. Domain continuity for the permanent QR URL space is unaddressed

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `domain-email` · **Lenses:** Operations/Launch

MVP-PRIORITIES P0 scaffold item 10 covers configuring Hosting and orchid-enthusiasts.com HTTPS routing, and MVP Section 8 plus Governance 13 make the printed QR URL (https://orchid-enthusiasts.com/p/{LabelID}) a permanent identifier surviving rename, sale, transfer, and archive. Missing: who owns the domain registration, renewal/expiry safeguards, DNS provider and access control, and any statement that the /p/* URL space is a permanent operational commitment backing physical labels.

**Why it matters:** Every 1x4-inch label PCO sticks in a pot physically encodes the domain — a lapsed registration or lost DNS access permanently bricks the QR system for the whole physical collection.

**Suggested requirement:** Record domain governance before pilot: registrar account ownership, auto-renew plus expiry alerting, restricted and documented DNS access; declare orchid-enthusiasts.com/p/* a permanent URL contract.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 8 (Orchid Label MVP); Governance Section 13 (Label and QR governance); MVP-PRIORITIES P0-Scaffold item 10; docs/CODE-REVIEW.md Labels and printing

The URL-permanence contract itself IS declared at product level: MVP Section 8 requires a 'Permanent QR code' opening https://orchid-enthusiasts.com/p/{LabelID} that 'remains valid if the orchid is Renamed, Moved, Reclassified, Sold, Transferred, Archived'; Governance 13 says 'Renaming, moving, sharing, selling, or archiving a Thing should not invalidate the QR'; CODE-REVIEW requires 'QR routes remain stable'. MVP-PRIORITIES P0 item 10 covers configuring Hosting and orchid-enthusiasts.com HTTPS routing. Genuinely missing: registrar account ownership, auto-renew/expiry safeguards, DNS provider and access control — 'registrar', 'renewal', and 'DNS' appear nowhere in the documentation set, and no document treats the domain registration as an operational commitment backing printed labels.

</details>

### 49. Oakland Acquisition modeled as a Collection, not an acquisition lot; batch intake cannot apply shared source/location/quarantine

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `domain-workflow` · **Lenses:** Orchid domain

MVP Section 5 models 'Oakland Acquisition' as a Collection ('a logical group', 'not a physical location'). ADR-002's BatchIntakeSession groups DraftThings for capture, but there is no acquisition lot / consignment / shipment entity carrying shared source, acquisition date, or destination. ADR-002 and AGENTS.md restrict bulk acceptance to 'allowlisted low-consequence fields' and explicitly forbid bulk-approving location, status, privacy, sale/transfer, and identity on AI confidence alone — and quarantine is a status/location, both excluded from bulk approval.

**Why it matters:** The Oakland Acquisition is the archetypal nursery intake: dozens of plants arriving together from one source that a grower wants to tag once as 'all from the California nursery, acquired this date, all into Quarantine'. The current model forces per-plant re-entry of the common source and blocks applying quarantine status/location across the lot, because those (correctly) high-consequence fields are excluded from bulk approval — yet no lot-level workflow exists to set them safely with a single confirmation. The headline multi-plant scenario becomes slow and error-prone.

**Suggested requirement:** Introduce a first-class acquisition-lot concept (distinct from Collection) that BatchIntakeSession can carry, holding shared source/vendor, acquisition date, and a proposed destination (e.g. Quarantine area + QUARANTINE status); allow a single explicit, audited confirmation to apply the lot's location/status/source to all items as a governed batch command, rather than treating those consequential fields as either per-item-only or unsafe AI bulk approval.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 5 (Collection behavior: 'Default location', 'Sharing default'); ADR-002 'Batch capture sessions' and 'Batch command orchestration'; AGENTS.md 'Batch workflows'

Partial coverage exists: MVP Section 5 gives every Collection a 'Default location' and 'Sharing default' (the Oakland Acquisition example sets Default Location: Main Growing Area), a 'Quarantine' collection is recommended, and ADR-002's BatchCommandRequest supports up to 50 explicit user-issued UPDATE_METADATA/RECORD_EVENT commands. The candidate also overstates the prohibition: AGENTS.md forbids bulk changes to location/status/sale 'solely because an AI confidence value is high' — an explicit user-confirmed batch command is not excluded. What genuinely remains missing: no acquisition-lot/consignment entity carries shared source/vendor or acquisition date (these are not Collection fields), and no document defines a single-confirmation workflow to apply a shared status/location/source across a lot's items.

</details>

### 50. Label physical durability and QR print quality for greenhouse conditions are unspecified and untestable

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `labels` · **Lenses:** Orchid domain, NFR/Quality

The MVP centers on a permanent 1x4 inch QR label PDF (Section 8), with 'Labels print accurately from PDF' and 'QR lookup works from the standard phone camera' as success criteria (Section 24); Governance 13 covers label content/QR permanence. ADR-001 defers native printer support 'until a reference printer and media are evaluated' but states no durability requirement, and the PDF path still ships at MVP for physical greenhouse use. No document specifies: label stock/ink durability (waterproof, UV-resistant, fertilizer-salt-resistant); PDF resolution/DPI; margins or quiet zone; QR error-correction level; minimum printed QR size; verified scan distance/conditions; text-overflow rules for long names (e.g. "Cymbidium Golden Elf 'Sundust'" on 1x4 in); or a reference printer and stock for acceptance testing.

**Why it matters:** The scan-and-retrieve workflow — the physical anchor of the whole product loop (print → scan → record) — assumes the QR remains readable on a tag living in constant water, humidity, fertilizer salts, and UV. Ordinary inkjet/laser paper labels smear and fade within weeks in a greenhouse, silently breaking the permanent-identity promise even though the digital record is fine, and 'prints accurately' currently has no objective acceptance test.

**Suggested requirement:** Specify: label PDFs render at 300 DPI equivalent with >= 2 mm QR quiet zone; QR at error-correction level Q at >= 0.75 in printed size; defined name-truncation/wrap rules for both 1x4 templates; recommended waterproof/UV-resistant label stock or synthetic tag. Acceptance: >= 95% scan success at 10-30 cm with a mid-range phone on the chosen reference printer and stock, including after a simulated humidity/abrasion/weathering cycle, verified as part of physical-device pilot QA.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 24 ('Labels print accurately from PDF', 'QR lookup works from the standard phone camera'); Section 8 label requirements; MVP-PRIORITIES P1 item 8 (physical-device QA); ADR-001 Labels; Governance 13

Goal-level acceptance criteria exist: Section 24 requires labels to 'print accurately from PDF' and QR lookup to work 'from the standard phone camera', P1 vertical-slice item 8 requires physical-device QA on iPhone and Android, and ADR-001 defers native printing 'until a reference printer and media are evaluated'. However, searching all 12 documents (including greps for durability, waterproof, DPI, error correction, quiet zone) found zero specification of label stock/ink durability, PDF resolution, quiet zone, QR error-correction level, minimum printed QR size, scan-distance acceptance conditions, text-overflow rules, or a reference printer/stock. Durability in greenhouse conditions is addressed nowhere; the success criteria have no objective test definition.

</details>

### 51. Member invitation flow is named but has no workflow, screen, release slot, or acceptance criteria

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `membership` · **Lenses:** Product/UX

The MVP Definition defines Owner/Editor/Viewer roles (Section 3) and says 'The initial MVP may begin with one Owner account and add invitations later in the release'; Tenant Administration (Section 21) lists 'Members and roles'. Yet no document defines the invitation journey: no invite/members screen in Section 19, no release in Section 26 or MVP-PRIORITIES tier contains invitations, and nothing specifies invite delivery, acceptance by new vs existing accounts, expiry/revocation, or role assignment/change/removal. Editor and Viewer roles are unreachable by any specified path. (The memberships schema is acknowledged as to-be-added; this finding is about the absent user workflow and sequencing.)

**Why it matters:** PCO is a nursery, plausibly with more than one person handling plants; the Editor/Viewer model is dead weight until someone can be added to the tenant. 'Later in the release' with no release assignment is unplannable, and the flow has hard dependencies (email delivery, account-linking, audited membership commands) that need lead time.

**Suggested requirement:** Add a Members screen and an invitation requirement to a named release: Owner invites by email with a chosen role; invitee with no account routes through Create Account and auto-joins on acceptance; invites expire and are revocable; membership grant/change/removal are trusted commands emitting audit events. State which MVP release ships it or formally defer to post-pilot.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 3 ('The initial MVP may begin with one Owner account and add invitations later in the release'), Owner role ('Manage members'); Section 21 Tenant Administration ('Members and roles'); MVP-PRIORITIES.md P0 contracts item 1 (canonical schemas include 'memberships').

The docs deliberately name the capability and defer it — Editor/Viewer roles are fully defined, 'Members and roles' is a tenant setting, and memberships schemas are a scheduled P0 contracts item. But 'add invitations later in the release' is 'add X later' without defining X: no invite journey, no Members screen in Section 19, no entry in Section 26's release sequence or any MVP-PRIORITIES tier, and nothing on delivery, acceptance for new vs existing accounts, expiry/revocation, or role change/removal. Grep for 'invit' finds only the single deferral sentence.

</details>

### 52. Cloud Monitoring alerts named with no signals, thresholds, or recipients

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `monitoring-alerting` · **Lenses:** Operations/Launch, NFR/Quality

MVP-PRIORITIES P1 Hardening item 6 is the only mention of alerting in the entire documentation set. It never says what to alert on (Functions error rate or latency, Hosting/QR-route availability, Auth failures, App Check rejection spikes, Firestore quota exhaustion, Vertex AI error rate or spend, sync-failure spikes, backup-job failure), what thresholds apply, where alerts are delivered, or who acknowledges them.

**Why it matters:** As written the item cannot be built or accepted — 'alerts' with no alert conditions is not a requirement. During the pilot, the first notice of a failing accession-allocation command or dead QR lookup would otherwise come from a confused non-technical PCO user, if it comes at all.

**Suggested requirement:** Enumerate a minimum production alert set with thresholds and delivery: callable-command error rate > 2% over 15 minutes; p95 command latency > 3s; any scheduled backup failure; App Check rejection spike; sync-failure spikes; storage/AI quota at 80%; daily Vertex AI spend above a set dollar threshold; QR public route availability check failing. Each alert names a delivery channel and a responsible responder.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES P1 Hardening item 6: 'Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts.'

The alerting requirement exists — P1 Hardening item 6 mandates configuring Cloud Monitoring alerts — but that single clause is the entire coverage in the documentation set. No document defines alert signals (error rates, latency, backup failure, App Check rejections, quota, AI spend, QR-route availability), thresholds, delivery channels, or responders. This is 'add X later' without defining X: PARTIALLY_COVERED per that standard, with the substantive alert definition entirely absent.

</details>

### 53. No notification mechanism for asynchronous events ('We found similar orchids', sync failures)

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `notifications` · **Lenses:** Product/UX

MVP Section 18 specifies the prompt 'We found similar orchids shared by other members. Would you like to see them?' but no document defines how the user learns this: ADR-001 says embeddings are generated asynchronously, so the match arrives after the user leaves the sharing flow, yet there is no in-app notification/inbox concept, no push requirement, no email channel, and no notification entry in the screens list, dashboard, or schemas. The same gap applies to other async outcomes users must act on: SYNC_ERROR drafts (core.schema.json syncState) and failed/partial batch items (ADR-002 requires the UI to distinguish them) are visible only if the user is looking at the right screen — nothing specifies proactive surfacing.

**Why it matters:** For occasional, older users who open the app weekly, an async discovery result or a stuck unsynced draft (unsaved plant data at risk) that is never surfaced is functionally lost. The offline-first architecture makes 'you have pending work' signaling a data-integrity concern, not a nicety — AGENTS.md requires visible synchronization state, but visibility on a screen nobody revisits is not a journey.

**Suggested requirement:** Define a minimal notification requirement for MVP: a badge/inbox on the tenant dashboard listing actionable items (drafts in SYNC_ERROR or WAITING_FOR_NETWORK beyond a threshold, failed batch/print items, and later similarity matches), each deep-linking to resolution. Explicitly defer push/email channels with a stated trigger for revisiting.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 20 dashboard tiles ('Orchids Needing Review', 'Labels Not Yet Printed', 'Recent Activity'); docs/CODE-REVIEW.md Offline ('Reconnect, application resume, manual sync, and pending-work review can trigger synchronization'); AGENTS.md ('Local drafts must show visible synchronization state'); ADR-002 ('The UI must clearly distinguish successful, conflicted, failed, and pending items').

There is real passive surfacing: the dashboard's needing-review/labels-not-printed tiles, a required 'pending-work review' concept, and mandatory visible sync state per draft. What remains missing matches the finding's core: no notification/inbox/badge concept in any screen list or schema, no push or email channel, no threshold or deep-link requirement, and — decisive for Section 18 — no defined delivery path for the asynchronous 'We found similar orchids' prompt after the user leaves the sharing flow (ADR-001 makes embedding generation asynchronous). Grep for notif/push/inbox/badge returns zero matches.

</details>

### 54. Pilot exit criteria beyond the section 24 UX checklist are undefined

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `pilot-governance` · **Lenses:** Operations/Launch

MVP Section 24 defines success as one PCO user completing the workflow without training plus nine qualitative operational targets. ADR-001 gates a paid pilot only on JSON/CSV export; ADR-002 defers FinOps benchmarks to 'measured pilot outcomes' and lists multi-tenant boundaries before commercialization as a benefit. No document defines when the pilot ends, what quantitative thresholds (adoption, records catalogued, sync-failure/retry/conflict rates from ADR-002's own metric list, AI proposal acceptance, cost per Thing) constitute pilot success or failure, or who owns the go/no-go decision for the paid pilot or a second tenant.

**Why it matters:** Without exit criteria the pilot drifts indefinitely and ADR-002's carefully specified measurements feed no decision. The team cannot distinguish 'the MVP workflow was demonstrated once' from 'the product is validated for commercialization' — materially different bars that determine whether PCO converts to a paying tenant.

**Suggested requirement:** Adopt a pilot charter before launch: fixed duration (e.g. 8 weeks from PCO go-live), quantitative exit thresholds (e.g. >= 100 orchids catalogued unassisted, >= 70% of intake sessions under two minutes, draft sync-failure rate < 2%, AI proposal acceptance >= 60%, cost per catalogued orchid under a set ceiling), a named go/no-go decision owner, and enumerated follow-on paths (paid pilot, second tenant, iterate, stop).

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 24 (MVP Success Criteria); ADR-001 Portability ('Basic JSON/CSV export is required before a paid pilot'); ADR-002 FinOps measurements and Delivery priority

MVP Section 24 defines a success bar (a PCO user completes the workflow without training) plus nine qualitative operational targets, and ADR-001 gates a paid pilot on JSON/CSV export, so some pilot success definition exists. But no document defines pilot duration, when the pilot ends, quantitative thresholds tied to ADR-002's own measurement list (retry/conflict rate, AI calls, cost per Thing feed no stated decision), or who owns the go/no-go for a paid pilot or second tenant. ADR-002 lists 'Multi-tenant boundaries established before commercialization' as a benefit without a commercialization decision process. Grep for 'go/no-go', 'pilot duration', 'charter' returned nothing.

</details>

### 55. Tenant JSON/CSV export is a paid-pilot precondition in ADR-001 but has no work item, screen, or release anywhere

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `portability` · **Lenses:** Product/UX, Contracts/Architecture · **(acknowledged schema gap)**

ADR-001 (Portability) mandates 'Basic JSON/CSV export is required before a paid pilot; complete media ZIP export may follow', its implementation order step 6 includes export, and Governance 11.7/21 require users be able to export their information. Yet the export workflow is absent from every plan: no P0/P1/P2 feature item in MVP-PRIORITIES implements it, no screen in Section 19 exposes it, no release in Section 26 includes it, and Tenant Administration has no export setting. Beyond the acknowledged missing exports schema, unresolved product questions include: who can export (Owner only? tenant-admin export vs per-user data export — Governance 11.7 is user-framed), what scope (tenant vs collection vs single orchid), what the JSON/CSV shape includes (narratives? history? private/sharing fields?), and what event 'before a paid pilot' maps to in the release sequence.

**Why it matters:** An explicitly stated launch gate with zero scheduled work behind it is how gates get missed — the classic way to discover a blocker at contract-signing time. Export is also the user-trust counterweight to a proprietary AI-organized record: 'Allow users to correct, undo, restore, and export' is a headline promise to collectors entrusting decades of provenance to the platform.

**Suggested requirement:** Add an export work item to MVP-PRIORITIES (P1 Hardening or a pre-pilot gate): Owner-initiated tenant export producing tenant-scoped JSON (full fidelity: things, narratives, lifecycle events, locations, collections, media manifest) and a simplified CSV, delivered via a Cloud Storage signed link from a tenant-scoped Cloud Function with an audit event; surface it in Tenant Settings; state that media ZIP export is deferred and whether a separate per-user data export is in MVP scope.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 Portability ('Basic JSON/CSV export is required before a paid pilot; complete media ZIP export may follow') and Implementation order step 6 ('Label generation, scanning, export, and field validation'); MVP-PRIORITIES.md P0 contracts item 1 (schemas include 'exports'); Governance 11.7 ('Export their information') and Section 6 power-user 'CSV import and export'; tenant-scoped exports in AGENTS.md, ADR-002, docs/CODE-REVIEW.md.

The finding slightly overstates 'no work item anywhere': ADR-001's implementation order step 6 sequences export, and the exports schema is inside P0 contracts item 1 — so the gate has both a stated requirement and two coarse scheduling hooks. What genuinely remains missing: no screen in Section 19, no Tenant Administration setting, no entry in the Section 26 release sequence, no MVP-PRIORITIES feature item implementing the export WORKFLOW (as opposed to its schema), and no product definition of who can export, at what scope, with what JSON/CSV content, or which release constitutes 'before a paid pilot'.

</details>

### 56. Acquisition/source is unstructured free text; no reusable vendor entity or acquisition record

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `provenance` · **Lenses:** Orchid domain

Acquisition is captured only as narrative plus AI extraction ('Bought from Andy for $34.44' extracted to Seller/Price, Section 7; 'Source' is a search facet, Section 16). core.schema.json's ACQUIRED event leaves details as untyped StructuredDetails, and there is no vendor/source entity anywhere. Governance 8.5 defines outbound transfer/sale as a structured, confirmed record (recipient, type, date, price, currency) — but there is no symmetric structured inbound acquisition requirement and no way to reuse a vendor across multiple acquisitions.

**Why it matters:** Provenance is a core CCE capability (Governance 4.1) and a nursery buys repeatedly from the same growers/importers. Storing 'Andy' as free text per plant means no reliable source rollups, no vendor reuse across a shipment, and weak provenance for valuable or CITES-relevant plants. The asymmetry (structured sale-out, unstructured acquisition-in) undermines the search-by-source and provenance promises.

**Suggested requirement:** Define a structured acquisition record on the ACQUIRED event (acquisition method, date, price, currency, and a reference to a reusable tenant Vendor/Source entity with name and optional location/contact), mirroring Governance 8.5's structured transfer/sale, kept private-by-default consistent with financial/source privacy rules.

<details>
<summary>Verification evidence</summary>

**Checked:** Governance 7.1 and 9.4 (CCE may extract 'Acquisition method: Purchase / Seller: Andy / Purchase price: $34.44'); MVP Section 7 Step 4 (Acquisition/Price extraction) and mobile Update ('Acquisition information included in the MVP'); Governance 4.1 ('Acquisition and provenance' shared capability); Section 16 ('Source' search facet); core.schema.json ACQUIRED event with untyped StructuredDetails.

Acquisition is not purely free text in intent: three documents name the specific extractable fields (method, seller, price, assessment, condition), acquisition info is an MVP update capability, and financial/source privacy defaults are set. But the finding's structural claims hold: the ACQUIRED event's StructuredDetails is an untyped object with no acquisition contract, no reusable Vendor/Source entity exists anywhere (P0 contracts item 1's schema list has no vendor/source), and there is no inbound structured-record requirement symmetric to Governance 8.5's confirmed transfer/sale fields. Extraction examples without a contract leave the reuse/rollup gap real.

</details>

### 57. AI latency and unavailability behavior in interactive intake is undefined

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `reliability` · **Lenses:** NFR/Quality

Intake Steps 4-6 (MVP Section 7) and 'Tell me about this orchid' (Section 10) depend on Genkit/Vertex AI responses, but no document defines a timeout, retry policy, progress UX, or fallback when the AI flow is slow or unavailable while the user is online. core.schema.json's syncState includes WAITING_FOR_AI and AI_REVIEW_REQUIRED for the asynchronous draft path, and MVP-PRIORITIES P1-Hardening item 5 names error states generically, but nothing specifies whether the user can save an orchid with narrative only and receive AI organization later, or after how many seconds that path is offered.

**Why it matters:** A Vertex AI incident, cold start, or regional slowdown during the PCO pilot would stall the flagship intake flow with no defined acceptable behavior; the success-criteria step 'Review AI summary' becomes unreachable through no fault of the user, in front of exactly the audience the MVP must not confuse.

**Suggested requirement:** If AI interpretation has not returned within T seconds (proposed: 15 s), intake must offer 'Save now — we'll organize this shortly': the record saves with narrative and media, enters AI_REVIEW_REQUIRED, and the user is notified when the summary is ready. 'Tell me about this orchid' must show progress within 1 s and present a retryable, plain-language error state on failure.

<details>
<summary>Verification evidence</summary>

**Checked:** core.schema.json syncState (WAITING_FOR_AI, AI_REVIEW_REQUIRED); ADR-002 Batch capture sessions ('Capture must not wait for network acknowledgement or AI completion'); MVP-PRIORITIES P1-Hardening item 5; MVP Definition Mobile interface requirements ('Visible loading and save status')

The asynchronous machinery exists: syncState includes WAITING_FOR_AI and AI_REVIEW_REQUIRED, ADR-002 forbids batch capture from waiting on AI completion, offline-first intake (ADR-001) means draft creation cannot structurally require AI, and P1-Hardening item 5 requires 'user-friendly validation, conflict, retry, and error states'. Genuinely missing: no timeout value, no retry policy, no progress UX, and no specified point at which the online interactive intake flow (MVP Section 7 Steps 4-6) offers a save-now-organize-later path; no failure/latency behavior for 'Tell me about this orchid' (Section 10). Grep for 'timeout', 'latency' (outside ADR-001's cost note), 'unavailable' (outside offline-action wording), 'fallback' returned nothing.

</details>

### 58. Backup requirement omits Cloud Storage media and lacks RPO/RTO, cadence, retention, and restore-test scope

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `resilience-backup` · **Lenses:** Security/Privacy/Compliance, Operations/Launch, NFR/Quality

The only backup requirement in the set is MVP-PRIORITIES P1 Hardening item 6: 'Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts.' It names Firestore only — Cloud Storage, which holds the original photographic evidence Governance 3/7.1 and AGENTS.md require preserved (plus label PDFs per P1 item 4), has no backup/versioning requirement anywhere; Firestore backup alone leaves every photograph unprotected against accidental deletion, bad code, or bucket misconfiguration. No document defines backup frequency, retention length, RPO (PITR vs scheduled backups) or RTO targets, restore-drill cadence or acceptance definition for 'verification', encryption/key-management expectations for backup exports, or the interaction between backup retention and the Governance 11.7 deletion promise.

**Why it matters:** For a collector, the photos and stories ARE the product ('CCE preserves the story'). Originals are durable source knowledge — losing PCO's photo evidence is unrecoverable and would end the pilot's trust. 'Backup-restore verification' with no objective cannot be built, accepted, or audited, and unbounded backup retention silently breaks any future deletion guarantee.

**Suggested requirement:** Expand P1 Hardening item 6: Firestore PITR enabled plus daily scheduled backups retained 30-90 days; Cloud Storage originals protected by object versioning, soft-delete, or cross-bucket replication with a defined recovery window; pilot targets RPO <= 24 hours and RTO <= 8 hours; a documented restore drill covering both Firestore and Storage executed in staging before pilot launch and quarterly thereafter with recorded results; backup retention windows recorded in the data-retention schedule so deletion requests fully expire.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES P1 Hardening item 6 ('Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts'); adjacent: AGENTS.md/ADR-002 original-evidence preservation per tenant policy; ADR-001 Portability (tenant export)

A backup requirement exists but only as stated in the candidate: P1 Hardening item 6 names Firestore backups and backup-restore verification. Searching all documents confirms no Cloud Storage backup, object-versioning, or soft-delete requirement anywhere — 'preserve originals according to tenant policy' (AGENTS.md, ADR-002) governs application behavior (not overwriting originals), not disaster recovery, and tenant export (ADR-001) is user-initiated portability, not backup. No document defines backup frequency, retention, RPO/RTO, restore-drill cadence, an acceptance definition for 'verification', or the interaction between backup retention and Governance 11.7 deletion requests.

</details>

### 59. Similar-orchid discovery: MVP Release 5 scope directly conflicts with ADR-001 'post-MVP'

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `scope-contradiction` · **Lenses:** Product/UX, Contracts/Architecture

The MVP Definition places similar-orchid discovery inside the MVP: Section 18 defines it ('viewing similar shared orchids is sufficient'), Section 2 lists it as an Orchid Enthusiasts responsibility, Section 23 lists 'Find similar shared orchids' under MVP AI Rules, and Release 5 includes 'Similar shared orchids'; MVP-PRIORITIES puts it in P2. ADR-001 states flatly: 'Embeddings and similarity are post-MVP.' The precedence rules do not cleanly resolve this — ADR-003's authority rule says ADRs control only the technical mechanism, and 'post-MVP' is a scope statement, not a mechanism. Also unaddressed: the ADR forbids embeddings specifically, so whether non-embedding similarity (e.g. taxonomy-name matching per Governance Section 12) could satisfy Release 5 is nowhere considered.

**Why it matters:** Pilot acceptance is ambiguous — is the MVP done without similarity? The feature drives dependent requirements (embedding lifecycle, revocation on unsharing, the Section 18 notification prompt) whose sequencing differs enormously between 'Release 5' and 'post-MVP'. PCO expectation-setting and the definition of MVP completion hinge on this; unresolved scope conflicts at the bottom of a release sequence surface as launch-week disputes.

**Suggested requirement:** Amend either document so they agree: state in ADR-001 that embedding-based similarity is post-MVP while Release 5 similarity is delivered via deterministic taxonomy/name matching over PLATFORM/PUBLIC-shared projections; or amend the MVP Definition and MVP-PRIORITIES to move similar-orchid discovery entirely to a named post-MVP milestone, removing it from the Release 5 list and MVP AI Rules with a note that the design is accepted but deferred.

<details>
<summary>Verification evidence</summary>

**Checked:** ADR-001 Similarity: 'Embeddings and similarity are post-MVP.' vs MVP Definition Section 18: 'For the first MVP, viewing similar shared orchids is sufficient.'; Section 23 MVP AI Rules: AI may 'Find similar shared orchids'; Release 5: 'Similar shared orchids'; MVP-PRIORITIES P2 item 6: 'Sharing and similar-orchid discovery.' Precedence: README 'Authoritative sources' order; ADR-003 'Documentation authority'.

Conflict CONFIRMED — the passages genuinely disagree: ADR-001 flatly states 'Embeddings and similarity are post-MVP' while the MVP Definition places similar-orchid discovery inside the MVP in three sections plus Release 5, and MVP-PRIORITIES schedules it at P2. The precedence machinery exists but does not resolve it: README's ordering applies 'when implementation details conflict', and ADR-003 says 'Product requirements remain valid unless an ADR changes only the technical mechanism used to deliver them' — a scope statement ('post-MVP') is not a technical mechanism, so both readings survive. Whether non-embedding (deterministic taxonomy-name) similarity could satisfy Release 5 is nowhere considered. Rated PARTIALLY_COVERED only because generic conflict-precedence rules exist; the scope contradiction itself is unresolved.

</details>

### 60. Auth session lifetime, sign-out, and revocation propagation unspecified (offline re-auth, shared devices, removed members)

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `session-management` · **Lenses:** Product/UX, Security/Privacy/Compliance

The MVP's 'Connectivity and session behavior' section covers draft preservation and retry but never authentication session lifetime. Unspecified: how long a signed-in session persists (Firebase Auth defaults to indefinite via refresh tokens — acceptable on shared nursery devices/tablets?); what happens when a token cannot refresh mid-intake after hours offline (ADR-001 requires intake to continue without connectivity); whether re-authentication preserves in-progress drafts and then syncs them; what App Check token expiry does to queued commands on reconnect; how sign-out interacts with locally stored unsynced drafts (retain-and-sync-later vs privacy-wipe); and whether an explicit sign-out control even exists (none appears in any screen list). Also missing: idle timeout, refresh-token revocation on password change, and how quickly a removed member loses direct Firestore Rules read access — ID-token claims can persist up to an hour after revocation, and AGENTS.md/docs/CODE-REVIEW.md's rule that JWT claims are not the sole membership authority covers trusted commands only, not Rules-based reads.

**Why it matters:** The flagship scenario — hours of offline greenhouse capture, syncing later — is exactly where unhandled auth expiry silently strands or discards drafts, contradicting AGENTS.md's requirement that local drafts survive and remain retryable. Conversely, indefinite sessions on a shared tablet at a nursery counter is a tenant-data exposure with no stated policy, and a revoked Editor (a departed PCO helper) can retain read access via cached claims. Neither behavior can be QA'd or asserted in Rules tests without a spec.

**Suggested requirement:** Specify session policy: sessions persist across app restarts by default; if credentials become invalid at sync time, drafts are retained locally, marked WAITING with a plain-language 're-sign-in' prompt, and sync resumes after re-auth by the same user; visible sign-out on all screens, warning when unsynced drafts exist and stating their fate; document App Check/refresh behavior for the offline-to-online transition and test in emulator suites. Define maximum tolerated ID-token claim staleness for Rules-based reads (with mitigation such as membership-document checks in Rules or forced token refresh on membership change), refresh-token revocation on password reset and member removal with access ending within 1 hour, and the chosen Firebase persistence mode for shared-device use.

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md Tenant authorization ('Trusted commands must validate current server-side membership and role'; 'JWT custom claims… must not be the sole source of dynamic tenant membership authorization'); ADR-001 command handler step 1 (validates membership per command); docs/CODE-REVIEW.md Tenant isolation. Searched MVP 'Connectivity and session behavior', all screen lists, MVP-PRIORITIES item 7; grep for sign-out/session lifetime/revoke/refresh token/idle.

One slice is covered: removed members lose trusted-command access immediately because every command validates current server-side membership, and claims are explicitly not the sole authority. The rest of the finding survives: no document specifies session lifetime/persistence mode, an explicit sign-out control (absent from every screen list), what happens when a token cannot refresh after hours offline, whether re-auth preserves and then syncs drafts, sign-out interaction with unsynced local drafts, idle timeout, refresh-token revocation on password change, or tolerated ID-token claim staleness for direct Firestore Rules reads. Grep confirms zero coverage of those topics.

</details>

### 61. 'For Sale' has no defined buyer-contact mechanism, and default privacy excludes contact info

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `sharing-sales` · **Lenses:** Orchid domain

The MVP supports FOR_SALE status, a 'For Sale' collection, a LISTED_FOR_SALE action (Sections 5, 6, 12) and PUBLIC/SHARED_LINK sharing, while deferring e-commerce checkout and payment (Section 25). Governance 11.2 says a sale listing 'May include ... Seller-controlled contact method', but the MVP never defines what that contact method is, how PCO configures it, or how it renders on a shared/public sale page — and both Section 17 and Governance 11.2/11.6 default to excluding personal contact information and exact location from public views.

**Why it matters:** For a nursery, 'For Sale' only has value if a buyer can reach the seller. With no defined contact channel — and a default that hides contact info — a public For-Sale listing is a dead end: buyers see a plant they cannot inquire about. The tension between 'seller-controlled contact method' and 'exclude personal contact by default' is unresolved.

**Suggested requirement:** Define a tenant-configurable, seller-controlled sale-contact method (e.g. a listing inquiry email/handle or link PCO opts into per listing) that appears only on FOR_SALE public/shared views, is excluded from non-sale public views, and never exposes private personal contact details by default — closing the gap between Governance 11.2 and the default-private rules.

<details>
<summary>Verification evidence</summary>

**Checked:** Governance 11.2 Sale listing ('May include ... Seller-controlled contact method'); Governance 12 (Connection consent); MVP Definition Section 17; Section 25

Governance 11.2 explicitly permits a sale listing to include a 'Seller-controlled contact method', and Governance 12 defines a controlled connection-request flow ('CCE should not expose member contact information automatically') — so the concept is acknowledged and the default-exclusion of 'Personal contact information' (MVP Section 17, Governance 11.2 public showcase) is an opt-out default rather than a hard contradiction with a seller-controlled opt-in. What remains missing: no document defines what the contact method actually is, how PCO configures it, or how it renders on FOR_SALE public/shared/QR pages; MVP Section 25 defers e-commerce and Section 18 defers member messaging, leaving no defined inquiry channel for the MVP's For Sale feature.

</details>

### 62. DraftThing's single Narrative string has no defined mapping to the first-class multi-entry narrative timeline

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `underspecified` · **Lenses:** Contracts/Architecture · **(acknowledged schema gap)**

core.schema.json draftThing holds exactly one Narrative string (max 20000 chars), while MVP Section 11 and Governance 7.2 make narratives a first-class dated timeline with create/append/update/remove/restore and audit history (scheduled in MVP-PRIORITIES P2). Nothing specifies: whether the draft narrative becomes the first narrative entity (with its own UUID, author, timestamp) at CREATE_THING commit; whether a user can add a second dated narrative to a not-yet-synced draft offline (the schema forbids it — one string only — even though offline intake is the flagship scenario and Section 11's example shows multiple dated entries); or how thingEvent.Narrative (free text on events) relates to the narrative timeline — two narrative homes with no stated relationship. The narratives schema is acknowledged as to-be-added; the draft-to-canonical mapping is the unresolved question.

**Why it matters:** Narratives are the product's core asset ('The user tells the story'). If the commit mapping is ad hoc, the original intake story risks losing its identity, timestamp, and audit lineage — exactly what Governance 7.1 ('Narrative is durable source knowledge') forbids — and offline users cannot record follow-up observations before first sync.

**Suggested requirement:** Specify in the narrative contract: draftThing carries an ordered array of draft narrative entries (each with NarrativeUUID, text, CreatedAt) rather than a single string; CREATE_THING commits each entry as a first-class narrative preserving its client timestamp and UUID; event-attached Narrative text is defined as a rendering of, or reference to, a narrative entity rather than an independent copy.

<details>
<summary>Verification evidence</summary>

**Checked:** core.schema.json draftThing.Narrative (single string, max 20000) and thingEvent.Narrative; MVP Definition Section 11 (multi-entry dated timeline); Governance 7.2; MVP-PRIORITIES P0 contracts item 1 ('narratives' schema planned) and P2 item 1 (first-class narratives)

The narrative timeline requirements exist (MVP Section 11's dated multi-entry example, Governance 7.2's create/append/update/remove/restore with audit history) and a narratives schema is explicitly planned in MVP-PRIORITIES P0 contracts item 1. But no document defines the draft-to-canonical mapping: draftThing holds exactly one Narrative string, nothing specifies how it becomes a first-class narrative entity at CREATE_THING commit (identity, timestamp, lineage), whether multiple dated entries can be added to an unsynced draft offline, or how thingEvent.Narrative relates to the timeline. The planned schema is undefined X, so PARTIALLY_COVERED at best.

</details>

### 63. Label template contract: printJob references templates that have no contract, and the privacy/physical/reprint-history requirements are undefined

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `underspecified` · **Lenses:** Contracts/Architecture · **(acknowledged schema gap)**

batch.schema.json printJob requires LabelTemplateID and LabelTemplateVersion, but nothing defines the template object: the physical contract for the 1x4 inch label (margins, DPI, QR minimum module size, text overflow rules for long names), the required 'compact label option' (MVP Section 8), or which record fields a template may render. Governance 13 says 'Labels should not expose private information unless explicitly configured' — implying a per-template field allowlist with privacy classification that no document specifies. Section 8 also requires 'Label reprint history', but printJob is queue state, not a per-Thing history projection, and the version semantics of reprints (original vs current LabelTemplateVersion after a template update) are undefined. The labels schema is acknowledged as to-be-added; these design questions remain beyond that.

**Why it matters:** Labels are the physical anchor of the product for PCO; the P0 prototype capability and P1-slice item 7 both depend on this contract. The privacy allowlist matters because a label travels with a plant when sold — printing acquisition price or private notes on it would violate governance defaults.

**Suggested requirement:** Define the label-template schema: LabelTemplateID, version, physical dimensions and print profile (300dpi, margins, QR error-correction and minimum module size), an explicit renderable-field allowlist with privacy classification (private-by-default fields excluded unless tenant-configured), the default and compact orchid templates as seed data, reprint semantics (reprints pin the originally used template version unless the user opts into the current one), and reprint history derived from LABEL_PRINT_REQUESTED/CONFIRMED events.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES 'P0 - Complete contracts' item 1 (schemas for '...labels...'); Governance 13 (label content list; 'Labels should not expose private information unless explicitly configured'); MVP Definition Section 8 (default + compact label, reprint history); Section 21 (default label template setting); batch.schema.json printJob (LabelTemplateID/LabelTemplateVersion)

Real but partial coverage: a labels schema is explicitly planned (MVP-PRIORITIES P0 contracts item 1), Governance 13 enumerates what a label may include and states the private-information rule, Section 8 requires default and compact templates plus reprint history, and printJob already carries LabelTemplateID/LabelTemplateVersion. However 'add labels schema' is undefined X: no document specifies the template object's physical contract (dimensions/DPI/margins/overflow), a renderable-field allowlist with privacy classification, reprint version-pinning semantics, or how reprint history derives from print events. The design questions the candidate raises are unanswered.

</details>

### 64. LabelID locked to UUID format produces a dense ~69-character QR URL on a 1x4 inch label; ADR-001 only requires 'opaque'

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `underspecified` · **Lenses:** Contracts/Architecture

The MVP specifies the QR target https://orchid-enthusiasts.com/p/{LabelID}, and core.schema.json constrains LabelID to format: uuid (in thingIdentity, thing, draftThing, printJob). The resulting ~69-byte URL requires roughly a version 4-5 QR (33x37 modules); on a 1x4 inch label the QR square is at most ~0.8-0.9 inch, giving ~0.6 mm module pitch — printable, but denser than necessary for greenhouse conditions (glare, moisture, weathered labels) and older users with standard phone cameras, and it leaves less headroom for higher error-correction levels that tolerate damage. ADR-001 requires only an 'opaque permanent QR identity generated on the client'; the UUID constraint is a schema choice no document justifies, and no decision is recorded between UUID and a shorter opaque code (which would need a collision/uniqueness strategy since LabelID is client-generated offline).

**Why it matters:** The MVP success criterion is 'QR lookup works from the standard phone camera' for non-technical users. Once PCO prints its first permanent labels the encoded format is frozen for those labels; choosing the code length deliberately now avoids either scan-reliability complaints or a dual-format /p/ route later.

**Suggested requirement:** Record an explicit decision on LabelID wire format before the first production labels: either keep UUID and require rendering at a minimum QR module size and error-correction level validated by a physical scan test (weathered label, older phone), or define LabelID as a shorter opaque code (e.g. 10-12 char base32) with a documented client-generation entropy/collision-check-at-sync strategy, relaxing the schema from format: uuid accordingly.

<details>
<summary>Verification evidence</summary>

**Checked:** core.schema.json (LabelID $ref uuid in thingIdentity, thing, draftThing; batch.schema.json printJob); ADR-001 'Three-tier identity' ('LabelID: opaque permanent QR identity generated on the client'); MVP Definition QR URL https://orchid-enthusiasts.com/p/{LabelID}

The wire format is in fact specified — core.schema.json constrains LabelID to format: uuid in four places, and the MVP fixes the /p/{LabelID} URL — so implementations would not diverge. What is genuinely absent, as claimed: no document records or justifies the UUID-vs-shorter-code decision (ADR-001 requires only 'opaque'), and no requirement ties the resulting QR density to a minimum module size, error-correction level, or physical scan validation. The schema choice stands unexamined against the Section 24 phone-camera scan criterion; the decision-record and scan-validation requirement the candidate asks for do not exist.

</details>

### 65. Standard-user conflict-resolution UX is undefined

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `usability` · **Lenses:** NFR/Quality

The conflict mechanism is fully specified (ExpectedVersion in ADR-001's command flow; VERSION_CONFLICT in batch.schema.json; docs/CODE-REVIEW.md: 'Conflicts produce reviewable outcomes rather than last-write-wins replacement'), and MVP-PRIORITIES P1-Hardening item 5 names user-friendly conflict states — but no document defines what a nontechnical user actually sees or must do when their edit, or an offline draft syncing after someone else's change, hits a version conflict. Governance Section 6 assigns conflict resolution to power-user capabilities, yet conflicts will reach standard users (two PCO staff editing, offline sync races).

**Why it matters:** The pilot audience is explicitly older and nontechnical; an unhandled or jargon-laden dialog ('version mismatch') dead-ends the workflow. 'Reviewable outcomes' cannot be implemented or tested until the user-facing behavior is designed and specified.

**Suggested requirement:** On VERSION_CONFLICT, the PWA shows a plain-language comparison of 'Your change' vs 'Current record' per field, with actions Keep mine / Keep theirs / Keep both (append), never silently discarding either side; conflicted offline drafts enter a visible 'Needs review' list; the copy and flow are included in the pilot usability test.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP-PRIORITIES P1-Hardening item 5 ('user-friendly validation, conflict, retry, and error states in the PWA'); ADR-002 ('The UI must clearly distinguish successful, conflicted, failed, and pending items'); docs/CODE-REVIEW.md ('Conflicts produce reviewable outcomes rather than last-write-wins replacement'); Governance 10.2 and Section 6

The mechanism is fully specified (ADR-001 command flow, VERSION_CONFLICT in batch.schema.json), and several documents require user-friendly conflicted states: P1-Hardening item 5, ADR-002's batch UI requirement, and CODE-REVIEW's 'reviewable outcomes'. Governance 10.2 even provides a resolution-options pattern — but only for conflicting INFORMATION (two identifications), not concurrent-edit version conflicts. Genuinely missing: no document designs what a nontechnical standard user sees or does on VERSION_CONFLICT (comparison view, keep-mine/keep-theirs actions, needs-review list), and Governance Section 6 assigns 'Conflict resolution' to power-user capabilities, leaving the standard-user path a one-line unelaborated requirement.

</details>

### 66. Sale/transfer statuses exist but the listing/transfer journey and post-transfer QR behavior are missing

**Priority:** P1 · **Verdict:** Partially covered · **Area:** `workflow-contract-gap` · **Lenses:** Product/UX

The docs establish sale/transfer as real MVP-adjacent state: thingStatus includes FOR_SALE, RESERVED, TRANSFERRED; the MVP recommends a 'For Sale' collection (Section 5), a dashboard 'Orchids for Sale' count (Section 20), history actions LISTED_FOR_SALE and TRANSFERRED (Section 12), and AI-confirmation rules for listing and transfer (Section 23); Governance 8.5 mandates confirming recipient, transfer type, date, and price. But no screen, intake flow, or release-sequence entry delivers listing-for-sale or recording a transfer, and what a TRANSFERRED orchid's QR shows to the new possessor is undefined. (The companion contract gap — the thingEvent enum omitting these events — is covered by the event-vocabulary finding.)

**Why it matters:** PCO is a nursery — selling and transferring plants is its business, and the recommended starter data ('For Sale' collection, dashboard metric) puts these states in front of the Owner on day one with no way to use them correctly.

**Suggested requirement:** Either add a minimal 'Mark for sale / Record transfer' action to the Orchid detail screen in a named release (with the Governance 8.5 confirmed recipient/type/date/price capture and a defined post-transfer QR view for the new possessor), or explicitly document that FOR_SALE/RESERVED/TRANSFERRED statuses are display-only until a post-MVP transfer workflow ships.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Section 12 history flow ('What happened with this orchid?' → CCE proposes → user confirms) whose initial action list includes LISTED_FOR_SALE and TRANSFERRED, delivered by Release 4 'Maintenance history'; Section 23 (AI must confirm listing/transfer); Governance 8.5 (system must confirm recipient, transfer type, date, price/currency; 'A transferred Thing should remain in the historical record'); Section 3 Owner 'Transfer or archive orchids'; Section 8 (QR remains valid if 'Sold', 'Transferred'); Mobile QR section ('When the user is not authorized, the page displays only the permitted public or limited view'); Governance 14 ('A scan should not… move a Thing across tenants without an explicit transfer workflow').

More exists than the finding credits: the generic confirmed history-event flow (Section 12, shipped in Release 4) is a plausible delivery path for recording LISTED_FOR_SALE/TRANSFERRED, Governance 8.5 specifies the exact fields the system must confirm, and post-transfer QR behavior is generically defined (QR stays valid; a non-member possessor sees the permitted public/limited view). Real gaps remain: no dedicated 'Mark for sale / Record transfer' action or screen maps Governance 8.5's structured capture into any listed UI; the new possessor's experience beyond a generic public view (claiming/receiving the record) is undefined; and Governance 14 names a cross-tenant 'explicit transfer workflow' that no document defines.

</details>

## P2 — post-pilot, decide and record now

Low urgency, but each is currently neither in scope nor explicitly deferred; a one-line scope decision now prevents drift later.

| # | Finding | Area | Verdict |
|---:|---|---|---|
| 67 | [No reminder, task, or care-scheduling capability, and it is neither in scope nor deferred](#67-no-reminder-task-or-care-scheduling-capability-and-it-is-neither-in-scope-nor-deferred) | `care-scheduling` | Missing |
| 68 | [No units or measurement standard defined for orchid data](#68-no-units-or-measurement-standard-defined-for-orchid-data) | `data-contract` | Missing |
| 69 | [No minimum-age or children's-privacy requirement for public account creation](#69-no-minimum-age-or-childrens-privacy-requirement-for-public-account-creation) | `legal-compliance` | Missing |
| 70 | [Care guidance depends on location, but locations carry no growing-condition (temperature class/light/humidity) attributes](#70-care-guidance-depends-on-location-but-locations-carry-no-growing-condition-temperature-classlighthumidity-attributes) | `locations` | Missing |
| 71 | [First-run experience and empty states undefined for a brand-new tenant](#71-first-run-experience-and-empty-states-undefined-for-a-brand-new-tenant) | `onboarding` | Missing |
| 72 | [No availability target, on-call, or incident-response expectations for the running service](#72-no-availability-target-on-call-or-incident-response-expectations-for-the-running-service) | `reliability-slo` | Missing |
| 73 | [Orchid awards (AOS etc.) have no field and are not listed as deferred](#73-orchid-awards-aos-etc-have-no-field-and-are-not-listed-as-deferred) | `taxonomy` | Missing |
| 74 | [Flowering event vocabulary mismatch and bloom tracking under-modeled for enthusiasts](#74-flowering-event-vocabulary-mismatch-and-bloom-tracking-under-modeled-for-enthusiasts) | `lifecycle-events` | Partially covered |
| 75 | [Secrets management is detective-only: storage, rotation, and CI deploy identity are unspecified](#75-secrets-management-is-detective-only-storage-rotation-and-ci-deploy-identity-are-unspecified) | `secrets-management` | Partially covered |

### 67. No reminder, task, or care-scheduling capability, and it is neither in scope nor deferred

**Priority:** P2 · **Verdict:** Missing · **Area:** `care-scheduling` · **Lenses:** Orchid domain

The system records care actions after the fact (WATERED, FERTILIZED, REPOTTED events) and the dashboard's 'Orchids Needing Review' concerns record completeness, not care due. No document defines any reminder, task, due-date, watering/fertilizing schedule, or care-notification concept. The Out of Scope list defers 'Automated watering' and 'Environmental sensors' but says nothing about reminders, leaving proactive care assistance in an undecided state.

**Why it matters:** Enthusiasts and nurseries manage collections on cadences (water weekly, 'weekly weakly' feeding, repot every 1-2 years, seasonal rest). A tool that only logs past actions and never surfaces 'these plants are due' misses a primary reason growers keep records, and older users especially benefit from gentle reminders. Because it is neither promised nor deferred, users and developers lack a clear expectation.

**Suggested requirement:** Make an explicit decision: either add a lightweight per-plant or per-area care-schedule/reminder capability (next-water/next-fertilize/next-repot due dates surfaced on the dashboard, no automation) to a named release, or add 'care reminders and scheduling' to the Out of Scope list so the omission is deliberate.

<details>
<summary>Verification evidence</summary>

Grep for 'remind', 'schedule', 'due', 'task' returned no relevant matches. All care events (WATERED, FERTILIZED, REPOTTED in MVP Section 12 and core.schema.json) are recorded after the fact; Section 14 care guidance is on-demand Q&A that 'does not become history until the user confirms that the work was completed'. The dashboard's 'Orchids Needing Review' (Section 20) is undefined but nothing links it to care due dates. Section 25's Out of Scope defers 'Automated watering' and 'Environmental sensors' but never mentions reminders or scheduling, leaving proactive care assistance genuinely undecided — neither promised nor deferred.

</details>

### 68. No units or measurement standard defined for orchid data

**Priority:** P2 · **Verdict:** Missing · **Area:** `data-contract` · **Lenses:** Orchid domain

The only units in the docs are currency (USD), time zone (America/Denver), and the 1x4 inch label. No document defines a measurement/unit standard for flower size, plant height, pot/mount size, or temperature, nor a bark-grade vocabulary (Section 12's repotting example says 'medium bark' but nothing standardizes fine/medium/coarse). Care/repotting guidance and bloom recording both imply measurements with no declared units.

**Why it matters:** Measurements are ambiguous without a standard: AOS/award flower measurements are in centimeters, US growers think in inch pots and degrees Fahrenheit, and 'medium bark' means a specific grade. Mixed or undeclared units in guidance, repotting notes, and bloom records lead to wrong advice and unusable data, and undermine any future award or culture comparison.

**Suggested requirement:** Adopt a tenant unit setting (measurement system and temperature scale, defaulting to US customary / Fahrenheit for PCO) and store measurements with explicit units in structured fields (flower size in cm for award compatibility, pot size, temperature), plus a controlled medium/bark-grade vocabulary.

<details>
<summary>Verification evidence</summary>

The only units anywhere in the set are Default Currency USD and Default Time Zone America/Denver (MVP Section 3), the 1x4 inch label (multiple docs), pixel values (320-pixel layouts, ADR-002's 1600/800-pixel image profiles), and dollar amounts in examples. Grep for fahrenheit/celsius/centimeter/cm returned nothing. Section 12's repotting example uses 'medium bark' with no bark-grade vocabulary defined; no measurement standard exists for flower size, plant height, pot size, or temperature; and no tenant unit-system setting appears in Section 21's tenant settings list (name, privacy, currency, time zone, accession format, etc.).

</details>

### 69. No minimum-age or children's-privacy requirement for public account creation

**Priority:** P2 · **Verdict:** Missing · **Area:** `legal-compliance` · **Lenses:** Security/Privacy/Compliance

MVP Section 19 includes a public Create account screen and Section 24 makes unassisted account creation a success criterion, but no document sets a minimum age, an age-attestation step, or a COPPA/children's-data position — 'age', 'minor', and 'children' do not appear anywhere in the set.

**Why it matters:** orchid-enthusiasts.com is an open consumer site; without an age gate, a child registering and submitting voice/photos/narratives puts CCE in COPPA territory (verifiable parental consent obligations it has no machinery for). A 13+/16+ term plus lightweight attestation at sign-up eliminates the exposure at near-zero build cost, and the Terms of Service need the number decided.

**Suggested requirement:** State in the Terms of Service and enforce at sign-up that users must be at least 16 (or 13 with the platform not directed at children), with a checkbox/date-of-birth attestation on Create account and a documented takedown procedure for discovered under-age accounts.

<details>
<summary>Verification evidence</summary>

Grep for age/minor/children/COPPA/'Terms of Service' across all 12 documents returned zero matches. MVP Section 19 lists a public 'Create account' screen and Section 24 makes unassisted account creation the first step of the success workflow; Governance Section 11 covers privacy-by-design in depth (voice deletion, location protection, export, account deletion) but contains no age gate, attestation, or children's-data position. No Terms of Service or legal-compliance document exists in the set.

</details>

### 70. Care guidance depends on location, but locations carry no growing-condition (temperature class/light/humidity) attributes

**Priority:** P2 · **Verdict:** Missing · **Area:** `locations` · **Lenses:** Orchid domain · **(acknowledged schema gap)**

MVP Section 14 states care guidance 'uses ... Location' as an input, and locations include semantically meaningful areas ('Main Growing Area', 'Flowering Area', 'Quarantine Area'). But the location model is purely spatial (Space > Area > Rack > Shelf > Slot) with no environmental attributes — no temperature class (cool/intermediate/warm), light level, or humidity. The locations schema is acknowledged as to-be-added; this is the specific design question it must answer.

**Why it matters:** Orchid culture is defined primarily by temperature class and light. If guidance claims to use location but location holds no growing conditions, either the guidance silently ignores location (making the promise hollow) or it invents conditions. A grower who places a warm-grower in a cool area needs the system to reason about that; without per-location conditions, the 'uses location' claim is unbuildable.

**Suggested requirement:** When defining the locations schema, allow optional growing-condition attributes on Area (overridable at Rack/Shelf) — temperature class (COOL/INTERMEDIATE/WARM), approximate light level, humidity range — and require care guidance to state whether it used them and to flag mismatches (warm grower in a cool area) rather than assuming ideal conditions.

<details>
<summary>Verification evidence</summary>

MVP Section 14 lists 'Location' as a care-guidance input, but every location definition in the set is purely spatial: Governance 8.1 and MVP Section 4 define only Space/Area/Rack/Shelf/Slot with names like 'Main Growing Area' and 'Flowering Area'. No temperature class, light level, or humidity attribute appears anywhere (greps for cool/intermediate/warm classes, humidity, and light attributes on locations returned nothing). MVP-PRIORITIES P0-Contracts item 1 lists 'locations' among schemas to be added but defines no content — 'add X later without defining X'. The specific design question (environmental attributes enabling the Section 14 promise) is unanswered in all documents.

</details>

### 71. First-run experience and empty states undefined for a brand-new tenant

**Priority:** P2 · **Verdict:** Missing · **Area:** `onboarding` · **Lenses:** Product/UX

No document specifies what a newly provisioned Owner sees on first sign-in. The dashboard spec (Section 20) defines only populated-state metrics; Collections, Orchid list, Locations, and Search screens have no zero-data specification. Sections 4-5 'recommend' initial locations and collections without stating whether first-run guides the Owner to create them or they arrive pre-seeded. There is no first-run walkthrough, sample orchid, or guided 'add your first orchid' requirement, despite the 'without training' criterion (Section 24) and Governance 16's mandate for limited choices and plain-language guidance.

**Why it matters:** The intake journey the MVP is designed to prove starts from an empty dashboard; if that moment reads as a blank database rather than the 'simple orchid assistant' the docs promise, the older-collector persona stalls at step zero. Empty states are also where the 'Add Orchid' primary action must be discoverable, and nothing requires that.

**Suggested requirement:** Add an empty-state requirement: every list screen and the dashboard define a zero-data view with one plain-language sentence and a single primary action (dashboard empty state leads directly to 'Add your first orchid'); locations/collections empty states offer one-tap creation of the recommended starter set; acceptance review walks the full success-criteria journey from a freshly provisioned empty tenant.

<details>
<summary>Verification evidence</summary>

Searched MVP Sections 4-5 (locations/collections), 19 (screens), 20 (dashboard), 24, 26 Release 1, and Governance 16. Sections 4-5 only 'recommend' initial PCO locations and collections without stating whether they are pre-seeded or whether first-run guides the Owner to create them; Section 20 defines dashboard metrics solely in populated form; the Section 19 screen list has no zero-data specification; Governance 16 says to avoid 'Long mandatory setup' but defines no first-run behavior. No walkthrough, sample record, empty-state, or 'add your first orchid' requirement exists anywhere ('empty', 'first-run', 'onboard', 'walkthrough' greps returned nothing relevant).

</details>

### 72. No availability target, on-call, or incident-response expectations for the running service

**Priority:** P2 · **Verdict:** Missing · **Area:** `reliability-slo` · **Lenses:** Operations/Launch, NFR/Quality

No document states any availability or latency objective for the public QR-lookup route, sign-in, or the trusted command functions; no incident-response ownership; no maintenance-window or status-communication policy; no pilot availability target. MVP-PRIORITIES P1 Hardening adds Cloud Monitoring alerts (themselves undefined — separate finding) but never says who responds to them or how fast, and neither ADR mentions service levels.

**Why it matters:** Printed QR labels are scanned at physical pots during PCO's working hours — the QR route is effectively nursery infrastructure. Even a lightweight pilot needs a written 'who fixes it, how fast' so an outage during PCO's business day (America/Denver) is not discovered days later, and so 'the pilot went badly' can be separated from 'the service was down'.

**Suggested requirement:** Adopt pilot-grade service expectations: QR lookup and sign-in target 99.5% monthly availability; a named responder acknowledges production alerts within 4 business hours (America/Denver); incidents affecting data integrity or availability get a brief written postmortem with corrective actions.

<details>
<summary>Verification evidence</summary>

Grep for availability/SLO/SLA/uptime/on-call/incident returned zero real matches (only substring noise like 'unavailable' in offline-action wording and 'translating'). The sole operational-response artifact is MVP-PRIORITIES P1-Hardening item 6: 'Configure Firestore backups, backup-restore verification, and Cloud Monitoring alerts' — infrastructure with no stated alert definitions, no responder, no response-time expectation, no availability or latency objective for QR lookup, sign-in, or trusted commands, and no maintenance-window, status-communication, or postmortem policy in any document including both ADRs' Consequences sections.

</details>

### 73. Orchid awards (AOS etc.) have no field and are not listed as deferred

**Priority:** P2 · **Verdict:** Missing · **Area:** `taxonomy` · **Lenses:** Orchid domain

No document provides any award concept. Governance 4.1 enumerates the orchid-specific additions (grex, clone, parentage, flowering, culture) with no awards; the orchid template field set is undefined; and the Out of Scope list (Section 25) defers formal registration verification and appraisals but never mentions awards — so awards are neither modeled nor explicitly deferred.

**Why it matters:** Awards are central to orchid identity, labeling, and value: an awarded clone's name conventionally includes the award (e.g. Cymbidium Golden Elf 'Sundust' AM/AOS), award type/points affect market price, and a nursery selling divisions of an awarded clone must display and preserve the award. Silently unmodeled awards mean the display name/label and For-Sale presentation cannot represent a plant's most value-relevant credential, with no conscious scope decision made.

**Suggested requirement:** Make an explicit scope decision: either add an optional structured award record to the orchid template (awarding body, award type/abbreviation, points, awarded clone, date) that can append to the display name and label and be excluded from private views, or add 'formal award tracking' to the Out of Scope list so the omission is deliberate and documented.

<details>
<summary>Verification evidence</summary>

Grep for 'award' across all 12 documents returned zero matches. Governance 4.1 enumerates orchid template additions as 'grex, clone, parentage, flowering, and culture' — no awards. MVP Section 25's Out of Scope list defers 'Formal orchid registration verification' and 'Formal appraisals', which are distinct concepts (RHS registration and valuation, not AOS/judging awards), and never mentions award tracking. The generic shared capability 'Evaluation' (Governance 4.1) is condition/assessment-oriented and nowhere defined to include awards. Awards are neither modeled nor explicitly deferred.

</details>

### 74. Flowering event vocabulary mismatch and bloom tracking under-modeled for enthusiasts

**Priority:** P2 · **Verdict:** Partially covered · **Area:** `lifecycle-events` · **Lenses:** Orchid domain

MVP Section 12 lists a single FLOWERED history action while core.schema.json defines paired BLOOM_STARTED/BLOOM_ENDED — the product doc and contract disagree on the flowering model (the reconciliation belongs with the event-vocabulary finding). Beyond that, neither defines any bloom detail structure: spike count, flower count per spike, flower size, fragrance, first-ever-bloom milestone, rebloom, inflorescence type — StructuredDetails on thingEvent is untyped with no bloom schema.

**Why it matters:** Bloom history is the payoff data orchid collectors care about most: first flowering of a seedling is a milestone, spike/flower counts and flower size feed award eligibility (AOS judging measures flowers in cm), and bloom timing/rebloom drives culture decisions. Without a bloom detail model, the 'Tell me about this orchid' flowering summary and any seasonal guidance cannot be accurate, and inconsistent FLOWERED-vs-paired-events history breaks duration reporting.

**Suggested requirement:** Reconcile to one event model (recommend BLOOM_STARTED/BLOOM_ENDED to capture duration) and update MVP Section 12; define a bloom StructuredDetails sub-schema capturing spikeCount, flowerCount, approximate flower size with unit, fragrance flag, firstBloom flag, and inflorescence type, so bloom milestones are queryable and support later award context.

<details>
<summary>Verification evidence</summary>

**Checked:** MVP Definition Section 12 (history action 'FLOWERED') vs core.schema.json thingEvent.EventType ('BLOOM_STARTED', 'BLOOM_ENDED'); Governance 4.1 ('Orchids add grex, clone, parentage, flowering, and culture')

Conflict CONFIRMED: MVP Section 12's initial history actions list contains 'FLOWERED' while core.schema.json's EventType enum contains 'BLOOM_STARTED' and 'BLOOM_ENDED' and no FLOWERED value — the product doc and contract genuinely disagree on the flowering event model. Flowering is otherwise acknowledged (Governance 4.1 names flowering as an orchid template addition; Governance 11.3 mentions 'Public flowering history'; a narrative example mentions 'two flower spikes'), so bloom tracking is partially addressed. Genuinely missing: no bloom detail structure anywhere — StructuredDetails is untyped ('type': 'object') with no spike count, flower count, flower size, fragrance, first-bloom, or inflorescence fields, and no document defines one.

</details>

### 75. Secrets management is detective-only: storage, rotation, and CI deploy identity are unspecified

**Priority:** P2 · **Verdict:** Partially covered · **Area:** `secrets-management` · **Lenses:** Security/Privacy/Compliance

AGENTS.md forbids committing credentials and requires secret scanning; README step 8 and MVP-PRIORITIES P0 add scanning to CI. That is entirely detective. No document states where runtime and CI secrets must live (Google Secret Manager vs CI-provider secrets), whether CI deploys to Firebase must use keyless OIDC/Workload Identity Federation instead of long-lived service-account keys, any key-rotation expectation, or least-privilege scoping for the deploy identity.

**Why it matters:** The imminent scaffold step creates CI that can deploy Hosting, Functions, and Rules to production — a leaked long-lived deploy key equals full tenant data compromise and malicious Rules deployment. Choosing WIF/OIDC and Secret Manager at scaffold time is nearly free; converting later, after keys proliferate, is not.

**Suggested requirement:** Add to the scaffold requirements: CI deploys authenticate via Workload Identity Federation (no exported service-account keys); any unavoidable secrets live in Google Secret Manager or the CI provider's secret store with least-privilege IAM per environment; deploy identity cannot read tenant data buckets/collections; rotation on personnel change is documented.

<details>
<summary>Verification evidence</summary>

**Checked:** AGENTS.md Repository constraints ('Do not commit credentials, service-account files, `.env` secrets...') and Required validation ('Secret scanning'); README Next-step 8 and MVP-PRIORITIES P0 items adding secret scanning to CI; ADR-003 Migration rule 5 ('Do not migrate secrets')

The docs do address secret hygiene: committing credentials and service-account files is prohibited (AGENTS.md), secret scanning is on every required-validation list and in the CI scaffold plan (README step 8, MVP-PRIORITIES P0-Contracts item 6), and ADR-003 forbids migrating secrets. Genuinely missing — confirmed by grep for 'Secret Manager', 'OIDC', 'Workload Identity', 'rotation': no document states where runtime/CI secrets must live, whether CI deploys use keyless WIF/OIDC versus long-lived service-account keys, any rotation expectation, or least-privilege scoping for the deploy identity, even though MVP-PRIORITIES P0 item 10 has CI-adjacent work deploying Hosting/Rules.

</details>

---

*Produced by a six-lens documentation review with adversarial verification of every finding against the source documents. See each finding's "Verification evidence" for the exact passages checked.*
