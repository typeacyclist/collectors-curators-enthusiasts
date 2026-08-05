# Operations and Launch Readiness Requirements

> Resolves gap-analysis findings 2, 3, 8, 32, 33, 35, 38, 44, 48, 52, 58, 72, 75
> (see `docs/MVP-REQUIREMENTS-GAP-ANALYSIS-2026-08-05.md`).

## 1. Environments (finding 3)

Two separate Firebase projects: **stage**, **prod**. *(Reduced from three on 2026-08-06 — an MVP scope decision; a dedicated dev project can be added post-pilot if emulator-based development proves insufficient.)*

- Local development uses the Firebase Emulator Suite exclusively; no dev cloud project exists. Anything the emulators cannot exercise (App Check, Vertex AI, real device QA) is developed and verified against **stage**.
- Stage mirrors prod configuration (Rules, App Check, functions regions) and hosts pre-release validation, bootstrap rehearsal, device QA, and scale testing. Stage data is disposable.
- Prod contains only real tenant data; no test data, no console experimentation.
- Vertex AI, Storage, and Firestore regions are pinned per project and identical across stage and prod (`us-central1` unless the privacy doc's residency requirement dictates otherwise).

## 2. Deployment pipeline and rollback (finding 2)

- All deploys run from CI (GitHub Actions), never from developer machines.
- Pipeline: checks (types, tests, schema validation, Rules tests, secret scan) → deploy to staging → smoke test → manual approval → deploy to prod.
- Deployable units: Hosting (PWA), Functions, Firestore Rules/indexes, Storage Rules. Each deploy records the git SHA.
- **Rollback:** Hosting uses Firebase Hosting release rollback; Functions/Rules roll back by redeploying the previous tagged SHA through the same pipeline. Rollback must be exercised once in staging before launch.
- Schema/contract changes deploy before the code that depends on them; Firestore index changes deploy before queries that need them.

## 3. Production bootstrap (finding 8)

A scripted, idempotent, audited bootstrap procedure — an Admin SDK script executed by a platform administrator through CI (not an ad-hoc console session) — creates, in order:

1. The platform-administrator custom claim on the named staff account.
2. The PCO tenant document with settings from MVP Definition Section 3 (name, short name PCO, type, default privacy Private, currency USD, time zone America/Denver, accession format `PCO-{YEAR}-{SEQUENCE}`).
3. The Owner membership bound to the real PCO Owner's verified Firebase Auth account.
4. The recommended locations (Section 4) and collections (Section 5).
5. The accession sequence initialized at zero for the current year.
6. Standard lifecycle events for every created entity, attributed to the bootstrap actor.

Rules:

- Idempotent: re-running detects existing state and makes no duplicate writes.
- Rehearsed in staging before every production run.
- Direct console mutation of canonical documents is prohibited in all environments; the bootstrap script and trusted commands are the only production write paths.

## 4. Transactional email (finding 35)

A transactional email capability is MVP infrastructure, required by password reset, email verification, and invitations:

- Firebase Authentication emails (verification, reset) are configured to send from a verified `orchid-enthusiasts.com` sending domain.
- Invitation and notification email uses one designated transactional provider (e.g. Postmark or SendGrid — selection recorded here when made) with SPF, DKIM, and DMARC configured before launch.
- Email content contains no private record data beyond what the recipient is entitled to see.

## 5. Error and crash reporting (finding 32)

- The PWA reports unhandled exceptions, failed sync operations, and command failures to an error-reporting service (Sentry or equivalent), tagged with app version and anonymous session id.
- Reports are scrubbed client-side: no narrative text, photo data, or personal information in error payloads; record identifiers (UUIDs) are permitted.
- Functions log structured errors to Cloud Logging with `ClientOperationID` correlation.

## 6. Monitoring and alerting (finding 52)

Cloud Monitoring alerts, delivered to the on-call email/channel, at minimum:

| Signal | Threshold (initial) |
|---|---|
| Callable function error rate | >5% over 15 min |
| Function p95 latency | >5 s over 15 min |
| Firestore Security Rules denial spike | >10× baseline over 1 h |
| Hosting uptime check (public QR route) | 2 consecutive failures |
| Daily backup job | any failure |
| Billing budget | 50% / 90% / 100% of monthly budget |
| Vertex AI request volume | >2× trailing 7-day average |

Thresholds are configuration, tuned during the pilot; removing an alert requires recording why here.

## 7. Backups and recovery (finding 58)

- **Firestore:** point-in-time recovery enabled, plus daily scheduled export to a locked Cloud Storage bucket; export retention 35 days.
- **Cloud Storage media:** object versioning with 30-day retention of prior/deleted versions; originals bucket included in disaster-recovery scope.
- **Targets:** RPO 24 hours, RTO 8 hours for the pilot.
- **Restore verification:** a documented restore test into staging runs before launch and monthly thereafter; the test restores both Firestore and a media sample and verifies tenant isolation of the restored data.
- Backup retention interacts with deletion rights per `PRIVACY-LEGAL-COMPLIANCE.md` (deleted data ages out of backups within the 35-day window).

## 8. AI model operations (finding 44)

- Vertex AI model versions are pinned per environment; proposals already record model/prompt/schema versions (core contract).
- A model or prompt change is a reviewed change: PR updating the pinned version/prompt, golden-set evaluation rerun (thresholds in `MEASUREMENT-ACCEPTANCE-NFR.md`) passing before deploy, staging soak before prod.
- Prompts are versioned files in the repository, never inline literals.

## 9. Domain continuity (finding 48)

`orchid-enthusiasts.com` is permanent infrastructure — every printed QR depends on it. Registrar auto-renew enabled with a monitored payment method; domain and DNS ownership documented under platform (not personal) accounts; expiry monitoring at 60 days; the domain never changes for printed-label routes, and any future domain migration must preserve `/p/{LabelID}` via permanent redirects.

## 10. Support and feedback (finding 38)

- In-app Help entry (tenant dashboard and public pages) linking to a getting-started guide and a support email address monitored by the platform team; pilot response expectation next business day.
- A lightweight in-app feedback form (free text + optional screenshot) available to pilot users; submissions land with the platform team and are triaged weekly with PCO.

## 11. Service-level expectations (finding 72)

Pilot targets, published to PCO: 99.5% availability for the authenticated application and the public QR route measured monthly; planned maintenance announced in advance; support per Section 10; no 24/7 on-call during the pilot (alerts route to business-hours on-call). These are pilot expectations, not contractual SLAs; commercialization revisits them.

## 12. Secrets management (finding 75)

- CI deploys authenticate via Workload Identity Federation (no long-lived service-account keys in GitHub).
- Runtime secrets (email provider key, error-reporting DSN) live in Secret Manager / Functions secret config; never in code, `.env` files, or Hosting assets.
- Secret scanning (already mandated) remains the detective control; any exposed credential is rotated immediately and the exposure recorded per the incident-response requirement.

## 13. Incident response (finding 33)

- A short runbook (kept with this doc) defines severity levels, the responder, and communication steps for: production outage, data-loss event, security breach, and abuse/takedown.
- Suspected personal-data breach: contain, assess scope, and notify affected tenant owners without undue delay — within 72 hours of confirmation — including what data was involved and remediation.
- Every incident gets a written post-incident note (cause, impact, fixes) shared with the pilot tenant when they were affected.
