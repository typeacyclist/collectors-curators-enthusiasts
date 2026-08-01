# CCE / Orchid Enthusiasts MVP

Mobile-first MVP for the **Collectors–Curators–Enthusiasts (CCE)** platform and the initial tenant **PCO — Park City Orchids and More**.

## CCE Business Case Executive Summary

## Target Solution

**Collectors–Curators–Enthusiasts (CCE)** is an AI-native, mobile-first platform for documenting, organizing, managing, understanding, and selectively sharing physical collections.

The initial specialty experience, **Orchid Enthusiasts**, will be validated with the first tenant:

> **PCO — Park City Orchids and More**

The initial MVP will allow a tenant administrator to:

- Manage explicit physical locations
- Add, view, update, archive, and restore orchid records
- Use photographs and natural-language descriptions during intake
- Capture essential orchid information while offline and synchronize it later
- Receive AI-assisted identification and information proposals
- Confirm important information before it becomes part of the record
- Generate permanent accession numbers and QR labels
- Print labels from iOS, Android, or desktop devices
- Scan a label to reopen the correct orchid record

The MVP establishes the reusable CCE foundation for future collection categories such as plants, watches, dolls, art, antiques, memorabilia, and other specialty collections.

------

## Business Problem

Collectors and small specialty businesses commonly manage valuable physical collections using a combination of:

- Spreadsheets
- Handwritten labels
- Photographs stored on personal devices
- Paper records
- Informal notes
- Disconnected inventory applications
- Personal memory

These methods create several operational problems:

- Important provenance and acquisition history is lost
- Physical items become separated from their records
- Location tracking becomes unreliable
- Records are inconsistent or incomplete
- Existing software requires excessive form entry
- Older or nontechnical users may avoid documenting items
- Knowledge is difficult to transfer to family, employees, buyers, or future curators
- Collection-specific applications are expensive to build and difficult to adapt
- AI-generated information may be presented without adequate evidence, confidence, or user control

The central market gap is not simply the absence of another inventory system. It is the absence of an easy, trustworthy way for users to tell the story of a physical thing while the system performs the difficult work of organizing that knowledge.

------

## Proposed Solution

CCE uses a narrative-first experience.

```text
Photograph the Thing
→ Tell its story
→ AI proposes what it understood
→ User confirms important information
→ CCE creates a durable, searchable record
→ The Thing receives a permanent QR identity
```

The user should experience a knowledgeable assistant rather than a complex database.

The platform preserves:

- Original narratives
- Photographs
- Labels and documents
- Confirmed structured information
- AI-derived proposals
- Sources and confidence
- Current location and operational status
- Historical changes
- Privacy and sharing decisions

The product principle is:

> **The user tells the story. AI organizes the knowledge. The user remains in control.**

------

## Target Customers

### Initial target

The first target is small and midsized orchid collectors, growers, specialty nurseries, societies, and collection managers that need to document and label plants without implementing a traditional nursery-management system.

The first operational tenant is:

```text
Park City Orchids and More
Specialty: Orchids
Initial role: Tenant administrator
Primary devices: iPhone, Android, tablet, and desktop
```

### Broader target

The reusable CCE platform can later support:

- Private collectors
- Specialty retailers
- Curators
- Estate managers
- Museums and small archives
- Clubs and enthusiast societies
- Dealers and appraisers
- Breeders and growers
- Family collections
- Insurance and provenance documentation

Potential specialty categories include:

- General plants
- Orchids
- Watches
- Dolls
- Art
- Antiques
- Coins
- Stamps
- Books
- Wine
- Vehicles
- Memorabilia

------

## Customer Value Proposition

CCE provides five primary benefits.

### 1. Easier collection documentation

Users can begin with a photograph and a spoken or typed description instead of completing a large form.

### 2. Better knowledge preservation

CCE retains the original story and evidence, allowing future templates and AI models to extract additional information without requiring the user to re-enter it.

### 3. Reliable physical identification

Each Thing receives a permanent identity, accession number, and QR label that remains valid when the Thing is moved, renamed, reclassified, transferred, or archived.

### 4. Trustworthy AI assistance

AI proposes information but does not silently perform consequential actions.

CCE distinguishes:

- Confirmed information
- User statements
- Observations
- AI extraction
- AI inference
- Unknown or conflicting information

### 5. Flexible specialty experiences

The same CCE platform can support multiple collection categories through configurable templates, terminology, prompts, labels, privacy policies, and AI extraction rules.

### 6. Field-ready operation

Users can capture photographs, narratives, and explicit locations in greenhouses, storage buildings, estates, and other environments with unreliable connectivity. Drafts remain visible and retryable until synchronization succeeds.

### 7. Data ownership and portability

Tenants can export confirmed collection information, narratives, locations, lifecycle events, and media in documented formats, reducing vendor-lock-in concerns.

------

## Strategic Differentiation

CCE is differentiated from traditional inventory applications by combining:

- Narrative-first intake
- AI-assisted interpretation
- Evidence and confidence tracking
- Mobile-first operation
- Permanent QR identity
- Explicit location management
- Privacy by design
- User confirmation of consequential actions
- Configurable collection templates
- Reusable infrastructure across specialty markets

The platform is not limited to a fixed orchid database or a fixed set of forms.

Instead, it provides an extensible experience engine where collection templates can define:

- Terminology
- Suggested photographs
- Intake prompts
- Structured attributes
- Validation
- AI extraction outputs
- Follow-up questions
- Statuses and events
- Privacy defaults
- Label layouts
- Guidance boundaries

This allows new specialty experiences to be introduced without rebuilding the entire application.

------

## AI-Native Strategy

AI is part of the product workflow rather than an optional chatbot.

Initial AI capabilities will include:

- Reading visible plant-label text
- Interpreting natural-language narratives
- Proposing display names and key facts
- Identifying missing information
- Asking one high-value follow-up question
- Explaining what is known about an orchid
- Distinguishing source, confidence, and uncertainty

The initial AI flow is deliberately bounded:

```text
User narrative and photographs
→ AI produces proposals
→ User reviews or corrects
→ Deterministic application logic saves confirmed information
```

AI will not independently:

- Publish a record
- Assign or change a location
- Change tenant access
- Mark an item sold
- Record a transfer
- Archive an item
- Replace a confirmed identity
- Change privacy settings

This approach creates user trust while still reducing data-entry effort.

------

## Mobile-First Strategy

All required MVP workflows will operate on:

- iPhone
- iPad
- Android phones
- Android tablets
- Desktop browsers

The product will use one React and TypeScript codebase delivered initially as a responsive Progressive Web Application and structured for future iOS and Android packaging through Capacitor.

Mobile workflows will prioritize:

- Camera capture
- Voice or keyboard dictation
- Large touch controls
- One decision per screen
- Draft preservation
- Simple location selection
- QR scanning
- Native print and share functions
- No desktop-only interaction requirements

------

## Technology Strategy

CCE will use a Google Cloud and Firebase-native architecture.

```text
React and TypeScript
    Mobile-first user experience

Firebase Hosting
    Secure web and PWA delivery

Firebase Authentication
    User identity

Cloud Firestore
    Mobile-aware operational data and synchronization

Firestore Security Rules
    Tenant isolation and authorization

Cloud Functions
    Privileged and validated operations

Genkit and Vertex AI
    Governed AI extraction and assistance

Cloud Storage
    Photographs and generated assets
```

The solution will not depend on FastAPI or a continuously operated application server for the MVP.

The backend will remain adaptable through:

- Versioned collection templates
- Language-neutral JSON Schema contracts
- Repository abstractions
- Command/query separation
- Versioned AI prompts and extraction contracts
- Explicit operational records
- Flexible narrative and attribute layers

This limits lock-in between the user interface and the initial database implementation.

------

## Initial MVP Scope

The first MVP is intentionally narrow.

### Included

- One platform administrator
- One tenant: PCO
- One PCO tenant administrator
- Authentication
- Explicit location hierarchy
- Orchid create, read, update, archive, and restore
- Permanent Thing identity
- Sequential PCO accession number
- Permanent LabelID
- QR label generation
- Mobile label preview and printing
- Scan-to-record lookup
- One AI-assisted orchid intake workflow
- User confirmation before saving AI proposals
- Basic audit history
- Tenant isolation

### Deferred

- Multiple specialty templates
- Public community features
- Direct member messaging
- E-commerce
- Payment processing
- Shipping
- Full nursery production management
- Formal orchid registration verification
- Automated appraisals
- Advanced breeding records
- Native printer-driver integration
- Complex multi-agent automation

------

## MVP Validation Goals

The MVP will test whether a user can complete the following without training:

```text
Sign in
→ Create or select a location
→ Photograph an orchid
→ Tell the orchid’s story
→ Review the AI proposal
→ Save the orchid
→ Print a QR label
→ Scan the label
→ Edit, move, archive, or restore the orchid
```

The MVP should validate:

- Mobile usability
- User acceptance of narrative-first intake
- Accuracy of AI proposals
- Effectiveness of the confirmation model
- Reliability of location and QR workflows
- Label readability and durability
- Tenant isolation
- Ease of adding additional collection templates

------

## Business Model Direction

The initial MVP is a product-validation release rather than a complete commercial offering.

Potential future revenue models include:

- Monthly tenant subscriptions
- User- or collection-size tiers
- Premium AI processing
- Advanced label and reporting packages
- Public showcase or marketplace features
- Society and club plans
- Professional curator or dealer plans
- Specialty template packages
- Data migration and onboarding services

The commercial model should be validated after measuring real collection size, AI usage, storage costs, onboarding effort, and customer willingness to pay.

------

## Strategic Expansion Path

The first release creates a platform rather than a single-purpose orchid application.

```text
PCO Orchid MVP
→ Additional orchid collectors and nurseries
→ Orchid societies and shared discovery
→ General plant collections
→ Watches and dolls
→ Additional collector categories
→ Specialty marketplaces and professional services
```

Each new specialty should reuse:

- Authentication
- Tenancy
- Roles
- Locations
- Thing identity
- Narratives
- Evidence
- AI proposals
- Labels
- Privacy
- Audit history
- Sharing controls

This enables CCE to expand across multiple enthusiast markets without building separate products for every category.

------

## Key Risks and Controls

| Risk                                          | Control                                                      |
| --------------------------------------------- | ------------------------------------------------------------ |
| AI presents incorrect information             | Evidence, confidence, user confirmation, conflict preservation |
| Users find the system too complex             | Narrative-first mobile workflow and progressive disclosure   |
| Flexible data becomes inconsistent            | Versioned templates, schemas, validation, and explicit operational fields |
| Private collection data is exposed            | Private defaults, tenant isolation, App Check, scoped sharing |
| Firestore becomes tightly coupled to the UI   | Repository abstraction and command layer                     |
| Native mobile capabilities are later required | Capacitor-compatible React architecture                      |
| AI costs grow unpredictably                   | Bounded workflows, server-side orchestration, quotas, and model routing |
| Product becomes orchid-specific               | Reusable CCE Thing model and configurable templates          |
| AI agents perform unauthorized actions        | AI may read and propose; only deterministic code commits changes |

------

## Executive Recommendation

Proceed with the CCE MVP as an **AI-native, mobile-first, configurable collection platform**, using Orchid Enthusiasts and PCO as the initial validation environment.

The MVP should not be treated as a conventional orchid inventory application. It should validate the defining CCE proposition:

> A person can photograph a physical Thing, tell its story naturally, allow AI to organize the information, confirm what matters, and create a durable, private, searchable, labeled record.

The immediate investment should focus on:

1. Architecture and AI-governance controls
2. Mobile-first React application foundation
3. Firebase authentication and tenant isolation
4. Explicit location and Orchid Thing management
5. One bounded AI-assisted intake workflow
6. Permanent QR labels and mobile printing
7. Automated testing for privacy, accuracy, mobile usability, and tenant isolation

If the MVP succeeds, CCE will have a reusable foundation capable of supporting multiple collection categories, specialty communities, and commercial subscription offerings without rebuilding the core platform.



## Architecture review decision

The authoritative CCE guidance requires a narrative-first interface, evidence-backed AI, explicit operational control, confidence handling, privacy by design, reversibility, and progressive disclosure. The working MVP also requires complete iOS and Android use without a desktop.

The revised design should be:

```text
Mobile-first React application
        │
        ├── PWA in mobile and desktop browsers
        ├── Capacitor iOS application
        └── Capacitor Android application
                 │
                 ▼
        Firebase Authentication
        Firebase App Check
                 │
         ┌───────┴────────┐
         ▼                ▼
Firestore query layer   Cloud Functions command layer
offline/mobile reads    validated canonical writes
         │                │
         └───────┬────────┘
                 ▼
        Server-side AI orchestration
        Genkit + Vertex AI
                 │
                 ▼
        Proposed facts and actions
                 │
                 ▼
        Human confirmation
                 │
                 ▼
        Deterministic record update
```

## Accepted client architecture disposition

The client review is accepted as the implementation direction, subject to the corrections below.

| Item | Recommendation | Disposition | Delivery target | Accepted adjustment |
| --- | --- | --- | --- | --- |
| 1 | Offline intake queue | Merge with modification | MVP | Use an abstract `OfflineDraftStore` with web and Capacitor adapters; synchronize on reconnect, application resume, pending-work review, or manual request. |
| 2 | Client-generated identity | Merge with modification | MVP | Use `ThingUUID`, `LabelID`, and server-assigned `AccessionNumber` as separate identifiers. |
| 3 | Native thermal printing | Partially merge | MVP interface; driver after hardware spike | Implement `LabelService` with PDF, browser print, and mobile share/print drivers. Defer BLE or printer-language support until hardware is selected. |
| 4 | Image optimization and limits | Merge with modification | MVP | Preserve originals and generate configurable display and AI derivatives; enforce request, rate, and tenant-usage limits. |
| 5 | Prompt-injection defenses | Merge with correction | MVP | Treat XML or other delimiters as formatting aids only; rely on no write tools, strict schemas, deterministic validation, and confirmation. |
| 6 | Botanical taxonomy | Merge with stronger model | MVP | Keep genus, species epithet, grex, clonal epithet, and cultivar epithet separate. |
| 7 | Append-only lifecycle events | Merge | MVP foundation | Append lifecycle events while retaining current operational state on the parent Thing. |
| 8 | Tenant export | Merge in stages | Before paid pilot | Deliver JSON/CSV metadata export first; add full media ZIP export later. |
| 9 | Vector similarity | Merge and defer | Post-MVP | Generate embeddings asynchronously only for records approved for platform or public discovery. |
| 10 | Idempotency and conflict handling | Merge | MVP | Use transactional operation-ledger deduplication and expected-version comparison for canonical commands. |

### Corrections and boundaries

1. `ThingUUID` and `LabelID` are identifiers, not authorization credentials.
2. A QR label created offline is pending activation until the Thing synchronizes.
3. `ClientOperationID` and `ExpectedVersion` do not independently guarantee safety; the command handler must use a transaction and operation ledger.
4. `nameType` and `hybridType` must not duplicate the same concept. Use `nameType` for identity form and an optional `hybridOrigin` only when origin is separately known.
5. XML boundaries do not eliminate prompt injection.
6. Direct thermal printer integration is not an MVP commitment until a reference printer and media are selected.

------

# 1. Overall assessment

| Requirement            | Current plan          | Assessment               | Revision                                                |
| ---------------------- | --------------------- | ------------------------ | ------------------------------------------------------- |
| GCP-native             | Firebase/GCP          | Correct                  | Retain                                                  |
| iOS and Android        | Responsive PWA        | Partially sufficient     | Add Capacitor from the beginning                        |
| Flexible frontend      | React                 | Correct foundation       | Add template-driven experience engine                   |
| Reconfigurable backend | Direct Firestore CRUD | Too tightly coupled      | Add repository and command abstractions                 |
| AI-native              | AI deferred           | Insufficient             | Build AI contracts and one AI intake flow into MVP      |
| Privacy                | Firebase rules        | Necessary but incomplete | Add App Check, scoped AI, confirmation gates, audit     |
| Accuracy               | Basic CRUD            | Insufficient             | Add evidence, source, confidence, and revision tracking |
| Ease of use            | Mobile forms          | Too conventional         | Use photo/story-first intake with AI-assisted review    |
| Python + React         | Planned monorepo      | Valid                    | Do not force Python into the first critical path        |
| FastAPI                | Removed               | Correct                  | Do not restore it                                       |

------

# 2. Mobile-first frontend recommendation

## Use React, Vite, PWA, and Capacitor

A PWA alone can satisfy the initial browser workflow, but CCE should be designed from the beginning so the same React application can be packaged as native iOS and Android applications.

Capacitor is specifically designed to wrap modern web applications as native iOS and Android applications while retaining access to native SDKs when required. ([Capacitor](https://capacitorjs.com/docs?utm_source=chatgpt.com))

Recommended frontend:

```text
React
TypeScript
Vite
React Router
Capacitor
Vite PWA / Workbox
Firebase Web SDK
```

This produces:

```text
One React codebase
├── Mobile web
├── Installable PWA
├── iOS through Capacitor
├── Android through Capacitor
└── Desktop web
```

### Why add Capacitor now

It provides a future path for:

- Reliable camera access
- QR and barcode scanning
- Native share sheets
- File access
- Push notifications
- Device speech capabilities
- Better printer integrations
- App Store and Play Store distribution

The first release can still deploy as a PWA. Adding the Capacitor structure now prevents the UI from becoming dependent on desktop/browser-only assumptions.

## Do not use a desktop form layout

The primary mobile workflow should be:

```text
Take photo
→ Speak or type a short story
→ AI proposes what it understood
→ User corrects or confirms
→ Select location
→ Save
→ Print label
```

The detailed structured form remains available under **More Details**.

## Mobile interface rules

The implementation should use:

- Bottom-positioned primary actions
- Large touch targets
- One principal decision per screen
- Card layouts rather than tables
- Explicit sync and save status
- Draft preservation during browser suspension
- Camera-first workflows
- No hover-dependent interactions
- No horizontally scrolling forms
- Plain-language confirmation dialogs

------

# 3. Flexible frontend: template-driven experience engine

The frontend should not hardcode an `OrchidForm.tsx` containing every orchid field.

Instead, create a reusable **CCE Experience Engine**.

## Template package

Each collection template should define a versioned package:

```text
Template
├── Identity and version
├── Terminology
├── Field definitions
├── Validation
├── UI sections and order
├── Intake prompts
├── AI extraction contract
├── Follow-up question rules
├── Privacy defaults
├── Label definition
├── Status options
├── Event types
└── Guidance configuration
```

Example:

```text
Template: ORCHIDS
Version: 1.0

Thing term: Orchid
Collection term: Orchid Collection
Primary prompt: Tell us about this orchid
Suggested photos:
  - Whole plant
  - Flower
  - Label
  - Roots
```

## Use JSON Schema as the language-neutral contract

A versioned JSON Schema can support:

- Runtime validation
- AI structured output
- TypeScript type generation
- Future Python model generation
- Import validation
- Template versioning
- Power-user structured editing

The UI should not blindly render a generic form from JSON Schema. Instead, it should use a curated component registry:

```text
short_text       → MobileTextField
long_narrative   → StoryInput
currency         → MoneyInput
location         → LocationPicker
photo_set        → PhotoCapture
confidence       → ConfidenceBadge
taxonomy_name    → OrchidNameEditor
```

The template controls composition. The application controls the quality of each component.

## Reconfiguration boundaries

Administrators should eventually be able to change without an application release:

- Terminology
- Field visibility
- Section order
- Suggested prompts
- Optional versus recommended fields
- Label content
- Privacy defaults
- AI follow-up prompts
- Help text

Adding an entirely new interaction component still requires a tested application release.

------

# 4. Backend and database recommendation

## Keep Firestore for the MVP

Firestore is the better initial choice because it has:

- Direct web, iOS, and Android SDKs
- Realtime synchronization
- Mobile and web offline persistence
- Flexible document structures
- Authentication and Security Rules integration

Firestore can cache active data, accept offline changes, and synchronize them when connectivity returns. On the web, persistent caching must be explicitly enabled and should only be enabled on a trusted device when private information is involved. ([Firebase](https://firebase.google.com/docs/firestore/manage-data/enable-offline?utm_source=chatgpt.com))

Firebase SQL Connect provides managed PostgreSQL, typed generated SDKs, and relational constraints. ([Firebase](https://firebase.google.com/docs/reference/sql-connect/rest?utm_source=chatgpt.com)) It is attractive for future complex reporting and highly relational workflows, but Firestore has a clearer mobile-offline advantage for this first release.

**Recommendation:** use Firestore now, but do not couple React components directly to Firestore.

## Offline-first intake and synchronization

Essential intake must work without connectivity.

```text
User captures photos and narrative
→ Local DraftThing is saved immediately
→ User may select a known explicit location
→ Draft remains visible with sync status
→ Connectivity returns
→ Media and metadata upload
→ Canonical create command runs
→ AI proposal is generated
→ User reviews and confirms
```

Use an `OfflineDraftStore` interface rather than binding the application directly to one library:

```text
OfflineDraftStore
├── Web adapter
│   └── IndexedDB
└── Capacitor adapter
    ├── Native filesystem for local media
    └── Native key-value storage for draft metadata
```

Synchronization must run when connectivity returns, the application resumes, the user opens pending work, or the user selects **Sync Now**. Browser background sync may assist but must not be the only mechanism.

Required draft states:

```text
LOCAL_ONLY
WAITING_FOR_NETWORK
UPLOADING
WAITING_FOR_AI
AI_REVIEW_REQUIRED
SYNCED
SYNC_ERROR
```

## Three-tier identity

```text
ThingUUID
    Immutable internal identity generated immediately on the device

LabelID
    Opaque permanent QR identity generated immediately on the device

AccessionNumber
    Human-readable tenant sequence assigned by trusted server logic
```

The permanent QR route uses `LabelID`:

```text
https://orchid-enthusiasts.com/p/{LabelID}
```

An offline label may be produced before synchronization, but the application must state that the remote QR record becomes available only after synchronization.

## Add a repository abstraction

React components should call:

```text
ThingRepository
LocationRepository
TenantRepository
TemplateRepository
LabelRepository
```

The initial implementation uses Firestore adapters:

```text
FirestoreThingRepository
FirestoreLocationRepository
```

A future SQL Connect implementation could replace those adapters without rewriting the UI.

## Use command/query separation

Use direct Firestore access primarily for authorized reads and mobile synchronization.

Use Cloud Functions for canonical operations that require validation:

```text
bootstrapTenant
createLocation
createOrchid
updateOrchid
moveOrchid
archiveOrchid
restoreOrchid
confirmAIProposal
allocateAccessionNumber
```

This is a lightweight command/query architecture:

```text
Queries
    Fast Firestore reads
    Offline cache
    Realtime updates

Commands
    Cloud Functions
    Authentication
    Tenant authorization
    Validation
    Idempotency
    Audit event
```

The client may create and preserve a complete local draft offline. Canonical commit, accession allocation, server-side AI, and remote QR activation require connectivity during the MVP.

Every canonical command must include:

```text
ClientOperationID
TenantUUID
ThingUUID
ExpectedVersion
ActorUserUUID
CommandType
Payload
```

The trusted command handler must use a Firestore transaction to:

1. Validate authentication, tenant membership, role, and App Check.
2. Check the operation ledger for a previously processed `ClientOperationID`.
3. Compare `ExpectedVersion` with the current canonical version.
4. Apply the validated state change.
5. Append the related lifecycle event.
6. Store the operation result for replay-safe retries.
7. Return the new canonical version.

A version mismatch produces a reviewable conflict rather than silently overwriting confirmed information.

## Preserve an explicit operational core

Do not make every property arbitrary JSON.

Keep these explicit and controlled:

```text
Thing identity
Tenant
Collection
Template and template version
Location
Status
Sharing
Label identity
Created and updated metadata
Archive state
```

Flexible template-specific knowledge can be represented separately as:

- Structured attributes
- Narratives
- Proposed claims
- Confirmed claims
- Events
- Evidence references

This follows the governing principle:

> Narrative describes the Thing; explicit information controls what the system does.

------

# 5. AI-native architecture

AI-native does not mean placing a chatbot beside a traditional form. It means AI is part of the intake, organization, explanation, and guidance model.

## AI should produce proposals, not database mutations

The core flow should be:

```text
User narrative and photos
        ↓
AI extraction
        ↓
Proposed claims
        ↓
Sources and confidence
        ↓
One high-value follow-up question
        ↓
User review
        ↓
Deterministic command
        ↓
Canonical record update
```

An AI model must never directly:

- Assign a location
- Publish a Thing
- Change tenant membership
- Mark a Thing sold
- Archive a Thing
- Replace a confirmed identity
- Alter privacy settings

The model may propose the action. A deterministic command handler performs it after authorization and confirmation.

## AI permission classes

Every AI capability should have one of three permission classes.

| Class       | Permitted behavior           | Examples                          |
| ----------- | ---------------------------- | --------------------------------- |
| `READ_ONLY` | Explain existing information | Tell me about this orchid         |
| `PROPOSE`   | Suggest facts or actions     | Possible identity, location match |
| `COMMIT`    | Not granted to an AI model   | Reserved for deterministic code   |

There should be no autonomous `COMMIT` agent.

## Initial bounded agents

Do not create a large multi-agent swarm. Begin with bounded, testable flows.

### 1. Intake Agent

Inputs:

- Narrative
- Selected photos
- Orchid template
- Existing label text
- Tenant context needed for the task

Outputs:

- Proposed display name
- Proposed structured facts
- Source for each fact
- Confidence category
- Uncertainties
- Major omission
- Recommended follow-up question

### 2. Clarification Agent

Selects only one high-value question.

Example:

> The tag appears to say “Golden Elf Sundust.” Would you like to use that as the current name?

### 3. Record Explainer

Supports:

> Tell me about this orchid.

It summarizes confirmed information, user statements, uncertainty, and missing information without modifying the record.

### 4. Guidance Agent

Later provides care and repotting guidance using versioned and approved orchid knowledge sources.

### 5. Similarity Agent

Later compares only records explicitly eligible for platform or public discovery.

Firestore supports vector similarity search, while embeddings must be generated separately, such as through Vertex AI. ([Firebase](https://firebase.google.com/docs/firestore/vector-search?hl=en&utm_source=chatgpt.com)) A separate privacy-filtered similarity index should be used rather than embedding complete private records.

------

# 6. AI framework decision

## Use server-side Genkit in TypeScript for the initial AI flow

Genkit provides structured outputs, multimodal generation, tool calling, prompt templates, workflows, tracing, and local developer tooling. ([Firebase](https://firebase.google.com/docs/genkit?utm_source=chatgpt.com))

Use it for:

```text
services/ai/
├── intakeFlow
├── clarificationFlow
├── explainThingFlow
├── prompts
├── tools
├── schemas
└── evaluations
```

Deploy these flows to Cloud Functions or Cloud Run.

## Multimodal media preparation and cost controls

Modern mobile photographs should not be submitted to AI at their original camera resolution by default.

```text
Original photo
→ Correct orientation
→ Create local preview
→ Create configurable AI derivative
→ Submit derivative for OCR or vision analysis
→ Preserve original separately for archive and reprocessing
```

The initial derivative profile may use WebP with an approximately 1280-pixel long edge, but dimensions and quality must remain configurable rather than embedded as permanent architectural constants.

Server controls must include:

- App Check enforcement
- Authentication and tenant authorization
- Maximum request and image sizes
- Maximum image count
- Per-user and per-tenant usage limits
- Duplicate-request detection
- Model routing by task
- Usage logging and billing alerts

Cloud budgets and alerts supplement these controls; they do not replace application-level limits.

## Do not place governed AI directly in the React client

Firebase AI Logic supports direct Gemini calls from web, iOS, and Android clients and can be protected with App Check. ([Firebase](https://firebase.google.com/docs/ai-logic/solutions/overview?utm_source=chatgpt.com))

However, for CCE’s canonical extraction and private collection data, server-side execution is preferable because it provides:

- Centralized prompt governance
- Controlled data minimization
- Consistent authorization
- Auditable tool calls
- Model and prompt version tracking
- Cost controls
- Stronger separation from client manipulation

Client-side AI Logic can later support low-risk, non-canonical convenience features.

## Python position

The monorepo may include Python, but Python should not be forced into the first production path.

Genkit’s Python SDK is currently identified as a preview release. ([Genkit](https://genkit.dev/python/docs/get-started?utm_source=chatgpt.com)) Therefore:

```text
MVP AI orchestration:
TypeScript Genkit

Later Python services:
Image processing
Batch reprocessing
Data science
Specialized inference
Advanced agents
Evaluation utilities
```

For advanced Python agent workloads, Vertex AI Agent Engine supports managed agent runtimes and has full integration with Google’s Agent Development Kit. ([Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/overview?authuser=3&utm_source=chatgpt.com))

No FastAPI service is required.

------

# 7. AI accuracy and evidence model

Every AI proposal should contain:

```text
value
source type
source reference
source excerpt or region
confidence category
model identifier
prompt version
template version
created timestamp
review status
reviewed by
```

Example:

```text
Proposed value:
Cymbidium Golden Elf ‘Sundust’

Source:
Photo 2, visible plant label

Confidence:
Likely

Status:
Awaiting user confirmation
```

## Avoid a single overall confidence score

Confidence should be per claim.

The system may be:

- Highly confident about the purchase price
- Moderately confident about the seller
- Uncertain about the orchid identity
- Unable to determine the acquisition date

## Preserve conflicts

AI should not silently choose between:

```text
Existing tag: Golden Elf ‘Sundust’
User narrative: Possibly Golden Boy
```

Both remain evidence. The current display identity is separately selected or remains uncertain.

## Orchid taxonomy contract

The taxonomy schema must preserve the name as entered and keep botanical concepts separate:

```text
nameAsEntered
displayName
genus
speciesEpithet
infraspecificRank
infraspecificEpithet
grex
clonalEpithet
cultivarEpithet
nameType
hybridOrigin
verificationStatus
sourceReferences
```

`nameType` describes the form of the name, for example:

```text
SPECIES
NATURAL_HYBRID
REGISTERED_HYBRID
UNREGISTERED_HYBRID
GENUS_ONLY
TRADE_NAME
UNKNOWN
```

`verificationStatus` records the evidence state:

```text
USER_STATED
LABEL_READ
AI_PROPOSED
USER_CONFIRMED
EXTERNALLY_VERIFIED
CONFLICTING
UNKNOWN
```

AI must not assign `EXTERNALLY_VERIFIED` from visual similarity or model knowledge alone. Deterministic normalization may correct capitalization, spacing, and recognized genus spelling while preserving the original entry and its source.

------

# 8. Privacy-by-design implementation

## Required protections

- Private by default
- Firebase Authentication
- Firebase App Check from early development
- Tenant-scoped authorization
- Separate public projections
- No public query against canonical private records
- Temporary audio only
- Minimum-data AI requests
- Exact locations excluded from AI unless needed
- Financial data excluded unless relevant
- Explicit public preview
- Audit of sharing changes
- Separate similarity index containing only approved fields

Firebase recommends introducing App Check early for mobile and web AI applications to reduce unauthorized use. ([Firebase](https://firebase.google.com/docs/ai-logic/solutions/overview?utm_source=chatgpt.com))

## Treat user content as untrusted instructions

Narratives, OCR text, labels, and uploaded documents may contain text that resembles instructions.

The AI orchestration layer must treat such content as evidence, not as system instructions. User-provided text must never expand tool permissions or data access.

## Voice

For the simplest MVP:

- Use device keyboard dictation.
- Store only the resulting text.
- Do not upload audio.

When CCE later adds its own audio transcription:

```text
Temporary upload
→ Transcription
→ User review
→ Transcript retained
→ Audio automatically deleted
```

## Label service and hardware boundary

All label output must use a common abstraction:

```text
LabelService
├── WebPdfLabelDriver
├── BrowserPrintLabelDriver
├── MobileSharePrintDriver
└── NativePrinterDriver
    └── Deferred until hardware selection
```

The MVP supports preview, PDF, browser print, and mobile share/print. A hardware spike must evaluate printer SDKs, Bluetooth or Wi-Fi support, control languages, label media, water resistance, UV resistance, and iOS/Android compatibility before a direct thermal driver is committed.

## Data portability

The storage model must support tenant exit from the beginning.

Before the first paid pilot, provide a tenant-authorized export containing:

```text
tenant.json
locations.json
things.json
events.json
narratives.json
collection.csv
```

A later asynchronous ZIP export will include original media organized by immutable `ThingUUID` with a manifest mapping each Thing to its accession number.

------

# 9. Hosting recommendation

## Firebase Hosting for the application MVP

The initial React/Vite application is a static single-page application, so Firebase Hosting remains the simplest deployment.

Firebase’s own comparison recommends regular Firebase Hosting for static sites and single-page applications, while App Hosting is more appropriate for dynamic, server-rendered applications. ([Firebase](https://firebase.google.com/docs/app-hosting/product-comparison?utm_source=chatgpt.com))

Use App Hosting later for a separate SEO-oriented public site if needed.

```text
apps/cce-app
    → Firebase Hosting

services/functions
    → Cloud Functions for Firebase

services/ai
    → Cloud Functions or Cloud Run

Firestore
    → Canonical operational data

Cloud Storage
    → Photos and temporary assets
```

------

# 10. Reconfiguration and release controls

## Remote Config

Firebase Remote Config can change application behavior and appearance without publishing a new application release. ([Firebase](https://firebase.google.com/docs/remote-config?utm_source=chatgpt.com))

Use it for:

- Feature flags
- Rollout percentages
- AI feature availability
- Model aliases
- Maximum image counts
- Prompt feature versions
- Experimental UX modes

Do not use client Remote Config for confidential prompts or secrets because client-delivered values are available to the client.

## Version everything that affects AI meaning

Version:

```text
Collection template
AI extraction schema
Prompt
Model alias
Knowledge pack
Label template
Privacy policy
Experience definition
```

Each AI result should record the versions used.

This allows older records to be reprocessed safely and explains why two AI runs may produce different proposals.

------

# 11. AI-assisted software development

The repository should itself be optimized for AI coding agents.

Firebase now publishes an MCP server and agent skills intended to give coding agents Firebase-specific tools and guidance. ([Firebase](https://firebase.google.com/docs/ai?hl=en&utm_source=chatgpt.com)) Genkit also includes a Developer UI for running and inspecting prompts, flows, tools, and evaluators. ([Genkit](https://genkit.dev/docs/python/devtools/?utm_source=chatgpt.com))

## Repository controls

Add:

```text
AGENTS.md
docs/architecture/
docs/adr/
packages/contracts/
packages/template-engine/
prompts/
evals/
test-data/golden/
```

### `AGENTS.md`

It should state:

- The authoritative governance document
- Tenant-isolation requirements
- AI permission classes
- Required confirmation rules
- Mobile-first acceptance requirements
- No direct AI database mutation
- No secrets in source
- Required tests before commit
- Naming and repository conventions

### Golden AI evaluation set

Create representative inputs:

```text
Clear orchid label
Unreadable orchid label
Contradictory narrative and label
Unknown orchid
Price without currency
Vague acquisition date
Location mentioned but not defined
Private information in narrative
Prompt-injection text inside a label
```

For each case, define expected:

- Extracted claims
- Uncertainty
- Follow-up question
- Forbidden actions
- Privacy behavior

## AI-generated code policy

AI coding agents may generate:

- Components
- Tests
- Template definitions
- Seed data
- Documentation
- Emulator fixtures
- CRUD adapters

AI-generated changes must not be accepted without automated validation for:

- TypeScript compilation
- Unit tests
- Firestore Security Rules
- Firebase emulator tests
- Tenant isolation
- Mobile viewport tests
- Accessibility
- AI schema validation
- Prompt evaluation

------

# 12. Revised monorepo

```text
collectors-curators-enthusiasts/
├── apps/
│   └── cce-app/
│       ├── src/
│       ├── public/
│       ├── android/
│       ├── ios/
│       ├── capacitor.config.ts
│       └── vite.config.ts
│
├── services/
│   ├── functions/
│   │   └── TypeScript command functions
│   ├── ai/
│   │   └── TypeScript Genkit flows
│   └── jobs-python/
│       └── Deferred batch and specialist jobs
│
├── packages/
│   ├── contracts/
│   │   └── Language-neutral JSON schemas
│   ├── template-engine/
│   ├── firebase-adapters/
│   ├── ui/
│   └── testing/
│
├── templates/
│   └── orchids/
│       ├── template.json
│       ├── experience.json
│       ├── extraction.schema.json
│       ├── labels.json
│       └── privacy.json
│
├── prompts/
├── evals/
├── test-data/
│   └── golden/
├── firebase/
│   ├── firestore.rules
│   ├── firestore.indexes.json
│   └── storage.rules
├── docs/
│   ├── architecture/
│   └── adr/
├── archive/
│   └── fastapi-prototype/
├── AGENTS.md
├── firebase.json
└── README.md
```

------

# 13. Revised MVP

The MVP remains narrow in business scope but includes the operational controls required for field use.

```text
One platform administrator
One PCO tenant
One PCO tenant administrator
Explicit tenant-managed locations
Offline photo and narrative drafts
Client-generated ThingUUID and LabelID
Server-assigned PCO accession number
Idempotent synchronization with conflict detection
Add, view, edit, move, archive, and restore orchids
Append-oriented lifecycle events
One governed AI-assisted intake flow
Taxonomy proposals with evidence and confidence
Permanent QR labels
PDF, browser, and mobile share/print
iOS, Android, and desktop operation
```

The primary intake flow is:

```text
Capture photo or typed/spoken story
→ Save locally, including while offline
→ Synchronize when connected
→ AI proposes display name and key facts
→ User reviews, corrects, or bypasses AI
→ Deterministic command creates or updates the Orchid
→ Accession number and remote QR record are activated
```

The user can bypass AI and enter the minimum required information manually.

Before the first paid pilot, CCE must also provide basic JSON/CSV tenant export and complete physical field testing on iPhone and Android.

------

# 14. Revised implementation order

## Phase 0 — Governance and contracts

1. Add and maintain `AGENTS.md`.
2. Add architecture decision records.
3. Establish JSON Schema contracts for Thing, DraftThing, command envelope, event, taxonomy, evidence, and AI proposal.
4. Define the Orchid template package.
5. Define AI proposal and confirmation contracts.
6. Define operation-ledger and conflict response contracts.
7. Archive the FastAPI prototype as reference-only material.

## Phase 1 — Mobile shell and offline infrastructure

1. Create the React/Vite application.
2. Add PWA support.
3. Add Capacitor configuration for iOS and Android.
4. Establish mobile navigation, design tokens, and accessibility baselines.
5. Implement `OfflineDraftStore` web and native adapters.
6. Implement local photo handling and draft recovery.
7. Implement client-generated ThingUUID and LabelID.
8. Add Firebase Emulator Suite support.

## Phase 2 — Security, tenancy, and synchronization

1. Configure Firebase Authentication.
2. Configure and enforce App Check.
3. Create the platform administrator, PCO tenant, and PCO tenant administrator.
4. Implement Firestore and Storage Security Rules.
5. Implement the trusted command layer.
6. Add transactional operation-ledger deduplication.
7. Add expected-version conflict detection.
8. Add tenant-isolation, retry, duplicate, and conflict tests.

## Phase 3 — Core CRUD, events, and labels

1. Implement location repositories and CRUD.
2. Implement Orchid query repositories.
3. Implement create, update, move, archive, and restore commands.
4. Allocate accession numbers during canonical create.
5. Implement append-oriented lifecycle events.
6. Implement `LabelService`.
7. Add PDF, browser, and mobile share/print drivers.
8. Implement QR lookup through `/p/{LabelID}`.

## Phase 4 — Governed AI intake and taxonomy

1. Generate configurable client-side image derivatives.
2. Implement the server-side Genkit intake flow.
3. Treat all narrative, OCR, and media content as untrusted evidence.
4. Validate strict structured AI output.
5. Implement taxonomy normalization and proposal contracts.
6. Implement evidence, confidence, conflict, and uncertainty display.
7. Implement one-question clarification.
8. Implement user review and deterministic confirmation commands.
9. Add golden-set and adversarial evaluations.

## Phase 5 — Pre-pilot validation and hardware spike

1. Build basic JSON/CSV tenant export.
2. Evaluate reference label printers and physical media.
3. Test iOS and Android printing paths.
4. Field-test offline capture and synchronization in greenhouse conditions.
5. Test failure recovery, retries, duplicate operations, and concurrent edits.
6. Validate usage limits, billing alerts, backup, and export recovery.

Post-MVP work includes native printer drivers, full media ZIP exports, public discovery, vector embeddings, and similarity matching.

------

## Final recommendation

The core technical choices should be:

```text
Frontend:
React + TypeScript + Vite + PWA + Capacitor

Mobile:
One codebase, browser plus native iOS/Android shells

Database:
Firestore for the mobile-first MVP

Backend:
Cloud Functions command layer; no FastAPI

AI:
Server-side TypeScript Genkit with Vertex AI

Python:
Retained for later specialist and batch services,
not required in the initial critical path

Flexibility:
Versioned templates, JSON Schema contracts,
repository adapters, and command/query separation

Governance:
AI proposes; users confirm; deterministic code commits

Field resilience:
Offline drafts, explicit sync state, idempotent commands, and conflict review

Identity:
Client ThingUUID and LabelID; server accession number

Portability:
JSON/CSV export before paid pilot; complete media export later
```

The next development task should be **Phase 0 architecture controls**, not the React scaffold. This prevents the initial code from hardcoding orchids, Firestore, or AI behavior into components that later become difficult to reconfigure.
