# Collectors–Curators–Enthusiasts (CCE)

CCE is a mobile-first platform for managing physical collections. The initial MVP is the Orchid Enthusiasts experience for the tenant **PCO — Park City Orchids and More**.

## MVP scope

- One platform administrator
- One tenant: PCO
- One PCO tenant administrator
- Explicit location hierarchy
- Orchid CRUD on iOS, Android, and desktop
- Permanent orchid identity and accession number
- QR label preview and printing

## GCP-native architecture

The MVP intentionally does **not** use FastAPI or Cloud SQL.

- Firebase Hosting — responsive PWA
- Firebase Authentication — administrator sign-in
- Cloud Firestore — tenants, memberships, locations, orchids, and counters
- Firestore Security Rules — tenant isolation and authorization
- Cloud Run functions for Firebase — privileged creation and bootstrap operations
- Browser print/PDF workflow — orchid labels

See the implementation branch and draft pull request for the initial scaffold.
