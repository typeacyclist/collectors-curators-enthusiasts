# Account and Tenant Lifecycle Requirements

> Resolves gap-analysis findings 1, 6, 24, 34, 51, 53, 60 (see
> `docs/MVP-REQUIREMENTS-GAP-ANALYSIS-2026-08-05.md`). Subordinate to the
> authoritative governance guidelines and the accepted ADRs.

## 1. Credential lifecycle (finding 1)

- **Password reset.** A "Forgot password" flow is a P0 public screen, reachable from Sign in, using Firebase Authentication email-based reset sent from the platform's verified sending domain. Acceptance test: a PCO Owner who forgets their password recovers access on a phone without support intervention.
- **Email verification.** Required before an account may create a tenant or accept a membership invitation. Unverified accounts may sign in but see only a "verify your email" state.
- **Password policy.** Minimum 10 characters; no forced periodic rotation; block known-breached passwords where the platform can check without transmitting the password in clear.
- **Account settings screen.** Change password, change email (with re-verification), sign out of all devices, and request account deletion.
- **MFA.** Optional TOTP multi-factor authentication offered to Owner accounts during pilot hardening (P1). Never required for Viewers in the MVP.

## 2. Non-member accounts and public sign-up (finding 6)

**Decision pending** (asked with the gap-analysis decision set): whether MVP sign-up is invite-only, open with a tenant-less welcome state, or self-serve tenant creation. Until the decision is recorded here, implementation must not build open sign-up flows beyond what the invitation flow requires.

Whatever the decision, the requirement stands that **every authenticated state has a defined screen**: no signed-in user may land on an undefined or blank state.

## 3. Roles and permissions (finding 24)

Role-to-command authorization matrix. Trusted commands enforce this server-side against current membership; the client only hides unavailable actions.

| Command | Owner | Editor | Viewer |
|---|:-:|:-:|:-:|
| CREATE_THING, UPDATE_TEMPLATE_DATA | ✅ | ✅ | — |
| ADD/UPDATE_NARRATIVE, RECORD_EVENT, PHOTOGRAPHED media upload | ✅ | ✅ | — |
| CHANGE_LOCATION | ✅ | ✅ | — |
| QUEUE_LABEL_PRINT | ✅ | ✅ | — |
| CHANGE_STATUS, CHANGE_COLLECTION | ✅ | ✅ | — |
| CHANGE_SHARING, LIST_FOR_SALE, REMOVE_SALE_LISTING | ✅ | — | — |
| RECORD_TRANSFER, ARCHIVE_THING, RESTORE_THING | ✅ | — | — |
| REMOVE_NARRATIVE / RESTORE_NARRATIVE | ✅ | own narratives only | — |
| REDACT_EVENT, DELETE_THING_PERMANENTLY | ✅ (typed confirmation) | — | — |
| Manage members, locations, collections, tenant settings, label templates | ✅ | — | — |
| Read tenant records, search, scan, "Tell me about this orchid" | ✅ | ✅ | ✅ |

- **"Elevated permission" for permanent deletion** (MVP Definition, archive section) means: Owner role, plus a typed confirmation naming the orchid, permitted only for erroneous records; the operation appends a terminal lifecycle event and is recorded in the audit history even though the record's content is removed.
- **Platform administrator** is a cross-tenant operational role held by named platform staff, implemented as a Firebase custom claim, used only for: production bootstrap, incident response, legal/abuse takedowns, and tenant deletion execution. Platform administrators hold no standing read access to tenant content; every use of the role appends an audit event. It is never a tenant role and is never granted to tenant users.

## 4. Subscription (finding 34)

Subscription plans, billing, and payment are **deferred** (now recorded in MVP Definition Section 25). The Owner "Manage subscription" area in the MVP is a placeholder screen stating that the pilot requires no subscription. No billing integration, plan model, or entitlement logic may be built for the MVP.

## 5. Member invitations (finding 51)

P1 (pilot hardening) scope, after the single-Owner vertical slice:

1. Owner enters an invitee email address and role (Editor or Viewer) in Tenant Settings → Members.
2. The platform emails an invitation link (single-use token, 7-day expiry, revocable by the Owner).
3. The invitee signs in or creates an account (email verification required) with any email address; accepting consumes the token.
4. Membership is created through a trusted command that validates the token server-side and appends a lifecycle event.
5. The Owner sees pending, accepted, revoked, and expired invitations.

Invitations depend on the transactional email capability defined in `OPERATIONS-LAUNCH-READINESS.md`.

## 6. Notifications (finding 53)

MVP notification surface is **in-app only**: a notification indicator on the tenant dashboard covering (a) sync failures needing attention, (b) "we found similar orchids" prompts when that feature ships, and (c) membership changes. Push notifications and email digests are deferred; the in-app list is the single source so nothing depends on email delivery for correctness.

## 7. Sessions and revocation (finding 60)

- Firebase Authentication session persistence is used as-is (long-lived refresh token) so greenhouse sessions survive suspension; ID tokens refresh hourly.
- **Membership revocation:** trusted commands always check current server-side membership (per AGENTS.md), so a removed member loses canonical-write ability immediately. Query access via Security Rules must also resolve membership dynamically — revocation takes effect on next token refresh at the latest, within one hour.
- **Sign out** clears local drafts only after confirming synchronization state with the user; unsynced drafts block silent sign-out with a clear warning.
- **Sign out of all devices** (Account settings) revokes refresh tokens.
- Shared-device guidance for the pilot: each PCO member uses their own account; no shared logins.
