"""Structured content for CrimeLens Chapter Four — System Design."""

from __future__ import annotations


CYAN_DARK = "0E7490"
GOLD = "D4AF37"
GREEN = "22C55E"
PURPLE = "A855F7"
RED = "EF4444"
BLUE = "2563EB"
TEAL = "2DD4BF"


CHAPTER_FOUR_FIGURES = [
    ("Figure 4.1", "Chapter-opening system-design background", 121),
    ("Figure 4.2", "High-level deployment context", 124),
    ("Figure 4.3", "Modular-monolith dependency diagram", 126),
    ("Figure 4.4", "Camera, gateway, and media design map", 130),
    ("Figure 4.5", "AI integration and secured intake design", 131),
    ("Figure 4.6", "ERD split map by bounded context", 134),
    ("Figure 4.7", "ERD — incident, dispatch, and crime response", 135),
    ("Figure 4.8", "ERD — cameras, gateway, and AI detection", 136),
    ("Figure 4.9", "ERD — officers, shifts, patrol, and field safety", 137),
    ("Figure 4.10", "ERD — users, authentication, roles, and administration", 138),
    ("Figure 4.11", "ERD — communication, evidence, audit, and configuration", 139),
    ("Figure 4.12", "Security architecture and trust boundaries", 142),
    ("Figure 4.13", "Queue, scheduling, and worker design", 149),
    ("Figure 4.14", "Evidence storage and signed-media delivery design", 150),
]


CHAPTER_FOUR_TABLES = [
    ("Table 4.1", "Chapter Four design outputs", 122),
    ("Table 4.2", "Architectural drivers and design responses", 123),
    ("Table 4.3", "Runtime components and responsibilities", 124),
    ("Table 4.4", "Layer responsibilities inside Laravel modules", 125),
    ("Table 4.5", "Module ownership and dependency direction", 126),
    ("Table 4.6", "Cross-module contracts", 127),
    ("Table 4.7", "Administrative design responsibilities", 128),
    ("Table 4.8", "Police operational design responsibilities", 129),
    ("Table 4.9", "Camera and gateway design responsibilities", 130),
    ("Table 4.10", "AI service contract and secured intake", 131),
    ("Table 4.11", "Field-officer mobile design responsibilities", 132),
    ("Table 4.12", "Database design conventions", 133),
    ("Table 4.13", "ERD segmentation plan", 134),
    ("Table 4.14", "Incident and dispatch entities", 135),
    ("Table 4.15", "Camera and AI entities", 136),
    ("Table 4.16", "Officer and field-operation entities", 137),
    ("Table 4.17", "Identity, authorization, and administration entities", 138),
    ("Table 4.18", "Evidence, communication, audit, and configuration entities", 139),
    ("Table 4.19", "Spatial, index, and lookup design", 140),
    ("Table 4.20", "Authentication guards and protected surfaces", 141),
    ("Table 4.21", "Security controls by trust boundary", 142),
    ("Table 4.22", "Authorization and tenancy design", 143),
    ("Table 4.23", "Data protection and media-access design", 144),
    ("Table 4.24", "Realtime and notification channels", 145),
    ("Table 4.25", "Interface design allocation", 146),
    ("Table 4.26", "Navigation and screen-group design", 147),
    ("Table 4.27", "API and integration boundary design", 148),
    ("Table 4.28", "Queues, jobs, and scheduled tasks", 149),
    ("Table 4.29", "Evidence storage and retention design", 150),
    ("Table 4.30", "Design decision record summary", 151),
    ("Table 4.31", "Chapter Four design validation checklist", 152),
]


CHAPTER_FOUR_REFERENCES = [
    (
        "[29]",
        "ISO/IEC/IEEE 42010:2022, Software, systems and enterprise—Architecture "
        "description, 2nd ed., International Organization for Standardization, 2022.",
    ),
    (
        "[30]",
        "CrimeLens Project Team, Architecture, modules, data model, security, "
        "realtime, camera, AI-integration, and API documentation, Beni-Suef "
        "University, Jun. 2026.",
    ),
    (
        "[31]",
        "Laravel, Official Laravel framework documentation, version-aligned project "
        "reference for routing, authentication, authorization, queues, events, "
        "broadcasting, validation, and filesystem services, accessed Jun. 2026.",
    ),
    (
        "[32]",
        "PostgreSQL Global Development Group and PostGIS Project, Official "
        "PostgreSQL and PostGIS documentation for relational storage, indexes, and "
        "geographic objects, accessed Jun. 2026.",
    ),
]


def figure(
    number: str,
    caption: str,
    filename: str,
    height: float = 7.6,
) -> tuple[str, str, str, float]:
    return (number, caption, filename, height)


def table(
    number: str,
    caption: str,
    headers: list[str],
    rows: list[list[str]],
    widths: list[float],
    *,
    accent: str = CYAN_DARK,
    font_size: float = 8.8,
) -> dict:
    return {
        "number": number,
        "caption": caption,
        "headers": headers,
        "rows": rows,
        "widths": widths,
        "accent": accent,
        "font_size": font_size,
    }


def chapter_four_page_specs() -> list[dict]:
    return [
        {
            "kicker": "Design foundation",
            "title": "Introduction to System Design",
            "section": "4.1",
            "paragraphs": [
                (
                    "System design converts the analysis models of Chapter Three into "
                    "an implementable technical blueprint. In CrimeLens, the design "
                    "problem is wider than drawing a database or choosing a framework: "
                    "the system must connect camera feeds, AI-generated observations, "
                    "human dispatch authority, officer mobility, geospatial selection, "
                    "realtime communication, evidence protection, and auditability in "
                    "one coherent operational structure.",
                    "[29], [30]",
                ),
                (
                    "The chapter therefore describes the architecture from several "
                    "viewpoints. The logical viewpoint explains modules and domain "
                    "boundaries; the development viewpoint explains controllers, "
                    "requests, services, actions, events, jobs, and models; the data "
                    "viewpoint explains the segmented Entity–Relationship Diagram (ERD); "
                    "the security viewpoint defines trust boundaries and authorization; "
                    "and the interface viewpoint maps web and mobile responsibilities.",
                    "[29], [30]",
                ),
                (
                    "Each design figure supports a specific viewpoint rather than repeating "
                    "implementation details. The diagrams are used to clarify boundaries, "
                    "dependencies, data ownership, and operational responsibilities that are "
                    "too dense to express through prose alone.",
                    None,
                ),
            ],
            "table": table(
                "Table 4.1",
                "Chapter Four design outputs",
                ["Design area", "Main output", "Why it matters"],
                [
                    ["Architecture", "Deployment context, runtime components, and layered structure", "Shows how web, mobile, AI, gateway, queues, and storage cooperate"],
                    ["Modules", "Bounded-context responsibilities and dependency direction", "Prevents feature ownership from becoming ambiguous"],
                    ["Data design", "Segmented ERD, entity groups, keys, spatial fields, and audit tables", "Connects implementation persistence to the domain model"],
                    ["Security", "Guards, trust boundaries, HMAC, encryption, signed media, and tenancy", "Protects sensitive public-safety workflows and device authority"],
                    ["Interfaces", "Information architecture for admin, station, dispatcher, officer, and helper surfaces", "Keeps each actor on the correct primary surface"],
                    ["Operations", "Queues, scheduled tasks, realtime events, evidence storage, and design trade-offs", "Explains how background work and live coordination remain reliable"],
                ],
                [3.5, 7.0, 5.7],
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Design drivers",
            "title": "Architectural Drivers and Design Principles",
            "paragraphs": [
                (
                    "The most important architectural driver is governed speed. The "
                    "platform should shorten the path from detection to response, but "
                    "it must not allow a machine observation to bypass human authority. "
                    "This creates the central design rule: AI reports, humans decide, "
                    "and the backend enforces the workflow.",
                    "[30]",
                ),
                (
                    "The second driver is operational separation. Administrators manage "
                    "the platform, stations coordinate local operations, dispatchers "
                    "make incident decisions, officers perform field actions, AI "
                    "models submit observations, and cameras supply media. Each actor "
                    "gets only the interface and privileges needed for its role.",
                    "[30]",
                ),
                (
                    "The third driver is evidence-grade accountability. Dispatch, "
                    "rejection, assignment, panic, escalation, evidence upload, and "
                    "important configuration changes must be reconstructable. Design "
                    "therefore favors explicit state transitions, named events, "
                    "immutable ledger entries, activity logs, and protected media URLs.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.2",
                "Architectural drivers and design responses",
                ["Driver", "Design response", "Affected components"],
                [
                    ["Human-in-the-loop authority", "Incident layer separates model reports from operational Crimes", "AI intake, dispatcher console, Crime service"],
                    ["Realtime coordination", "Private channels, push notifications, presence, queues, and browser updates", "Pusher/Echo, FCM, Redis, Horizon"],
                    ["Multi-surface access", "Separate guards and interfaces for admin, station, dispatcher, officer, and AI model", "Laravel auth, Inertia web, Flutter mobile"],
                    ["Camera safety", "Backend-mediated PTZ/control and signed stream delivery", "Camera module, gateway service, HMAC middleware"],
                    ["Geospatial response", "Redis GEO hot path with PostGIS persistence and analytics support", "Officer location service, dispatch assignment"],
                    ["Auditability", "Hash-chained ledger and activity logs", "Core module, database triggers, scheduled verification"],
                ],
                [4.1, 6.1, 6.0],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Architecture overview",
            "title": "High-Level Runtime Architecture",
            "section": "4.2",
            "paragraphs": [
                (
                    "CrimeLens is designed as a Laravel modular monolith supported by "
                    "specialized external services. The Laravel application owns the "
                    "domain workflow, authentication, authorization, persistence, "
                    "events, queues, signed media routes, web consoles, and mobile "
                    "Application Programming Interface (API) contracts. External "
                    "services handle streaming fan-out, browser realtime delivery, "
                    "mobile push delivery, AI inference, and geospatial storage support.",
                    "[30], [31]",
                ),
                (
                    "The main human surfaces are an administrative web console, a "
                    "police-station web console, a dispatcher live-monitoring surface, "
                    "and a Flutter officer mobile application. A station companion "
                    "mobile surface may assist with limited actions, but the station "
                    "web console remains the main operational interface because it can "
                    "display maps, queues, streams, incident details, and multi-panel "
                    "monitoring more effectively.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.3",
                "Runtime components and responsibilities",
                ["Component", "Responsibility", "Primary communication"],
                [
                    ["Laravel application", "Domain workflow, web consoles, APIs, jobs, auth, and persistence", "HTTP, sessions, Sanctum tokens, queues"],
                    ["React/Inertia web clients", "Admin, station, and dispatcher browser interfaces", "Inertia visits, private channels, signed media"],
                    ["Flutter officer app", "Field assignment, navigation, location, panic, evidence, and resolution", "REST APIs, FCM, maps"],
                    ["AI detection service", "Receives assigned streams and submits signed detections", "Sanctum token, HMAC headers, encrypted stream payloads"],
                    ["Python camera gateway", "Registers cameras, starts/stops streams, controls devices, exposes HLS/WebRTC", "Gateway token, HMAC webhooks, FFmpeg/MediaMTX"],
                    ["PostgreSQL/PostGIS", "System of record, spatial history, relational integrity, analytics", "Eloquent models, migrations, spatial indexes"],
                    ["Redis/Horizon", "Queues, cache, presence, nonce blocking, hot officer location", "Redis data structures and queued workers"],
                    ["Pusher and Firebase", "Browser realtime and mobile background notifications", "Echo channels and FCM tokens"],
                ],
                [3.4, 7.0, 5.8],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 4.2",
                "High-level deployment context",
                "CH04_FIG_02_High_Level_Deployment_Context.png",
                6.2,
            ),
        },
        {
            "kicker": "Code organization",
            "title": "Layered Application Design",
            "paragraphs": [
                (
                    "Inside each Laravel module, the design follows a layered request "
                    "model. Controllers remain thin and translate HTTP requests into "
                    "application operations. Form Requests and Data Transfer Objects "
                    "(DTOs) validate and shape input. Services perform reusable domain "
                    "operations. Actions contain multi-step workflows with side effects. "
                    "Models represent persistence and relationships. Events and jobs "
                    "separate realtime notification and long-running work from the "
                    "request-response path.",
                    "[30], [31]",
                ),
                (
                    "This structure matters because CrimeLens contains many operations "
                    "that look simple in the user interface but are not simple in the "
                    "backend. Dispatching a crime, for example, must check authority, "
                    "lock or claim the incident, calculate priority context, select an "
                    "officer, write database state, broadcast updates, notify a mobile "
                    "device, and preserve an audit trail. A layered design prevents "
                    "that workflow from being hidden inside one controller method.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.4",
                "Layer responsibilities inside Laravel modules",
                ["Layer", "Responsibility", "Design rule"],
                [
                    ["Routes and middleware", "Expose role-specific entry points and guard boundaries", "Never rely on UI hiding alone"],
                    ["Controllers", "Receive requests and return responses", "No complex business workflow should live here"],
                    ["Form Requests / DTOs", "Validate input, authorize simple request conditions, shape payloads", "Reject invalid state before services run"],
                    ["Services", "Reusable business operations and simple orchestration", "Keep methods named by domain intent"],
                    ["Actions", "Complex transactional workflows and side effects", "Use explicit names for operations such as dispatch or escalation"],
                    ["Models and enums", "Persistence, relationships, casts, and valid state values", "Use backed enums for status/type fields"],
                    ["Events, listeners, jobs", "Broadcast updates, execute slow tasks, and schedule maintenance", "Do not block user actions with slow work"],
                ],
                [3.7, 6.3, 6.2],
                accent=TEAL,
            ),
        },
        {
            "kicker": "Module architecture",
            "title": "Modular Monolith and Bounded Contexts",
            "paragraphs": [
                (
                    "CrimeLens uses a modular monolith rather than separate deployable "
                    "microservices for every domain. This choice keeps development, "
                    "testing, transactions, and deployment manageable for a graduation "
                    "project while still preserving clear internal boundaries. Each "
                    "module owns its routes, controllers, services, models, migrations, "
                    "translations, and tests, but the application is still deployed as "
                    "one Laravel system.",
                    "[30]",
                ),
                (
                    "The dependency direction is intentional. Core provides shared "
                    "cross-cutting capabilities. Police is the operational center. "
                    "Camera and Gateway provide sensing and media delivery. AiModel "
                    "provides the machine-client contract. Admin governs platform "
                    "configuration and monitoring. User interfaces call module "
                    "controllers; modules do not depend on the front-end screens.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.5",
                "Module ownership and dependency direction",
                ["Module", "Owns", "Depends on / serves"],
                [
                    ["Core", "Settings, chat, ledger, geocoding, shared services", "Serves all modules"],
                    ["Police", "Incidents, crimes, dispatch, officers, tips, BOLO, panic, station UI", "Consumes Core, Camera, Gateway, AiModel"],
                    ["Camera", "Camera CRUD, PTZ/control, filters, tamper, recording, scene extraction", "Serves Police, Admin, Gateway, AI assignment"],
                    ["Gateway", "Laravel bridge to Python gateway and stream provisioning", "Connects Camera module to external gateway"],
                    ["AiModel", "AI identities, camera assignment, heartbeat, signed detection intake", "Feeds Incident layer and detection logs"],
                    ["Admin", "Stations, AI models, settings, monitoring, health, high-level governance", "Configures all operational modules"],
                ],
                [2.8, 8.1, 5.3],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 4.3",
                "Modular-monolith dependency diagram",
                "CH04_FIG_03_Modular_Monolith_Dependency_Diagram.png",
                5.7,
            ),
        },
        {
            "kicker": "Module interaction",
            "title": "Cross-Module Contracts",
            "paragraphs": [
                (
                    "A module boundary is useful only when the contracts crossing it are "
                    "explicit. CrimeLens avoids treating modules as folders only; each "
                    "module exposes a recognizable set of commands, queries, events, "
                    "models, and jobs. For example, the Police module should not know "
                    "how a Tapo camera command is executed internally; it asks the "
                    "Camera/Gateway boundary to supply a stream, command a device, or "
                    "prepare evidence.",
                    "[30]",
                ),
                (
                    "The strongest contract is the Incident boundary. AI intake, citizen "
                    "tips, manual dispatcher creation, pattern alerts, and camera context "
                    "can all create or influence an Incident, but only dispatcher review "
                    "turns the Incident into an operational Crime. This keeps machine "
                    "and citizen input useful without giving them final authority.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.6",
                "Cross-module contracts",
                ["Contract", "Provider", "Consumer / effect"],
                [
                    ["Incident creation", "Police module", "AI reports, manual station actions, and citizen-tip promotion enter a unified review queue"],
                    ["Priority scoring", "Police services and settings", "Dispatch console receives a tier, score, and factor breakdown"],
                    ["Camera stream access", "Camera/Gateway modules", "Dispatcher, officer, AI model, and recording paths receive role-appropriate media access"],
                    ["AI camera assignment", "AiModel and Camera modules", "Model can request only assigned cameras and receives encrypted connection material"],
                    ["Officer location", "Police location service", "Dispatch assignment, maps, panic, and analytics use current and historical positions"],
                    ["Ledger writing", "Core module", "Dispatch, rejection, escalation, and tip promotion become defensible audit events"],
                ],
                [4.0, 4.4, 7.8],
                accent=GOLD,
            ),
            "info": (
                "Design boundary",
                "Chapter Four describes the design that makes these module contracts "
                "clear. Chapter Five will explain implementation details and selected "
                "code-level examples.",
                CYAN_DARK,
                "BOUNDARY",
            ),
        },
        {
            "kicker": "Admin surface",
            "title": "Administrative Console Design",
            "section": "4.3",
            "paragraphs": [
                (
                    "The administrative console is a governance surface, not a dispatch "
                    "surface. It is responsible for setting up police stations, managing "
                    "AI model identities, assigning cameras to models, reviewing system "
                    "health, configuring global settings, and receiving high-level "
                    "notifications. It should not silently become the place where live "
                    "police-station dispatch decisions are made.",
                    "[30]",
                ),
                (
                    "This separation reduces authority confusion. An administrator can "
                    "see whether an AI model is alive, whether a camera is active, or "
                    "whether a station requires configuration support. A dispatcher, "
                    "however, remains the operational actor who claims, reviews, rejects, "
                    "links, and dispatches incidents for the station.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.7",
                "Administrative design responsibilities",
                ["Area", "Design responsibility", "Important data / controls"],
                [
                    ["Station administration", "Create, update, import, export, and reset station accounts", "Police-station identity, password rotation, contact data"],
                    ["AI governance", "Register AI models, whitelist IPs, assign cameras, monitor heartbeat", "AiModel identity, signing secret, active status"],
                    ["Camera governance", "Review active cameras, health state, tamper alerts, and configuration", "Camera status, gateway key, assigned station"],
                    ["System settings", "Maintain priority weights, timeouts, radii, Firebase, and gateway configuration", "Cached key/value settings"],
                    ["System health", "Monitor queue depth, model heartbeat, camera health, and important notifications", "Admin dashboard widgets and channels"],
                ],
                [3.5, 7.3, 5.4],
                accent=BLUE,
            ),
        },
        {
            "kicker": "Station surface",
            "title": "Police Station and Dispatcher Design",
            "paragraphs": [
                (
                    "The station web surface is the operational center of CrimeLens. It "
                    "is designed for a larger screen because it must combine an incident "
                    "queue, camera streams, maps, officer availability, citizen tips, "
                    "chat, notifications, and detailed review panels. The institutional "
                    "station account provides supervisory access, while station users "
                    "represent individual dispatchers with permissioned identities.",
                    "[30]",
                ),
                (
                    "Dispatcher design emphasizes safe concurrency. Incidents may be "
                    "claimed, released, reviewed, linked, rejected, or dispatched. These "
                    "actions need clear ownership so that two dispatchers do not act on "
                    "the same incident as if they were alone. The interface should make "
                    "the current owner, status, priority, evidence, and eligible officer "
                    "context visible before the final dispatch decision.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.8",
                "Police operational design responsibilities",
                ["Capability", "Design responsibility", "Main interaction surface"],
                [
                    ["Incident review", "Display pending incidents with source, priority, confidence, location, evidence, and status", "Dispatcher web queue"],
                    ["Claim/release", "Control dispatcher ownership and prevent uncontrolled concurrent edits", "Dispatcher action bar"],
                    ["Manual incident creation", "Allow authorized users to create incidents from calls, observation, or local reports", "Station web form"],
                    ["Officer assignment", "Show availability, location, load, and recommended responders", "Dispatch map and officer panel"],
                    ["Citizen-tip triage", "Review public reports, media, and location; promote or dismiss", "Station inbox"],
                    ["Communication", "Coordinate with officers and receive panic/backup events", "Chat, notification center, and realtime channels"],
                ],
                [3.5, 8.0, 4.7],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Sensing design",
            "title": "Camera, Gateway, and Media Design",
            "paragraphs": [
                (
                    "A camera is not treated merely as a stored record. In CrimeLens it "
                    "is a physical sensor, a map object, a stream source, a possible "
                    "evidence source, and a device that may accept backend-mediated "
                    "commands. The design therefore stores camera identity, station "
                    "ownership, encrypted credentials, stream paths, storage type, "
                    "coverage geometry, health state, and gateway routing keys.",
                    "[30]",
                ),
                (
                    "The Python gateway isolates camera-specific media work from the "
                    "Laravel domain. It manages stream registration, start/stop control, "
                    "FFmpeg processes, MediaMTX publication, low-latency WebRTC, HLS "
                    "delivery, and Tapo/ONVIF command forwarding. Laravel remains the "
                    "authority for who may request these operations.",
                    "[3]–[5], [30]",
                ),
            ],
            "table": table(
                "Table 4.9",
                "Camera and gateway design responsibilities",
                ["Concern", "Laravel-side responsibility", "Gateway-side responsibility"],
                [
                    ["Camera ownership", "Store station ownership, activation, credentials, and coverage", "Receive only registered camera definitions"],
                    ["Stream provisioning", "Request start/stop/status and generate signed playback routes", "Run FFmpeg/MediaMTX and publish RTSP/HLS/WebRTC outputs"],
                    ["Device control", "Authorize and rate-limit command routes", "Execute Tapo/ONVIF operations against the physical camera"],
                    ["Evidence extraction", "Dispatch jobs and persist scene records", "Support media access and segment handling where needed"],
                    ["Tamper events", "Validate webhook signature and create tamper event records", "Analyze feed and report blackout, static stream, or field-of-view shift"],
                    ["Health recovery", "Schedule checks and sync state", "Expose health and restartable stream processes"],
                ],
                [3.6, 6.4, 6.2],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 4.4",
                "Camera, gateway, and media design map",
                "CH04_FIG_04_Camera_Gateway_Media_Design_Map.png",
                6.5,
            ),
        },
        {
            "kicker": "AI integration",
            "title": "AI Model Integration Design",
            "paragraphs": [
                (
                    "The AI model is a machine actor with useful observations but limited "
                    "authority. It authenticates through a dedicated guard, must originate "
                    "from a whitelisted Internet Protocol (IP) address, receives only "
                    "assigned cameras, and submits reports through signed endpoints. "
                    "This design prevents the AI service from becoming a privileged "
                    "general-purpose backend client.",
                    "[30]",
                ),
                (
                    "A detection report enters the backend as a suspicious-activity alert "
                    "containing camera context, confidence, and optional description. The "
                    "backend applies camera-specific filters, writes detection logs, "
                    "suppresses repeated alerts from the same camera inside a short duplicate "
                    "window, calculates priority for new accepted reports, and creates an "
                    "Incident for human review. The dispatcher-facing Incident carries "
                    "enough context to support a decision without exposing raw camera "
                    "credentials.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.10",
                "AI service contract and secured intake",
                ["Design element", "Purpose", "Security / workflow effect"],
                [
                    ["Dedicated identity", "AI model account with active status and station/camera assignment", "Machine access is separate from users and officers"],
                    ["IP allow-listing", "Reject requests from unexpected network origins", "Limits stolen-token usefulness"],
                    ["HMAC signature", "Sign alert payloads with timestamp and nonce", "Blocks tampering and replay"],
                    ["Encrypted camera payload", "Return stream material encrypted per model session", "Protects credentials and internal URLs"],
                    ["Detection filters", "Apply per-camera confidence thresholds and duplicate-window suppression", "Reduces noisy detections before incident creation"],
                    ["Incident boundary", "Convert accepted observation into pending human review", "Preserves human-in-the-loop dispatch authority"],
                ],
                [3.6, 6.0, 6.6],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 4.5",
                "AI integration and secured intake design",
                "CH04_FIG_05_AI_Integration_Secured_Intake_Design.png",
                6.4,
            ),
        },
        {
            "kicker": "Mobile design",
            "title": "Officer Mobile and Station Companion Design",
            "paragraphs": [
                (
                    "The officer mobile application is the primary field-response surface. "
                    "It must support receiving assignments, accepting or declining, "
                    "navigating to a scene, updating status, sending location, requesting "
                    "backup, activating panic/SOS, communicating with the station, uploading "
                    "evidence, and resolving a crime. These actions are time-sensitive and "
                    "must remain usable while the officer is away from a desktop workstation.",
                    "[30]",
                ),
                (
                    "The station companion mobile concept is treated as an assisting surface "
                    "rather than the main station interface. It can support lightweight "
                    "notifications or limited follow-up, but the web console remains the "
                    "authoritative station environment for live monitoring, detailed review, "
                    "camera grids, maps, and dispatch decisions.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.11",
                "Field-officer mobile design responsibilities",
                ["Capability", "Design responsibility", "Backend dependency"],
                [
                    ["Assignment reception", "Display crime summary, priority, map, and station instructions", "Crime API, FCM, officer guard"],
                    ["Status lifecycle", "Accept, arrive, in-progress, not-visited, resolved, or escalated states", "Crime status service and audit logs"],
                    ["Location updates", "Send GPS points and maintain current availability", "Redis GEO hot path and PostGIS persistence"],
                    ["Panic/SOS", "Send emergency location and optional audio context", "Panic events, station channel, officer notification rules"],
                    ["Evidence upload", "Attach body-cam or supporting media to the crime", "Signed/private storage and body_cam_uploads"],
                    ["Communication", "Chat with station or receive notifications", "Chat messages, database notifications, FCM tokens"],
                ],
                [3.5, 7.2, 5.5],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Data design",
            "title": "Database Design Overview",
            "section": "4.4",
            "paragraphs": [
                (
                    "The database design is organized around the operational spine of "
                    "CrimeLens: Camera to Incident to Crime to Officer, with supporting "
                    "groups for identity, communication, evidence, audit, settings, and "
                    "machine integration. PostgreSQL is used as the system of record, "
                    "while PostGIS supports spatial fields and geospatial queries.",
                    "[30], [32]",
                ),
                (
                    "The ERD is split into five focused diagrams because a single all-table "
                    "drawing would be too dense for a graduation book page. The diagrams "
                    "should still be consistent with one another: shared entities such as "
                    "police_stations, officers, cameras, incidents, crimes, and ledger "
                    "entries must keep the same naming, key direction, and multiplicity "
                    "across every figure.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.12",
                "Database design conventions",
                ["Convention", "Design use", "Example"],
                [
                    ["System-of-record tables", "Persist authoritative domain state", "incidents, crimes, cameras, officers"],
                    ["Pivot tables", "Represent many-to-many assignments", "camera_ai_model, admin_station"],
                    ["Polymorphic relations", "Allow multiple actor or owner types to share one table", "created_by, notifiable, tokenable, sender/receiver"],
                    ["JSON/JSONB fields", "Store structured but flexible payloads", "priority_factors, media_paths, incident_ids"],
                    ["Enums", "Constrain state/type values at model level", "IncidentStatus, CrimeStatus, OfficerStatus"],
                    ["Spatial columns", "Support nearest and heatmap operations", "cameras.location, officers.current_location"],
                    ["Audit tables", "Preserve consequential actions and history", "ledger_entries, activity_logs"],
                ],
                [3.7, 7.2, 5.3],
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "ERD planning",
            "title": "ERD Segmentation Strategy",
            "paragraphs": [
                (
                    "The ERD figures should not be decorative database screenshots. Each "
                    "diagram should show primary keys, important foreign keys, major status "
                    "fields, and relationship cardinalities. Less important columns can be "
                    "summarized when they would make the diagram unreadable. The goal is to "
                    "communicate the design logic, not to paste every migration line into a "
                    "single crowded image.",
                    "[30]",
                ),
                (
                    "The segmentation below follows bounded contexts: incident/dispatch, "
                    "camera/AI, officer/field operations, identity/authorization, and "
                    "communication/evidence/audit. This grouping keeps related entities "
                    "together while showing the cross-links that bind the full system.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.13",
                "ERD segmentation plan",
                ["Figure", "Entity group", "Must show"],
                [
                    ["Figure 4.7", "Incident, dispatch, and crime response", "incidents, crimes, crime_types, incident_links, pattern_alerts"],
                    ["Figure 4.8", "Cameras, gateway, and AI detection", "cameras, ai_models, camera_ai_model, camera_detection_filters, ai_detection_logs, camera_tamper_events"],
                    ["Figure 4.9", "Officers and field operations", "officers, officer_shifts, officer_status_logs, officer_activity_logs, panic_events, bolos"],
                    ["Figure 4.10", "Users, authentication, roles, and administration", "admins, police_stations, station_users, permission tables, personal_access_tokens, admin_station"],
                    ["Figure 4.11", "Communication, evidence, audit, and configuration", "scenses, body_cam_uploads, chat_messages, notifications, firebase_tokens, ledger_entries, activity_logs, settings"],
                ],
                [3.2, 5.2, 7.8],
                accent=GOLD,
            ),
            "figure": figure(
                "Figure 4.6",
                "ERD split map by bounded context",
                "CH04_FIG_06_ERD_Split_Map_By_Bounded_Context.png",
                6.0,
            ),
        },
        {
            "kicker": "ERD segment",
            "title": "Incident, Dispatch, and Crime Response Entities",
            "paragraphs": [
                (
                    "The incident/dispatch ERD segment is the core of the platform. An "
                    "Incident represents a candidate operational event that may originate "
                    "from AI, a manual dispatcher action, a citizen tip, or another supported "
                    "source. A Crime represents the committed field response. This separation "
                    "is the database expression of the human-in-the-loop design principle.",
                    "[30]",
                ),
                (
                    "The diagram should show the relationship from incidents to crimes, the "
                    "crime type catalogue, links between related incidents, pattern alerts "
                    "that reference multiple incident identifiers, and dispatcher ownership "
                    "fields. Relationship labels should show optionality clearly because not "
                    "every Incident becomes a Crime.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.14",
                "Incident and dispatch entities",
                ["Entity", "Design purpose", "Key relationships"],
                [
                    ["incidents", "Review queue, source, status, priority score, confidence, dispatcher ownership", "camera, ai_model, station, crime, created_by"],
                    ["crimes", "Committed response assigned to an officer or resolved by workflow", "incident, officer, camera, scene, body-cam uploads"],
                    ["crime_types", "Catalogue and severity weight used by priority scoring", "incidents/crimes through selected type"],
                    ["incident_links", "Manual relationship between two related incidents", "incident_a and incident_b"],
                    ["pattern_alerts", "Clustered or repeated pattern warning for a station/geohash", "station and incident identifier list"],
                ],
                [3.0, 7.4, 5.8],
                accent=RED,
            ),
            "figure": figure(
                "Figure 4.7",
                "ERD — incident, dispatch, and crime response",
                "CH04_FIG_07_ERD_Incident_Dispatch_Crime_Response.png",
                6.6,
            ),
        },
        {
            "kicker": "ERD segment",
            "title": "Camera, Gateway, and AI Detection Entities",
            "paragraphs": [
                (
                    "The camera/AI ERD segment describes how physical devices, model "
                    "identity, assignment, filtering, tamper, and detection history are "
                    "stored. The diagram should make the camera_ai_model pivot explicit "
                    "because it is the core authorization rule that limits what a model "
                    "can request.",
                    "[30]",
                ),
                (
                    "Camera credentials and model signing secrets are sensitive fields and "
                    "should be visually marked as protected or encrypted in the figure. "
                    "The diagram should also show that detection filters and detection logs "
                    "are separate: a filter defines a rule; a log records what happened.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.15",
                "Camera and AI entities",
                ["Entity", "Design purpose", "Key relationships / notes"],
                [
                    ["cameras", "Device identity, gateway key, station ownership, credentials, stream paths, coverage, health", "belongs to police_station; has many filters/logs/tamper events"],
                    ["ai_models", "Machine-client identity, IP, encrypted signing secret, heartbeat state", "many-to-many with cameras"],
                    ["camera_ai_model", "Assignment pivot between cameras and AI models", "unique camera/model pair"],
                    ["camera_detection_filters", "Per-camera/per-crime threshold and enabled flag", "camera plus crime_type"],
                    ["ai_detection_logs", "Detection history and filter decision", "camera, crime_type, ai_model"],
                    ["camera_tamper_events", "Camera blackout, static stream, field-of-view shift, and similar events", "camera and optional admin acknowledgement"],
                ],
                [3.5, 7.5, 5.2],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 4.8",
                "ERD — cameras, gateway, and AI detection",
                "CH04_FIG_08_ERD_Cameras_Gateway_AI_Detection.png",
                6.6,
            ),
        },
        {
            "kicker": "ERD segment",
            "title": "Officer, Shift, Patrol, and Field-Safety Entities",
            "paragraphs": [
                (
                    "The officer ERD segment covers the field-response side of CrimeLens. "
                    "An officer belongs to a station, carries availability and shift context, "
                    "streams location updates, receives Crimes, and may activate panic/SOS. "
                    "The design stores both current state and historical traces because "
                    "dispatch needs fast current lookup while reports need later analysis.",
                    "[30]",
                ),
                (
                    "The diagram should distinguish the latest officer location from route "
                    "history. It should also show that panic events, BOLO records, shifts, "
                    "and status logs are not the same thing: each supports a different "
                    "operational or accountability need.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.16",
                "Officer and field-operation entities",
                ["Entity", "Design purpose", "Key relationships / notes"],
                [
                    ["officers", "Responder identity, station ownership, status, shift flag, current location", "belongs to police_station; assigned to crimes"],
                    ["officer_shifts", "Active work windows and patrol zone geometry", "belongs to officer"],
                    ["officer_status_logs", "Accountability for availability and status changes", "belongs to officer"],
                    ["officer_activity_logs", "Daily route, distance, and location-update summary", "belongs to officer"],
                    ["panic_events", "Officer-safety emergency with location and optional audio", "officer and station"],
                    ["bolos", "Be-On-the-Look-Out broadcast with area, severity, and expiry", "station and created_by actor"],
                ],
                [3.6, 7.2, 5.4],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 4.9",
                "ERD — officers, shifts, patrol, and field safety",
                "CH04_FIG_09_ERD_Officers_Shifts_Patrol_Field_Safety.png",
                6.6,
            ),
        },
        {
            "kicker": "ERD segment",
            "title": "Identity, Authorization, and Administration Entities",
            "paragraphs": [
                (
                    "CrimeLens does not use one generic user table for every actor. The "
                    "design separates administrators, police stations, station users, "
                    "officers, and AI models because each actor has different credentials, "
                    "guards, authority, profile fields, and workflow responsibilities. "
                    "Sanctum tokens and role/permission tables support tokenized and "
                    "permissioned access where needed.",
                    "[30], [31]",
                ),
                (
                    "The ERD figure should make the distinction between institutional and "
                    "individual station identity clear. A police station can log in as an "
                    "institution, while station_users represent individual dispatchers "
                    "inside that station. The admin_station pivot can scope administrative "
                    "responsibility where the project requires it.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.17",
                "Identity, authorization, and administration entities",
                ["Entity", "Design purpose", "Key relationships / notes"],
                [
                    ["admins", "System governance users", "can scope to stations through admin_station"],
                    ["police_stations", "Tenant, institutional login, and operational owner", "owns station users, officers, cameras, incidents, tips"],
                    ["station_users", "Individual dispatcher/operator accounts", "belong to police_station and receive roles/permissions"],
                    ["personal_access_tokens", "Sanctum token storage for mobile and machine clients", "tokenable polymorphic owner"],
                    ["permission tables", "Role and permission assignment for station users", "Spatie permission model tables"],
                    ["admin_station", "Optional admin-to-station scoping", "pivot between admins and stations"],
                    ["password_reset_codes", "Multi-guard reset workflow", "resettable polymorphic owner"],
                ],
                [3.6, 7.3, 5.3],
                accent=BLUE,
            ),
            "figure": figure(
                "Figure 4.10",
                "ERD — users, authentication, roles, and administration",
                "CH04_FIG_10_ERD_Users_Authentication_Roles_Administration.png",
                5.6,
            ),
        },
        {
            "kicker": "ERD segment",
            "title": "Communication, Evidence, Audit, and Configuration Entities",
            "paragraphs": [
                (
                    "The supporting ERD segment collects tables that make the operational "
                    "workflow usable and defensible. Communication tables carry chat and "
                    "notifications. Evidence tables connect media to crimes. Audit tables "
                    "record what happened. Settings tables let important operational values "
                    "change without code changes.",
                    "[30]",
                ),
                (
                    "This diagram should avoid hiding audit and evidence as side details. "
                    "For a public-safety project, media, notification, and ledger paths are "
                    "part of the design quality. They explain how the system can notify the "
                    "right person, protect sensitive files, and reconstruct decisions later.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.18",
                "Evidence, communication, audit, and configuration entities",
                ["Entity", "Design purpose", "Key relationships / notes"],
                [
                    ["scenses", "Extracted camera evidence clip linked to a crime", "crime_id and media time window"],
                    ["body_cam_uploads", "Officer-uploaded field media", "crime and officer"],
                    ["chat_messages", "Text, image, voice, and quick-reply communication", "sender and receiver polymorphic actors"],
                    ["notifications", "In-app notification center", "notifiable polymorphic owner"],
                    ["firebase_tokens", "Device tokens for mobile push", "tokenable polymorphic owner"],
                    ["ledger_entries", "Append-only hash chain for consequential decisions", "subject and actor polymorphic references"],
                    ["activity_logs", "General audit trail for model or workflow changes", "loggable polymorphic owner"],
                    ["settings", "Cached key/value configuration", "grouped configuration keys"],
                ],
                [3.5, 7.0, 5.7],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 4.11",
                "ERD — communication, evidence, audit, and configuration",
                "CH04_FIG_11_ERD_Communication_Evidence_Audit_Configuration.png",
                6.5,
            ),
        },
        {
            "kicker": "Spatial design",
            "title": "Spatial, Index, and Lookup Design",
            "paragraphs": [
                (
                    "CrimeLens uses two complementary location strategies. PostgreSQL with "
                    "PostGIS stores authoritative spatial data and supports durable queries "
                    "for cameras, officers, heatmaps, and analytics. Redis supports the hot "
                    "path for high-frequency officer lookup because dispatch may need to "
                    "find eligible nearby officers quickly while locations update frequently.",
                    "[30], [32]",
                ),
                (
                    "The design should not treat latitude and longitude as decoration. "
                    "Spatial columns, indexes, and current-location synchronization affect "
                    "officer assignment, map rendering, blind-spot reasoning, panic response, "
                    "and operational reports. Camera coverage fields also describe radius, "
                    "angle, and bearing so the interface can draw approximate fields of view.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.19",
                "Spatial, index, and lookup design",
                ["Design element", "Purpose", "Usage"],
                [
                    ["cameras.location", "Geographic point for camera placement", "Nearest camera, heatmap, map display"],
                    ["officers.current_location", "Latest officer point in persistent storage", "Officer history, station maps, reporting"],
                    ["Redis GEO officer set", "Fast lookup for nearby active officers", "Dispatch recommendation hot path"],
                    ["coverage radius/angle/bearing", "Approximate observable camera area", "Coverage cone display and blind-spot reasoning"],
                    ["GiST spatial indexes", "Efficient geographic filtering", "PostGIS nearest and area queries"],
                    ["Status and foreign-key indexes", "Fast queues and scoped tenant retrieval", "Incident queues, officer lists, station isolation"],
                ],
                [4.1, 6.1, 6.0],
                accent=TEAL,
            ),
            "info": (
                "Design note",
                "Chapter Six should only report measured lookup latency after a recorded "
                "test environment exists. Chapter Four describes the intended design.",
                GOLD,
                "MEASURE",
            ),
        },
        {
            "kicker": "Security design",
            "title": "Authentication Guards and Protected Surfaces",
            "section": "4.5",
            "paragraphs": [
                (
                    "CrimeLens uses multiple authentication guards because each actor type "
                    "has a different trust model. Browser consoles use session guards and "
                    "Cross-Site Request Forgery (CSRF) protection. Mobile and machine "
                    "clients use Sanctum bearer tokens. The design keeps these identities "
                    "separate so an officer token cannot act like an administrator session, "
                    "and an AI model cannot behave like a station dispatcher.",
                    "[30], [31]",
                ),
                (
                    "Guard separation also clarifies interface design. Admins use the admin "
                    "web console, police stations and station users use web station surfaces, "
                    "officers use the Flutter application, AI models use signed machine "
                    "endpoints, and the camera gateway uses protected internal routes and "
                    "webhooks.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.20",
                "Authentication guards and protected surfaces",
                ["Guard", "Transport", "Protected surface"],
                [
                    ["admin", "Session", "Administrative web console"],
                    ["police_station_web", "Session", "Station institutional web console"],
                    ["station_user_web", "Session", "Individual dispatcher web console"],
                    ["police_station", "Sanctum token", "Station companion mobile/API assistance"],
                    ["officer", "Sanctum token", "Officer mobile field application"],
                    ["ai_model", "Sanctum token + machine hardening", "AI detection service endpoints"],
                    ["api", "Sanctum token", "Default mobile/API guard path where used"],
                    ["web", "Session", "Framework default surface"],
                ],
                [3.8, 4.8, 7.6],
                accent=RED,
            ),
        },
        {
            "kicker": "Trust boundaries",
            "title": "Security Architecture and Trust Boundaries",
            "paragraphs": [
                (
                    "The system contains several trust boundaries: human browser sessions, "
                    "mobile tokens, machine-client AI requests, gateway control requests, "
                    "public citizen-tip intake, signed media delivery, and internal queued "
                    "work. Each boundary uses a control appropriate to its risk instead of "
                    "assuming one mechanism protects everything.",
                    "[30]",
                ),
                (
                    "The most sensitive boundaries are machine and device boundaries. The "
                    "AI model can generate operational candidates, and the gateway can command "
                    "physical cameras. These surfaces therefore use IP allow-listing, HMAC "
                    "signatures, timestamps, nonces, rate limiting, encrypted secrets, and "
                    "narrow route scope.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.21",
                "Security controls by trust boundary",
                ["Boundary", "Primary risk", "Design controls"],
                [
                    ["Admin browser", "Unauthorized governance actions", "Session guard, CSRF, password rotation, station scoping"],
                    ["Station/dispatcher browser", "Cross-station visibility or unauthorized dispatch", "Station guard, RBAC, query scoping, channel authorization"],
                    ["Officer mobile", "Stolen mobile token or false location/status action", "Sanctum, token revocation, officer scoping, rate limits"],
                    ["AI service", "Forged detection or replayed payload", "IP allow-list, HMAC, timestamp, nonce, assigned-camera filtering"],
                    ["Camera gateway", "Unauthorized PTZ/control or tamper spoofing", "Gateway token, IP allow-list, HMAC, rate limiting"],
                    ["Media routes", "Leaked evidence or stream URLs", "Signed URLs, private disks, bounded TTL, relative signatures where needed"],
                    ["Public tips", "Spam, unsafe media, or untrusted reports", "Validation, triage state, expiry, review before promotion"],
                ],
                [3.3, 5.1, 7.8],
                accent=RED,
            ),
        },
        {
            "kicker": "Trust boundary diagram",
            "title": "Security Architecture Boundary Map",
            "figure": figure(
                "Figure 4.12",
                "Security architecture and trust boundaries",
                "CH04_FIG_12_Security_Architecture_Trust_Boundaries.png",
                6.4,
            ),
        },
        {
            "kicker": "Authorization",
            "title": "Tenancy, RBAC, and Decision Authority",
            "paragraphs": [
                (
                    "Multi-tenant isolation is a design requirement because police stations "
                    "must not see each other's incidents, officers, cameras, tips, or "
                    "operational history. The design enforces this at query level, route "
                    "authorization level, channel authorization level, and interface level. "
                    "Cross-station access should fail as if the resource does not exist.",
                    "[30]",
                ),
                (
                    "Role-Based Access Control (RBAC) is applied inside the station user "
                    "surface. Not every station user should be able to dispatch, create manual "
                    "incidents, send certain messages, or administer users. The institutional "
                    "station account can supervise, while individual station users carry "
                    "auditable permissioned identities.",
                    "[30], [31]",
                ),
            ],
            "table": table(
                "Table 4.22",
                "Authorization and tenancy design",
                ["Concern", "Design rule", "Example"],
                [
                    ["Station tenancy", "Every station-owned query must be scoped by police_station_id", "Incidents, cameras, officers, tips"],
                    ["Dispatcher authority", "Only authorized station users may claim, reject, link, or dispatch", "incidents.dispatch permission"],
                    ["Institutional vs individual identity", "Station account and station user are separate actors", "Supervisor login vs dispatcher action identity"],
                    ["Channel authorization", "Private channels authorize tenant/person ownership", "station.{id}, officer.{id}, panic events"],
                    ["AI camera authority", "Model sees only assigned cameras", "camera_ai_model pivot"],
                    ["Backend-mediated device authority", "UI cannot talk directly to camera devices", "Tapo/ONVIF commands pass through backend/gateway"],
                ],
                [4.0, 7.2, 5.0],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Data protection",
            "title": "Encryption, Signed Media, and Sensitive Data Design",
            "paragraphs": [
                (
                    "CrimeLens stores and transfers sensitive material: camera credentials, "
                    "model signing secrets, police-station data, incident evidence, citizen "
                    "tip media, body-camera uploads, chat media, and stream URLs. The design "
                    "therefore uses encryption at rest for credentials and secrets, signed "
                    "media URLs for private files, bounded access lifetimes, and careful "
                    "serialization to avoid leaking hidden values.",
                    "[30], [31]",
                ),
                (
                    "Signed URLs are especially important because browser video players and "
                    "mobile clients must fetch playlists, segments, clips, thumbnails, and "
                    "media files without receiving raw storage access. A short-lived signed "
                    "route lets the application authorize a request while keeping storage "
                    "private.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.23",
                "Data protection and media-access design",
                ["Asset", "Protection method", "Design reason"],
                [
                    ["Camera credentials", "Encrypted casts and hidden serialization", "Protect device access secrets"],
                    ["AI signing secret", "Encrypted storage and HMAC verification", "Prevent forged model reports"],
                    ["AI camera payload", "Per-session encryption of stream material", "Reduce exposure if a response is intercepted"],
                    ["Evidence clips", "Private storage and signed URLs", "Protect crime media from public access"],
                    ["Citizen-tip media", "Signed routes with controlled visibility", "Allow review without public storage exposure"],
                    ["HLS segments/playlists", "Signed playback route and short TTL", "Permit players while limiting link reuse"],
                    ["Ledger hashes", "Append-only chain and verification", "Detect tampering with consequential decisions"],
                ],
                [3.7, 5.9, 6.6],
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Realtime design",
            "title": "Realtime Channels, Push Notifications, and Presence",
            "section": "4.6",
            "paragraphs": [
                (
                    "The realtime design separates foreground and background delivery. "
                    "Browser consoles receive live updates through private channels, while "
                    "mobile devices receive Firebase Cloud Messaging (FCM) push notifications "
                    "for assignments, panic, backup, and chat when the application may not "
                    "be open. Database notifications support an in-app notification center.",
                    "[30], [31]",
                ),
                (
                    "Realtime events should always supplement the database, not replace it. "
                    "If a browser misses a WebSocket event, refreshing the page must still "
                    "recover the authoritative incident state. This design keeps the database "
                    "as the source of truth and treats broadcasts as a fast synchronization "
                    "rail.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.24",
                "Realtime and notification channels",
                ["Channel / mechanism", "Consumers", "Purpose"],
                [
                    ["station.{id}", "Station and dispatcher browser clients", "Incidents, assignments, tips, panic, chat, and status updates"],
                    ["officer.{id}", "Officer mobile and officer-specific listeners", "Assignment, backup, chat, and status-related updates"],
                    ["admin.camera-health", "Admin console", "Camera tamper, offline, and system-health alerts"],
                    ["Firebase tokens", "Officer and mobile users", "Background push delivery"],
                    ["Database notifications", "Web and mobile notification centers", "Durable notification history"],
                    ["Redis presence/cache", "Dispatcher and assignment services", "Online state, active location, nonce blocking, fast lookup"],
                ],
                [4.1, 5.3, 6.8],
                accent=TEAL,
            ),
        },
        {
            "kicker": "Interface design",
            "title": "Interface Allocation by Actor",
            "paragraphs": [
                (
                    "The interface design follows actor authority rather than feature "
                    "popularity. Each actor should see the tasks it is responsible for and "
                    "should not receive controls that belong to another authority level. "
                    "This keeps the product understandable and reduces accidental misuse.",
                    "[30]",
                ),
                (
                    "The most important allocation decision is that the police station and "
                    "dispatcher experience is web-first. Live monitoring, incident triage, "
                    "multi-camera layouts, map panels, officer lists, citizen-tip media, and "
                    "linked incidents are easier to operate from a desktop browser than from "
                    "a small mobile screen. Officer work is mobile-first because it happens "
                    "in the field.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.25",
                "Interface design allocation",
                ["Actor", "Primary surface", "Design focus"],
                [
                    ["System administrator", "Admin web console", "Governance, station/AI management, settings, health, notifications"],
                    ["Police station", "Station web console", "Institutional management, officers, cameras, users, station operations"],
                    ["Dispatcher / station user", "Dispatcher web surface", "Incident review, claim, dispatch, maps, streams, tips, chat"],
                    ["Field officer", "Flutter mobile app", "Assignments, navigation, status, panic, evidence, resolution"],
                    ["Station companion", "Mobile assistance surface", "Lightweight support only; not the main dispatch console"],
                    ["AI model", "Machine API", "Authentication, assigned cameras, heartbeat, signed detection reporting"],
                    ["Camera gateway", "Machine/internal API", "Stream provisioning, device commands, tamper webhook"],
                    ["Citizen reporter", "Public web/SMS intake", "Submit tip, location, message, and optional media"],
                ],
                [3.5, 4.7, 8.0],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Information architecture",
            "title": "Navigation and Screen Group Design",
            "paragraphs": [
                (
                    "A good interface architecture reduces the number of decisions an "
                    "operator must make under pressure. CrimeLens groups screens according "
                    "to operational flow: monitoring, incident queue, incident details, "
                    "dispatch map, officer management, camera management, citizen tips, "
                    "chat, analytics, settings, and audit. Each screen group should expose "
                    "actions that are valid for the current role and current entity state.",
                    "[30]",
                ),
                (
                    "Interface evidence is selected for the design decision it demonstrates, "
                    "not for decoration. Representative views should clarify live monitoring, "
                    "incident review, officer assignment, admin AI management, camera control, "
                    "citizen-tip triage, panic alert, or evidence display.",
                    None,
                ),
            ],
            "table": table(
                "Table 4.26",
                "Navigation and screen-group design",
                ["Screen group", "Primary actor", "Design evidence demonstrated"],
                [
                    ["Admin dashboard", "Admin", "System health, stations, AI models, and configuration visibility"],
                    ["Dispatcher live monitoring", "Dispatcher", "Camera grid, incident queue, and realtime context in one workspace"],
                    ["Incident details", "Dispatcher", "Priority factors, source, evidence, location, and decision actions"],
                    ["Officer assignment map", "Dispatcher", "Eligible officers, distance, status, and assignment confirmation"],
                    ["Camera management", "Station/Admin", "Camera identity, status, streams, filters, and control boundaries"],
                    ["Officer mobile assignment", "Officer", "Accept/navigation/status workflow in field context"],
                    ["Panic/SOS", "Officer and station", "Emergency alert visibility and location escalation"],
                    ["Evidence view", "Station/officer", "Signed media display and crime-linked evidence"],
                ],
                [4.2, 3.8, 8.2],
                accent=BLUE,
            ),
        },
        {
            "kicker": "API boundaries",
            "title": "API and Integration Boundary Design",
            "section": "4.7",
            "paragraphs": [
                (
                    "CrimeLens exposes API boundaries according to client type. Browser "
                    "consoles use server-side routes and Inertia responses; mobile clients "
                    "use token-protected JSON endpoints; the AI model uses machine-specific "
                    "endpoints with additional request signing; the gateway uses internal "
                    "routes and webhooks; public citizens use constrained intake routes. "
                    "This prevents one general API from accidentally becoming too powerful.",
                    "[30], [31]",
                ),
                (
                    "Integration design is also shaped by failure. A gateway may be offline, "
                    "an AI model may miss heartbeats, a push notification may be delayed, "
                    "a camera may lose connection, or a queue may retry a job. Interfaces "
                    "therefore need explicit status, retry, timeout, and audit behavior.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.27",
                "API and integration boundary design",
                ["Boundary", "Client", "Design controls"],
                [
                    ["Web console routes", "Admin, station, dispatcher browsers", "Session guard, CSRF, Inertia responses, station scoping"],
                    ["Officer mobile API", "Flutter officer app", "Sanctum, officer guard, rate limits, JSON resources"],
                    ["Station mobile assistance API", "Station companion app", "Sanctum, limited station capabilities"],
                    ["AI model API", "Detection service", "AI guard, IP allow-list, HMAC, timestamp, nonce, assigned cameras"],
                    ["Gateway API/webhooks", "Python gateway", "Gateway token, HMAC, allow-list, rate limits"],
                    ["Public tip intake", "Citizen reporter/SMS", "Validation, media limits, triage state, expiry"],
                    ["Signed media routes", "Browser/mobile players", "Temporary signature, private storage, bounded TTL"],
                ],
                [4.0, 4.6, 7.6],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Background work",
            "title": "Queue, Scheduling, and Worker Design",
            "paragraphs": [
                (
                    "Several CrimeLens operations should not block the user request that "
                    "triggered them. Stream synchronization, scene extraction, notifications, "
                    "camera recording, cleanup, heartbeat checks, ledger verification, and "
                    "analytics-oriented work are better handled through queued jobs and "
                    "scheduled commands. Laravel queues and Horizon provide operational "
                    "visibility for this background workload.",
                    "[30], [31]",
                ),
                (
                    "Queue design should group jobs by operational risk. User-facing alerts "
                    "and assignments need faster handling than maintenance cleanup. Scene "
                    "extraction and media processing may be heavier and should run on a "
                    "dedicated queue so they do not starve dispatch notifications.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.28",
                "Queues, jobs, and scheduled tasks",
                ["Work item", "Design purpose", "Recommended operational grouping"],
                [
                    ["SyncCameraGatewayStreamJob", "Keep gateway streams aligned with active camera state", "gateway/streaming"],
                    ["ExtractCrimeScene", "Generate crime evidence clip and thumbnail", "scenes/media"],
                    ["Camera health checks", "Detect offline cameras and notify stations", "monitoring"],
                    ["Model heartbeat checks", "Detect inactive AI models", "monitoring"],
                    ["Notifications and push delivery", "Deliver browser/mobile operational updates", "notifications"],
                    ["CleanupOldRecordings", "Remove old segments and expired evidence according to retention", "maintenance"],
                    ["ledger:verify", "Re-walk hash chain and detect ledger integrity breaks", "security/audit"],
                ],
                [4.4, 6.6, 5.2],
                accent=GOLD,
            ),
            "figure": figure(
                "Figure 4.13",
                "Queue, scheduling, and worker design",
                "CH04_FIG_13_Queue_Scheduling_Worker_Design.png",
                6.0,
            ),
        },
        {
            "kicker": "Storage design",
            "title": "Evidence Storage and Signed-Media Delivery",
            "paragraphs": [
                (
                    "Evidence storage design connects cameras, officer uploads, citizen-tip "
                    "media, chat media, and generated reports. The design goal is to let "
                    "authorized users view the media they need while keeping the underlying "
                    "storage private. Media should be linked to domain entities so that it "
                    "can be understood in context rather than becoming an unmanaged file.",
                    "[30]",
                ),
                (
                    "Scene extraction is designed around a time window and a camera source. "
                    "When available, the system can cut an evidence clip from camera segments "
                    "or retrieve an appropriate clip from camera storage. Body-camera uploads "
                    "are linked to a Crime and officer. Citizen-tip media is reviewed before "
                    "promotion so public reports do not automatically become official evidence.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.29",
                "Evidence storage and retention design",
                ["Media type", "Linked entity", "Design notes"],
                [
                    ["Camera scene clip", "Crime / scene record", "Generated from Incident creation to dispatch approval and served through signed URL"],
                    ["Thumbnail/sample frame", "Scene or tamper event", "Used for quick review without opening a full video"],
                    ["Body-camera upload", "Crime and officer", "Private storage, metadata, signed playback/download"],
                    ["Citizen-tip media", "Citizen tip", "Triage before promotion; relative signed access where host may vary"],
                    ["Chat media/voice note", "Chat message", "Private route and sender/receiver authorization"],
                    ["Report exports", "Report/job owner", "Generated file should respect actor authorization and expiry"],
                    ["Recording segments", "Camera storage path", "Retention cleanup prevents uncontrolled growth"],
                ],
                [4.0, 4.3, 7.9],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 4.14",
                "Evidence storage and signed-media delivery design",
                "CH04_FIG_14_Evidence_Storage_Signed_Media_Delivery.png",
                6.1,
            ),
        },
        {
            "kicker": "Design decisions",
            "title": "Major Design Decisions and Trade-Offs",
            "paragraphs": [
                (
                    "Design decisions involve trade-offs. A modular monolith is less "
                    "independently deployable than microservices, but it is easier to "
                    "develop, test, and keep transactionally consistent in a graduation "
                    "project. Web-first station operations are less portable than an "
                    "all-mobile station interface, but they support richer monitoring and "
                    "safer dispatch context. Signed media routes add implementation work, "
                    "but they protect evidence.",
                    "[30]",
                ),
                (
                    "The design also favors explicit boundaries over hidden automation. "
                    "AI detections become Incidents, not instant Crimes. Cameras are "
                    "commanded through the backend, not directly from a browser. Realtime "
                    "updates synchronize state but do not replace database authority. "
                    "These decisions make the platform more explainable and safer.",
                    "[30]",
                ),
            ],
            "table": table(
                "Table 4.30",
                "Design decision record summary",
                ["Decision", "Benefit", "Trade-off"],
                [
                    ["Modular monolith", "Clear boundaries with simple deployment", "Less independent scaling than microservices"],
                    ["Incident before Crime", "Human review and false-alarm control", "Adds one workflow stage"],
                    ["Web-first station console", "Better maps, streams, queues, and multitasking", "Not ideal for small screens"],
                    ["Officer mobile-first field workflow", "Supports real patrol work and GPS/panic", "Requires robust mobile API and push"],
                    ["Gateway fan-out", "One camera source can serve AI, HLS, and WebRTC needs", "Gateway becomes an important operational dependency"],
                    ["Redis + PostGIS", "Fast live lookup plus durable spatial analytics", "Requires synchronization discipline"],
                    ["Hash-chained ledger", "Tamper-evident decision history", "Adds write and verification complexity"],
                ],
                [4.7, 6.0, 5.5],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Design validation",
            "title": "Design Consistency and Validation Checklist",
            "paragraphs": [
                (
                    "A system-design chapter should be validated against the analysis chapter "
                    "and the implementation chapter. Every major actor from Chapter Three "
                    "should have a corresponding interface, guard, or integration boundary. "
                    "Every major workflow should have persistent state, authorization, events, "
                    "and audit where appropriate. Every table in the ERD should support a "
                    "real requirement or operational concern.",
                    "[30]",
                ),
                (
                    "The validation checklist also guards against decorative diagrams. Each "
                    "diagram should support a design relationship. If a diagram cannot be read "
                    "on an A4 page, it should be split rather than reduced until its text "
                    "becomes unusable.",
                    None,
                ),
            ],
            "table": table(
                "Table 4.31",
                "Chapter Four design validation checklist",
                ["Check", "Expected evidence", "Where to verify"],
                [
                    ["Actors are mapped to surfaces", "Admin, station, dispatcher, officer, AI, gateway, citizen each has a boundary", "Tables 4.20, 4.25, 4.27"],
                    ["ERD supports workflows", "Incident, Crime, Camera, Officer, Evidence, Audit entities connect correctly", "Figures 4.7 to 4.11"],
                    ["Security boundaries are explicit", "Guards, HMAC, IP allow-list, encryption, signed URLs, tenancy", "Tables 4.20 to 4.23"],
                    ["Realtime is recoverable", "Events supplement persistent state rather than replacing it", "Table 4.24"],
                    ["Queues are separated by workload", "Media work and notifications do not block critical requests", "Table 4.28"],
                    ["Interface evidence supports design decisions", "Each referenced view demonstrates a workflow or authority boundary", "Table 4.26"],
                    ["Future limitations are deferred", "Known gaps are discussed in Chapter Seven rather than hidden in design", "Conclusion and Future Work"],
                ],
                [4.2, 7.0, 5.0],
                accent=CYAN_DARK,
            ),
            "info": (
                "Chapter close",
                "Chapter Four defines how the system is designed. Chapter Five should "
                "then show how the Laravel, React/Inertia, Flutter, AI, streaming, "
                "database, queues, and deployment pieces were implemented.",
                GREEN,
                "NEXT",
            ),
        },
    ]
