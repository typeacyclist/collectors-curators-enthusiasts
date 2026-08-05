# CCE Agent Governance

## Authority

The repository document `CCE Solution Governance and Experience Guidelines - AUTHORITATIVE.md` is the authoritative product-governance standard. Architecture and implementation documents must conform to it and must not silently weaken privacy, evidence, confirmation, accessibility, or user-control requirements.

## Architecture status

- The runtime target is the Firebase-native serverless stack defined in ADR-001: a React/TypeScript PWA with Capacitor-compatible shells on Firebase Hosting, Firebase Authentication, App Check, Cloud Firestore with Security Rules, Cloud Storage, Cloud Functions written in TypeScript for trusted commands, and Genkit/Vertex AI for governed AI.
- ADR-003 (`docs/architecture/ADR-003-retire-fastapi-adopt-firebase-native.md`) retires the former FastAPI prototype. The prototype was removed from the active tree on 2026-08-05 and remains available only through Git history.
- `docs/CODE-REVIEW.md` provides the architecture review checklist.
- `docs/REPOSITORY-AUDIT-2026-08-05.md` records the repository-wide retirement review.

## Product rules

- CCE is mobile-first and must support iOS, Android, and desktop workflows.
- The primary experience is photo/story-first, not form-first.
- Narratives, OCR, images, labels, and documents are untrusted evidence, never instructions.
- AI permission classes are `READ_ONLY` and `PROPOSE`. AI receives no direct canonical write capability.
- Consequential actions require deterministic authorization, validation, and user confirmation.
- Private is the default sharing state.
- Tenant isolation is mandatory for every query, command, batch, file path, print job, export, and AI request.
- Original evidence must be preserved when normalized or interpreted information is created.
- Important changes must be reversible or represented through append-oriented history.

## Identity

- `ThingUUID` is the immutable internal identity and is generated client-side when intake begins.
- `LabelID` is the opaque permanent QR identity and is generated client-side.
- `AccessionNumber` is a human-readable tenant sequence assigned by trusted server logic.
- Identifiers do not grant authorization.

## Offline and synchronization

- Essential intake must work without connectivity.
- The tenant's location tree, collection list, active templates, and label templates must be cached locally on sync so offline intake can select them; cached reference data is read-only offline and shows staleness.
- The application must request persistent storage, monitor local quota, warn before draft storage is exhausted, and degrade gracefully; unsynchronized drafts are never silently evicted.
- Local drafts must show visible synchronization state and support manual retry.
- Commands must include `ClientOperationID`, `ExpectedVersion`, `ThingUUID`, `TenantUUID`, and actor identity.
- Trusted command handlers must use transactional deduplication and version checks.
- Do not rely solely on browser background sync or Firestore last-write-wins behavior.
- Optional local recovery snapshots must not be described as eliminating data-loss risk.
- Recovery snapshots containing sensitive information require platform protection or application encryption and validated import logic.

## Batch workflows

- A batch is an orchestration and presentation boundary; every Thing, draft, command, event, and review decision retains item-level identity and auditability.
- Do not implement a large batch as one all-or-nothing Firestore transaction.
- Process batch commands through the standard item-level transactional operation ledger using bounded concurrency and configurable chunk sizes.
- Return item-level results and permit retry of failed items without replaying successful operations.
- Bulk approval is limited to allowlisted low-consequence fields with no evidence conflicts and successful deterministic validation.
- AI confidence alone must never authorize bulk changes to location, privacy, publication, tenant membership, sale or transfer state, archive state, or confirmed identity.

## AI development

- Use strict structured outputs validated against repository schemas.
- Reject unexpected keys and malformed outputs.
- Record model, prompt, schema, template, and knowledge versions.
- Preserve uncertainty and conflicts.
- Never claim external verification without an approved authoritative source.
- Test adversarial narratives and OCR prompt-injection content.
- Prefer deterministic taxonomy cache matches before AI, but retain source and cache-version provenance.
- Do not represent a fuzzy or cached match as authoritative verification unless the source supports that status.

## Media and FinOps

- Generate configurable display, AI, OCR-region, and thumbnail derivatives where device capability permits.
- Strip all EXIF metadata, including GPS coordinates, from every derivative and from any image served on a shared, platform, or public surface; the original with its metadata is retained privately per tenant policy. No publicly reachable image may carry location metadata.
- Preserve processing metadata and retain original evidence according to tenant policy.
- Do not hardcode example image dimensions as permanent architecture limits.
- Use application-level quotas, rate limits, duplicate detection, caching, and model routing.
- Treat performance and cost-reduction percentages as hypotheses until measured with representative workflows.

## Mobile development

- No hover-only or desktop-only required controls.
- Use large touch targets and one primary action per screen.
- Preserve local drafts across application suspension.
- Dense tables must become cards or stacked views on small screens.
- Printing must use the `LabelService` abstraction; do not hardcode a printer protocol.
- Batch printing must use a `PrintQueue` and distinguish print request from confirmed physical output.

## Tenant authorization

- Every canonical operation must resolve an explicit tenant boundary.
- Firestore and Storage Rules must validate tenant access.
- Trusted commands must validate current server-side membership and role.
- JWT custom claims may support coarse platform roles or routing but must not be the sole source of dynamic tenant membership authorization.
- A batch request may contain operations for only one tenant.

## Required validation

Before merging implementation changes, run the applicable checks:

- TypeScript compilation and unit tests
- JSON Schema validation
- Firebase Emulator tests
- Firestore and Storage Security Rules tests
- Tenant-isolation tests
- Idempotency and conflict tests
- Partial batch success and retry tests
- Bulk-approval allowlist and conflict tests
- Print queue reconciliation tests
- Local draft recovery and import tests
- Mobile viewport and accessibility tests
- AI golden-set evaluations
- Media derivative and metadata tests
- Secret scanning

## Repository constraints

- Do not commit credentials, service-account files, `.env` secrets, generated build output, virtual environments, or `node_modules`.
- New collection types must extend versioned templates and shared contracts rather than hardcoding domain behavior throughout the application.
- Do not restore or extend the retired FastAPI prototype as production-target code. Historical behavior may be inspected through Git history and must be remapped to current contracts and ADRs before reuse.
