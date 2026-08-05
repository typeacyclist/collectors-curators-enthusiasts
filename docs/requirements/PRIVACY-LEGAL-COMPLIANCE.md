# Privacy, Legal, and Compliance Requirements

> Resolves gap-analysis findings 4, 19, 25, 26, 28, 36, 40, 46, 47, 69
> (see `docs/MVP-REQUIREMENTS-GAP-ANALYSIS-2026-08-05.md`). Extends, and is
> subordinate to, Governance Section 11 (Privacy by design).

## 1. Legal surface (findings 4, 69)

- **Terms of Service** and **Privacy Policy** are P0 public pages (now in the MVP screens list), linked from the home page, account creation, and every public/shared page footer. Account creation requires affirmative acceptance; material changes require re-acceptance.
- The Privacy Policy must accurately describe: what is collected (accounts, narratives, photos, transcripts, telemetry per Section 6), AI processing (Vertex AI, Section 3), sharing behavior, retention and deletion (Section 4), and the contact route for privacy requests.
- **Minimum age 18.** The pilot serves adult collectors; the ToS states the platform is not directed to children and accounts require being 18 or older. No parental-consent flows are built; this removes COPPA/GDPR-child-consent scope from the MVP. Revisit if a future audience decision changes this.
- Legal text is drafted with counsel before public launch; engineering treats the two pages and the acceptance gate as the requirement.

## 2. Photo metadata (finding 19)

All EXIF metadata — including GPS coordinates, capture device identifiers, and embedded thumbnails — is stripped from every derivative at processing time and from **any image served on a shared, platform, or public surface**. The retained private original keeps its metadata under tenant policy. Acceptance test: download every image variant reachable from a public share and verify zero location metadata. (Also recorded in AGENTS.md Media rules.)

## 3. AI data governance (finding 26)

- Tenant content sent to AI flows is processed only through Vertex AI with Google Cloud's default **no-training** data-usage terms; any AI vendor or product whose terms permit training on customer data is prohibited.
- AI processing region is pinned to the project region (US for the pilot); tenant content does not leave the configured region for AI processing.
- AI request/response logs used for debugging or evaluation are tenant-scoped, retained at most 90 days, excluded from backups' long-term retention, and deleted on tenant deletion.
- Golden-set evaluation data derived from real tenant content requires tenant consent (PCO pilot agreement covers this) and is scrubbed of personal names/contacts before storage.

## 4. Deletion and retention (findings 46, 47)

- **Account deletion:** a signed-in user requests deletion in Account settings; a 30-day grace period allows cancellation; then the auth account and personal data are removed. If the user is a tenant's sole Owner, deletion requires first transferring or deleting the tenant.
- **Tenant deletion:** requested by the Owner, executed by a platform administrator through an audited script after written confirmation; removes Firestore documents, Storage originals and derivatives, AI logs, and export artifacts for the tenant.
- **Propagation:** deletion covers primary data immediately, error-report payloads by identifier scrubbing, and backups by aging out of the 35-day backup window; the requester is told this timeline.
- **Append-only history vs privacy (finding 47):** lifecycle events may embed personal data in free text. A `REDACT_EVENT` command (Owner-only, typed confirmation) replaces the free-text content of a specific event with a tombstone via a superseding `REDACTED` event, preserving event structure, type, and timestamps while removing the content. Redaction is reserved for privacy/legal need, is itself audited, and is the mechanism used when a data-subject request targets narrative history.
- Voice audio: already governed (deleted after transcription); the deletion pipeline must be verifiable in logs.

## 5. Public surface protection (findings 25, 28, 40)

- **Public QR route abuse (40):** LabelIDs are unguessable (opaque, high-entropy — enumeration infeasible); the public route is rate-limited per IP at the edge, served cache-friendly for valid public views, and returns the identical generic page for private, pending, and nonexistent labels (per MVP Definition scan states). App Check protects authenticated APIs; the public route relies on rate limiting + non-enumerability since App Check cannot gate anonymous camera-app opens.
- **SHARED_LINK semantics (25):** a shared link is a **separate revocable grant**, not the QR URL. Enabling SHARED_LINK mints a distinct high-entropy share token routing to `/s/{ShareToken}`; revoking it invalidates that token without affecting the permanent `/p/{LabelID}` QR route, whose visibility is always governed by the orchid's current sharing level. Re-enabling mints a new token. The QR printed on a physical label therefore never becomes a secret bearer credential.
- **Content moderation (28):** every public or platform-shared page shows a "Report" action (no sign-in required) reaching the platform team; the platform administrator can unpublish any shared page pending review; a designated copyright/abuse contact address is published in the ToS; takedown requests are acknowledged within 2 business days during the pilot. Full DMCA agent registration is evaluated before opening sharing beyond the pilot tenant.

## 6. Telemetry policy (finding 36)

- Product telemetry is **first-party, minimal, and content-free**: workflow events (screen, action, duration, success/failure, counts) with no narrative text, no photo data, no orchid names, and no third-party advertising or cross-site trackers.
- Telemetry is keyed by anonymous per-install id plus tenant id (needed for pilot metrics); the Privacy Policy discloses it; a tenant-level opt-out is honored except for security and billing-relevant events.
- Aggregated metrics (the `MEASUREMENT-ACCEPTANCE-NFR.md` set) may be shared with the pilot tenant; raw event streams are internal, retained 12 months.
