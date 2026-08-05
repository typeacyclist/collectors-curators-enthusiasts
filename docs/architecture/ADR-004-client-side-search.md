# ADR-004: Client-Side Local Search Index for MVP Search

- Status: Accepted
- Scope: CCE platform and Orchid Enthusiasts MVP search (MVP Definition Section 16)
- Depends on: ADR-001, ADR-003
- Resolves: gap-analysis finding 5 (`docs/MVP-REQUIREMENTS-GAP-ANALYSIS-2026-08-05.md`)

## Context

MVP Definition Section 16 requires search over display name, accession number, label identifier, narrative text, collection, location, status, source, and tag text — including free-text queries like "Bought from Andy" and "Needs TLC." Cloud Firestore provides no native full-text search. The alternatives were a managed search service (Algolia/Typesense — a paid dependency, a sync pipeline, and a new tenant-isolation surface) or deferring narrative full-text out of the MVP (weakening a headline feature).

The MVP design envelope is 5,000 orchids per tenant (`docs/requirements/MEASUREMENT-ACCEPTANCE-NFR.md` Section 3); the pilot tenant starts with hundreds. At that scale a device-local index is fast and removes the infrastructure entirely.

## Decision

MVP search executes **client-side against a local index of the tenant's records** the authorized user can already read.

- The index is built from the synchronized tenant data (Things, narratives, collections, locations) and maintained incrementally on sync; it lives in the same local storage domain as the offline draft store.
- Indexed fields: display name, accession number, LabelID, taxonomy fields, narrative text, collection name, location path, status, acquisition source text.
- Tokenized substring/prefix matching with basic normalization (case, diacritics); ranking favors name and accession matches over narrative matches.
- Search works offline over whatever is locally synchronized, consistent with the offline-first architecture; staleness follows the offline reference-data rules (MVP Definition, connectivity section).
- **Tenant isolation and sharing are inherited, not re-implemented:** the index only ever contains records the authenticated member is authorized to read via Security Rules, is stored per account, and is cleared on sign-out (subject to the unsynced-draft safeguards in `ACCOUNT-TENANT-LIFECYCLE.md` Section 7).
- AI-assisted natural-language search (Section 16's "Show orchids bought from Andy") is a `READ_ONLY` AI flow that translates the query into structured filters/terms executed against the same local index; the AI receives the query, not the corpus.

## Not chosen

- **Managed search service** — rejected for the MVP: cost, sync-pipeline complexity, and a second copy of tenant data to isolate and delete. It remains the expected escalation path.
- **Defer narrative full-text** — rejected: narrative search is core to the product thesis ("the user tells the story… and can find it again").

## Revisit criteria

Adopt a managed search service (new ADR) when any tenant approaches the design envelope (≥ 5,000 Things), when cross-device index build time exceeds the Section 2 performance budgets on floor devices, or when server-rendered surfaces (public galleries) need search that a client index cannot serve.

## Consequences

- No new infrastructure, no additional data-processing agreement, no per-query cost; search inherits offline capability.
- Index build/maintenance code becomes client complexity with device-matrix test coverage (floor devices included).
- Search over data not yet synchronized to the device is impossible by design; the UI must show sync recency where that matters.
- Multi-thousand-record initial sync cost is bounded by the design envelope and measured during the pilot (FinOps metrics).
