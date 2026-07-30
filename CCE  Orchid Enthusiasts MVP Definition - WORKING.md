# CCE / Orchid Enthusiasts MVP Definition - WORKING

# Mobile Requirement: Orchid CRUD

All Orchid Thing CRUD workflows must be fully usable on both **iOS and Android** mobile devices.

## Supported approach

The MVP should use a **mobile-first responsive web application or Progressive Web App (PWA)** rather than requiring separate native iOS and Android applications.

```text
One application
├── Desktop browser
├── iPhone and iPad
└── Android phone and tablet
```

The implementation must support current mobile Safari and Chrome browsers.

Native applications may be introduced later without changing the underlying CCE APIs or Thing records.

------

## Required Orchid CRUD capabilities

### Create

A tenant administrator can create an orchid from a phone or tablet.

```text
Open Add Orchid
→ Enter or dictate orchid information
→ Select location
→ Save
→ Generate ThingUUID, LabelID, and accession number
→ Preview or print label
```

The mobile Create workflow must support:

- Large touch-friendly controls
- On-screen keyboard
- Voice-to-text using the device keyboard
- Collection and location selection
- Minimum required fields
- Automatic save protection
- Clear validation messages
- Portrait and landscape layouts

### Read

The mobile Orchid detail page must display:

- Orchid display name
- Accession number
- Current location
- Status
- LabelID
- QR label preview
- Optional orchid details
- Created and updated dates

Primary mobile actions:

```text
[Edit]
[Change Location]
[Print Label]
[Scan Another]
```

### Update

Users must be able to update an orchid on mobile, including:

- Display name
- Genus
- Species or grex
- Cultivar or clone
- Location
- Status
- Optional notes
- Acquisition information included in the MVP

Location changes must use defined tenant locations.

### Delete or archive

For the MVP, Orchid Things should normally be **archived**, not permanently deleted.

Mobile archive workflow:

```text
Open Orchid
→ More Actions
→ Archive Orchid
→ Confirm
```

Permanent deletion, when permitted for erroneous records, must require an additional confirmation and elevated permission.

------

## Mobile QR scanning

The mobile application must support scanning through:

1. The phone’s standard camera application
2. An in-application QR scanner

The QR code opens:

```text
https://orchid-enthusiasts.com/p/{LabelID}
```

When the user is authenticated and authorized, the page displays the tenant management view.

When the user is not authorized, the page displays only the permitted public or limited view.

------

## Mobile location workflow

A tenant administrator must be able to assign or change a location from a mobile device.

```text
Select Orchid
→ Change Location
→ Browse or search defined locations
→ Select Space / Area / Rack / Shelf / Slot
→ Confirm
```

Power-user scanning may later support:

```text
Scan Orchid
→ Scan Location
→ Confirm Move
```

The initial MVP must at minimum provide a touch-friendly location selector.

------

## Mobile label workflow

From the Orchid detail page, the user must be able to:

```text
Preview Label
→ Generate PDF
→ Open device print/share dialog
→ Print, save, or send PDF
```

The application does not need direct native printer-driver integration for the MVP.

The generated PDF must work with:

- iOS print and share functions
- Android print and share functions
- Desktop browsers

------

## Mobile interface requirements

The Orchid CRUD interface must provide:

- Responsive layouts beginning at approximately 320 pixels wide
- Minimum touch-target size appropriate for mobile use
- Large readable text
- High contrast
- No horizontal page scrolling
- No hover-only controls
- No required right-click actions
- Sticky Save or primary-action button where useful
- Clear success and error messages
- Confirmation before destructive actions
- Visible loading and save status
- Support for mobile browser back navigation
- Automatic handling of portrait and landscape orientation

Dense tables should convert into cards or stacked rows on mobile.

------

## Connectivity and session behavior

The MVP should tolerate normal mobile conditions, including:

- Temporary signal interruption
- Slow cellular connections
- Browser suspension when the user changes applications
- Accidental refresh or navigation

At minimum:

- Unsaved form data should be preserved locally during the active session.
- Duplicate submissions should be prevented.
- Save operations should provide clear confirmation.
- Failed saves should permit retry without re-entering the record.

Full offline CRUD synchronization is not required for the MVP.

------

## Mobile acceptance criteria

The mobile requirement is satisfied when the complete workflow can be performed on both an iPhone and an Android phone:

```text
1. Sign in as PCO tenant administrator.
2. Open the PCO tenant.
3. Create or select a location.
4. Add an orchid.
5. Edit the orchid.
6. Assign or change its location.
7. View the orchid record.
8. Generate the orchid label.
9. Open the print-ready PDF.
10. Scan the QR code and reopen the correct orchid.
11. Archive and restore the orchid.
```

The workflow must not require a desktop computer.

## Governing requirement

```text
Orchid Thing CRUD is mobile-first.

Every required MVP operation must work on iOS and Android
through the responsive CCE / Orchid Enthusiasts application.
```



## 1. MVP Purpose

The initial MVP will validate the core CCE experience using:

```text
Platform: Collectors–Curators–Enthusiasts (CCE)
Specialty Site: orchid-enthusiasts.com
Initial Tenant: PCO — Park City Orchids and More
Initial Collection Template: Orchids
```

The MVP should prove that an older or nontechnical collector can:

1. Add an orchid using photographs and a natural-language story.
2. Allow AI to organize the information.
3. Review a simple summary.
4. Print a QR plant label.
5. Scan the label to retrieve the orchid.
6. Add history and location changes.
7. Ask, “Tell me about this orchid.”
8. Privately manage the collection or selectively share an orchid.

The first release should not attempt to implement every CCE collection type or advanced nursery workflow.

------

# 2. Initial Platform Structure

```text
CCE Platform
├── Users
├── Tenants
│   └── PCO — Park City Orchids and More
│       ├── Members
│       ├── Locations
│       ├── Collections
│       ├── Orchids
│       ├── Label Templates
│       └── Tenant Settings
│
├── Collection Templates
│   └── Orchids
│
└── Specialty Sites
    └── orchid-enthusiasts.com
```

## Platform responsibilities

CCE provides:

- User accounts
- Tenant access
- Roles and permissions
- Collection management
- Location management
- Thing identity
- Narratives
- AI interpretation
- Photographs
- QR labels
- Search
- Sharing
- Audit history

## Orchid Enthusiasts responsibilities

Orchid Enthusiasts provides:

- Orchid-specific terminology
- Orchid intake prompts
- Orchid identification fields
- Orchid care and repotting guidance
- Orchid labels
- Orchid-specific history events
- Orchid similarity discovery
- Orchid-focused public presentation

------

# 3. Initial Tenant

## Tenant

```text
Tenant Name: Park City Orchids and More
Tenant Short Name: PCO
Tenant Type: Collector / Nursery
Default Specialty: Orchids
Default Privacy: Private
Default Currency: USD
Default Time Zone: America/Denver
```

## Initial member roles

### Owner

Can:

- Manage the tenant
- Manage members
- Manage locations
- Create and manage collections
- Add and edit orchids
- Print labels
- Change sharing
- Transfer or archive orchids
- Manage subscription and tenant settings

### Editor

Can:

- Add and edit orchids
- Add narratives
- Add photographs
- Record maintenance
- Update locations
- Print labels

### Viewer

Can:

- View tenant records
- Search orchids
- Scan labels
- Use “Tell me about this orchid”

The initial MVP may begin with one Owner account and add invitations later in the release.

------

# 4. Initial Locations

Locations must be explicitly created and managed.

```text
Space
└── Area
    └── Rack
        └── Shelf
            └── Slot
```

## Recommended initial PCO locations

```text
PCO Growing Facility
├── Main Growing Area
│   ├── Rack 1
│   │   ├── Shelf 1
│   │   └── Shelf 2
│   └── Rack 2
│       ├── Shelf 1
│       └── Shelf 2
│
├── Quarantine Area
│   └── Quarantine Rack
│
├── Flowering Area
│   └── Display Rack
│
└── Storage Area
```

PCO may rename or expand these locations.

A plant may be assigned to:

- A Space
- An Area
- A Rack
- A Shelf
- A Slot

Exact Slot assignment is optional.

------

# 5. Initial Collections

Collections are logical groups of orchids.

Recommended initial PCO collections:

```text
PCO Collections
├── Main Orchid Collection
├── Oakland Acquisition
├── Quarantine
├── For Sale
└── Archived Orchids
```

## Collection behavior

Each collection contains:

- Collection name
- Description
- Status
- Sharing default
- Default location
- Orchid records

A collection is not a physical location.

Example:

```text
Collection: Oakland Acquisition
Default Location: Main Growing Area
Default Sharing: Private
```

An orchid within the collection may have a different explicit location.

------

# 6. Orchid Thing Record

Each orchid is a CCE Thing using the Orchid collection template.

```text
Orchid
├── Permanent identity
├── Current collection
├── Current location
├── Current status
├── Narratives
├── Photographs
├── AI-organized knowledge
├── History
├── Label
└── Sharing
```

## Essential explicit information

The MVP requires only:

- Permanent Thing identity
- Tenant
- Collection
- Orchid display name or temporary name
- Current status
- Sharing level
- Label identifier
- Creation date

Location and photograph are strongly encouraged but may initially be omitted.

## Default orchid status

```text
ACTIVE
```

Other MVP statuses:

```text
QUARANTINE
FOR_SALE
RESERVED
TRANSFERRED
ARCHIVED
```

------

# 7. Primary Orchid Intake Experience

## Step 1 — Select a collection

The user selects:

```text
Main Orchid Collection
Oakland Acquisition
Quarantine
For Sale
```

The Orchid template is inherited from the collection.

## Step 2 — Take photographs

The user sees:

> Take a few pictures of this orchid.

Suggested photographs:

1. Whole plant
2. Flowers, when present
3. Existing plant tag
4. Roots or pot, when useful

The user may continue with one photograph or no photograph.

## Step 3 — Tell the story

Primary prompt:

> **Tell us about this orchid.**

Optional guidance:

> You can tell us what it is, where it came from, what you paid, how it is doing, or anything else you want to remember.

Example user narrative:

> Bought from Andy for $34.44. Good price, but it needs some TLC. The label says Golden Elf Sundust.

Voice input is transcribed. Only the transcript is retained.

## Step 4 — AI interpretation

CCE may organize the narrative as:

```text
Possible name:
Cymbidium Golden Elf ‘Sundust’

Acquisition:
Purchased from Andy

Price:
$34.44 USD

User assessment:
Good price

Condition:
Needs some care

Identification:
Based on existing label; not yet verified
```

## Step 5 — Major omission prompt

CCE asks only one useful follow-up question.

Example:

> Would you like to photograph the existing tag so we can check the name?

Other possible prompts:

> About when did you acquire it?

> What appears to need attention?

> Where are you keeping it?

The user may select:

```text
Answer
Skip
Not Sure
Finish
```

## Step 6 — Review

The user sees:

```text
Here is what we understood:

Cymbidium Golden Elf ‘Sundust’
Purchased from Andy for $34.44
You described it as a good price that needs some care.

Identification: Needs confirmation

[Looks Right]
[Change Something]
```

## Step 7 — Save and label

After saving:

```text
Your orchid has been added.

[Print Label]
[Add Another Orchid]
[View Orchid]
```

------

# 8. Orchid Label MVP

## Default label

```text
Cymbidium Golden Elf
‘Sundust’

PCO-2026-0001

[QR CODE]
```

## Label requirements

The MVP should support:

- One default orchid label
- One compact label option
- Print one label
- Print multiple selected labels
- PDF output
- Permanent QR code
- Label reprint history

The QR code opens the permanent Orchid Enthusiasts record.

```text
https://orchid-enthusiasts.com/p/{LabelID}
```

The QR code remains valid if the orchid is:

- Renamed
- Moved
- Reclassified
- Sold
- Transferred
- Archived

------

# 9. Scan and Lookup

The user may scan the QR using:

- A normal phone camera
- The Orchid Enthusiasts scanning screen

The record opens with:

```text
Primary photograph

Cymbidium Golden Elf ‘Sundust’
PCO-2026-0001

Current status: Active
Current location: Rack 1 / Shelf 2
Last activity: Added July 30, 2026
```

Primary actions:

```text
Tell Me About This Orchid
Add Information
Update Location
Record Care
Add Photos
Print Label
Share
```

------

# 10. “Tell Me About This Orchid”

This is the main AI read action.

Example response:

> This appears to be a Cymbidium Golden Elf ‘Sundust’. PCO acquired it from Andy for $34.44. The original narrative describes it as a good purchase that needs some care. Its identification is based on the existing label and has not yet been independently confirmed. It is currently assigned to Rack 1, Shelf 2. No repotting history has been recorded.

The response should distinguish:

```text
Confirmed
User stated
AI inferred
Unknown
Suggested next step
```

Suggested next actions:

```text
[Add More Information]
[Care Instructions]
[How Should I Repot It?]
[Update Location]
[Record Maintenance]
```

This action does not change the record.

------

# 11. Narrative Management

Users may:

- Create a narrative
- Append more information
- Update or correct a narrative
- Remove a narrative
- Restore a removed narrative when permitted

Example timeline:

```text
July 30, 2026
Bought from Andy for $34.44. Good price, but it needs some TLC.

August 3, 2026
Andy said the plant originally came from a nursery in California.

February 12, 2027
It produced two flower spikes.
```

Narratives remain available for future AI extraction.

------

# 12. Orchid History MVP

Initial history actions:

```text
ACQUIRED
MOVED
REPOTTED
WATERED
FERTILIZED
TREATED
INSPECTED
FLOWERED
DIVIDED
PHOTOGRAPHED
LISTED_FOR_SALE
TRANSFERRED
ARCHIVED
GENERAL_NOTE
```

The normal user does not need to select from a technical list.

Prompt:

> **What happened with this orchid?**

User:

> I repotted it in medium bark and removed several dead roots.

CCE proposes:

```text
Activity: Repotted
Date: Today
Medium: Medium bark
Observation: Several dead roots removed
```

The user confirms before the event is saved.

------

# 13. Location Update MVP

## Standard mode

Prompt:

> **Where is this orchid now?**

The user may:

- Choose an existing location
- Scan a location code
- Speak or type a location

Example:

> Rack one, second shelf.

CCE resolves the statement to an existing location and asks for confirmation when necessary.

## Power-user mode

```text
Scan Orchid
→ Scan Rack or Shelf
→ Enter Slot
→ Confirm
→ Update location
→ Create history event
→ Generate narrative
```

Generated narrative:

> This orchid was moved to Rack 1, Shelf 2, Slot 3.

Undefined locations must not be silently created.

------

# 14. Care and Guidance

The MVP should support:

> What are the best care instructions?

> How should I pot this orchid?

> What may be wrong with it?

Guidance uses:

- Orchid identification
- Narratives
- Photographs
- Location
- Current condition
- Prior care history

The response should state:

- What is known
- What is assumed
- Recommended action
- What additional information would improve the advice

Guidance does not become history until the user confirms that the work was completed.

------

# 15. Photographs

The MVP should support:

- Upload from phone
- Direct camera capture
- Multiple photos per orchid
- Primary photo selection
- Caption
- Photo category
- Capture timestamp
- Upload timestamp
- Rotate
- Crop
- Visibility setting

Initial categories:

```text
WHOLE_PLANT
FLOWER
LABEL
ROOTS
POT
CONDITION
OTHER
```

The original photograph should be retained when an edited version is created.

------

# 16. Search

Basic search should include:

- Display name
- Accession number
- Label identifier
- Narrative text
- Collection
- Location
- Status
- Source
- Tag or label text

Example searches:

```text
Golden Elf
Bought from Andy
Needs TLC
Rack 1
For sale
Oakland
```

AI-assisted natural-language search may support:

> Show orchids bought from Andy.

> Find orchids that need care.

> Show orchids without a confirmed name.

------

# 17. Sharing

Default:

```text
PRIVATE
```

MVP sharing options:

```text
PRIVATE
TENANT
PLATFORM
SHARED_LINK
PUBLIC
```

The user selects exactly what will be shared.

Public and shared views should exclude by default:

- Exact location
- Purchase price
- Private valuation
- Internal notes
- Personal contact information

The user may preview the shared page before publishing.

------

# 18. Similar Orchid Discovery

When an orchid is shared at the PLATFORM or PUBLIC level, CCE may compare it with other shared orchids.

Prompt:

> We found similar orchids shared by other members. Would you like to see them?

Actions:

```text
[See Similar Orchids]
[Not Now]
```

A future connection workflow may add:

```text
[Connect with Collector]
```

For the first MVP, viewing similar shared orchids is sufficient. Direct member messaging may be deferred.

------

# 19. MVP Screens

## Public and account screens

1. Orchid Enthusiasts home
2. Sign in
3. Create account
4. Shared orchid page
5. QR orchid page

## Tenant application

1. Tenant dashboard
2. Collections
3. Orchid list
4. Add orchid
5. Orchid detail
6. Scan
7. Locations
8. Labels
9. Search
10. Tenant settings

## Orchid detail tabs or sections

```text
Overview
Story
Photos
History
Location
Label
Sharing
More Details
```

Standard users see a simple overview.

Power users may open **More Details**.

------

# 20. PCO Dashboard

The PCO dashboard should initially show:

```text
Total Orchids
Orchids Added Recently
Orchids Needing Review
Orchids in Quarantine
Orchids for Sale
Labels Not Yet Printed
Recent Activity
```

Primary actions:

```text
[Add Orchid]
[Scan Orchid]
[Print Labels]
[Search Collection]
```

------

# 21. Tenant Administration

Initial settings:

- Tenant name and logo
- Default privacy
- Default currency
- Time zone
- Accession-number format
- Collections
- Locations
- Members and roles
- Default label template
- AI assistance level

Recommended accession format:

```text
PCO-{YEAR}-{SEQUENCE}

Example:
PCO-2026-0001
```

------

# 22. MVP Privacy Rules

The MVP follows the authoritative **CCE Solution Governance and Experience Guidelines**.

Required privacy controls:

- Private by default
- Voice audio deleted after transcription
- Exact locations private by default
- Financial information private by default
- Sharing requires explicit action
- Public preview before publication
- Private data excluded from similarity matching
- User-controlled removal of public access
- Tenant access enforced by role
- Audit history for significant actions

------

# 23. MVP AI Rules

AI may:

- Transcribe voice
- Read orchid labels
- Extract information from narratives
- Suggest an orchid name
- Suggest acquisition information
- Suggest condition descriptions
- Ask one high-value follow-up question
- Generate a summary
- Generate care guidance
- Generate label content
- Search narratives
- Find similar shared orchids

AI must obtain confirmation before:

- Changing location
- Changing collection
- Changing status
- Publishing an orchid
- Listing an orchid for sale
- Recording a transfer
- Archiving
- Replacing a confirmed identification

------

# 24. MVP Success Criteria

The MVP is successful when a PCO user can complete this workflow without training:

```text
Create account
→ Open PCO tenant
→ Select collection
→ Photograph orchid
→ Speak or type story
→ Review AI summary
→ Save orchid
→ Print QR label
→ Scan QR label
→ Ask “Tell me about this orchid”
→ Add a care or location event
```

Operational targets:

- Orchid creation works on a phone
- A basic record can be created in under two minutes
- Optional questions can always be skipped
- QR lookup works from the standard phone camera
- Labels print accurately from PDF
- Narratives remain editable
- Location changes create readable history
- AI clearly distinguishes user statements from inference
- Sharing remains private unless explicitly changed

------

# 25. Out of Scope for the First MVP

Defer:

- Watches and dolls
- General plant template
- E-commerce checkout
- Payment processing
- Full nursery inventory
- Shipping
- Accounting
- Automated CITES management
- Environmental sensors
- Automated watering
- Native mobile applications
- Complex social network
- Direct member chat
- Formal orchid registration verification
- Formal appraisals
- AI-only verified identification
- Advanced breeding management
- Detailed production costing

------

# 26. MVP Release Sequence

## Release 1 — Foundation

- CCE user accounts
- PCO tenant
- Owner role
- Orchid collection template
- Collections
- Explicit locations
- Basic privacy

## Release 2 — Orchid records

- Add orchid
- Narrative input
- Voice transcription
- Photo upload
- AI summary
- Orchid detail page
- Search

## Release 3 — Labels and scanning

- Label identifiers
- QR lookup
- PDF labels
- Batch label printing
- Scan screen

## Release 4 — History and guidance

- Maintenance history
- Location changes
- “Tell me about this orchid”
- Care guidance
- Narrative append/update/remove

## Release 5 — Sharing and discovery

- Shared orchid pages
- Platform visibility
- Similar shared orchids
- Public preview
- Privacy controls

------

# 27. MVP Governing Experience

```text
The user experiences:

Photo
→ Story
→ Helpful question
→ Clear summary
→ Save
→ Label
→ Scan
→ Ongoing conversation
CCE provides:

Identity
→ Knowledge preservation
→ AI interpretation
→ Explicit operational control
→ History
→ Guidance
→ Search
→ Privacy
→ Sharing
```

The MVP should feel like a simple orchid assistant while establishing the reusable CCE foundation for future Plants, Watches, Dolls, and other specialty collection templates.

# Google Cloud Platform Hosting

## 1. Hosting requirement

The CCE / Orchid Enthusiasts MVP will be hosted entirely on **Google Cloud Platform**.

```text
Platform: CCE
Specialty Site: orchid-enthusiasts.com
Initial Tenant: PCO — Park City Orchids and More
Cloud Provider: Google Cloud Platform
```

The MVP will use managed GCP services to minimize infrastructure administration and provide a path from the initial single-tenant deployment to the future multi-tenant CCE platform.

------

## 2. MVP GCP architecture

```text
iOS / Android / Desktop Browser
              │
              ▼
orchid-enthusiasts.com
              │
              ▼
Global HTTPS Load Balancer
              │
              ▼
Cloud Run
Mobile-first web application and API
              │
       ┌──────┼────────┐
       ▼      ▼        ▼
Identity   Cloud SQL   Secret Manager
Platform   PostgreSQL
              │
              ▼
        Cloud Storage
      Label PDFs and exports
```

Cloud Run is the recommended application runtime because it provides a fully managed container platform with minimal infrastructure to operate. Google recommends considering serverless runtimes such as Cloud Run before Kubernetes when the workload is suitable.

------

## 3. Required GCP services

| Requirement                         | GCP service                               |
| ----------------------------------- | ----------------------------------------- |
| Responsive web application and API  | Cloud Run                                 |
| User authentication                 | Identity Platform                         |
| Application database                | Cloud SQL for PostgreSQL                  |
| Label PDF and export storage        | Cloud Storage                             |
| Credentials and application secrets | Secret Manager                            |
| Container images                    | Artifact Registry                         |
| Application deployment              | Cloud Build or GitHub Actions             |
| Logs and metrics                    | Cloud Logging and Cloud Monitoring        |
| Domain, HTTPS, and routing          | Global external Application Load Balancer |
| DNS                                 | Cloud DNS or existing domain registrar    |

Google currently recommends a global external Application Load Balancer for mapping custom domains to Cloud Run. This also provides a future path to Cloud CDN and Cloud Armor.

------

## 4. Application deployment

Deploy one Cloud Run application for the MVP.

```text
Cloud Run service:
cce-orchid-enthusiasts

Responsibilities:
├── Mobile and desktop user interface
├── Platform administration
├── PCO tenant administration
├── Location CRUD
├── Orchid CRUD
├── Accession-number generation
├── QR-code generation
├── Label preview
├── PDF label generation
└── QR lookup
```

The application may initially combine the frontend and backend API in one deployable service.

This keeps the MVP simple:

```text
One source repository
One container
One Cloud Run service
One database
```

The frontend and API may be separated later without changing the product model.

------

## 5. Authentication

Use **Google Cloud Identity Platform** for the two initial authenticated roles:

```text
Platform Administrator
Tenant Administrator
```

Identity Platform supports authentication for web, mobile, API, and multi-tenant SaaS applications.

For the MVP:

- Create one platform user.
- Assign the user the Platform Administrator role.
- Create or associate one user as the PCO Tenant Administrator.
- Store CCE tenant and role associations in the CCE application.
- Validate Identity Platform tokens on every authenticated request.
- Require HTTPS.
- Do not create a separate Identity Platform tenant for PCO during the MVP.

CCE tenancy remains an application-level concept:

```text
Identity Platform UserUUID
        │
        ▼
CCE User
        │
        ▼
TenantUUID: PCO
        │
        ▼
Role: Tenant Administrator
```

This avoids coupling the CCE tenant model to the authentication provider’s tenant model.

------

## 6. Database

Use **Cloud SQL for PostgreSQL**.

The MVP database will contain:

- Platform user references
- Tenant
- User-to-tenant role association
- Locations
- Collection
- Orchids
- Orchid location assignments
- Accession-number sequence
- Label identities
- Label-generation history
- Audit information

Cloud Run and Cloud SQL should be deployed in the same selected GCP region to reduce latency and avoid unnecessary network transfer.

Required database protections:

- Automated backups
- Point-in-time recovery
- Encrypted connections
- Least-privilege application account
- Separate migration and application credentials
- No public database access unless explicitly required
- TenantUUID on all tenant-owned records

Google provides supported patterns for connecting Cloud Run to Cloud SQL while storing credentials in Secret Manager.

------

## 7. File storage

Use a private Cloud Storage bucket for generated files.

```text
cce-orchid-mvp-files
├── tenants
│   └── {TenantUUID}
│       ├── labels
│       │   └── {LabelJobUUID}.pdf
│       └── exports
```

For the MVP, Cloud Storage is used for:

- Generated label PDFs
- Future tenant exports
- Optional generated QR assets

Public access must be disabled.

The application provides authorized downloads or short-lived signed access when required.

------

## 8. Domain structure

Recommended domain routing:

```text
https://orchid-enthusiasts.com
    Public specialty-site entry point

https://app.orchid-enthusiasts.com
    Authenticated CCE application

https://orchid-enthusiasts.com/p/{LabelID}
    Permanent QR lookup
```

The same Cloud Run application may initially serve all three routes.

The load balancer will provide:

- Managed HTTPS
- Domain routing
- Redirect from HTTP to HTTPS
- Redirect from `www` to the canonical domain
- Future Cloud Armor support
- Future routing to additional CCE services

------

## 9. Mobile delivery

The Cloud Run application will deliver a mobile-first responsive web application or PWA.

It must support:

```text
iOS Safari
iPadOS Safari
Android Chrome
Desktop Chrome
Desktop Edge
Desktop Safari
```

No native iOS or Android hosting infrastructure is required for the MVP.

The same HTTPS application and APIs serve all devices.

------

## 10. Security baseline

### Public access

Only these routes should be publicly reachable without authentication:

```text
/
 /sign-in
 /p/{LabelID}
 /health
```

The QR route reveals only information permitted by the Thing’s sharing rules.

### Authenticated access

All administration and Orchid CRUD routes require an Identity Platform session.

### Service identity

The Cloud Run service must use a dedicated service account with only the permissions needed to:

- Connect to Cloud SQL
- Read required secrets
- Read and write the designated Cloud Storage bucket
- Write logs and metrics

Google recommends using a service identity with the minimum required permissions when Cloud Run connects to other GCP services.

### Secrets

Store outside source code:

- Database credentials
- Session-signing configuration
- Identity Platform configuration requiring protection
- PDF-generation settings requiring secrets
- Future AI provider credentials

Use Secret Manager and grant access only to the Cloud Run service account.

------

## 11. GCP environments

Use separate GCP projects:

```text
cce-orchid-dev
    Development and testing

cce-orchid-prod
    Production
```

Each project should have separate:

- Cloud Run service
- Cloud SQL database
- Identity Platform configuration
- Cloud Storage bucket
- Secrets
- Service accounts
- Logs
- Domain configuration

Production data must not be copied into development unless it has been appropriately sanitized.

------

## 12. Deployment workflow

```text
Developer commits code
        ↓
Automated tests
        ↓
Container build
        ↓
Artifact Registry
        ↓
Database migration
        ↓
Cloud Run deployment
        ↓
Health check
        ↓
Production traffic
```

Initial deployment may use:

- GitHub repository
- GitHub Actions or Cloud Build
- Artifact Registry
- Cloud Run revisions

Each deployment should create an immutable Cloud Run revision that can be rolled back.

------

## 13. Logging and monitoring

Enable:

- Application request logs
- Authentication failure logs
- Database error logs
- Label-generation failures
- QR lookup failures
- Administrative audit events
- Cloud Run latency and error metrics
- Cloud SQL health and storage metrics

Initial alerts should cover:

```text
Cloud Run unavailable
High server-error rate
Cloud SQL unavailable
Database storage approaching limit
Repeated authentication failures
Label-generation failures
```

------

## 14. MVP GCP acceptance criteria

The GCP deployment is complete when:

1. `orchid-enthusiasts.com` is served over HTTPS.
2. The application runs on Cloud Run.
3. The platform administrator can authenticate through Identity Platform.
4. The platform administrator can create or access PCO.
5. The PCO tenant administrator can authenticate.
6. PCO locations can be created and stored in Cloud SQL.
7. An orchid can be created, viewed, edited, archived, and restored from iOS and Android.
8. The system generates a permanent LabelID and accession number.
9. A label PDF is generated and can be opened through iOS, Android, and desktop print dialogs.
10. The QR code resolves to the correct orchid.
11. Tenant data is isolated by TenantUUID.
12. Database backups are enabled.
13. Application secrets are stored in Secret Manager.
14. Logs and basic alerts are operational.

------

## 15. MVP hosting principle

```text
Cloud Run
    runs the CCE / Orchid Enthusiasts application

Identity Platform
    authenticates users

Cloud SQL
    stores tenants, locations, orchids, and labels

Cloud Storage
    stores generated files

Secret Manager
    protects credentials

Google Cloud Load Balancing
    provides HTTPS and domain routing
```

The GCP deployment should remain small and economical for the MVP while establishing a production-compatible foundation for additional tenants, templates, specialty sites, media, narratives, and AI services.