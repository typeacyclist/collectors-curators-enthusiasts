# CCE Solution Governance and Experience Guidelines - AUTHORITATIVE

## 1. Purpose

Collectors–Curators–Enthusiasts, or **CCE**, is a platform for preserving, organizing, understanding, managing, and sharing knowledge about physical things.

CCE supports broad collection types through configurable collection templates. Initial templates include:

- General plants
- Orchids
- Watches
- Dolls

Specialty experiences, such as **orchid-enthusiasts.com**, operate on the CCE platform and use specialized terminology, prompts, guidance, and presentation while retaining the same underlying governance principles.

These guidelines establish how CCE solutions will be designed, how users will interact with them, how artificial intelligence will be used, and how privacy, accuracy, safety, and user control will be maintained.

------

# 2. Governing vision

CCE should make it easy for a person to preserve the story and knowledge surrounding a physical thing.

The normal experience should feel like speaking with a knowledgeable assistant rather than completing an inventory database.

```text
User tells the story
→ CCE preserves the story
→ AI organizes and enriches the information
→ The user confirms important actions
→ The record becomes more useful over time
```

The platform should serve both:

- Older, less technical, or occasional users who want a simple conversational experience
- Experienced collectors, curators, and power users who need structured data, advanced controls, bulk operations, and detailed records

Both experiences must operate on the same underlying Thing record.

------

# 3. Core design principles

CCE solutions will be:

## Narrative-first

Users should be able to begin by typing or speaking naturally.

Primary prompts include:

> Tell us about this thing.

> How did you find or acquire it?

> Is there anything special about its history?

The platform should preserve what the user says before attempting to force the information into predefined fields.

## AI-forward

AI should help users:

- Transcribe spoken information
- Interpret narratives
- Identify important facts
- Detect omissions
- Suggest follow-up questions
- Generate readable summaries
- Produce labels
- Provide collection-specific guidance
- Find similar shared things
- Convert narratives into structured information
- Reprocess older narratives as templates and AI capabilities improve

## Operationally explicit

Information that controls system behavior must remain explicit.

This includes:

- Tenant association
- Collection assignment
- Location assignment
- Current status
- Sharing level
- Label assignment
- Sale or transfer
- Archive state
- User permissions

AI may suggest these actions, but it must not silently perform consequential changes.

## Evidence-backed

Important information should remain connected to its source, such as:

- User narrative
- Voice transcript
- Photograph
- Existing label
- Receipt
- Certificate
- Document
- System event
- External reference

## Confidence-aware

CCE must distinguish:

- Confirmed information
- User-stated information
- Observations
- AI-extracted information
- AI inference
- AI deduction
- Unknown or conflicting information

The platform should use understandable terms such as:

- Confirmed
- Likely
- Possible
- Unknown
- Needs review

Numeric confidence scores should remain available to power users but hidden from standard users unless useful.

## Privacy-controlled

Users and tenants control what is shared, with whom, and for what purpose.

## Reversible and traceable

Important changes should be undoable or restorable where practical. Previous values, histories, and source narratives should not be silently erased.

## Progressively disclosed

The interface should reveal complexity only when the user needs it.

------

# 4. How CCE solutions will be created

## 4.1 Build around shared capabilities

All collection templates should begin with common capabilities for physical things:

- Identification
- Acquisition and provenance
- Location
- Labels
- Photographs
- Evaluation
- Value
- Maintenance
- Transfer
- Sale
- Sharing
- Archive
- Narrative history

Specialized templates should add only information and workflows unique to that collection type.

Examples:

- Orchids add grex, clone, parentage, flowering, and culture
- Watches add movement, case, dial, reference, and service history
- Dolls add maker, series, materials, clothing, markings, and restoration
- General plants add botanical names, cultivation, health, and growth information

## 4.2 Avoid field-heavy design

New features should not begin with the question:

> What fields should the user complete?

They should begin with:

> What is the simplest question or action that allows the user to provide this information naturally?

The structured backend may be detailed, but the standard interface should remain conversational and task-oriented.

## 4.3 Preserve source information

Source narratives, photographs, documents, and system events should remain available even when structured metadata is later added.

Structured information should improve the record without replacing the source story.

## 4.4 Use templates for specialization

Collection templates should control:

- Terminology
- Suggested prompts
- Evaluation names
- Maintenance event names
- Label content
- Search behavior
- Guidance
- Similarity matching
- Recommended photographs
- Advanced structured information

Templates should not create separate, incompatible platforms.

## 4.5 Specialty sites remain part of CCE

A specialty site may provide:

- Specialized branding
- A default collection template
- Domain-specific prompts
- Domain-specific knowledge
- Specialized public galleries
- Relevant member discovery

Specialty sites must retain CCE’s shared identity, privacy, security, user, tenant, and governance model.

------

# 5. Standard user experience

## 5.1 Primary interaction

The standard workflow should be:

```text
Select or enter a collection
→ Take or upload photographs
→ Tell us about the thing
→ Review a short AI summary
→ Save
→ Print a label, when applicable
```

A user should be able to create a useful Thing record with:

- A photograph
- A short typed narrative or voice transcript
- A collection assignment
- A system-generated identity

Missing optional information should not block creation.

## 5.2 Voice interaction

Users may speak instead of typing.

The workflow is:

```text
User speaks
→ CCE transcribes
→ User may review or correct the transcript
→ Transcript is retained
→ Temporary voice recording is deleted
```

CCE retains the transcript, not the voice recording.

The platform should not create or retain voice biometric profiles.

## 5.3 Guided completion

After processing the user’s initial narrative, CCE may suggest one useful follow-up question.

Example:

> You mentioned that it needs some care. What appears to need attention?

The user may select:

- Answer
- Skip
- Not sure
- Finish

CCE should ask only about material omissions, such as:

- What the thing is
- Where it came from
- When it was acquired
- Where it is currently located
- Major condition concerns
- Important template-specific identification

CCE should not present a long sequence of mandatory questions.

## 5.4 Easy correction

The standard interface should allow users to:

- Add more information
- Correct the narrative
- Append to the story
- Remove a narrative
- Correct an AI summary
- Change the current name
- Update the current location
- Record an action

The user should not need to understand structured metadata to correct the record.

## 5.5 “Tell me about this thing”

Every Thing should support a primary read action:

> Tell me about this thing.

CCE should produce a current, readable summary using:

- Narratives
- Confirmed information
- Photos and documents
- Acquisition history
- Current location and status
- Maintenance and evaluation history
- AI-derived information
- Missing or uncertain information

The response should distinguish what is confirmed from what is inferred.

It must not change the record.

------

# 6. Power-user experience

CCE must support advanced users without exposing complexity to everyone.

Power-user capabilities may include:

- Complete structured metadata
- Direct field editing
- Source and confidence review
- Batch updates
- Barcode and QR scanning
- CSV import and export
- Advanced search and filters
- Template configuration
- Label configuration
- Bulk label printing
- Conflict resolution
- Reprocessing and re-extraction
- Saved views
- Collection-specific reports
- Detailed audit history

Power-user mode should be optional and user-controlled.

------

# 7. Narrative governance

## 7.1 Narrative is durable source knowledge

Narratives preserve:

- Personal stories
- Acquisition history
- Informal observations
- Uncertain identifications
- Condition descriptions
- Memories
- Explanations
- Context that may not yet fit a structured field

Example:

> Bought from Andy for $34.44. Good price, but it needs some TLC.

CCE may extract:

- Acquisition method: Purchase
- Seller: Andy
- Purchase price: $34.44
- User assessment: Good price
- Condition note: Needs TLC

The original statement remains available.

## 7.2 Narrative operations

Users may:

- Create a narrative
- Update a narrative
- Append additional information
- Remove a narrative
- Restore a removed narrative when permitted

Previous versions should remain in the audit history unless permanent removal is required for privacy, legal, or account-deletion purposes.

## 7.3 System-generated narratives

CCE may generate readable narratives from explicit system actions.

Example:

> On July 30, 2026, this orchid was moved to Greenhouse 1, Rack 3, Shelf B, Slot 3.

A system-generated narrative must indicate that it was created from a structured event.

It should not be represented as user-authored text.

------

# 8. Explicit operational information

Some information must be deliberately defined or confirmed.

## 8.1 Locations

Locations must be explicit tenant-managed entities.

CCE may support:

```text
Space
→ Area
→ Rack
→ Shelf
→ Slot
```

A user may say:

> Put it on Rack 3, Shelf B, Slot 3.

CCE may resolve that statement to an existing location, but it must not silently create or assign an undefined location.

When a location cannot be resolved, the user should be offered:

- Choose an existing location
- Create a new location
- Leave the location unassigned

## 8.2 Collection assignment

A Thing must belong to a defined collection.

AI may suggest a collection based on the narrative, but the assignment must resolve to an explicit collection.

## 8.3 Status

Statuses such as active, for sale, transferred, and archived affect system behavior and must be explicit.

AI may suggest a status change but must obtain confirmation before applying it.

## 8.4 Sharing

Sharing must always be explicit.

The user must control whether a Thing is:

- Private
- Visible to tenant members
- Visible to platform members
- Available through a shared link
- Publicly visible
- Listed for sale

## 8.5 Transfer and sale

A sale is a type of transfer.

The system must confirm:

- Recipient or destination
- Transfer type
- Date
- Price and currency, when applicable

A transferred Thing should remain in the historical record.

## 8.6 Archive

Archive is a status, not deletion.

Archived Things should retain:

- Identity
- Narratives
- Photos
- Documents
- History
- Labels
- Provenance

------

# 9. AI governance

## 9.1 Permitted uses of AI

AI may:

- Transcribe voice
- Read visible label or document text
- Extract facts from narratives
- Suggest structured metadata
- Classify and summarize information
- Identify likely omissions
- Generate follow-up prompts
- Produce labels and descriptions
- Find similar shared Things
- Generate guidance
- Detect conflicts
- Suggest relationships
- Reprocess older records
- Create public or sale descriptions from approved information

## 9.2 AI must distinguish source types

AI should distinguish among:

- User statement
- User observation
- User opinion
- Information read from an image
- Information read from a document
- AI inference
- AI deduction
- External verification
- System-generated information

## 9.3 AI must not present inference as fact

Examples:

> The user stated that the plant needs TLC.

is acceptable.

> The plant has root rot.

is not acceptable unless supported by sufficient evidence or confirmed evaluation.

## 9.4 AI may extract explicit information

When a statement is clear:

> I bought it from Andy for $34.44.

AI may extract:

- Acquisition method: Purchase
- Seller: Andy
- Price: $34.44

## 9.5 AI should suggest consequential actions

AI should request confirmation before:

- Assigning or changing a location
- Changing a collection
- Publishing information
- Creating a public listing
- Marking a Thing as sold
- Recording a transfer
- Archiving
- Removing significant content
- Changing a confirmed identity

## 9.6 AI must preserve uncertainty

When information is uncertain, CCE should retain that uncertainty.

Examples:

- Possibly German
- Label may be incorrect
- Likely from the 1980s
- Identification not confirmed
- Condition needs review

## 9.7 AI-generated guidance

Questions such as:

> How should I pot this plant?

> What are the best care instructions?

are guidance requests.

AI guidance should clearly distinguish:

- Known information
- Assumptions
- Recommendation
- Confidence
- Information that would improve the answer

Guidance does not become history until the user confirms that an action was completed.

## 9.8 Reprocessing

CCE may reprocess existing narratives and media when:

- Templates gain new fields
- AI improves
- New evidence is added
- A user requests re-analysis
- Conflicts are detected

Reprocessing must not silently replace user-confirmed information.

------

# 10. Accuracy and confidence

## 10.1 Accuracy hierarchy

CCE should generally prioritize:

```text
User-confirmed information
→ Verified external information
→ Explicit user statements
→ Evidence from labels or documents
→ High-confidence extraction
→ AI inference
→ AI deduction
```

This hierarchy is contextual. A later authoritative document may correct an earlier user recollection.

## 10.2 Conflicting information

CCE should preserve conflicting statements and ask the user to resolve important conflicts.

Example:

> The existing label says Golden Elf ‘Sundust’, but your narrative suggests Golden Boy. Which should be shown as the current identification?

Options should include:

- Use the first identification
- Use the second identification
- Keep the identification uncertain

## 10.3 Field-level traceability

Power users should be able to see:

- Current value
- Prior values
- Source
- Confidence
- Confirmation status
- Date changed

## 10.4 Avoid false precision

CCE should not infer:

- Exact dates from vague statements
- Exact values from broad descriptions
- Verified identity from visual similarity alone
- Exact location from an uncertain narrative
- Ownership or transfer without confirmation

------

# 11. Privacy by design

## 11.1 Private by default

New Things, narratives, photographs, values, locations, and documents should be private by default unless the tenant has explicitly selected another default.

## 11.2 Minimum necessary disclosure

Public and shared views should include only information necessary for the selected purpose.

Examples:

### Public showcase

May include:

- Display name
- Selected photographs
- General story
- Public history

Should normally exclude:

- Exact physical location
- Purchase price
- Private valuation
- Personal contact information
- Internal notes
- Private documents

### Sale listing

May include:

- Description
- Selected photos
- Asking price
- General location
- Seller-controlled contact method

Should exclude unrelated private history.

## 11.3 Field-level privacy

Privacy should be controllable by category or field where practical.

Examples:

- Public name, private price
- Public photographs, private location
- Public flowering history, private acquisition source
- Public sale listing, private owner identity

## 11.4 Voice privacy

Voice audio should be temporary and deleted after transcription.

Only the transcript is retained.

## 11.5 AI privacy

Private tenant information should not be exposed to other members through:

- Similarity matching
- Public summaries
- Search
- AI guidance
- Generated social content
- Connection recommendations

## 11.6 Location protection

Exact locations should remain private by default.

The platform may display broader approved information such as:

- Utah
- Salt Lake area
- Private collection
- Commercial greenhouse

without revealing exact placement.

## 11.7 User control

Users should be able to:

- Review what will be shared
- Preview public pages
- Change sharing settings
- Remove public listings
- Disconnect from another member
- Block connection requests
- Export their information
- Request account or tenant deletion

------

# 12. Similarity and member connection

CCE may identify similar Things that members have chosen to share.

Suggested prompt:

> We found similar things shared by other members. Would you like to see them or connect with their collectors?

Similarity may consider:

- Name
- Classification
- Maker or grower
- Model, grex, cultivar, series, or edition
- Visual similarity
- Narrative meaning
- Acquisition history
- Condition
- Time period

Only appropriately shared Things may be included.

## Connection consent

CCE should not expose member contact information automatically.

A connection should begin through a controlled request.

Members may:

- Accept
- Decline
- Block
- Cancel

## Similarity transparency

The system should provide a simple reason:

> Similar because both records appear to be Cymbidium Golden Elf ‘Sundust’.

It should not imply that similarity proves identity.

------

# 13. Label and QR governance

Labels provide a durable connection between a physical Thing and its CCE record.

A label may include:

- QR code
- Label identifier
- Accession number
- Display name
- Collection name
- Tenant name
- Template-specific information

The QR should reference a permanent identifier.

Renaming, moving, sharing, selling, or archiving a Thing should not invalidate the QR.

Labels should not expose private information unless explicitly configured.

------

# 14. Barcode and scan workflows

Power users may use scans for fast operational actions.

Example:

```text
Scan Thing
→ Scan Rack or Shelf
→ Enter Slot 3
→ Confirm
→ Update location
→ Create history event
→ Generate readable narrative
```

Scan workflows must verify:

- Active tenant
- User permission
- Thing identity
- Location identity
- Valid location relationship
- Consequential action confirmation when required

A scan should not create an undefined location or move a Thing across tenants without an explicit transfer workflow.

------

# 15. Generated views and content

CCE may generate multiple views from the same Thing knowledge:

- “Tell me about this thing” summary
- Public profile
- Social preview
- Sale listing
- Label
- Condition summary
- Insurance report
- Curator record
- Care instructions
- Provenance summary

Generated views should not become separate competing records.

They should be regenerated from approved source information and current structured state.

------

# 16. Accessibility and ease of use

CCE is designed for users with varying technical confidence, vision, dexterity, and familiarity with digital systems.

The standard experience should use:

- Large, readable text
- Clear action labels
- Limited choices per screen
- Voice input
- Mobile camera capture
- One-question-at-a-time prompts
- Plain-language confirmations
- Easy correction
- Clear undo and restore options
- Minimal required information
- Consistent navigation
- Visible save status

Avoid:

- Dense forms
- Technical terminology
- Long mandatory setup
- Unexplained icons
- Hidden destructive actions
- Numeric confidence scores in standard mode
- Complex nested settings during normal intake

------

# 17. Safety and responsible guidance

CCE may provide care, maintenance, restoration, valuation preparation, or storage guidance.

The platform should:

- State assumptions
- Avoid presenting uncertain advice as definitive
- Recommend professional assistance when appropriate
- Warn users before potentially destructive restoration or maintenance
- Avoid implying authentication, appraisal, or certification without appropriate evidence
- Avoid encouraging actions that could damage rare, historic, fragile, or valuable objects

Examples:

- A watch should not be polished based solely on AI guidance
- A rare doll should not be cleaned with chemicals without material-specific verification
- A plant treatment should not be recommended without sufficient context
- An orchid should not be assigned a verified name based only on visual similarity

------

# 18. Auditability and history

CCE should maintain understandable histories for:

- Narrative changes
- Location changes
- Status changes
- Sharing changes
- Name and identification changes
- Evaluations
- Values
- Maintenance
- Transfers
- Sales
- Archive and restore actions
- AI-generated suggestions
- User confirmations

Standard users should see a readable timeline.

Power users may access more detailed audit information.

------

# 19. User control over AI

Users should be able to choose an AI-assistance level.

## Minimal

- Voice transcription
- Basic extraction
- Simple summaries

## Standard

- Follow-up prompts
- Structured suggestions
- Guidance
- Similarity discovery

## Advanced

- Identification assistance
- Reprocessing
- Conflict detection
- Batch extraction
- Detailed confidence and provenance
- Template-specific analysis

AI controls should be understandable and should not require technical knowledge.

------

# 20. Product governance

## 20.1 Feature review

New features should be reviewed against these questions:

1. Does this make the standard experience simpler or more complex?
2. Can the user provide the information naturally?
3. Is the source information preserved?
4. Is AI output distinguishable from confirmed fact?
5. Does the action affect operational state?
6. Is confirmation required?
7. Is the action reversible?
8. Is privacy protected by default?
9. Can a power user inspect and control the result?
10. Does the feature work across collection templates or require a specialized extension?

## 20.2 Template review

A new collection template should define:

- User-friendly terminology
- Important identification concepts
- Suggested photographs
- High-value prompts
- Evaluation categories
- Maintenance activities
- Label options
- Guidance boundaries
- Similarity criteria
- Privacy considerations
- Destructive-action warnings

## 20.3 AI review

AI behavior should be tested for:

- Unsupported assumptions
- False certainty
- Misclassification
- Failure to preserve uncertainty
- Privacy leakage
- Overly frequent prompts
- Confusing explanations
- Inappropriate operational changes
- Bias toward popular or common identifications
- Failure to recognize conflicting evidence

## 20.4 Release criteria

A feature should not be released until:

- Standard users can complete the workflow without understanding the backend
- Users can skip optional prompts
- Important actions require confirmation
- Errors can be corrected
- Privacy defaults are appropriate
- AI output is source-aware
- Public output excludes private information
- Audit history is available
- The workflow works on a mobile device
- Accessibility has been reviewed

------

# 21. Governing product rules

```text
Make it easy to tell the story.

Preserve the original narrative and evidence.

Use AI to organize, enrich, and explain.

Clearly distinguish observation, inference, and fact.

Keep operational state explicit.

Ask for confirmation when an action matters.

Ask only high-value follow-up questions.

Keep private information private by default.

Allow users to correct, undo, restore, and export.

Support power users without burdening standard users.

Let knowledge become more structured and useful over time.
```

# 22. Final principle

CCE should feel simple because the system performs the complex work.

The user should experience:

```text
Photo
→ Story
→ Helpful question
→ Clear summary
→ Save
```

The platform should provide:

```text
Knowledge preservation
→ AI interpretation
→ Structured understanding
→ Explicit operational control
→ Privacy and security
→ Search, labels, guidance, discovery, and sharing
```

The interface should remain human, conversational, and forgiving.

The underlying solution should remain flexible, powerful, traceable, privacy-preserving, and continuously improvable.