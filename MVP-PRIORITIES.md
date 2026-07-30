# CCE / Orchid Enthusiasts MVP Priorities

## P0 - First usable vertical slice

| Priority | Work item | Status |
|---:|---|---|
| 1 | One deployable mobile-first application | Complete |
| 2 | Seed platform administrator and PCO tenant administrator | Complete |
| 3 | Tenant isolation and PCO tenant context | Complete |
| 4 | Explicit Space / Area / Rack / Shelf / Slot locations | Complete |
| 5 | Orchid Create / Read / Update / Archive / Restore | Complete |
| 6 | Permanent ThingUUID, LabelID, and PCO accession number | Complete |
| 7 | QR lookup and 1 x 4 inch PDF label | Complete |
| 8 | iOS/Android responsive layouts | Implemented; device QA pending |
| 9 | Automated end-to-end MVP test | Complete |

## P0 - Next deployment tasks

1. Provision the GCP development project and required APIs.
2. Create Cloud SQL for PostgreSQL and move from startup table creation to Alembic migrations.
3. Configure Google Identity Platform email/password authentication.
4. Store the session secret and database credentials in Secret Manager.
5. Deploy the container to Cloud Run and connect Cloud SQL.
6. Configure `orchid-enthusiasts.com` HTTPS routing.
7. Test create, edit, archive, restore, PDF printing, and QR lookup on a physical iPhone and Android phone.

## P1 - Immediate hardening after deployment

1. Add CSRF protection to state-changing form submissions.
2. Add administrative audit events for tenant, location, orchid, and label changes.
3. Add structured location-change history.
4. Store generated label PDFs in Cloud Storage when retention is required.
5. Add error pages and user-friendly validation summaries.
6. Add automated backup verification and Cloud Monitoring alerts.

## P2 - First CCE experience expansion

1. First-class narratives with create, update, append, and remove.
2. Mobile photograph upload.
3. AI narrative extraction and one-question-at-a-time completion prompts.
4. “Tell me about this orchid.”
5. Orchid care and repotting guidance.
6. Sharing and similar-orchid discovery.
