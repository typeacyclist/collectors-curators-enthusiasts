# Measurement, Acceptance, and Non-Functional Requirements

> Resolves gap-analysis findings 7, 14, 15, 27, 39, 41, 42, 45, 50, 54, 57, 65
> (see `docs/MVP-REQUIREMENTS-GAP-ANALYSIS-2026-08-05.md`).

## 1. Success-metric instrumentation (finding 15)

Every MVP Definition Section 24 target and ADR-002 FinOps metric maps to a first-party telemetry event (privacy rules in `PRIVACY-LEGAL-COMPLIANCE.md`):

| Target / metric | Instrument |
|---|---|
| Basic record under two minutes | intake_started → thing_committed duration, per session |
| Creation works on a phone | platform/form-factor tag on intake events |
| Optional questions skippable | prompt_shown / prompt_skipped counts |
| QR lookup from camera | public QR route hits with referrer class; scan_to_record_opened duration |
| Labels print accurately | print_requested / print_confirmed counts (PrintQueue events) |
| AI distinguishes statement vs inference | golden-set evaluation (Section 5), not runtime telemetry |
| ADR-002 FinOps set (capture time, review time, AI calls per Thing, function invocations, bytes per profile, AI cost per accepted proposal, cache hit rate, label jobs per interaction, retry/conflict rate) | dedicated counters emitted by the client and functions, aggregated per tenant per week |

A pilot metrics dashboard (even a scheduled export to a spreadsheet) exists before Release 2 so baselines accumulate from first use.

## 2. Performance budgets (finding 7)

Measured on a mid-range Android phone over 4G (the greenhouse reality), p95:

| Interaction | Budget |
|---|---|
| Cold load to interactive dashboard | ≤ 4 s |
| Warm navigation between screens | ≤ 1 s |
| QR scan → record visible (online) | ≤ 2 s after resolve |
| Save draft locally (offline) | ≤ 500 ms perceived |
| Search results (tenant of Section 3 scale) | ≤ 1 s |
| Label PDF generation (single label) | ≤ 3 s |
| AI intake summary | ≤ 10 s with visible progress; skippable at any time |

Budgets are release criteria for the feature that owns them; regressions block release until re-accepted here.

## 3. Scale envelope (finding 27)

The MVP is designed and tested for, per tenant: **5,000 orchids, 25,000 photos, 100 locations, 10 collections, 10 members, 5 concurrent active users**; PCO's expected initial load (hundreds of orchids) sits well inside it. List views, dashboards, search, and batch flows must be exercised at envelope scale in staging with generated data before launch. Exceeding the envelope is a post-pilot scaling task, not silent degradation: approaching limits surfaces a warning to the platform team.

## 4. FinOps guardrails (finding 14)

- Monthly GCP budget for the pilot project: **$100 provisional** (billing alerts at 50/90/100%; the number is a recorded starting point, adjustable by the product owner — revisit after the first month's measured baseline).
- Per-service quota ceilings set in the project: Vertex AI requests/day, Functions invocations/day, Storage egress/day, sized ~5× expected pilot load; hitting a ceiling alerts rather than silently failing user flows where possible (AI degrades to "process later", per Section 8).
- Application-level limits (already required by ADR-001/002): per-tenant AI call quotas and media limits get concrete initial values in tenant settings defaults: 200 AI calls/day, 500 photo uploads/day per tenant for the pilot.

## 5. AI golden-set evaluation (finding 42)

- **Owner:** product owner (with PCO consent per the privacy doc).
- **Contents:** ≥ 50 real-style intake narratives (including PCO-donated examples), ≥ 15 label/tag photos for OCR, ≥ 10 adversarial cases (prompt-injection narratives and OCR text per ADR-001), ≥ 10 conflict cases (label vs narrative disagreement).
- **Thresholds to pass a model/prompt/schema change:** ≥ 90% correct field extraction on unambiguous statements; zero fabricated "verified" identifications; zero injection cases that alter behavior or output schema; 100% of conflict cases preserve both values and surface the conflict; uncertainty wording preserved in ≥ 95% of uncertain cases.
- Evaluation runs in CI against the pinned model; results are stored with the run SHA. This is the merge gate AGENTS.md already mandates.

## 6. Usability protocol for "without training" (finding 39)

The Section 24 criterion is measured by a moderated usability test before pilot acceptance:

- 5 participants who have never seen the product, including at least 2 aged 60+, at least 3 on their own phones.
- Each attempts the Section 24 workflow (create account → add orchid with photo and story → review AI summary → save → print label → scan → "Tell me about this orchid" → record an event) with no instruction beyond the product's own UI.
- **Pass:** ≥ 4 of 5 complete the workflow unaided (facilitator answers no product questions); every blocker found is fixed or explicitly accepted before launch.

## 7. Accessibility (finding 41)

- Standard: **WCAG 2.1 AA** for all MVP screens.
- Verification: automated axe scan in CI on key screens; manual screen-reader smoke test (VoiceOver on iOS, TalkBack on Android) of the intake, scan, and detail flows each release; 200% text-size and portrait/landscape checks on the device matrix.
- The governance doc's qualitative rules (large text, contrast, no hover-only controls) remain binding; this section defines how they are tested.

## 8. AI latency and unavailability (finding 57)

Interactive intake never blocks on AI: capture and save always complete locally regardless of AI state. If the AI summary exceeds its 10 s budget or Vertex AI is unavailable, the draft saves with state `WAITING_FOR_AI`/`AI_REVIEW_REQUIRED` and the user may finish; the summary arrives asynchronously for later review. AI failures are invisible data-entry-wise: no user retypes anything because AI was down.

## 9. Device and browser matrix (finding 45)

- **Support floor:** iOS 16+ Safari; Android 10+ with current Chrome; latest two major desktop versions of Chrome, Safari, Edge, Firefox.
- **Physical-device QA set (the "physical-device QA" named in MVP-PRIORITIES):** one recent iPhone (iOS current), one iPhone at the support floor, one mid-range Android (e.g. Samsung A-series) at Android 10-12, one current Android flagship, one iPad. Camera capture, QR scan, offline intake, and print/share must pass on each.
- Known iOS PWA storage-eviction behavior is covered by the offline quota requirements (MVP Definition connectivity section).

## 10. Conflict-resolution UX (finding 65)

When a trusted command returns `VERSION_CONFLICT` to a standard user:

- The app reloads the current record and shows a plain-language screen: "This orchid was changed while you were editing," listing the user's pending change against the current value, per field.
- Choices per field: **Keep mine** (reapply on the new version) or **Keep theirs** (discard mine). For narratives, both are always kept (append, never overwrite).
- No merge jargon, no version numbers in standard mode; power users may see versions in More Details.
- Offline-queued commands that conflict on sync surface in the pending-work review, never silently dropped (consistent with ADR-001's no-last-write-wins rule).

## 11. Label print quality (finding 50)

- Default label: 1 × 4 inch at 300 DPI; QR symbol ≥ 0.6 × 0.6 inch quiet-zone included (also in the labelTemplate contract); text minimum 8 pt equivalent.
- **Durability requirement:** pilot labels print on waterproof synthetic stock (laser-safe polyester sheet labels or thermal synthetic stock once a printer is selected per ADR-001's deferred hardware decision). Acceptance: a printed label scans with a standard phone camera after 30 days in the PCO greenhouse (humidity, watering, UV) — verified once during the pilot.
- PDF output embeds fonts and renders identically across iOS/Android/desktop print dialogs (existing MVP requirement, now testable against the above numbers).

## 12. Pilot exit criteria (finding 54)

The pilot is complete and successful when all of the following hold, assessed jointly with PCO:

1. The Section 6 usability protocol passed.
2. PCO has catalogued ≥ 200 orchids and used the system for ≥ 8 consecutive weeks as its working record.
3. Zero data-loss incidents (no unsynchronized-draft loss, no canonical record loss).
4. Success-metric targets (Section 1) met for the final 4 weeks: median record creation < 2 min; QR scan success ≥ 95%.
5. Monthly cost within the Section 4 budget.
6. PCO affirms it would continue using the product and would pay for it at a price to be tested — the commercial signal the MVP exists to obtain.
7. All P0 findings in the gap analysis are resolved and no open P1 finding is assessed as blocking a paid pilot.
