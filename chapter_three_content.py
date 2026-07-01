"""Structured content for CrimeLens Chapter Three — System Analysis."""

from __future__ import annotations


CYAN_DARK = "0E7490"
GOLD = "D4AF37"
GREEN = "22C55E"
PURPLE = "A855F7"
RED = "EF4444"
BLUE = "2563EB"
TEAL = "2DD4BF"


CHAPTER_THREE_FIGURES = [
    ("Figure 3.1", "CrimeLens system context and external entities", 63),
    ("Figure 3.2", "Actor authority and interface-surface map", 64),
    ("Figure 3.3", "Data Flow Diagram — Context Level 0", 85),
    ("Figure 3.4", "Data Flow Diagram — Level 1", 86),
    ("Figure 3.5", "Data Flow Diagram — Level 2 detection intake and priority", 87),
    ("Figure 3.6", "Data Flow Diagram — Level 2 dispatch and field response", 88),
    ("Figure 3.7", "Data Flow Diagram — Level 2 supporting services", 89),
    ("Figure 3.8", "CrimeLens use-case overview", 91),
    ("Figure 3.9", "System-administrator use cases", 92),
    ("Figure 3.10", "Police-station management use cases", 93),
    ("Figure 3.11", "Dispatcher operational use cases", 94),
    ("Figure 3.12", "Field-officer mobile use cases", 95),
    ("Figure 3.13", "AI, camera, citizen, and worker use cases", 96),
    ("Figure 3.14", "Sequence diagram — AI detection to Incident", 112),
    ("Figure 3.15", "Sequence diagram — claim, review, and dispatch", 113),
    ("Figure 3.16", "Sequence diagram — officer response and escalation", 114),
    ("Figure 3.17", "Activity diagram — Incident lifecycle", 115),
    ("Figure 3.18", "Activity diagram — citizen tip and evidence flow", 116),
    ("Figure 3.19", "Incident, Crime, and Panic state machines", 117),
    ("Figure 3.20", "Conceptual class diagram", 118),
    ("Figure 3.21", "Requirements traceability map", 119),
]


CHAPTER_THREE_TABLES = [
    ("Table 3.1", "Chapter scope and analysis outputs", 61),
    ("Table 3.2", "Analysis sources and evidence hierarchy", 62),
    ("Table 3.3", "Actor authority matrix", 64),
    ("Table 3.4", "Human-actor responsibilities", 67),
    ("Table 3.5", "Machine, external, and supporting actors", 68),
    ("Table 3.6", "Interface allocation by actor and device", 68),
    ("Table 3.7", "Functional-requirement families", 69),
    ("Table 3.8", "Authentication and identity requirements", 70),
    ("Table 3.9", "Administrator functional requirements", 71),
    ("Table 3.10", "Station identity and user-management requirements", 72),
    ("Table 3.11", "Officer and camera-management requirements", 73),
    ("Table 3.12", "Incident intake and priority requirements", 74),
    ("Table 3.13", "Dispatch and field-response requirements", 75),
    ("Table 3.14", "Officer-mobile functional requirements", 76),
    ("Table 3.15", "Station-mobile assistance requirements", 77),
    ("Table 3.16", "AI-service functional requirements", 78),
    ("Table 3.17", "Gateway and evidence requirements", 79),
    ("Table 3.18", "Citizen-tip and realtime requirements", 80),
    ("Table 3.19", "Audit and reporting requirements", 81),
    ("Table 3.20", "Performance and reliability requirements", 82),
    ("Table 3.21", "Security, scalability, and quality requirements", 83),
    ("Table 3.22", "Use-case relationship rules applied in CrimeLens", 90),
    ("Table 3.23", "Authentication and profile use-case specifications", 97),
    ("Table 3.24", "Administrator station-management use-case specifications", 98),
    ("Table 3.25", "Administrator AI and governance use-case specifications", 99),
    ("Table 3.26", "Station user and officer-management use-case specifications", 100),
    ("Table 3.27", "Camera and monitoring use-case specifications", 101),
    ("Table 3.28", "Incident creation, claim, and release use-case specifications", 102),
    ("Table 3.29", "Incident inspection, linking, and rejection use-case specifications", 103),
    ("Table 3.30", "Dispatch and officer-selection use-case specifications", 104),
    ("Table 3.31", "Citizen-tip, BOLO, and pattern-alert use-case specifications", 105),
    ("Table 3.32", "Chat and notification use-case specifications", 106),
    ("Table 3.33", "Officer acceptance and no-visit use-case specifications", 107),
    ("Table 3.34", "Officer location, status, and Panic use-case specifications", 108),
    ("Table 3.35", "Resolution and evidence use-case specifications", 109),
    ("Table 3.36", "AI authentication, camera retrieval, and heartbeat use cases", 110),
    ("Table 3.37", "AI reporting and gateway use-case specifications", 111),
]


CHAPTER_THREE_REFERENCES = [
    (
        "[25]",
        "Object Management Group, Unified Modeling Language (UML), Version 2.5.1, "
        "formal/17-12-05, Dec. 2017.",
    ),
    (
        "[26]",
        "ISO/IEC/IEEE 29148:2018, Systems and software engineering—Life cycle "
        "processes—Requirements engineering, 2nd ed., Nov. 2018.",
    ),
    (
        "[27]",
        "E. Yourdon, Modern Structured Analysis. Englewood Cliffs, NJ, USA: "
        "Prentice Hall, 1989.",
    ),
    (
        "[28]",
        "CrimeLens Project Team, Current actors, workflows, dispatch, functional "
        "requirements, non-functional requirements, security, API, and domain-model "
        "documentation, Beni-Suef University, Jun. 2026.",
    ),
]


def requirement_table(
    number: str,
    caption: str,
    rows: list[list[str]],
    *,
    font_size: float = 7.3,
    accent: str = CYAN_DARK,
) -> dict:
    return {
        "number": number,
        "caption": caption,
        "headers": ["ID", "Requirement", "Implementation / acceptance note"],
        "rows": rows,
        "widths": [2.5, 8.0, 5.7],
        "accent": accent,
        "font_size": font_size,
    }


def use_case_table(
    number: str,
    caption: str,
    rows: list[list[str]],
    *,
    font_size: float = 6.6,
    accent: str = PURPLE,
) -> dict:
    return {
        "number": number,
        "caption": caption,
        "headers": [
            "Use case",
            "Actor / trigger",
            "Preconditions",
            "Main and alternate flows",
            "Postconditions",
        ],
        "rows": rows,
        "widths": [2.7, 3.1, 3.1, 5.2, 2.6],
        "accent": accent,
        "font_size": font_size,
    }


def figure(
    number: str,
    caption: str,
    filename: str,
    height: float = 8.3,
) -> tuple[str, str, str, float]:
    return (number, caption, filename, height)


def chapter_three_page_specs() -> list[dict]:
    return [
        {
            "kicker": "Analysis foundation",
            "title": "Introduction to System Analysis",
            "section": "3.1",
            "paragraphs": [
                (
                    "System analysis translates the project vision into a precise statement "
                    "of who interacts with the system, what each actor is permitted to do, "
                    "which information crosses the system boundary, and which quality "
                    "conditions constrain the solution. For CrimeLens, this step is especially "
                    "important because the platform combines public-safety operations, "
                    "machine-generated observations, camera control, realtime communication, "
                    "field response, and auditability. A diagram that omits authority or an "
                    "exception can imply an unsafe workflow even when the implementation is "
                    "correct.",
                    "[25], [26]",
                ),
                (
                    "This chapter models the current project rather than an imagined future "
                    "system. It uses the implemented actors, current route inventory, domain "
                    "states, requirements documents, and operational workflows as evidence. "
                    "The chapter covers stakeholder and actor analysis, functional and "
                    "non-functional requirements, hierarchical Data Flow Diagrams, UML use "
                    "cases and specifications, sequence diagrams, activity diagrams, state "
                    "machines, and a conceptual class model. Database tables, keys, indexes, "
                    "physical deployment, and detailed component architecture are deliberately "
                    "reserved for Chapter Four.",
                    "[28]",
                ),
            ],
            "table": {
                "number": "Table 3.1",
                "caption": "Chapter scope and analysis outputs",
                "headers": ["Analysis question", "Output in Chapter Three", "Deferred material"],
                "rows": [
                    ["Who interacts with CrimeLens?", "Actors, responsibilities, authority boundaries", "Interface screenshots and implementation code"],
                    ["What must the system do?", "Functional requirements and use cases", "Controller/service implementation"],
                    ["How does information move?", "Context and leveled DFDs", "Database schema and network topology"],
                    ["How do scenarios unfold?", "Sequence and activity diagrams", "Concrete protocol payloads and deployment"],
                    ["How do domain states change?", "State machines and conceptual classes", "ERD, migrations, indexes, normalization"],
                    ["How will quality be judged?", "NFRs and traceability map", "Measured results in Chapter Six"],
                ],
                "widths": [4.8, 6.2, 5.2],
                "accent": CYAN_DARK,
                "font_size": 7.5,
            },
        },
        {
            "kicker": "Method and notation",
            "title": "Analysis Method, Evidence, and Modeling Standards",
            "paragraphs": [
                (
                    "Requirements are written as uniquely identified, verifiable statements "
                    "and are grouped by operational capability. This approach follows the "
                    "requirements-engineering principles described by ISO/IEC/IEEE 29148: "
                    "requirements must be understandable, necessary, feasible, singular, "
                    "traceable, and capable of verification. Implemented controls are "
                    "distinguished from acceptance targets that still require measurement.",
                    "[26]",
                ),
                (
                    "Behavioral and structural diagrams follow UML 2.5.1 semantics. Actors "
                    "remain outside the system boundary; use cases express actor goals using "
                    "verb phrases; include relationships identify mandatory reused behavior; "
                    "extend relationships represent optional or conditional additions; "
                    "sequence diagrams order messages from top to bottom; activity diagrams "
                    "model control flow; state machines model states and triggering "
                    "transitions; and the conceptual class diagram represents domain concepts "
                    "and associations without becoming a database design.",
                    "[25]",
                ),
                (
                    "DFDs use a consistent structured-analysis notation containing external "
                    "entities, numbered processes, data stores, and named data flows. DFD "
                    "arrows represent data rather than control, and decision diamonds are not "
                    "used. Each lower-level DFD balances with its parent by preserving the "
                    "relevant external inputs and outputs while decomposing internal data "
                    "movement.",
                    "[27]",
                ),
            ],
            "table": {
                "number": "Table 3.2",
                "caption": "Analysis sources and evidence hierarchy",
                "headers": ["Evidence source", "Use in the chapter", "Reliability rule"],
                "rows": [
                    ["Current requirements and technical documentation", "Primary description of intended and implemented behavior", "Use revision-aligned documents"],
                    ["Laravel route inventory and domain enums", "Confirms exposed actions, guards, and state values", "Routes show capability, not necessarily UI prominence"],
                    ["Models, services, events, and scheduled jobs", "Confirms relationships, concurrency, and lifecycle behavior", "Document known inactive schedules explicitly"],
                    ["Flutter and web surface documentation", "Allocates actions to primary or helper interfaces", "Web remains the main station surface"],
                    ["Template headings", "Preserves faculty-required chapter organization", "Improve detail without moving Chapter Four content forward"],
                ],
                "widths": [5.0, 6.0, 5.2],
                "accent": GOLD,
                "font_size": 7.6,
            },
        },
        {
            "kicker": "System boundary",
            "title": "Scope, External Entities, and Operational Boundary",
            "paragraphs": [
                (
                    "The CrimeLens system boundary contains the Laravel application, web "
                    "consoles, mobile API, incident and dispatch logic, persistence, realtime "
                    "events, queued work, AI integration endpoints, and camera-gateway "
                    "coordination. Cameras, the Python AI process, citizens, human operators, "
                    "field officers, and third-party delivery providers interact with the "
                    "platform but remain external actors or collaborating systems from the "
                    "analysis perspective.",
                    "[28]",
                ),
                (
                    "The boundary enforces two central authority rules. First, an AI report "
                    "creates a reviewable Incident rather than directly creating an "
                    "operational Crime. Second, physical camera commands are mediated by the "
                    "backend rather than being issued directly by AI or officers. These "
                    "rules separate observation from commitment and preserve an auditable "
                    "decision point.",
                    None,
                ),
                (
                    "Third-party services such as Firebase Cloud Messaging, Pusher-compatible "
                    "realtime delivery, Twilio-style inbound messaging, map services, email, "
                    "and speech transcription are dependencies rather than owners of domain "
                    "decisions. Their failure can delay a delivery channel, but persistent "
                    "application state remains the source of truth.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.1",
                "CrimeLens system context and external entities",
                "Chapter 3/System_Context.png",
                8.1,
            ),
        },
        {
            "kicker": "Stakeholder model",
            "title": "Actor Overview and Authority Matrix",
            "paragraphs": [
                (
                    "CrimeLens has distinct human, machine, device, external, and supporting "
                    "actors. The System Administrator governs platform configuration and "
                    "observability. The Police Station institutional account supervises the "
                    "station and manages resources. A Dispatcher or Station User owns live "
                    "incident decisions under a personal identity. The Field Officer "
                    "executes the response from the mobile application. The AI Detection "
                    "Service reports observations, while the Camera and Gateway provide "
                    "media and execute backend-mediated commands. Citizens supply tips, and "
                    "scheduled or queued workers perform asynchronous maintenance and "
                    "delivery tasks.",
                    "[28]",
                ),
                (
                    "Role separation is not a visual convenience. It prevents an "
                    "institutional station login from impersonating a dispatcher, prevents "
                    "AI from committing a public-safety response, and prevents officers from "
                    "managing stations or independently moving cameras. Each use case and "
                    "sequence diagram therefore identifies the initiating actor and the "
                    "authorization boundary crossed by the interaction.",
                    None,
                ),
            ],
            "table": {
                "number": "Table 3.3",
                "caption": "Actor authority matrix",
                "headers": ["Capability", "Admin", "Station account", "Dispatcher", "Officer", "AI / Gateway"],
                "rows": [
                    ["Platform governance", "Full authorized scope", "No", "No", "No", "No"],
                    ["Resource management", "Stations / AI", "Users / officers / cameras", "Operational only", "Own profile/status", "Own assigned resources"],
                    ["Incident review decision", "Observe", "Supervise", "Claim / dispatch / reject", "No", "Report only"],
                    ["Field-response transition", "Observe", "Observe", "Assign / monitor", "Accept / no-visit / resolve", "No"],
                    ["Camera control", "Through backend", "Through backend", "Through backend", "Authorized limited path", "Device executes only"],
                    ["Audit and analytics", "Cross-scope", "Station scope", "Operational timeline", "Own activity", "Health/diagnostics only"],
                ],
                "widths": [3.7, 2.5, 3.2, 3.0, 2.7, 2.5],
                "accent": PURPLE,
                "font_size": 6.9,
            },
            "figure": figure(
                "Figure 3.2",
                "Actor authority and interface-surface map",
                "Chapter 3/Actor_Authority_Map.png",
                4.1,
            ),
        },
        {
            "kicker": "Human governance actor",
            "title": "System Administrator",
            "paragraphs": [
                (
                    "The System Administrator uses the Admin web console to govern the "
                    "platform rather than to handle live dispatch. Administrative goals "
                    "include managing police-station identities and locations, importing or "
                    "exporting station records, resetting credentials, registering AI "
                    "services, assigning cameras to AI identities, configuring system, "
                    "camera, and Firebase settings, and previewing or applying priority-weight "
                    "proposals.",
                    "[28]",
                ),
                (
                    "The administrator also observes crimes, officer locations, heatmaps, AI "
                    "confidence and latency analytics, model comparisons, camera-health and "
                    "tamper events, queue and service health, reports, notifications, chat, "
                    "activity logs, and the decision ledger. Tamper events can be "
                    "acknowledged or classified as false alarms. Gateway test operations can "
                    "register, start, stop, inspect, or command a stream for controlled "
                    "diagnosis.",
                    None,
                ),
                (
                    "Administrative access does not silently grant live dispatcher identity. "
                    "The analysis therefore models observing and governing incidents as "
                    "separate from claiming or committing the review decision. This preserves "
                    "least privilege and makes operational responsibility attributable to a "
                    "station user.",
                    None,
                ),
            ],
            "bullets": [
                "Primary interface: Admin web console.",
                "Key managed resources: stations, cities, AI models, camera assignments, settings, and priority proposals.",
                "Key observability: crimes, maps, model analytics, health, reports, audit, and ledger verification.",
                "Excluded authority: personal ownership of a live dispatcher queue item.",
            ],
        },
        {
            "kicker": "Institutional and personal identities",
            "title": "Police Station Account and Dispatcher",
            "paragraphs": [
                (
                    "The Police Station institutional account represents the organization. "
                    "It authenticates to the station web console and can supervise the full "
                    "station queue, manage officers, cameras, and station users, inspect "
                    "crimes and maps, operate live monitoring, manage BOLO records, review "
                    "citizen tips, use chat and notifications, and access supporting mobile "
                    "features. Because it is not an individual person, it does not receive a "
                    "personal dispatcher ownership lane.",
                    "[28]",
                ),
                (
                    "A Dispatcher or Station User is an individual identity scoped to one "
                    "station and authorized through roles and permissions. The dispatcher "
                    "maintains presence, claims and releases Incidents, examines source, "
                    "confidence, priority factors, camera context, map location, and nearby "
                    "officers, then dispatches or rejects the Incident. Claim, review, and "
                    "decision events are attributed to this personal identity.",
                    None,
                ),
                (
                    "The distinction solves a concurrency and accountability problem. A "
                    "station may have several active operators, but only one can own a "
                    "particular pending Incident at a time. The institutional account remains "
                    "suitable for oversight, while the personal account supports atomic claim "
                    "and release operations, workload balancing, stale-claim recovery, and a "
                    "defensible decision history.",
                    None,
                ),
            ],
            "info": (
                "Identity rule",
                "The station account supervises; a named Station User claims and commits the "
                "dispatch decision. The diagrams must never merge these two identities.",
                GOLD,
                "BOUNDARY",
            ),
        },
        {
            "kicker": "Field actor",
            "title": "Field Officer",
            "paragraphs": [
                (
                    "The Field Officer works primarily from the Flutter mobile application. "
                    "The officer receives assigned crimes with location, severity, camera "
                    "context, evidence links, and a pre-arrival brief; accepts or declines the "
                    "assignment; launches navigation; updates availability and location; "
                    "reports arrival or progress; submits a no-visit outcome with a reason; "
                    "resolves the Crime with notes; and uploads authorized body-camera "
                    "evidence.",
                    "[28]",
                ),
                (
                    "Safety and coordination functions include Panic/SOS creation and "
                    "cancellation, backup notifications, active BOLO viewing, chat, voice "
                    "messages, quick replies, notifications, profile management, task "
                    "history, daily activity, and authorized camera-stream access. Location "
                    "updates are filtered by movement or time and feed Redis geospatial "
                    "presence plus durable or fallback spatial paths.",
                    None,
                ),
                (
                    "The officer does not manage police stations, station users, or AI "
                    "identities and does not independently dispatch work. Camera actions, "
                    "where enabled, remain authorization-checked backend operations. This "
                    "keeps the field interface focused on rapid response while preventing "
                    "administrative or physical-device authority from being inferred merely "
                    "because a camera stream is visible.",
                    None,
                ),
            ],
            "table": {
                "number": "Table 3.4",
                "caption": "Human-actor responsibilities",
                "headers": ["Actor", "Primary goal", "Principal actions", "Authority boundary"],
                "rows": [
                    ["Administrator", "Govern and observe platform", "Manage stations/models/settings; analytics; audit; health", "No personal live dispatch ownership"],
                    ["Station account", "Supervise station resources", "Manage users/officers/cameras; monitoring; reports", "No named dispatcher claim identity"],
                    ["Dispatcher", "Review and commit response", "Claim, inspect, dispatch, reject, link, triage tips", "One station; personally attributable decisions"],
                    ["Field Officer", "Execute field response", "Accept, navigate, update GPS/status, panic, evidence, resolve", "Own assignments; no station governance"],
                ],
                "widths": [3.0, 4.2, 5.7, 3.3],
                "accent": GREEN,
                "font_size": 7.2,
            },
        },
        {
            "kicker": "Non-human and external actors",
            "title": "AI, Camera, Citizen, and Supporting Services",
            "paragraphs": [
                (
                    "The AI Detection Service is a constrained machine client. It logs in "
                    "from a registered IP address, retrieves only assigned cameras through an "
                    "encrypted payload, sends heartbeats, and submits signed suspicious-"
                    "activity alerts with confidence and optional description. It cannot "
                    "create a Crime, assign an officer, claim an Incident, or command a "
                    "camera; a Crime is created only after station review and dispatch.",
                    "[28]",
                ),
                (
                    "The Camera Device and Python Gateway provide media and physical-device "
                    "integration. A camera streams RTSP and receives supported commands, while "
                    "the gateway manages a process per camera key and exposes RTSP relay, HLS, "
                    "and WebRTC outputs. Health, stream status, tamper reports, recordings, and "
                    "supported Tapo operations cross the backend boundary using configured "
                    "tokens, IP allow-listing, HMAC, signed URLs, and throttling.",
                    None,
                ),
                (
                    "A Citizen Reporter is an unauthenticated source who submits a web or SMS "
                    "tip with optional location and media. The tip enters a triage queue; it "
                    "does not directly become a dispatch. Scheduled and queued workers act as "
                    "supporting system actors for stale-claim release, notifications, reports, "
                    "cleanup, transcription, heartbeat checks, and ledger verification.",
                    None,
                ),
            ],
            "table": {
                "number": "Table 3.5",
                "caption": "Machine, external, and supporting actors",
                "headers": ["Actor", "Inputs to CrimeLens", "Outputs from CrimeLens", "Restriction"],
                "rows": [
                    ["AI Detection Service", "Heartbeat and signed suspicious-activity alert", "Encrypted assigned cameras, API response", "Reports observations only"],
                    ["Camera / Gateway", "RTSP, health, tamper, recordings", "Registration, stream/control command", "Backend-mediated authority"],
                    ["Citizen / Twilio", "Tip, media, location, inbound SMS", "Acknowledgement or dispatcher reply", "No direct Incident decision"],
                    ["Pusher / FCM / maps / speech", "Delivery result or external data", "Event, push, route, transcription request", "Supporting dependency"],
                    ["Scheduler / queue worker", "Persisted jobs and schedules", "Maintenance, delivery, verification result", "Acts under application policy"],
                ],
                "widths": [3.4, 4.6, 4.8, 3.4],
                "accent": GOLD,
                "font_size": 7.1,
            },
            "table_2": {
                "number": "Table 3.6",
                "caption": "Interface allocation by actor and device",
                "headers": ["Surface", "Primary audience", "Role in the project"],
                "rows": [
                    ["Admin web console", "System Administrator", "Complete governance, analytics, health, reporting, and audit surface"],
                    ["Station web console", "Station account and dispatcher", "Primary complete large-screen operational surface"],
                    ["Station mobile mode", "Station account", "Supplementary dashboards, maps, cameras, chat, and statistics"],
                    ["Officer Flutter app", "Field Officer", "Primary assignment, navigation, location, safety, and evidence surface"],
                    ["Machine API", "AI and gateway", "Authenticated integration without a human UI"],
                    ["Public tip portal / webhook", "Citizen and messaging provider", "Unauthenticated but throttled intake"],
                ],
                "widths": [4.0, 4.7, 7.5],
                "accent": CYAN_DARK,
                "font_size": 7.4,
            },
        },
        {
            "kicker": "Requirements organization",
            "title": "Functional Requirements",
            "section": "3.2",
            "paragraphs": [
                (
                    "Functional requirements describe observable capabilities and are "
                    "organized by actor goal and domain workflow. The identifier prefix "
                    "indicates the requirement family, while the numeric suffix allows "
                    "traceability into use cases, diagrams, implementation, and tests. "
                    "Requirements use the word shall for mandatory behavior and separate "
                    "current capability from deployment notes or known integration limits.",
                    "[26], [28]",
                ),
                (
                    "The current specification contains authentication, administration, "
                    "station operations, Incident intake, dispatch, field response, mobile, "
                    "AI, gateway, evidence, citizen-tip, realtime communication, audit, and "
                    "reporting requirements. Related low-level actions such as create, view, "
                    "update, delete, import, export, reset, assign, acknowledge, or dismiss "
                    "are grouped under a meaningful actor goal rather than modeled as "
                    "unrelated top-level use cases.",
                    None,
                ),
            ],
            "table": {
                "number": "Table 3.7",
                "caption": "Functional-requirement families",
                "headers": ["Prefix", "Capability family", "Examples"],
                "rows": [
                    ["FR-AUTH", "Authentication and identity", "Separate guards, tokens, password recovery, AI IP verification"],
                    ["FR-ADM", "Administration", "Stations, AI identities, settings, analytics, health, audit"],
                    ["FR-STA", "Station and dispatcher", "Resources, queue ownership, review, maps, camera operations"],
                    ["FR-INC", "Incident and priority", "Sources, status, score, factors, concurrency"],
                    ["FR-DSP", "Dispatch and field response", "Crime creation, officer selection, notifications, escalation"],
                    ["FR-OFF / FR-SMOB", "Mobile surfaces", "Officer response and station helper mode"],
                    ["FR-AI / FR-GTW", "Machine and gateway integration", "Assigned cameras, heartbeat, reporting, stream processes"],
                    ["FR-EVD / FR-TIP", "Evidence and citizen intake", "Recording, signed media, tip triage and retention"],
                    ["FR-RTC / FR-AUD / FR-REP", "Communication and governance", "Realtime, chat, ledger, analytics, reports"],
                ],
                "widths": [2.7, 5.0, 8.5],
                "accent": CYAN_DARK,
                "font_size": 7.2,
            },
        },
        {
            "kicker": "Identity controls",
            "title": "Authentication and Identity Requirements",
            "paragraphs": [
                (
                    "CrimeLens uses separate authentication contexts because a web "
                    "administrator, institutional station, named dispatcher, officer, and AI "
                    "machine identity have different session, token, scope, and authorization "
                    "requirements. Forced password change and password-reset flows protect "
                    "newly created human accounts, while machine login adds registered-IP "
                    "verification and session encryption material.",
                    "[28]",
                ),
                (
                    "Successful authentication is not sufficient authorization. Station "
                    "users remain constrained by station ownership and role permissions, "
                    "officers by assignment and resource policies, AI identities by assigned "
                    "cameras and registered IP, and private channels by explicit broadcast "
                    "authorization. Physical-device and consequential domain actions also use "
                    "throttling and confirmation where appropriate.",
                    None,
                ),
            ],
            "table": requirement_table(
                "Table 3.8",
                "Authentication and identity requirements",
                [
                    ["FR-AUTH-01", "Provide separate Admin, Police Station web, and Station User web guards.", "Prevents institutional and personal identities from being merged."],
                    ["FR-AUTH-02", "Provide Sanctum bearer authentication for Police Station API/mobile, Officer, and AI clients.", "Tokens are bounded to the relevant guard."],
                    ["FR-AUTH-03", "Require forced password change for newly created station and officer accounts.", "The forced-change route bypasses its own redirect loop."],
                    ["FR-AUTH-04", "Support password-reset codes for supported human identities.", "Send, verify, and reset phases are throttled."],
                    ["FR-AUTH-05", "Verify the registered AI IP at login and on protected requests.", "A valid token from another IP is insufficient."],
                    ["FR-AUTH-06", "Issue supported clients a session key for encrypted camera payloads.", "Used with AES-protected machine camera data."],
                    ["FR-AUTH-07", "Authorize Station Users through station scope plus role/permission checks.", "Authentication alone does not grant dispatcher actions."],
                ],
                accent=BLUE,
            ),
        },
        {
            "kicker": "Platform governance",
            "title": "Administrator Requirements",
            "paragraphs": [
                (
                    "Administrative requirements combine resource governance and "
                    "observability. CRUD, import, export, bulk deletion, credential reset, "
                    "camera assignment, and configuration operations support controlled "
                    "onboarding. Analytics, comparisons, heatmaps, health checks, camera "
                    "tamper review, reports, notifications, activity logs, and the decision "
                    "ledger provide evidence that the platform remains understandable after "
                    "deployment.",
                    "[28]",
                ),
            ],
            "table": requirement_table(
                "Table 3.9",
                "Administrator functional requirements",
                [
                    ["FR-ADM-01", "Manage Police Station accounts, locations, status, import/export, cities, and password reset.", "Administrative scope and validation apply."],
                    ["FR-ADM-02", "Manage AI identities, IPs, signing secrets, camera assignments, import/export, and credentials.", "Secrets are not exposed after creation."],
                    ["FR-ADM-03", "Configure system settings and inspect priority-engine weights.", "Stored proposals do not imply current runtime use."],
                    ["FR-ADM-04", "Simulate priority scoring without creating a production Incident.", "Dry-run output supports governance."],
                    ["FR-ADM-05", "View crimes, maps, tracking, heatmaps, and reports in authorized scope.", "Observation is separate from dispatch authority."],
                    ["FR-ADM-06", "View AI volume, confidence, latency, uptime, drift, and model comparisons where data exists.", "Missing metrics are displayed honestly."],
                    ["FR-ADM-07", "Inspect, acknowledge, or classify camera-health and tamper events.", "Actions create accountable state."],
                    ["FR-ADM-08", "Inspect audit logs, ledger status, notifications, health, queues, and gateway diagnostics.", "Exports and tests remain authorized."],
                ],
                accent=PURPLE,
                font_size=7.0,
            ),
        },
        {
            "kicker": "Station identities",
            "title": "Station Users and Resource Ownership",
            "paragraphs": [
                (
                    "A Police Station owns operational resources and provides the tenancy "
                    "boundary for station users, officers, cameras, Incidents, Crimes, tips, "
                    "BOLO records, and private realtime channels. The institutional account "
                    "manages these resources, while individual station users perform "
                    "permission-controlled operational work. Cross-station queries and "
                    "actions are rejected unless an explicitly authorized administrative "
                    "scope applies.",
                    "[28]",
                ),
            ],
            "table": requirement_table(
                "Table 3.10",
                "Station identity and user-management requirements",
                [
                    ["FR-STA-01a", "Manage station users through create, update, delete, list, and password-reset actions.", "Only authorized station identities may manage users."],
                    ["FR-STA-01b", "Manage officers through CRUD, import, password reset, patrol zones, location, and activity views.", "All officers remain station scoped."],
                    ["FR-STA-01c", "Manage cameras through CRUD, import, connection test, filters, and stream access.", "Gateway registration follows camera persistence."],
                    ["FR-STA-02", "Expose only the station's Incidents, Crimes, officers, cameras, tips, and messages.", "Scopes, policies, and channel authorization enforce isolation."],
                    ["FR-STA-10", "Monitor officers and cameras on maps, heatmaps, crime pages, and live grids.", "The web console is the primary complete surface."],
                    ["FR-STA-12", "Receive realtime Incident, panic, tip, chat, notification, and status updates.", "Database state remains authoritative."],
                ],
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Station-managed resources",
            "title": "Officer and Camera Management Requirements",
            "paragraphs": [
                (
                    "Officer management includes identity lifecycle, rank and profile data, "
                    "availability, patrol zones, shifts, historical activity, and current "
                    "location. Camera management includes ownership, connection information, "
                    "stream status, model assignment, detection filters, live playback, "
                    "health, and physical controls. Both resource families must preserve "
                    "station isolation and avoid leaking credentials into logs or client "
                    "interfaces.",
                    "[28]",
                ),
            ],
            "table": requirement_table(
                "Table 3.11",
                "Officer and camera-management requirements",
                [
                    ["FR-STA-01d", "Create, inspect, update, delete, and import officers; reset credentials and set patrol zones.", "Deletes and changes require ownership and policy checks."],
                    ["FR-STA-01e", "View officer live locations, location history, daily activity, and status.", "Redis is the primary live path; durable data supports history."],
                    ["FR-STA-01f", "Create, inspect, update, delete, and import cameras; test connectivity.", "Gateway and camera credentials remain protected."],
                    ["FR-STA-01g", "Configure camera detection filters and view managed stream outputs.", "Changes are station scoped."],
                    ["FR-STA-11", "Trigger supported alarm and PTZ movement through backend-mediated commands.", "No direct client-to-camera authority."],
                    ["FR-GTW-07", "Observe and restart failed managed streams without recreating the camera.", "Process state is separate from camera identity."],
                ],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Candidate-event governance",
            "title": "Incident Intake and Priority Requirements",
            "paragraphs": [
                (
                    "The Incident is the central analysis boundary between observation and "
                    "response. Accepted AI alerts, manual station reports, and promoted "
                    "citizen tips become Incidents. A new Incident is normally "
                    "pending review and records its source, station, optional camera and model, "
                    "location, description, confidence, priority score, tier, factor "
                    "breakdown, review ownership, decision timestamps, and eventual Crime "
                    "relationship.",
                    "[28]",
                ),
                (
                    "Priority scoring is explainable rather than a single opaque label. "
                    "Implemented factors include confidence, crime-type weight, weapon "
                    "evidence, repeat-area context, time of day, and crowd context. The score "
                    "and normalized factor values are preserved so later pages, reports, and "
                    "ledger records can explain the queue order.",
                    None,
                ),
            ],
            "table": requirement_table(
                "Table 3.12",
                "Incident intake and priority requirements",
                [
                    ["FR-INC-01", "Create Incidents from accepted AI alerts, manual reports, and promoted citizen tips.", "All sources join a governed review layer."],
                    ["FR-INC-02", "Set new Incidents to pending_review unless a configured narrow auto-dispatch policy qualifies.", "Human review is the default."],
                    ["FR-INC-03", "Calculate an explainable score and priority tier for AI-originated Incidents.", "Critical ≥ .85; High ≥ .65; Medium ≥ .45; otherwise Low."],
                    ["FR-INC-04", "Persist normalized factors and applied weights.", "Supports audit and later evaluation."],
                    ["FR-INC-05", "Include confidence, crime type, weapon, repeat area, time, and crowd factors.", "Missing inputs use documented defaults."],
                    ["FR-INC-05a", "Reuse a recent pending AI Incident for the same camera during a three-minute duplicate window.", "Prevents alert storms while preserving detection logs."],
                    ["FR-STA-03/04", "Allow personal claim/release and automatically return stale claims to the shared queue.", "Conditional updates prevent double claim."],
                    ["FR-INC-06/07", "Make dispatch transaction-safe and mutually exclusive with rejection.", "One Incident cannot create two Crimes."],
                ],
                accent=RED,
                font_size=6.9,
            ),
        },
        {
            "kicker": "Operational commitment",
            "title": "Dispatch and Field-Response Requirements",
            "paragraphs": [
                (
                    "Dispatch commits resources and therefore requires stronger guarantees "
                    "than ordinary CRUD. The service locks or conditionally updates the "
                    "Incident, creates one Crime linked to that Incident, stores an immutable "
                    "priority snapshot, selects an explicitly chosen or nearest eligible "
                    "officer, and publishes assignment notifications. Failure at any critical "
                    "step must not leave a partially committed duplicate response.",
                    "[28]",
                ),
            ],
            "table": requirement_table(
                "Table 3.13",
                "Dispatch and field-response requirements",
                [
                    ["FR-DSP-01", "Create a Crime containing the Incident relationship and immutable priority snapshot.", "Committed operational state is distinct from candidate state."],
                    ["FR-DSP-02", "Find the nearest eligible officer from live location when none is selected.", "Station, shift, status, radius, and distance rules apply."],
                    ["FR-DSP-03", "Notify the selected officer and station when assignment succeeds.", "Push/realtime augment persistent state."],
                    ["FR-DSP-04", "Support accept, no-visit/false-alarm outcome, and resolve with notes.", "No-visit reason determines reassignment behavior."],
                    ["FR-DSP-05/06", "Process periodic GPS and derive approach or arrival information.", "Movement/time filtering reduces unnecessary traffic."],
                    ["FR-DSP-07/08", "Allow Panic/SOS and notify nearby officers for backup.", "Panic has active, cancelled, and resolved states."],
                    ["FR-DSP-09", "Support stale-Crime escalation and reassignment when the command runs.", "Capability exists; the command is not currently scheduled."],
                ],
                accent=GREEN,
                font_size=7.0,
            ),
        },
        {
            "kicker": "Primary mobile surface",
            "title": "Officer Mobile Requirements",
            "paragraphs": [
                (
                    "The officer application minimizes interaction during field response. "
                    "Authentication, active session, assignment details, pre-arrival context, "
                    "navigation, location updates, status transitions, Panic/SOS, BOLO, chat, "
                    "notifications, and evidence are organized around the current task. "
                    "Actions that can affect safety or evidence require clear state and "
                    "authorization feedback.",
                    "[28]",
                ),
            ],
            "table": requirement_table(
                "Table 3.14",
                "Officer-mobile functional requirements",
                [
                    ["FR-OFF-01/02", "Authenticate the officer and display assigned and historical Crimes.", "The active token and assignment scope are preserved."],
                    ["FR-OFF-03/04", "Display location, camera/context details, evidence, brief, and navigation.", "Signed links protect private media."],
                    ["FR-OFF-05", "Submit location periodically and after significant movement.", "Approximate policy: 100 m or 30 s."],
                    ["FR-OFF-06", "Submit accept, status, no-visit, and resolution actions with required notes.", "Invalid transitions are rejected."],
                    ["FR-OFF-07", "Support Panic/SOS, BOLO, chat, quick reply, and notifications.", "Safety events receive priority delivery."],
                    ["FR-OFF-08", "Upload authorized body-camera evidence for an assigned Crime.", "Upload and serving paths are controlled."],
                    ["FR-OFF-09", "Open authorized camera streams and controls when enabled.", "Visibility does not remove backend authorization."],
                ],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Supplementary station channel",
            "title": "Station Mobile Assistance",
            "paragraphs": [
                (
                    "The shared Flutter application also contains a Police Station mode. "
                    "This mode is treated as a supplementary access channel rather than the "
                    "primary dispatcher workspace. It can expose dashboards, officers, "
                    "crimes, cameras, maps, chat, notifications, statistics, streaming, and "
                    "authorized controls when a station needs mobile access away from the "
                    "large-screen console.",
                    "[28]",
                ),
                (
                    "The station web console remains the complete operational surface because "
                    "incident queues, maps, multi-camera monitoring, side panels, resource "
                    "management, and dense contextual information benefit from a larger "
                    "screen. The analysis therefore shows station mobile features as helper "
                    "use cases that reuse API capabilities rather than as a replacement for "
                    "the web dispatcher workflow.",
                    None,
                ),
            ],
            "table": requirement_table(
                "Table 3.15",
                "Station-mobile assistance requirements",
                [
                    ["FR-SMOB-01", "Support Police Station authentication in the shared Flutter application.", "Uses the Police Station API guard."],
                    ["FR-SMOB-02", "Expose dashboards, officers, Crimes, cameras, maps, chat, notifications, and statistics.", "Helper access; web remains primary."],
                    ["FR-SMOB-03", "Support authorized camera stream and control operations.", "Same backend policy and throttling apply."],
                    ["FR-AUTH-02", "Use bounded bearer authentication for station mobile requests.", "A mobile token does not grant dispatcher-user identity."],
                    ["NFR-USA-01", "Preserve the large-screen web workflow for queue, map, and context together.", "Station mobile complements rather than replaces it."],
                ],
                accent=TEAL,
            ),
            "info": (
                "Surface allocation",
                "The Police Station web console remains the primary operational workflow, "
                "while mobile access is limited to supporting actions away from the console.",
                GOLD,
                "SURFACE",
            ),
        },
        {
            "kicker": "Machine observation",
            "title": "AI Detection Service Requirements",
            "paragraphs": [
                (
                    "AI integration is modeled as an authenticated machine conversation. "
                    "The service signs in, receives a bounded token and session encryption "
                    "material, retrieves only cameras assigned to its identity, monitors "
                    "their streams, sends health heartbeats, and reports suspicious alerts. "
                    "Alert request bodies use HMAC-SHA256, "
                    "timestamp, and nonce protection in addition to bearer authentication and "
                    "registered-IP verification.",
                    "[28]",
                ),
            ],
            "table": requirement_table(
                "Table 3.16",
                "AI-service functional requirements",
                [
                    ["FR-AI-01", "Authenticate through the model login endpoint.", "Login is rate-limited and IP checked."],
                    ["FR-AI-02/03", "Retrieve only assigned cameras with encrypted connection payloads.", "AES-256 with session-specific material protects credentials."],
                    ["FR-AI-04", "Send periodic heartbeats.", "Health analytics can identify stale models."],
                    ["FR-AI-05", "Sign alert requests with HMAC, timestamp, and nonce.", "Replay and body tampering are rejected."],
                    ["FR-AI-06", "Submit alerts with camera identifier, confidence, and optional description.", "Creates or reuses a suspicious AI-originated Incident."],
                    ["FR-AI-07", "Apply camera detection filters and a short duplicate window before creating another Incident.", "Controls alert volume without granting AI dispatch authority."],
                    ["FR-AI-08/09", "Support runtime thresholds, enable/disable controls, annotated frames, and diagnostic scores.", "Diagnostic scores are not all dispatch signals."],
                ],
                accent=GOLD,
                font_size=7.0,
            ),
        },
        {
            "kicker": "Media and evidence",
            "title": "Camera Gateway and Evidence Requirements",
            "paragraphs": [
                (
                    "The gateway prevents every consumer from opening a separate physical "
                    "camera connection. Laravel registers the camera, and the Python service "
                    "starts or stops one managed stream process per camera key, reports "
                    "status, and exposes RTSP, HLS, and WebRTC forms for AI, mobile, and web "
                    "consumers. Camera commands remain explicit backend requests and are "
                    "subject to gateway tokens or inbound HMAC and IP controls.",
                    "[28]",
                ),
                (
                    "Evidence can originate from segmented camera recording, camera storage, "
                    "automatically merged scene windows, citizen-tip media, or officer "
                    "body-camera uploads. Private media is served through authorization or "
                    "expiring signatures, while retention jobs distinguish benign segments, "
                    "expired tips, and confirmed evidence.",
                    None,
                ),
            ],
            "table": requirement_table(
                "Table 3.17",
                "Gateway and evidence requirements",
                [
                    ["FR-GTW-01/02", "Register cameras and manage start, stop, and status for one process per camera key.", "Process state is restartable without recreating identity."],
                    ["FR-GTW-03", "Expose RTSP relay, HLS, and WebRTC outputs.", "Each format serves a different consumer need."],
                    ["FR-GTW-04", "Execute supported Tapo commands for registered cameras.", "Includes PTZ, alarm, privacy, detection, recording, and device operations where supported."],
                    ["FR-GTW-05/06", "Protect Laravel-to-gateway and gateway-to-Laravel traffic.", "Token, IP allow-list, HMAC, replay protection, and throttling apply by direction."],
                    ["FR-EVD-01/02", "Record segments and merge or fetch an event window into Scene evidence.", "Depends on timestamps and available storage."],
                    ["FR-EVD-03/04", "Serve private evidence securely and accept authorized body-cam upload.", "Signed media URLs limit disclosure."],
                    ["FR-EVD-05", "Clean old recording segments according to retention rules.", "Confirmed evidence must not be removed as benign data."],
                ],
                accent=RED,
                font_size=6.9,
            ),
        },
        {
            "kicker": "Public intake and delivery",
            "title": "Citizen Tips and Realtime Communication",
            "paragraphs": [
                (
                    "Citizens can submit a tip through a public station-specific form or a "
                    "configured inbound messaging webhook. Location can help resolve the "
                    "nearest station, media is stored behind a signed serving route, and the "
                    "tip remains pending until a dispatcher promotes, dismisses, or replies. "
                    "Promotion creates an Incident and brings the report into the governed "
                    "dispatch workflow.",
                    "[28]",
                ),
                (
                    "Realtime communication uses separate channels according to the "
                    "recipient and durability need. Browser consoles receive private events, "
                    "mobile clients receive push notifications, database notifications "
                    "preserve history, and chat supports text, media, voice, quick replies, "
                    "read state, and optional queued transcription. Delivery failure does not "
                    "erase the underlying domain transition.",
                    None,
                ),
            ],
            "table": requirement_table(
                "Table 3.18",
                "Citizen-tip and realtime requirements",
                [
                    ["FR-TIP-01/02", "Accept public web tips and configured inbound messaging webhooks.", "Public intake is throttled and station routed."],
                    ["FR-TIP-03", "Route tips using location and context.", "Nearest-station lookup assists the reporter."],
                    ["FR-TIP-04/05", "Allow dispatchers to review, promote, dismiss, and reply; promotion creates an Incident.", "A citizen never directly dispatches."],
                    ["FR-TIP-06", "Purge expired tips and associated media.", "Retention is scheduled."],
                    ["FR-RTC-01/02", "Deliver authorized browser realtime events and mobile push notifications.", "Private channel authorization and device tokens apply."],
                    ["FR-RTC-03", "Preserve database notifications for in-app history.", "Read and deletion actions remain per recipient."],
                    ["FR-RTC-04/05", "Support authorized chat, media, voice, quick reply, and optional transcription.", "Files use protected serving paths."],
                ],
                accent=BLUE,
                font_size=6.9,
            ),
        },
        {
            "kicker": "Accountability and insight",
            "title": "Audit and Reporting Requirements",
            "paragraphs": [
                (
                    "CrimeLens uses complementary accountability mechanisms. Activity logs "
                    "record actor, action, and metadata for operational visibility. The "
                    "decision ledger stores consequential decisions in an append-only "
                    "hash-chained sequence so later verification can reveal a break. Incident "
                    "priority factors and Crime priority snapshots preserve the reasoning "
                    "available when the decision occurred.",
                    "[28]",
                ),
                (
                    "Reports and analytics summarize crimes, stations, officers, AI "
                    "performance, confidence, latency, uptime, camera health, and geographic "
                    "patterns. Generation can be queued or scheduled, and every result must "
                    "respect administrator scope or station tenancy. An analytics page does "
                    "not override the source data or grant a new operational action.",
                    None,
                ),
            ],
            "table": requirement_table(
                "Table 3.19",
                "Audit and reporting requirements",
                [
                    ["FR-AUD-01", "Create activity-log entries for sensitive domain actions.", "Actor, action, target, and metadata are captured where available."],
                    ["FR-AUD-02", "Write consequential decisions to an append-only hash-chained ledger.", "Rows are protected from ordinary update/delete."],
                    ["FR-AUD-03", "Verify the ledger chain on a schedule.", "Break detection is an integrity signal."],
                    ["FR-AUD-04", "Store enough context to explain priority and dispatch decisions.", "Factors and snapshots support reconstruction."],
                    ["FR-REP-01", "Expose authorized crime, officer, station, camera, and AI analytics.", "Queries remain scoped."],
                    ["FR-REP-02", "Generate queued reports and a scheduled daily summary.", "Heavy work runs outside normal requests."],
                    ["FR-REP-03", "Enforce station and administrator scope on reports.", "Export does not bypass tenancy."],
                ],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Quality attributes",
            "title": "Performance and Reliability Requirements",
            "paragraphs": [
                (
                    "Non-functional requirements constrain how the functional behavior must "
                    "operate. Implemented controls such as Redis geospatial lookup, PostGIS "
                    "durability, queues, stream reuse, transactions, conditional updates, "
                    "health endpoints, Horizon visibility, failed-job handling, scheduled "
                    "stale-claim release, and persistent notifications are separated from "
                    "targets that still require measurement in the final environment.",
                    "[26], [28]",
                ),
            ],
            "table": {
                "number": "Table 3.20",
                "caption": "Performance and reliability requirements",
                "headers": ["Requirement group", "Implemented control", "Acceptance evidence still required"],
                "rows": [
                    ["Location and assignment", "Redis GEO primary path; PostGIS durable/fallback data", "Nearest-officer lookup under 100 ms with recorded dataset"],
                    ["Detection-to-dispatch", "Realtime event + queued/push delivery", "Timestamped camera-to-dispatch run under 10 s target"],
                    ["Streaming", "One gateway process per camera; HLS/WebRTC fan-out", "Measured LAN glass-to-glass latency around 1 s or lower"],
                    ["Normal APIs", "Pagination, query logging, caching, queues", "Load-test report for p95 CRUD response target below 500 ms"],
                    ["Concurrency", "Transactions, locks, unique constraints, guarded claim updates", "Automated race tests and failure recovery evidence"],
                    ["Availability", "Independent heartbeats, health endpoints, failed jobs, process supervisors", "Recorded recovery and service-level test"],
                    ["Scheduling", "Stale claim, cleanup, reports, ledger checks", "Confirm production scheduler; stale-Crime escalation is not currently scheduled"],
                ],
                "widths": [4.1, 6.5, 5.6],
                "accent": GREEN,
                "font_size": 7.0,
            },
        },
        {
            "kicker": "Security and sustainable evolution",
            "title": "Security, Scalability, Maintainability, and Usability",
            "paragraphs": [
                (
                    "Security requirements use layered identity, authorization, network, "
                    "cryptographic, media, tenancy, throttling, and secret-management controls. "
                    "Scalability requirements separate latency-sensitive queues, reuse stream "
                    "processes, paginate large datasets, and avoid writing every live location "
                    "sample synchronously to the main database. Maintainability requirements "
                    "preserve modular boundaries, service-layer business rules, typed "
                    "validation, enums, formatting, tests, and current documentation.",
                    "[28]",
                ),
                (
                    "Usability requirements recognize different operating environments. The "
                    "station web console must present queue, map, and context together; "
                    "priority and state cannot rely only on color; loading is explicit; "
                    "Arabic/English and light/dark themes are supported where translations "
                    "exist; officer flows minimize field interactions; and destructive or "
                    "physical-device actions request confirmation. Compatibility, quality "
                    "gates, and retention requirements complete the specification.",
                    None,
                ),
            ],
            "table": {
                "number": "Table 3.21",
                "caption": "Security, scalability, and quality requirements",
                "headers": ["Quality area", "Representative requirements", "Analysis implication"],
                "rows": [
                    ["Security / privacy", "Separate guards; CSRF; bounded tokens; IP/HMAC; encrypted credentials; signed media; station isolation", "Every diagram preserves trust boundaries"],
                    ["Scalability", "Queue separation; Horizon supervisors; Redis location; pagination; stream reuse", "Heavy and realtime workloads are not modeled as one synchronous path"],
                    ["Maintainability", "Modular monolith; services/actions; Form Requests/DTOs; enums; tests; updated docs", "Conceptual model avoids framework-specific coupling"],
                    ["Usability / accessibility", "Large-screen station workflow; non-color cues; skeletons; localization; short officer flows", "Surface allocation follows actor context"],
                    ["Compatibility", "Chromium/Firefox; Android/iOS; containerized gateway; HLS/WebRTC fallback", "External environment is explicit"],
                    ["Testing / quality", "Pest, browser E2E, Flutter, signing tests, Vite build, honest test claims", "Traceability points forward to Chapter Six"],
                    ["Data retention", "Clean benign recordings and expired tips; retain confirmed evidence; sanitize logs", "Object lifecycle includes cleanup and preservation"],
                ],
                "widths": [3.4, 8.0, 4.8],
                "accent": RED,
                "font_size": 6.9,
            },
        },
        {
            "kicker": "Model portfolio",
            "title": "System Models and Diagram Hierarchy",
            "section": "3.3",
            "paragraphs": [
                (
                    "No single diagram can explain a system with the breadth of CrimeLens. "
                    "The model portfolio answers different questions. DFDs show what "
                    "information enters, leaves, and is stored. Use-case diagrams show actor "
                    "goals and reusable or optional behavior. Use-case specifications expand "
                    "those goals into preconditions, flows, alternatives, and postconditions. "
                    "Sequence diagrams show ordered cross-boundary messages. Activity "
                    "diagrams show control and responsibility flow. State machines define "
                    "valid lifecycle transitions. The conceptual class diagram identifies "
                    "domain concepts and associations.",
                    "[25], [27]",
                ),
                (
                    "The native Draw.io source uses a separate page for each model so complex "
                    "domains are decomposed rather than squeezed into one unreadable picture. "
                    "Diagrams use white backgrounds, explicit system boundaries, consistent "
                    "labels and line styles, readable verb phrases, named data flows, and "
                    "guarded alternatives so the analysis remains legible at print scale.",
                    None,
                ),
            ],
            "bullets": [
                "DFD hierarchy: Context Level 0 → Level 1 → focused Level 2 diagrams.",
                "Use-case hierarchy: overview → actor-specific pages → textual specifications.",
                "Behavior hierarchy: end-to-end sequences → activities → state machines.",
                "Structural limit: conceptual classes only; database ERD remains in Chapter Four.",
            ],
        },
        {
            "kicker": "Structured analysis",
            "title": "DFD Context Level 0",
            "paragraphs": [
                (
                    "The context DFD treats CrimeLens as one process and shows only external "
                    "entities and the principal data exchanged with them. Administrator input "
                    "contains configuration and governance data, while outputs contain "
                    "analytics and audit information. Stations and dispatchers provide review "
                    "decisions and management data and receive operational queues, maps, and "
                    "status. Officers exchange assignment responses, location, evidence, and "
                    "safety events. AI and cameras exchange reports, stream information, and "
                    "authorized commands. Citizens provide tips and receive acknowledgements "
                    "or replies.",
                    "[27], [28]",
                ),
                (
                    "Control logic is intentionally absent. The arrow labelled review "
                    "decision means decision data crosses the boundary; it does not encode "
                    "the branching sequence. That control behavior is modeled later in "
                    "activity and sequence diagrams.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.3",
                "Data Flow Diagram — Context Level 0",
                "Chapter 3/Context_Level_0.png",
                10.5,
            ),
        },
        {
            "kicker": "Major processes",
            "title": "DFD Level 1",
            "paragraphs": [
                (
                    "Level 1 decomposes the platform into identity and governance, detection "
                    "intake and priority, dispatcher triage, dispatch and field response, "
                    "camera and evidence, tips and communication, and analytics and audit. "
                    "The associated stores hold identities/settings, Incidents, Crimes and "
                    "officer location, camera/stream/evidence data, communication data, and "
                    "activity or ledger records.",
                    "[28]",
                ),
                (
                    "The decomposition preserves balancing with the context diagram. For "
                    "example, the AI detection report entering the context process reappears "
                    "as input to detection intake, while the station's review decision enters "
                    "dispatcher triage. Internal data stores appear only after decomposition "
                    "because they are not external entities.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.4",
                "Data Flow Diagram — Level 1",
                "Chapter 3/DFD_Level_1.png",
                11.0,
            ),
        },
        {
            "kicker": "Detection decomposition",
            "title": "DFD Level 2 — Detection Intake and Priority",
            "paragraphs": [
                (
                    "The detection-intake DFD begins with machine authentication and request "
                    "validation. Identity, camera assignment, IP, token, signature, timestamp, "
                    "and nonce data establish trust. The payload is normalized, the camera "
                    "and owning station are resolved, location and context are loaded, and "
                    "the priority engine produces a score, tier, and factor breakdown. The "
                    "result is persisted as a pending Incident and broadcast to the station.",
                    "[28]",
                ),
                (
                    "Manual incidents and promoted tips enter at the persistence boundary "
                    "with their own source context. They share the Incident store but do not "
                    "currently pass through every AI-specific scoring step. The distinction "
                    "is visible rather than hidden because it affects later comparison and "
                    "testing.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.5",
                "Data Flow Diagram — Level 2 detection intake and priority",
                "Chapter 3/DFD_L2_Detection_Priority.png",
                11.0,
            ),
        },
        {
            "kicker": "Operational decomposition",
            "title": "DFD Level 2 — Dispatch and Field Response",
            "paragraphs": [
                (
                    "The dispatch DFD traces information from claim and review through Crime "
                    "creation, officer selection, assignment delivery, live response, "
                    "evidence, escalation, and audit. The dispatcher supplies ownership and "
                    "decision data; the Incident store supplies candidate context; Redis and "
                    "PostGIS supply availability and distance; the officer supplies status, "
                    "GPS, no-visit, resolution, and evidence data; and notification providers "
                    "carry delivery payloads.",
                    "[28]",
                ),
                (
                    "The DFD does not imply that the notification provider creates the "
                    "assignment. The Crime and assignment are persisted first, and external "
                    "delivery carries information about that committed state. This protects "
                    "consistency when a push or realtime channel is temporarily unavailable.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.6",
                "Data Flow Diagram — Level 2 dispatch and field response",
                "Chapter 3/DFD_L2_Dispatch_Response.png",
                11.0,
            ),
        },
        {
            "kicker": "Supporting-domain decomposition",
            "title": "DFD Level 2 — Camera, Evidence, Tips, Communication, and Audit",
            "paragraphs": [
                (
                    "Supporting services are separated to keep the main CAD flow readable. "
                    "Camera and gateway processes manage stream registration, fan-out, status, "
                    "control, tamper events, recordings, and evidence. Tip processes validate, "
                    "route, store, triage, reply, dismiss, or promote public reports. "
                    "Communication processes persist and deliver chat or notifications. "
                    "Analytics processes aggregate scoped data, generate reports, monitor "
                    "health, apply retention, and verify the decision ledger.",
                    "[28]",
                ),
                (
                    "Although these processes support the main dispatch path, they have "
                    "independent stores, security boundaries, and failure modes. Separating "
                    "them makes it possible to discuss asynchronous execution and retention "
                    "without turning the central DFD into a control-flow chart.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.7",
                "Data Flow Diagram — Level 2 supporting services",
                "Chapter 3/DFD_L2_Supporting_Services.png",
                11.0,
            ),
        },
        {
            "kicker": "UML semantics",
            "title": "Use-Case Modeling Rules",
            "paragraphs": [
                (
                    "A use case represents a goal that produces observable value for an "
                    "actor; it is not a screen, route, database operation, or implementation "
                    "method. Actors remain outside the CrimeLens boundary, use-case names use "
                    "verb phrases, and associations indicate participation. A solid actor "
                    "association does not define message order.",
                    "[25]",
                ),
                (
                    "An include relationship is used when a base use case always reuses a "
                    "mandatory sub-behavior, such as Dispatch Incident including Select "
                    "Eligible Officer and Persist Crime. An extend relationship represents "
                    "conditional behavior, such as Auto-Dispatch extending Review Incident "
                    "only when narrow policy gates are satisfied. Generalization is used only "
                    "when a specialized actor or use case truly inherits the parent's "
                    "participation or behavior.",
                    None,
                ),
            ],
            "table": {
                "number": "Table 3.22",
                "caption": "Use-case relationship rules applied in CrimeLens",
                "headers": ["Notation", "Meaning", "CrimeLens example", "Common error avoided"],
                "rows": [
                    ["Actor association", "Actor participates in the goal", "Dispatcher — Review Incident", "Using arrows to imply sequence"],
                    ["«include»", "Mandatory reusable behavior", "Dispatch Incident includes Select Officer", "Using include for optional behavior"],
                    ["«extend»", "Conditional addition at extension point", "Auto-dispatch extends review policy", "Reversing the arrow direction"],
                    ["Generalization", "Specialized actor/use case inherits parent relations", "Station User specializes authenticated station person where applicable", "Using inheritance only to reduce lines"],
                    ["System boundary", "Separates actor from system-owned behavior", "Citizen outside; Submit Tip inside", "Placing external services inside CrimeLens"],
                ],
                "widths": [2.7, 4.4, 5.3, 3.8],
                "accent": PURPLE,
                "font_size": 7.2,
            },
        },
        {
            "kicker": "Goal map",
            "title": "Use-Case Overview",
            "paragraphs": [
                (
                    "The overview groups actor goals into platform governance, station "
                    "resource management, incident triage and dispatch, field response, "
                    "machine detection reporting, citizen-tip intake, camera and evidence "
                    "operations, communication, and maintenance or audit. Lower-level pages "
                    "decompose each group so the overview remains readable.",
                    "[28]",
                ),
            ],
            "figure": figure(
                "Figure 3.8",
                "CrimeLens use-case overview",
                "Chapter 3/Use_Case_Overview.png",
                11.2,
            ),
        },
        {
            "kicker": "Administrative goals",
            "title": "Administrator Use Cases",
            "paragraphs": [
                (
                    "Administrative use cases preserve the difference between managing a "
                    "resource and observing its operation. Manage Police Stations includes "
                    "create, view, update, delete, import, export, bulk deletion, city data, "
                    "and credential reset. Manage AI Models includes identity lifecycle, "
                    "camera assignment, configuration, imports, exports, credential reset, "
                    "analytics, and comparison. Governance includes settings, priority "
                    "dry-run or apply, crimes, maps, reports, audit, health, tamper review, "
                    "gateway diagnostics, chat, notifications, profile, and simulation.",
                    "[28]",
                ),
            ],
            "figure": figure(
                "Figure 3.9",
                "System-administrator use cases",
                "Chapter 3/Admin_Use_Cases.png",
                11.2,
            ),
        },
        {
            "kicker": "Station-governance goals",
            "title": "Police Station Management Use Cases",
            "paragraphs": [
                (
                    "Station-management use cases cover authenticated institutional access, "
                    "forced credential change, station-user lifecycle, officer lifecycle, "
                    "camera lifecycle, imports, connection tests, detection filters, patrol "
                    "zones, locations, activity, monitoring, heatmaps, Crimes, BOLO, chat, "
                    "notifications, profile, streaming, camera control, and supplementary "
                    "mobile access. Personal dispatcher ownership actions remain on a "
                    "separate diagram.",
                    "[28]",
                ),
            ],
            "figure": figure(
                "Figure 3.10",
                "Police-station management use cases",
                "Chapter 3/Station_Management_Use_Cases.png",
                11.2,
            ),
        },
        {
            "kicker": "Live operations goals",
            "title": "Dispatcher Use Cases",
            "paragraphs": [
                (
                    "Dispatcher goals center on queue ownership and commitment. The actor "
                    "views personal and shared queues, maintains presence, claims or releases "
                    "Incidents, inspects context, loads nearest officers, creates manual "
                    "Incidents, links related Incidents, dispatches or rejects, tracks the "
                    "active Crime and officer, resolves station-visible Panic events, triages "
                    "citizen tips, manages BOLO records, handles pattern alerts, communicates, "
                    "and manages notifications. Dispatch includes Crime persistence and "
                    "officer selection; rejection extends review with a required reason.",
                    "[28]",
                ),
            ],
            "figure": figure(
                "Figure 3.11",
                "Dispatcher operational use cases",
                "Chapter 3/Dispatcher_Use_Cases.png",
                11.2,
            ),
        },
        {
            "kicker": "Field-response goals",
            "title": "Field Officer Use Cases",
            "paragraphs": [
                (
                    "Officer use cases are grouped into workspace access, response, and "
                    "safety or communication. Authentication and profile actions prepare the "
                    "workspace. Assignment use cases include viewing the brief, accepting, "
                    "declining with a no-visit reason, navigating, updating status and "
                    "location, arriving, resolving, and uploading evidence. Safety and "
                    "communication include Panic, cancellation, backup, BOLO, text or voice "
                    "chat, quick replies, notifications, and authorized camera access.",
                    "[28]",
                ),
            ],
            "figure": figure(
                "Figure 3.12",
                "Field-officer mobile use cases",
                "Chapter 3/Officer_Use_Cases.png",
                11.2,
            ),
        },
        {
            "kicker": "Machine and public goals",
            "title": "AI, Gateway, Citizen, and Worker Use Cases",
            "paragraphs": [
                (
                    "Machine and public actors require their own diagram because they use "
                    "different trust and timing models. AI actions include login, logout, "
                    "encrypted camera retrieval, heartbeat, alert, and confirmed-detection "
                    "reporting. Gateway actions include register, start, stop, status, "
                    "fan-out, control, health, tamper, and recording. Citizen actions include "
                    "nearest-station resolution, web or SMS submission, media, receipt, and "
                    "reply. Scheduled or queued workers release stale claims, perform "
                    "maintenance, deliver notifications, transcribe voice, generate reports, "
                    "check health, and verify the ledger.",
                    "[28]",
                ),
            ],
            "figure": figure(
                "Figure 3.13",
                "AI, camera, citizen, and worker use cases",
                "Chapter 3/Machine_Citizen_Worker_Use_Cases.png",
                11.2,
            ),
        },
        {
            "kicker": "Detailed use-case specifications",
            "title": "Authentication and Profile Use Cases",
            "paragraphs": [
                (
                    "The following compact specifications describe goals rather than HTTP "
                    "routes while retaining every relevant action. Preconditions identify "
                    "the trust state required before the flow begins; alternate flows capture "
                    "invalid credentials, forced password change, expired codes, unauthorized "
                    "scope, and delivery failure; postconditions state the durable result.",
                    "[25], [28]",
                ),
            ],
            "table": use_case_table(
                "Table 3.23",
                "Authentication and profile use-case specifications",
                [
                    ["UC-AUTH-01 Authenticate human user", "Admin, Station, Dispatcher, Officer submits credentials", "Identity active; login endpoint available", "Validate credentials and throttle; establish session/token. Alternate: invalid credentials, inactive account, wrong guard.", "Authenticated context or unchanged state"],
                    ["UC-AUTH-02 Change forced password", "New Station/Officer follows redirect", "Authenticated; must_change_password=true", "Validate current/new password; update hash; clear flag. Alternate: validation failure.", "Normal protected routes become available"],
                    ["UC-AUTH-03 Recover password", "Human requests code", "Supported identity and delivery channel", "Send throttled code; verify code; reset password. Alternate: unknown account, expired/invalid code, rate limit.", "Credential replaced; reset state cleared"],
                    ["UC-AUTH-04 Manage profile/session", "Authenticated human", "Valid session or bearer token", "View/update profile; change password; remove avatar; logout; register Firebase token. Alternate: unauthorized field/file.", "Profile/session/device-token state updated"],
                ],
                accent=BLUE,
            ),
        },
        {
            "kicker": "Administrative specifications",
            "title": "Manage Police Stations",
            "paragraphs": [
                (
                    "Station administration is modeled as one goal with mandatory validation "
                    "and audit sub-behavior and optional bulk or credential operations. Import "
                    "and export do not bypass the same field and scope rules applied to normal "
                    "creation or viewing.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.24",
                "Administrator station-management use-case specifications",
                [
                    ["UC-ADM-01 Manage station record", "Admin creates/views/updates/deletes", "Admin authenticated and authorized", "Validate identity, coordinates, status, city; persist or remove. Alternate: duplicate/invalid data, protected dependency.", "Station lifecycle change audited"],
                    ["UC-ADM-02 Import/export stations", "Admin uploads or requests file", "Valid file/export scope", "Parse headings; validate rows; persist valid records; report failures, or generate scoped export.", "Import summary or downloadable export"],
                    ["UC-ADM-03 Bulk delete stations", "Admin selects records", "All selected records authorized", "Validate set; delete allowed records. Alternate: dependencies or partial validation failure.", "Authorized records removed and logged"],
                    ["UC-ADM-04 Manage cities/locations", "Admin lists/adds city data", "Admin authenticated", "Load city options; validate and store new city/location context.", "Updated reference data"],
                    ["UC-ADM-05 Reset station password", "Admin requests reset", "Target station exists and is authorized", "Generate/reset credential; require later change. Alternate: target missing.", "New station credential and forced-change state"],
                ],
                font_size=6.3,
                accent=BLUE,
            ),
        },
        {
            "kicker": "Administrative specifications",
            "title": "Manage AI Models and Platform Governance",
            "paragraphs": [
                (
                    "AI administration combines identity lifecycle and camera assignment "
                    "with analytics. Platform-governance goals include settings, priority "
                    "experimentation, tamper handling, health, reports, audit, gateway "
                    "diagnostics, communication, and simulation. These actions are grouped "
                    "because they govern the operating environment rather than dispatching "
                    "a specific Incident.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.25",
                "Administrator AI and governance use-case specifications",
                [
                    ["UC-ADM-06 Manage AI identity", "Admin creates/configures/deletes/imports/exports", "Admin authenticated", "Validate email, IP, status, signing data; persist; reset password or bulk delete as requested.", "AI identity lifecycle updated"],
                    ["UC-ADM-07 Assign cameras to AI", "Admin assigns/unassigns camera", "Model and camera exist; scope valid", "Validate relation; attach/detach camera. Alternate: duplicate or incompatible ownership.", "Assignment controls later machine retrieval"],
                    ["UC-ADM-08 Analyze and compare models", "Admin opens overview/model/compare", "Metrics available in authorized scope", "Aggregate detections, confidence, latency, uptime, drift; compare selected models.", "Read-only analytical result"],
                    ["UC-ADM-09 Configure platform", "Admin changes system/camera/Firebase settings or priority proposal", "Valid configuration", "Validate; dry-run priority; apply or store settings; clear optimized cache when requested.", "Configuration or simulation result persisted"],
                    ["UC-ADM-10 Monitor and audit", "Admin views health, reports, audit, ledger, tamper, crimes, maps", "Admin authorized", "Query scoped data; export audit; acknowledge/false-alarm tamper; generate report.", "Read model or classified event/report"],
                    ["UC-ADM-11 Diagnose gateway/simulation", "Admin registers/starts/stops/status/commands or triggers demo", "Diagnostic access and gateway available", "Send controlled request; record result. Alternate: gateway failure or invalid command.", "Diagnostic result without bypassing production policy"],
                ],
                font_size=5.9,
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Station specifications",
            "title": "Manage Station Users and Officers",
            "paragraphs": [
                (
                    "The station account manages people within its tenancy boundary. Station "
                    "users are operational identities; officers are field identities with "
                    "rank, status, patrol, activity, and location concerns. Password reset "
                    "sets a new credential and can require a later forced change.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.26",
                "Station user and officer-management use-case specifications",
                [
                    ["UC-STA-01 Manage station users", "Station manager lists/creates/edits/deletes", "Authenticated station; permission granted", "Validate station scope, roles, permissions, identity data; persist or delete.", "Station-user set updated"],
                    ["UC-STA-02 Reset station-user password", "Station manager requests reset", "Target belongs to same station", "Generate/reset credential; flag change where configured.", "New credential state"],
                    ["UC-STA-03 Manage officers", "Station manager CRUD/imports Officer", "Same-station authorization", "Validate identity, rank, contact, status; import rows; persist/update/delete.", "Officer resource updated"],
                    ["UC-STA-04 Reset officer password", "Station manager requests reset", "Officer belongs to station", "Replace credential and require change. Alternate: active policy prevents action.", "New officer credential"],
                    ["UC-STA-05 Manage patrol and activity", "Station sets zone or views locations/logs", "Officer belongs to station", "Validate polygon/zone; store patrol data; retrieve realtime/history/daily activity.", "Patrol updated or read-only operational view"],
                ],
                font_size=6.2,
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Station specifications",
            "title": "Manage Cameras and Live Monitoring",
            "paragraphs": [
                (
                    "Camera use cases distinguish persistent camera identity from gateway "
                    "process state and physical-device commands. Creating or updating a "
                    "camera may register it with the gateway, while stream start, stop, "
                    "status, alarm, PTZ, detection filters, and connection tests remain "
                    "separate interactions under the same management goal.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.27",
                "Camera and monitoring use-case specifications",
                [
                    ["UC-CAM-01 Manage camera", "Station creates/views/updates/deletes/imports", "Station authenticated; ownership valid", "Validate address, credentials, coordinates, model; persist; register gateway as needed.", "Camera identity updated"],
                    ["UC-CAM-02 Test connection", "Station submits camera connection data", "Authorized request; throttle available", "Attempt connection without unsafe persistence; return capability/status details.", "Diagnostic result only"],
                    ["UC-CAM-03 Configure detection filters", "Station updates per-camera filters", "Camera belongs to station", "Validate enabled classes/thresholds; store filter policy.", "Later detections use configured policy"],
                    ["UC-CAM-04 View monitoring grid", "Station opens monitoring", "Authorized cameras and signed stream routes", "Load stream descriptors; render HLS/WebRTC; show health and status.", "Read-only monitoring session"],
                    ["UC-CAM-05 Control camera", "Authorized operator triggers alarm or PTZ", "Camera controllable; confirmation/throttle satisfied", "Backend authorizes and forwards gateway command. Alternate: unsupported/offline/failure.", "Device command result and audit context"],
                    ["UC-CAM-06 Recover stream", "Operator/health flow checks or restarts process", "Camera registered", "Query status; start/stop/restart managed process without recreating camera.", "Updated stream-process state"],
                ],
                font_size=5.9,
                accent=GOLD,
            ),
        },
        {
            "kicker": "Dispatcher specifications",
            "title": "Create, Claim, and Release Incidents",
            "paragraphs": [
                (
                    "Queue ownership use cases are specified separately because they contain "
                    "race conditions. Claim uses a guarded atomic update and fails when "
                    "another dispatcher already owns the Incident. Release requires the "
                    "current owner. Presence and stale-claim jobs prevent abandoned work from "
                    "remaining invisible.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.28",
                "Incident creation, claim, and release use-case specifications",
                [
                    ["UC-INC-01 Create manual Incident", "Dispatcher submits phone/beat report", "Named dispatcher or authorized station; valid location/description", "Validate source and station; create pending Incident; broadcast queue update.", "Manual Incident visible in shared queue"],
                    ["UC-INC-02 View Incident queue", "Station/Dispatcher loads dashboard", "Authenticated station scope", "Return Mine and Shared sets ordered by priority/time with active context.", "Read-only queue snapshot"],
                    ["UC-INC-03 Maintain dispatcher presence", "Dispatcher client pings/leaves", "Named station user", "Update Redis presence; trim TTL; optionally rebalance.", "Active-dispatcher set updated"],
                    ["UC-INC-04 Claim Incident", "Dispatcher selects shared Incident", "Pending; same station; unassigned", "Conditional update assigned_dispatcher_id and assigned_at; broadcast claimed. Alternate: 403 institutional account, 409 already claimed.", "Incident moves to personal queue"],
                    ["UC-INC-05 Release Incident", "Owner returns Incident", "Pending; same station; owned by actor", "Conditional clear assignment; broadcast released. Alternate: actor not owner.", "Incident returns to shared queue"],
                    ["UC-INC-06 Auto-release stale claim", "Scheduled worker detects expired ownership", "Claim older than configured TTL", "Clear owner; broadcast/rebalance.", "Queue self-heals"],
                ],
                font_size=5.8,
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Dispatcher specifications",
            "title": "Inspect, Link, and Reject Incidents",
            "paragraphs": [
                (
                    "Review must provide enough context to make a defensible decision. The "
                    "dispatcher examines source, station, camera, AI identity, confidence, "
                    "priority score, tier, factor breakdown, location, description, age, "
                    "evidence, related Incidents, nearby officers, and live media where "
                    "available. Linking preserves correlation without merging records.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.29",
                "Incident inspection, linking, and rejection use-case specifications",
                [
                    ["UC-INC-07 Inspect Incident", "Dispatcher selects queue item", "Same station; pending or authorized history", "Load full Incident, source, factors, camera, map, evidence, ownership, links, nearest officers.", "Read-only decision context"],
                    ["UC-INC-08 Link related Incidents", "Dispatcher selects two related Incidents", "Both authorized; not identical; relation valid", "Validate and persist directional/symmetric link as implemented. Alternate: duplicate link.", "Correlation available to future review"],
                    ["UC-INC-09 Reject false alarm", "Owning dispatcher chooses reject", "Pending; same station; actor owns or is authorized", "Require reason code and optional note; lock/guard status; mark rejected; timestamp; ledger; broadcast.", "Terminal rejected_false_alarm state"],
                    ["UC-INC-10 View pattern alerts", "Dispatcher loads active pattern detections", "Station scope", "Return weapon/location clusters; inspect supporting Incidents.", "Read-only pattern context"],
                    ["UC-INC-11 Dismiss pattern alert", "Dispatcher dismisses alert", "Active alert in station scope", "Validate actor and update dismissal state.", "Alert removed from active list"],
                ],
                font_size=6.0,
                accent=RED,
            ),
        },
        {
            "kicker": "Dispatcher specifications",
            "title": "Dispatch and Select an Officer",
            "paragraphs": [
                (
                    "Dispatch is the primary success scenario of the CAD workflow. It must "
                    "remain idempotent under concurrent requests, preserve the Incident's "
                    "priority snapshot, and either commit all essential records or roll back. "
                    "Officer selection can use an explicit dispatcher choice or the nearest "
                    "eligible candidate.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.30",
                "Dispatch and officer-selection use-case specifications",
                [
                    ["UC-DSP-01 List candidate officers", "Dispatcher requests nearest/candidate list", "Pending same-station Incident with location", "Query on-shift, available, same-station Officers; compute distance from Redis/PostGIS; rank and return.", "Read-only eligible set"],
                    ["UC-DSP-02 Dispatch Incident", "Owning dispatcher confirms response", "Pending; not previously dispatched; actor authorized", "Lock/guard Incident; select Officer; create Crime; snapshot priority; mark dispatched; commit; notify.", "One Crime linked; assigned Officer notified"],
                    ["UC-DSP-03 Explicit officer assignment", "Dispatcher selects candidate", "Officer eligible and in scope", "Validate selection and assign during dispatch or Crime assignment.", "Crime assigned to selected Officer"],
                    ["UC-DSP-04 Automatic nearest selection", "No explicit Officer", "Location and eligible Officer data available", "Search radius/rank; choose nearest qualified Officer. Alternate: no candidate.", "Crime assigned or pending/escalated according to policy"],
                    ["UC-DSP-05 Track active response", "Station opens Crime/track view", "Authorized active Crime", "Load Officer location, status, timeline, camera/evidence, and realtime updates.", "Read-only operational view"],
                    ["UC-DSP-06 Reassign stale Crime", "Escalation command/service invoked", "Assigned Crime stale; attempts remain", "Select next eligible Officer; increment escalation; notify; log. Alternate: maximum attempts reached.", "New assignment or supervisor escalation"],
                ],
                font_size=5.7,
                accent=GREEN,
            ),
        },
        {
            "kicker": "Supporting operational specifications",
            "title": "Citizen Tips, BOLO, and Pattern Alerts",
            "paragraphs": [
                (
                    "Citizen-tip, BOLO, and pattern-alert use cases provide operational "
                    "context around the core queue. They remain station scoped, preserve "
                    "media authorization, and do not bypass Incident review. BOLO media is "
                    "served through signed links, while public tip submission is throttled.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.31",
                "Citizen-tip, BOLO, and pattern-alert use-case specifications",
                [
                    ["UC-TIP-01 Submit citizen tip", "Citizen submits web form or inbound message", "Station code/nearest station resolvable; throttle allows", "Validate text/location/media; route station; store pending tip; show thanks; notify station.", "Pending tip and protected media"],
                    ["UC-TIP-02 Review/promote/dismiss tip", "Dispatcher opens tip queue", "Tip belongs to station and is pending", "Inspect details/media; promote to Incident or dismiss with reason.", "Incident link or terminal dismissed tip"],
                    ["UC-TIP-03 Reply to citizen", "Dispatcher sends reply", "Provider/contact available", "Validate message; enqueue/send through provider; record result.", "Reply history or delivery failure"],
                    ["UC-BOLO-01 Manage BOLO", "Station creates/views/deletes broadcast", "Authorized station; valid description/media/expiry", "Persist and publish; serve signed media; list active to Officers; delete/expire.", "BOLO lifecycle updated"],
                    ["UC-PAT-01 Handle pattern alert", "Dispatcher views/dismisses cluster", "Active station alert", "Inspect related pattern evidence; dismiss when handled.", "Pattern-alert state updated"],
                ],
                font_size=5.9,
                accent=BLUE,
            ),
        },
        {
            "kicker": "Communication specifications",
            "title": "Chat and Notifications",
            "paragraphs": [
                (
                    "Communication use cases separate persistent message or notification "
                    "state from delivery channels. Text, media, voice, quick replies, read "
                    "state, heartbeat, unread counts, and device-token registration belong to "
                    "one communication goal, while Pusher and Firebase are replaceable "
                    "delivery mechanisms.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.32",
                "Chat and notification use-case specifications",
                [
                    ["UC-RTC-01 View conversations/messages", "Admin, Station, or Officer opens chat", "Authenticated and authorized conversation", "List conversations; load messages/new messages; update heartbeat.", "Read-only view and presence state"],
                    ["UC-RTC-02 Send text/media message", "Authenticated participant sends", "Conversation/recipient authorized", "Validate content/media; persist; broadcast/push. Alternate: file or scope rejected.", "Message stored and delivery attempted"],
                    ["UC-RTC-03 Send voice / quick reply", "Station/Officer submits audio or predefined reply", "Authorized; throttle allows", "Store protected audio/message; optionally queue transcription; notify recipient.", "Message and optional transcription job"],
                    ["UC-RTC-04 Manage notification", "Recipient lists/reads/deletes", "Authenticated recipient", "Return scoped notifications/unread counts; mark one/all read; delete one/all.", "Recipient notification state updated"],
                    ["UC-RTC-05 Register device token", "Web/mobile client submits FCM token", "Authenticated identity", "Validate and associate token; replace/update when necessary.", "Future push delivery target available"],
                ],
                font_size=6.0,
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Officer specifications",
            "title": "Accept or Decline an Assignment",
            "paragraphs": [
                (
                    "Officer assignment actions are constrained by assignment ownership and "
                    "current Crime state. Accept changes the Crime to in progress and records "
                    "acceptance time. No-visit requires a reason type and detail; a busy or "
                    "support-related outcome may trigger reassignment, while a confirmed "
                    "false alarm can terminate the operational response.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.33",
                "Officer acceptance and no-visit use-case specifications",
                [
                    ["UC-OFF-01 View assignment and brief", "Officer opens assigned Crime", "Authenticated; Crime assigned to actor", "Load Crime, map, description, camera/context, signed evidence, pre-arrival brief.", "Read-only task context"],
                    ["UC-OFF-02 Accept assignment", "Officer confirms response", "Crime assigned and transition valid", "Authorize ownership; set in_progress and accepted_at; broadcast station update.", "Active response begins"],
                    ["UC-OFF-03 Submit no-visit", "Officer cannot or should not visit", "Assigned/in-progress as permitted; reason required", "Validate type and note; store outcome; if busy/support, initiate reassignment; if false alarm, close appropriately.", "Not-visited, reassigned, or false-alarm outcome"],
                    ["UC-OFF-04 Navigate to scene", "Officer requests navigation", "Crime has location", "Open embedded/external navigation with authorized coordinates.", "Navigation session; no domain state change by itself"],
                    ["UC-OFF-05 View task history", "Officer opens historical list", "Authenticated Officer", "Return scoped past assignments and outcomes.", "Read-only history"],
                ],
                font_size=6.1,
                accent=GREEN,
            ),
        },
        {
            "kicker": "Officer specifications",
            "title": "Location, Status, and Panic",
            "paragraphs": [
                (
                    "Location and status use cases are high frequency and must minimize "
                    "network and database cost. The client sends after significant movement "
                    "or elapsed time, the API authorizes and validates the sample, Redis "
                    "updates current geospatial presence, and the service evaluates proximity "
                    "to active Crimes. Panic creates a separate safety lifecycle that can be "
                    "cancelled by the officer or resolved by the station.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.34",
                "Officer location, status, and Panic use-case specifications",
                [
                    ["UC-OFF-06 Update location", "Mobile background/foreground service sends GPS", "Authenticated Officer; valid coordinate", "Apply movement/time policy; update Redis and durable/fallback data; evaluate approaching/arrived; broadcast.", "Current location and proximity state updated"],
                    ["UC-OFF-07 Update availability status", "Officer selects available/busy/offline", "Authenticated; transition allowed", "Validate status; persist; record log; notify station where applicable.", "Officer eligibility changes"],
                    ["UC-OFF-08 View daily activity", "Officer requests summary", "Authenticated", "Aggregate status/location/task activity for current day.", "Read-only activity result"],
                    ["UC-OFF-09 Trigger Panic/SOS", "Officer presses emergency action", "Authenticated; no conflicting active Panic", "Create active Panic; capture location/context; notify station and nearby Officers.", "Active Panic event and urgent notifications"],
                    ["UC-OFF-10 Cancel/resolve Panic", "Officer cancels or station resolves", "Active Panic; actor authorized for transition", "Update status and timestamp; broadcast closure.", "Cancelled or resolved Panic"],
                ],
                font_size=6.0,
                accent=RED,
            ),
        },
        {
            "kicker": "Officer specifications",
            "title": "Resolve Crime and Manage Evidence",
            "paragraphs": [
                (
                    "Resolution is a terminal field action and must preserve notes, timing, "
                    "evidence, and audit context. Evidence upload can occur before resolution, "
                    "but access is limited to the assigned or otherwise authorized Crime. "
                    "Camera scene extraction and body-camera upload are complementary sources "
                    "rather than interchangeable files.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.35",
                "Resolution and evidence use-case specifications",
                [
                    ["UC-OFF-11 Upload body-cam evidence", "Officer selects media for assigned Crime", "Authorized assignment; file rules and throttle satisfied", "Validate file; store privately; create upload metadata; return signed/authorized access reference.", "Evidence linked to Crime"],
                    ["UC-OFF-12 Resolve Crime", "Officer submits resolution notes", "In-progress/arrived state as permitted", "Validate note/outcome; set resolved_at/status; calculate response time; persist; ledger; broadcast.", "Terminal resolved Crime"],
                    ["UC-EVD-01 Build Scene evidence", "Backend job/service receives event window", "Camera/recording available and timestamps preserved", "Find/merge segments or fetch storage clip; create Scene; link Crime.", "Protected Scene evidence"],
                    ["UC-EVD-02 Serve private evidence", "Authorized viewer opens media", "Policy or signed URL valid and unexpired", "Resolve protected path; stream file. Alternate: invalid signature/scope.", "Media delivered without public exposure"],
                    ["UC-EVD-03 Apply retention", "Scheduled cleanup scans segments/tips", "Retention configuration available", "Remove eligible benign/expired data; preserve confirmed evidence; log failures.", "Storage lifecycle enforced"],
                ],
                font_size=6.0,
                accent=GOLD,
            ),
        },
        {
            "kicker": "AI specifications",
            "title": "AI Login, Camera Retrieval, and Heartbeat",
            "paragraphs": [
                (
                    "AI machine access uses a stronger precondition than normal bearer "
                    "authentication. Login checks credentials and registered IP before "
                    "issuing a token and encryption material. Every protected request repeats "
                    "the model-IP check, and camera retrieval is filtered by explicit "
                    "assignment.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.36",
                "AI authentication, camera retrieval, and heartbeat use cases",
                [
                    ["UC-AI-01 Login AI service", "Python model submits credentials from host", "AI identity active; source IP registered", "Throttle; validate credential and IP; issue Sanctum token and session key. Alternate: wrong IP/credential.", "Authenticated machine session"],
                    ["UC-AI-02 Retrieve assigned cameras", "Authenticated AI requests cameras", "Valid token and current IP", "Query only assigned active cameras; encrypt connection payload with session material; return metadata.", "No unassigned credentials disclosed"],
                    ["UC-AI-03 Send heartbeat", "AI periodically posts health signal", "Valid token/IP", "Update last-seen/status and optional diagnostics.", "Model health freshness updated"],
                    ["UC-AI-04 Logout", "AI terminates session", "Valid token", "Revoke current token/session context.", "Machine session closed"],
                ],
                font_size=6.4,
                accent=GOLD,
            ),
        },
        {
            "kicker": "Machine and gateway specifications",
            "title": "Report Detection and Operate Gateway",
            "paragraphs": [
                (
                    "Detection reporting adds body integrity and replay protection to the "
                    "authenticated machine session. Gateway use cases handle stream process "
                    "lifecycle and physical-device commands but do not own Incident policy. "
                    "The backend remains the point that maps reports and commands to station, "
                    "camera, and authorization context.",
                    None,
                ),
            ],
            "table": use_case_table(
                "Table 3.37",
                "AI reporting and gateway use-case specifications",
                [
                    ["UC-AI-05 Report alert", "AI posts camera_id, confidence, and optional description", "Valid token/IP; assigned camera; valid HMAC/timestamp/nonce", "Verify signature/replay; normalize; pass filters; create or reuse scored AI-alert Incident; broadcast only on new Incident. Alternate: stale/replay/unassigned/low confidence.", "Pending Incident or rejected request"],
                    ["UC-AI-06 Suppress duplicate alert burst", "AI repeats alert for same camera", "A pending AI Incident exists inside the three-minute window", "Log detection; return existing Incident instead of creating another report.", "Existing pending Incident remains the review target"],
                    ["UC-GTW-01 Manage stream process", "Laravel/admin registers, starts, stops, or checks stream", "Gateway token valid; camera key registered", "Create/reuse process; return state; restart without camera recreation.", "Managed stream status"],
                    ["UC-GTW-02 Fan-out media", "Authorized AI/web/mobile consumer requests format", "Active stream and signed/authorized access", "Relay RTSP or serve HLS/WebRTC descriptor/segments.", "Media delivered to intended consumer"],
                    ["UC-GTW-03 Execute camera command", "Backend sends supported Tapo/ONVIF action", "Authorized actor; token/HMAC/IP/throttle by path", "Validate command parameters; call device; return result; audit sensitive action.", "Device state/result recorded"],
                    ["UC-GTW-04 Report tamper/health", "Gateway posts event/status", "Registered trusted gateway", "Verify IP/HMAC; store sample/event; notify admin; allow acknowledge/false-alarm classification.", "Observable camera-health event"],
                ],
                font_size=5.6,
                accent=RED,
            ),
        },
        {
            "kicker": "Interaction model",
            "title": "Sequence — AI Detection to Incident",
            "paragraphs": [
                (
                    "The sequence diagram orders the trust and persistence steps that a DFD "
                    "cannot express. The AI sends a signed alert through the "
                    "gateway/API. Token, IP, HMAC, timestamp, and nonce are verified before "
                    "the Incident service resolves camera and station context. The priority "
                    "engine returns score, tier, and factors; a transaction persists the "
                    "pending Incident; and an asynchronous event updates the station queue. "
                    "Return messages are dashed, while the station broadcast is asynchronous.",
                    "[25], [28]",
                ),
            ],
            "figure": figure(
                "Figure 3.14",
                "Sequence diagram — AI detection to Incident",
                "Chapter 3/Sequence_AI_To_Incident.png",
                11.2,
            ),
        },
        {
            "kicker": "Concurrency interaction",
            "title": "Sequence — Claim, Review, and Dispatch",
            "paragraphs": [
                (
                    "This sequence includes two dispatchers to expose the race condition. "
                    "Dispatcher A claims the Incident through a conditional update. "
                    "Dispatcher B's concurrent claim affects zero rows and returns conflict. "
                    "The owner later dispatches; the service locks or guards the Incident, "
                    "selects an officer, creates one Crime with a priority snapshot, marks the "
                    "Incident dispatched, commits the transaction, and publishes assignment "
                    "events. The alternative rejection path follows the same terminal-state "
                    "guard but does not create a Crime.",
                    "[25], [28]",
                ),
            ],
            "figure": figure(
                "Figure 3.15",
                "Sequence diagram — claim, review, and dispatch",
                "Chapter 3/Sequence_Claim_Dispatch.png",
                11.2,
            ),
        },
        {
            "kicker": "Field interaction",
            "title": "Sequence — Officer Response and Escalation",
            "paragraphs": [
                (
                    "The officer sequence begins after persistent assignment and delivery. "
                    "The app loads the authorized Crime and pre-arrival brief, accepts the "
                    "assignment, sends filtered GPS updates, and receives proximity state. "
                    "Evidence upload and resolution update protected resources and broadcast "
                    "the outcome. An alternative fragment handles decline or timeout by "
                    "calling the escalation service to select the next eligible officer and "
                    "publish reassignment.",
                    "[25], [28]",
                ),
            ],
            "figure": figure(
                "Figure 3.16",
                "Sequence diagram — officer response and escalation",
                "Chapter 3/Sequence_Officer_Response.png",
                11.2,
            ),
        },
        {
            "kicker": "Control-flow model",
            "title": "Activity — Incident Lifecycle",
            "paragraphs": [
                (
                    "The activity diagram uses partitions to show responsibility across "
                    "intake, backend, dispatcher, officer, and audit or notification concerns. "
                    "A decision node separates the narrow auto-dispatch policy from the normal "
                    "pending-review path. A second decision separates dispatch and rejection, "
                    "and an officer decision separates acceptance from decline or timeout. "
                    "Loops return reassignment to officer selection, while terminal outcomes "
                    "join in audit and notification.",
                    "[25], [28]",
                ),
            ],
            "figure": figure(
                "Figure 3.17",
                "Activity diagram — Incident lifecycle",
                "Chapter 3/Activity_Incident_Lifecycle.png",
                11.2,
            ),
        },
        {
            "kicker": "Supporting control flow",
            "title": "Activity — Citizen Tip and Evidence",
            "paragraphs": [
                (
                    "The citizen-tip activity separates unauthenticated submission from "
                    "station triage. Validation, throttling, station resolution, storage, and "
                    "notification occur before dispatcher review. The triage decision can "
                    "dismiss, reply, or promote. Promotion creates an Incident and preserves "
                    "linked source media; all branches eventually enter retention according "
                    "to status and evidence policy.",
                    "[25], [28]",
                ),
            ],
            "figure": figure(
                "Figure 3.18",
                "Activity diagram — citizen tip and evidence flow",
                "Chapter 3/Activity_Tip_Evidence.png",
                11.2,
            ),
        },
        {
            "kicker": "Lifecycle constraints",
            "title": "Incident, Crime, and Panic State Machines",
            "paragraphs": [
                (
                    "State machines define legal lifecycle changes rather than procedural "
                    "steps. Incident begins at pending_review and terminates as dispatched, "
                    "rejected_false_alarm, or expired. Crime can move from pending to assigned "
                    "and in_progress, may enter escalated or not_visited based on response, "
                    "and terminates as resolved or false_alarm. Panic begins active and "
                    "terminates as cancelled or resolved.",
                    "[25], [28]",
                ),
                (
                    "Transition labels use the form trigger [guard] / effect. Guards such as "
                    "pending state, actor authorization, assignment ownership, reason type, "
                    "or remaining escalation attempts prevent invalid changes. The diagrams "
                    "also reveal a documentation truth: there is no arbitrary backward "
                    "transition from a terminal Incident to pending review.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.19",
                "Incident, Crime, and Panic state machines",
                "Chapter 3/State_Machines.png",
                10.2,
            ),
        },
        {
            "kicker": "Conceptual structure",
            "title": "Conceptual Class Model",
            "paragraphs": [
                (
                    "The conceptual class model captures domain vocabulary and behavior "
                    "without reproducing Laravel models or database columns. PoliceStation "
                    "contains StationUsers, Officers, and Cameras; an AiModel is assigned to "
                    "Cameras and reports Incidents; a StationUser claims and reviews "
                    "Incidents; an Incident can create at most one Crime; a Crime is assigned "
                    "to an Officer and can have SceneEvidence; Citizens contribute "
                    "CitizenTips; and consequential concepts contribute DecisionLedger "
                    "records.",
                    "[25], [28]",
                ),
                (
                    "Associations show conceptual multiplicity, while composition is used "
                    "only where lifecycle ownership is meaningful. Framework traits, foreign "
                    "keys, pivot tables, polymorphic storage, indexes, migrations, and "
                    "physical normalization are excluded because they belong to the design "
                    "chapter and ERD.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.20",
                "Conceptual class diagram",
                "Chapter 3/Conceptual_Class_Diagram.png",
                10.5,
            ),
        },
        {
            "kicker": "Completeness and handoff",
            "title": "Requirements Traceability and Chapter Conclusion",
            "paragraphs": [
                (
                    "Traceability connects stakeholder goals to requirement identifiers, "
                    "system models, future verification, and evidence. Proactive detection "
                    "maps to AI and Incident requirements and the intake models. "
                    "Human-governed dispatch maps to station and dispatch requirements and "
                    "the concurrency sequence. Field response maps to officer requirements "
                    "and the response sequence. Security and accountability map to trust "
                    "boundaries, state transitions, and the decision ledger. Scalability and "
                    "maintainability map to queues, streaming reuse, modular boundaries, and "
                    "future quality tests.",
                    "[26], [28]",
                ),
                (
                    "The analysis demonstrates that CrimeLens is not one AI model connected "
                    "to one screen. It is a governed multi-actor workflow with explicit "
                    "authority, traceable requirements, decomposed data movement, concurrent "
                    "dispatcher behavior, field-state transitions, evidence, communication, "
                    "and accountability. Chapter Four will transform this logical analysis "
                    "into architecture, database, interface, security, and deployment design "
                    "without repeating the requirements described here.",
                    None,
                ),
            ],
            "figure": figure(
                "Figure 3.21",
                "Requirements traceability map",
                "Chapter 3/Requirements_Traceability.png",
                8.5,
            ),
            "info": (
                "Analysis-to-design handoff",
                "Chapter Three defines what the system must do and how actors, information, "
                "and states behave. Chapter Four defines how the software and data structures "
                "realize that behavior.",
                GREEN,
                "HANDOFF",
            ),
        },
    ]
