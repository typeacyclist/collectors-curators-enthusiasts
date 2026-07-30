# CCE / Orchid Enthusiasts MVP

Mobile-first MVP for the **Collectors–Curators–Enthusiasts (CCE)** platform and the initial tenant **PCO — Park City Orchids and More**.

## Implemented

- One seeded platform administrator
- One PCO tenant and tenant-administrator association
- Explicit location hierarchy: Space → Area → Rack → Shelf → Slot
- Orchid create, read, update, archive, and restore
- Mobile-responsive iOS/Android web interface
- Permanent Thing UUID, LabelID, and sequential PCO accession number
- QR lookup route
- One-inch by four-inch print-ready orchid label PDF
- Development authentication and Google Identity Platform production scaffolding
- SQLite for local development and PostgreSQL/Cloud SQL support for production
- Cloud Run Dockerfile and Cloud Build deployment configuration

## Local run

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8080
```

Open `http://localhost:8080`, select **Sign in**, and continue as the seeded PCO administrator.

## Test

```bash
pytest -q
```

## Production configuration

Set these environment variables through Cloud Run and Secret Manager:

```text
APP_ENV=production
AUTH_MODE=identity_platform
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@/DATABASE?host=/cloudsql/PROJECT:REGION:INSTANCE
SESSION_SECRET=<Secret Manager secret>
PUBLIC_BASE_URL=https://orchid-enthusiasts.com
FIREBASE_API_KEY=<Identity Platform web API key>
FIREBASE_AUTH_DOMAIN=<project>.firebaseapp.com
FIREBASE_PROJECT_ID=<project-id>
```

The Cloud Run service must be configured with the Cloud SQL instance connection and a least-privilege service account.

## Recommended first GCP deployment order

1. Create development GCP project.
2. Enable Cloud Run, Cloud Build, Artifact Registry, Cloud SQL, Secret Manager, and Identity Platform.
3. Create PostgreSQL Cloud SQL instance and database.
4. Create Secret Manager secrets for database credentials and session signing.
5. Create Artifact Registry repository named `cce`.
6. Build and deploy the container.
7. Configure Identity Platform email/password authentication.
8. Create the initial administrator account using the same email as the seeded application user, or update the application user association.
9. Configure HTTPS domain routing for `orchid-enthusiasts.com`.
10. Test iOS Safari, Android Chrome, PDF printing, and QR reopening.

## Current limitations

- Database migrations are not yet formalized; the MVP creates tables on startup.
- The label PDF is generated on demand and returned directly; Cloud Storage persistence is the next step.
- Identity Platform account provisioning still requires environment-specific configuration.
- Narrative AI, photographs, history, and sharing are intentionally outside this first build slice.
