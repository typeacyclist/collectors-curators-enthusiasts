# ADR-001: AI-Native, Mobile-First, Offline-Resilient CCE Architecture

- Status: Accepted
- Scope: CCE platform and Orchid Enthusiasts MVP
- Initial tenant: PCO - Park City Orchids and More

## Context

CCE must provide an easy narrative-first experience while maintaining explicit operational state, evidence, confidence, privacy, tenant isolation, and historical integrity. Orchid intake and management must work on iOS and Android in greenhouse environments where connectivity may be intermittent.

## Decision

### Client application

Use one React and TypeScript codebase delivered as a responsive PWA and structured for Capacitor iOS and Android shells.

### Google Cloud services

- Firebase Hosting for the application
- Firebase Authentication for identity
- Firebase App Check for application attestation
- Cloud Firestore for operational data and synchronized query views
- Cloud Storage for original media and derivatives
- Cloud Functions for trusted commands
- Genkit with Vertex AI for governed server-side AI flows

FastAPI and Cloud SQL are not part of the MVP target architecture.

### Template-driven experience

Collection behavior is controlled by versioned templates and language-neutral JSON Schema contracts. React components use a curated component registry rather than hardcoded orchid-only forms or unrestricted schema-generated interfaces.

### Offline-first intake

A user can create a local `DraftThing`, capture narrative and media, select an explicit known location, and continue without connectivity. The application synchronizes on reconnect, application resume, manual request, and pending-work review. Browser background sync is optional and is not the only mechanism.

### Three-tier identity

- `ThingUUID`: immutable internal identity generated on the client
- `LabelID`: opaque permanent QR identity generated on the client
- `AccessionNumber`: tenant sequence assigned by trusted server logic during canonical commit

A QR generated before synchronization is pending activation and does not grant access.

### Command/query separation

Authorized queries use repository adapters over Firestore. Canonical changes use trusted commands for creation, movement, archive/restore, confirmation, and accession allocation.

Each command contains:

- `ClientOperationID`
- `TenantUUID`
- `ThingUUID`
- `ExpectedVersion`
- command type and payload

The command handler uses a Firestore transaction to:

1. Validate authentication, tenant membership, role, and App Check.
2. Check an operation ledger for prior processing.
3. Compare `ExpectedVersion` with the canonical record version.
4. Apply the validated change.
5. Append the related event.
6. Record the operation result.
7. Return the new canonical version.

Version fields alone do not guarantee conflict safety. The transaction and operation ledger are required.

### AI permissions

AI may read approved context and produce proposals. AI receives no canonical database-write tool. Proposed claims include evidence references, confidence, uncertainty, and version metadata. Deterministic command logic commits only user-confirmed or explicitly permitted results.

### Prompt-injection controls

Narratives, OCR text, images, labels, and documents are untrusted evidence. Delimiters may clarify evidence boundaries but are not a security boundary. Controls include:

- No privileged tools in extraction flows
- Strict output schemas with unexpected keys rejected
- Data minimization
- Deterministic post-validation
- Human confirmation
- Adversarial evaluation cases

### Media processing

Preserve originals. Create configurable display and AI derivatives locally where practical, correcting orientation and removing unnecessary metadata. Enforce request-size, image-count, rate, and tenant-usage limits server-side.

### Taxonomy

Keep botanical concepts separate. Do not combine species epithet, grex, clonal epithet, or cultivar epithet. Preserve the name as entered and distinguish name classification from verification status.

### Lifecycle history

Maintain explicit current operational state on the Thing and append-oriented lifecycle events for historical changes. Corrections create superseding or corrective events rather than erasing history.

### Labels

Use a `LabelService` abstraction. MVP drivers support preview, PDF, browser print, and mobile share/print. Native printer support is deferred until a reference printer and media are evaluated.

### Portability

Contracts and storage paths must support tenant export. Basic JSON/CSV export is required before a paid pilot; complete media ZIP export may follow.

### Similarity

Embeddings and similarity are post-MVP. Only approved public/platform projections are eligible. Embeddings are generated asynchronously and are removed or deactivated when discoverability is revoked.

## Corrections to client feedback

1. `nameType` and `hybridType` must not duplicate the same classification. The accepted taxonomy contract uses `nameType` for identity form and an optional `hybridOrigin` only when origin is separately known.
2. `ClientOperationID` and `ExpectedVersion` do not independently guarantee safety. Transactional operation-ledger deduplication and version comparison are required.
3. XML boundaries are a formatting aid, not protection that eliminates prompt injection.
4. Direct thermal printing is not mandatory until hardware is selected and validated.

## Consequences

### Benefits

- Field-ready offline intake
- Durable identifiers and QR labels
- Governed AI with human control
- Reconfigurable collection experiences
- Reduced frontend/database coupling
- Explicit conflict handling
- Portability and future specialty expansion

### Costs

- More up-front contract and emulator testing
- Local draft and synchronization complexity
- Media lifecycle management
- Command-function latency for canonical writes
- Hardware-specific work for direct thermal printing

## Implementation order

1. Governance and contracts
2. Mobile shell and offline draft infrastructure
3. Authentication, App Check, tenancy, and command layer
4. Location and Orchid CRUD with lifecycle events
5. Governed AI intake and taxonomy proposals
6. Label generation, scanning, export, and field validation
