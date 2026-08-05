# Orchid Domain Requirements

> Resolves gap-analysis findings 31, 37, 43, 49, 56, 61, 66, 68, 70, 71, 73, 74
> (see `docs/MVP-REQUIREMENTS-GAP-ANALYSIS-2026-08-05.md`). Complements the
> orchid template contract (`orchidTemplateData` in `core.schema.json`).

## 1. Care and repotting knowledge source (finding 43)

- AI care/repotting guidance draws on a **curated, versioned care knowledge base**: per-genus care sheets (light, temperature range, watering, media, repotting cadence) authored or licensed by the platform, stored in the repository or a governed collection, each entry carrying source attribution and version.
- Guidance responses cite which care sheet (and version) they used, state the identification assumption ("assuming this is a Cymbidium…"), and follow Governance Section 17 safety rules. The AI must not generate care advice from model memory alone when no knowledge-base entry covers the genus — it says so and gives only general-orchid guidance labeled as such.
- The knowledge version is recorded on proposals/guidance (already in the aiProposal contract as `KnowledgeVersion`).
- Initial coverage before Release 4: the genera in PCO's collection (survey during onboarding), minimum: Cymbidium, Phalaenopsis, Cattleya, Dendrobium, Oncidium, Paphiopedilum.

## 2. Quarantine workflow (finding 31)

Quarantine is a defined workflow, not just a status value:

- **Entering:** setting status `QUARANTINE` (or intake with quarantine-on-intake) prompts for a reason (new arrival, pest, disease, unknown) recorded as a `STATUS_CHANGED` event detail, and suggests (never forces) moving the plant to a Quarantine-area location.
- **During:** quarantined orchids are visually flagged in lists and on the detail page; the dashboard "Orchids in Quarantine" count links to the filtered list; recommended default quarantine period is 30 days for new arrivals (guidance text, not enforcement).
- **Exiting:** leaving `QUARANTINE` prompts one confirmation ("cleared, treated, or other?") recorded in the event; the AI may remind about plants in quarantine longer than the default period via the in-app notification list (no scheduler dependency — computed at dashboard load).
- Pest/disease observations are `TREATED` / `INSPECTED` events with structured details (issue, treatment, product used as free text in MVP); a structured pest/disease taxonomy is deferred.

## 3. Division and propagation lineage (finding 37)

Recording a `DIVIDED` event offers "create records for the divisions": each child orchid is created with its own full identity (ThingUUID, LabelID, accession number), an `ACQUIRED` event of method `DIVISION` referencing the parent, and inherited identification fields (marked LABEL_BASED at best, since division does not verify identity). The parent's `DIVIDED` event lists the child ThingUUIDs (`RelatedThingUUIDs` in the event contract). The detail page shows "divided from" / "divisions" links. Deeper breeding lineage (seed parents, crosses) remains deferred per MVP Definition Section 25.

## 4. Acquisition lots and the Oakland scenario (finding 49)

`BatchIntakeSession` (batch contract) now carries **shared acquisition defaults** (source, method, date, default collection/location, quarantine-on-intake) applied to each draft at capture time as ordinary per-draft values the user can override. This is how "the Oakland Acquisition" works: one session, shared source and date, every plant still individually identified, located, and auditable. A first-class acquisition-lot entity (lot-level cost allocation, lot reports) is deferred; the session name and shared source text preserve enough to reconstruct lots later.

## 5. Acquisition source (finding 56)

Acquisition source remains **free text** in the MVP (`AcquisitionSourceText`), per the deferral now recorded in MVP Definition Section 25. Requirement on the free text: search matches it (the "Bought from Andy" example), and the AI normalizes obvious repeats within a tenant when proposing ("Andy" ≈ "andy") without inventing a vendor entity. Structured vendor records with contact info are post-MVP.

## 6. Sale and transfer journey (findings 61, 66)

- **Listing:** `LIST_FOR_SALE` (Owner-only, confirmation required) sets status `FOR_SALE`, optionally records an asking price, and — only with an explicit additional sharing choice — publishes a sale view per Governance 11.2. Listing never implicitly changes sharing.
- **Buyer contact:** the sale page shows the tenant's designated public contact method only (defined in MVP Definition Section 17). No in-app messaging, offers, or checkout in the MVP.
- **Transfer:** `RECORD_TRANSFER` (Owner-only, confirmation required) captures recipient description (free text), transfer type (sale, gift, trade, other), date, and price/currency when a sale. Status becomes `TRANSFERRED`; the record and its history remain in the tenant per Governance 8.5.
- **Post-transfer QR:** scanning a transferred orchid's label shows, to unauthorized viewers, the same generic private page as any private record; to tenant members, the historical record marked Transferred. Linking a transferred plant to a new owner's CCE tenant is deferred.

## 7. Units and measurements (finding 68)

- Currency: ISO 4217 code stored with every monetary amount; tenant default (USD for PCO) applies when unstated.
- Dates: stored UTC with the event's `EffectiveAtPrecision`; displayed in the tenant time zone.
- Physical measurements (leaf span, pot size, temperatures) in the MVP are free text within narratives/notes; when structured measurement fields arrive (post-MVP), values store metric with per-tenant display preference. Recorded now so the schema decision is not accidental later.

## 8. Growing conditions on locations (finding 70)

Deferred as structured data (recorded in MVP Definition Section 25). MVP accommodation: locations get an optional free-text `EnvironmentNotes` (added when the locations contract lands) that AI guidance may quote ("your Flowering Area notes say it runs warm") without structured semantics.

## 9. First-run experience and empty states (finding 71)

Every MVP screen defines its empty state, and the first-run path is: after bootstrap, the Owner's first dashboard shows a short "get started" card (add your first orchid → print its label → scan it) replacing empty metrics; empty collections/locations/search states each carry one plain-language sentence and the single relevant action button. No blank tables, no unexplained zeros. (The PCO bootstrap pre-creates locations and collections, so PCO's true first run starts at "add your first orchid.")

## 10. Awards (finding 73)

Award records (AOS and other judging systems) are **deferred** and now recorded in MVP Definition Section 25. In the MVP, awards mentioned in narratives are preserved as narrative text and may appear in the AI summary as user-stated information; no structured award fields, no award verification.

## 11. Bloom tracking (finding 74)

The canonical events are `BLOOM_STARTED` / `BLOOM_ENDED`; the user-facing vocabulary "Flowered" maps to `BLOOM_STARTED` (MVP Definition Section 12). Spike emergence, flower counts, and photo-linked bloom records are deferred; in the MVP a bloom event may carry a narrative and photos like any event, which covers the enthusiast's "it produced two flower spikes" example without new structure.
