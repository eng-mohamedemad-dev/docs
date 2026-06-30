"""Structured content for CrimeLens Chapter Five — System Implementation."""

from __future__ import annotations


CYAN_DARK = "0E7490"
GOLD = "D4AF37"
GREEN = "22C55E"
PURPLE = "A855F7"
RED = "EF4444"
BLUE = "2563EB"
TEAL = "2DD4BF"


CHAPTER_FIVE_FIGURES = [
    ("Figure 5.1", "Chapter-opening implementation background", 154),
    ("Figure 5.2", "Implementation evidence and traceability map", 155),
    ("Figure 5.3", "Agile vertical-slice delivery timeline", 156),
    ("Figure 5.4", "Repository and module structure", 157),
    ("Figure 5.5", "Laravel modular-monolith implementation map", 159),
    ("Figure 5.6", "Database migration and seeding implementation flow", 161),
    ("Figure 5.7", "Station route slice from browser to service layer", 162),
    ("Figure 5.8", "Admin console implementation surface", 164),
    ("Figure 5.9", "Dispatcher console implementation surface", 166),
    ("Figure 5.10", "Incident service transaction flow", 167),
    ("Figure 5.11", "Officer mobile implementation architecture", 170),
    ("Figure 5.12", "AI model service runtime lifecycle", 173),
    ("Figure 5.13", "Camera gateway runtime and stream fan-out", 175),
    ("Figure 5.14", "Realtime event and notification implementation", 177),
    ("Figure 5.15", "Horizon queue topology and scheduled workers", 178),
    ("Figure 5.16", "Security implementation layers", 181),
    ("Figure 5.17", "Local development and demo runtime stack", 184),
    ("Figure 5.18", "Testing and quality evidence map", 185),
    ("Figure 5.19", "Screenshot insertion checklist for Chapter Five", 187),
]


CHAPTER_FIVE_TABLES = [
    ("Table 5.1", "Implementation chapter scope", 155),
    ("Table 5.2", "Agile implementation increments", 156),
    ("Table 5.3", "Repository implementation map", 157),
    ("Table 5.4", "Technology stack realized in code", 158),
    ("Table 5.5", "Laravel module implementation responsibilities", 159),
    ("Table 5.6", "Backend code-layer implementation pattern", 160),
    ("Table 5.7", "Migration and seeding implementation", 161),
    ("Table 5.8", "API and web route implementation groups", 162),
    ("Table 5.9", "Inertia and React implementation pattern", 163),
    ("Table 5.10", "Admin console implemented features", 164),
    ("Table 5.11", "Station and dispatcher implemented features", 165),
    ("Table 5.12", "Live monitoring and camera-control implementation", 166),
    ("Table 5.13", "Incident and dispatch service implementation", 167),
    ("Table 5.14", "Priority and auto-dispatch implementation", 168),
    ("Table 5.15", "Officer field workflow implementation", 169),
    ("Table 5.16", "Flutter mobile implementation structure", 170),
    ("Table 5.17", "Mobile networking and notification implementation", 171),
    ("Table 5.18", "Citizen tips, BOLO, panic, and chat implementation", 172),
    ("Table 5.19", "AI model runtime implementation", 173),
    ("Table 5.20", "AI backend integration implementation", 174),
    ("Table 5.21", "Camera gateway and stream implementation", 175),
    ("Table 5.22", "Evidence and media implementation", 176),
    ("Table 5.23", "Realtime event implementation", 177),
    ("Table 5.24", "Queues and schedules implemented", 178),
    ("Table 5.25", "Settings, reports, analytics, and observability implementation", 179),
    ("Table 5.26", "Security controls implemented in code", 180),
    ("Table 5.27", "Authentication and authorization implementation", 181),
    ("Table 5.28", "Data protection implementation", 182),
    ("Table 5.29", "Configuration and environment implementation", 183),
    ("Table 5.30", "Development and demo commands", 184),
    ("Table 5.31", "Testing and quality implementation evidence", 185),
    ("Table 5.32", "Software-engineering practices applied", 186),
    ("Table 5.33", "Chapter Five screenshot and evidence checklist", 187),
]


CHAPTER_FIVE_REFERENCES = [
    (
        "[33]",
        "CrimeLens Project Team, CrimeLens source repository, modules, route files, "
        "services, jobs, events, React/Inertia pages, Flutter application, AI model "
        "server, gateway scripts, tests, and internal documentation, Beni-Suef "
        "University, Jun. 2026.",
    ),
    (
        "[34]",
        "A. Cockburn, Agile Software Development: The Cooperative Game, 2nd ed. "
        "Boston, MA, USA: Addison-Wesley, 2006.",
    ),
    (
        "[35]",
        "R. C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship. "
        "Upper Saddle River, NJ, USA: Prentice Hall, 2008.",
    ),
    (
        "[36]",
        "CrimeLens Project Team, Project implementation plans, system guides, "
        "frontend notification notes, camera gateway notes, and testing inventory, "
        "Beni-Suef University, 2026.",
    ),
]


def figure(
    number: str,
    caption: str,
    filename: str,
    height: float = 6.3,
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


def code(title: str, snippet: str) -> tuple[str, str]:
    return (title, snippet)


def chapter_five_page_specs() -> list[dict]:
    return [
        {
            "kicker": "Implementation evidence",
            "title": "Introduction to System Implementation",
            "section": "5.1",
            "paragraphs": [
                (
                    "Chapter Five explains how the design of Chapter Four was realized "
                    "inside the actual CrimeLens repository. The chapter is written from "
                    "a software-engineering viewpoint: it connects requirements to code "
                    "modules, modules to runtime services, services to routes and jobs, "
                    "and implemented features to tests, configuration, and demo evidence.",
                    "[33]",
                ),
                (
                    "The implementation is not presented as one large script. CrimeLens "
                    "was built as a set of vertical slices: authentication, cameras, "
                    "AI intake, incident review, dispatch, mobile response, realtime "
                    "notifications, evidence, analytics, reports, and quality checks. "
                    "Each slice contains database state, backend logic, user interface, "
                    "integration behavior, and validation evidence.",
                    "[33], [34]",
                ),
            ],
            "table": table(
                "Table 5.1",
                "Implementation chapter scope",
                ["Implementation area", "What is described", "Evidence type"],
                [
                    ["Backend", "Laravel modules, routes, controllers, services, actions, events, jobs", "PHP source and route inventory"],
                    ["Database", "Migrations, models, factories, seeders, enums, relationships", "Schema files and demo seeders"],
                    ["Web", "Admin and station consoles built with Inertia, React, TypeScript, Tailwind", "Entry points, pages, layouts, browser tests"],
                    ["Mobile", "Flutter officer workflows, API client, token storage, push, maps, media", "Dart code, features, pubspec, tests"],
                    ["AI", "Flask model server, API client, inference services, camera manager", "Python code and model-server services"],
                    ["Gateway", "Flask gateway, FFmpeg, MediaMTX, HLS/WebRTC, Tapo control", "Python gateway, scripts, configuration"],
                    ["Operations", "Queues, scheduler, Horizon, Telescope, Pail, setup commands", "Config files and scheduled providers"],
                ],
                [3.3, 8.0, 4.9],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 5.2",
                "Implementation evidence and traceability map",
                "CH05_FIG_02_Implementation_Evidence_Traceability_Map.png",
                5.6,
            ),
        },
        {
            "kicker": "Agile process",
            "title": "Agile and Incremental Delivery",
            "paragraphs": [
                (
                    "CrimeLens was implemented using an Agile, integration-oriented "
                    "approach rather than a purely sequential handoff. The team moved "
                    "from analysis to working slices, then refined the design as "
                    "integration evidence appeared. This is visible in the repository: "
                    "requirements, routes, services, tests, seeders, demo data, and "
                    "documentation evolved together.",
                    "[34], [36]",
                ),
                (
                    "The practical Agile unit was the vertical slice. A slice was not "
                    "considered meaningful when only a screen existed or only a database "
                    "table existed. A complete slice connected user intent, validation, "
                    "authorization, persistence, service logic, realtime side effects, "
                    "and test or demo evidence. This approach reduced integration risk.",
                    "[33], [34]",
                ),
            ],
            "table": table(
                "Table 5.2",
                "Agile implementation increments",
                ["Increment", "Main delivered capability", "Engineering evidence"],
                [
                    ["Foundation", "Laravel modules, guards, database, seeders, shared conventions", "Migrations, auth config, module providers"],
                    ["Sensing", "Camera CRUD, gateway registration, streams, filters, tamper", "Camera module, gateway service, Python gateway"],
                    ["AI intake", "Model identity, encrypted camera handshake, signed alert endpoint", "AiModel module, model-server ApiClient"],
                    ["Dispatch", "Incident queue, claim/release, priority, dispatch/reject, officer recommendation", "Police services, station routes, events"],
                    ["Field response", "Officer mobile assignment, GPS, status, panic, body-cam, chat", "Flutter app, officer APIs, FCM"],
                    ["Operations", "Queues, schedules, reports, analytics, ledger, monitoring", "Horizon config, scheduled providers, tests"],
                ],
                [3.1, 7.1, 6.0],
                accent=GOLD,
            ),
            "figure": figure(
                "Figure 5.3",
                "Agile vertical-slice delivery timeline",
                "CH05_FIG_03_Agile_Vertical_Slice_Delivery_Timeline.png",
                5.8,
            ),
        },
        {
            "kicker": "Repository map",
            "title": "Repository Structure and Implementation Boundaries",
            "paragraphs": [
                (
                    "The repository is organized around the implemented system boundaries. "
                    "The Laravel application lives at the project root and is separated "
                    "into Admin, Police, Camera, Gateway, AiModel, and Core modules. The "
                    "AI model server and Flutter mobile application are separate folders "
                    "because they have different runtimes, dependencies, tests, and "
                    "deployment concerns.",
                    "[33]",
                ),
                (
                    "This layout supports maintainability. A developer looking for camera "
                    "behavior starts in the Camera module and gateway scripts; a developer "
                    "looking for dispatch logic starts in the Police module; a developer "
                    "working on mobile assignments starts in the Flutter application; and "
                    "a developer working on model inference starts in the model-server.",
                    "[33], [35]",
                ),
            ],
            "table": table(
                "Table 5.3",
                "Repository implementation map",
                ["Path", "Implementation responsibility", "Notes"],
                [
                    ["Modules/Admin", "Administrative web console, settings, reports, AI management", "Inertia pages and PHP services"],
                    ["Modules/Police", "CAD workflow, dispatcher console, officers, incidents, crimes", "Largest operational module"],
                    ["Modules/Camera", "Camera persistence, control, gateway sync, recording, evidence", "Owns camera policies and jobs"],
                    ["Modules/AiModel", "Machine identity, secure intake, AI analytics, heartbeat", "API-first module"],
                    ["Modules/Core", "Shared chat, notifications, settings, ledger, encryption", "Cross-cutting services"],
                    ["Modules/Gateway", "Python gateway, MediaMTX, FFmpeg helper scripts", "External runtime alongside Laravel"],
                    ["mobile-app/...", "Flutter field application", "Officer-first mobile surface"],
                    ["ai-model/...", "Flask AI model server and inference services", "Computer-vision runtime"],
                ],
                [3.5, 7.4, 5.3],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 5.4",
                "Repository and module structure",
                "CH05_FIG_04_Repository_Module_Structure.png",
                6.2,
            ),
        },
        {
            "kicker": "Technology realization",
            "title": "Implemented Technology Stack",
            "paragraphs": [
                (
                    "The implemented stack matches the design chapter: PHP/Laravel for "
                    "the backend, PostgreSQL/PostGIS for relational and spatial data, "
                    "Redis for cache, queues, presence, nonce protection, and hot "
                    "location lookup, React/Inertia for the web consoles, Flutter for "
                    "the field application, Python/Flask for the camera gateway and AI "
                    "model server, and Pusher/Firebase for realtime delivery.",
                    "[33]",
                ),
                (
                    "The implementation also uses engineering tooling that supports "
                    "repeatability: Composer scripts for setup and development, Vite for "
                    "asset builds, Horizon for queue supervision, Telescope and Pail for "
                    "debugging, Pest and browser tests for backend/web behavior, Flutter "
                    "tests for mobile behavior, and model-server tests for selected AI "
                    "client behavior.",
                    "[33], [36]",
                ),
            ],
            "table": table(
                "Table 5.4",
                "Technology stack realized in code",
                ["Layer", "Implemented technologies", "Repository evidence"],
                [
                    ["Backend", "PHP 8.4 target, Laravel 13, Sanctum, Horizon, Telescope", "composer.json, config, modules"],
                    ["Web frontend", "Inertia v3, React 19, TypeScript, Tailwind CSS v4, Vite", "package.json, admin.tsx, station.tsx"],
                    ["Mobile", "Flutter, BLoC/Cubit, Dio, Firebase Messaging, Pusher, maps, media packages", "pubspec.yaml, lib/features"],
                    ["AI service", "Flask, OpenCV, NumPy, PyTorch/TensorFlow, Ultralytics, scikit-learn", "model-server requirements and services"],
                    ["Gateway", "Flask, pytapo, FFmpeg, MediaMTX, HLS, WebRTC relay", "tapo_server.py and gateway scripts"],
                    ["Data/ops", "PostgreSQL/PostGIS, Redis, queues, scheduler, signed storage", "migrations, config, jobs, providers"],
                ],
                [3.0, 7.8, 5.4],
                accent=TEAL,
            ),
        },
        {
            "kicker": "Backend modules",
            "title": "Laravel Modular Backend Implementation",
            "section": "5.2",
            "paragraphs": [
                (
                    "The backend is implemented as a modular monolith using Laravel modules. "
                    "This gives the project clear internal boundaries without the deployment "
                    "overhead of many independent services. Each module has its own routes, "
                    "controllers, providers, services, jobs, events, policies, tests, and "
                    "resource files where needed.",
                    "[33]",
                ),
                (
                    "This implementation choice is consistent with clean architecture "
                    "principles at project scale. The modules are cohesive around business "
                    "capabilities, while shared concerns such as settings, chat, encryption, "
                    "notifications, and the decision ledger are centralized in Core to reduce "
                    "duplication.",
                    "[33], [35]",
                ),
            ],
            "table": table(
                "Table 5.5",
                "Laravel module implementation responsibilities",
                ["Module", "Implemented responsibilities", "Representative evidence"],
                [
                    ["Admin", "Station governance, AI management, settings, reports, health, audit, chat", "Admin routes, services, React pages"],
                    ["Police", "Incidents, crimes, officers, dispatch, tips, BOLO, panic, station web", "Station routes, services, events, jobs"],
                    ["Camera", "Camera CRUD, gateway service, control routes, tamper, recording, scenes", "Camera routes, jobs, services, policies"],
                    ["AiModel", "Model auth, heartbeat, camera assignment, signed alert intake", "Model routes, services, tests"],
                    ["Gateway", "Python gateway and Laravel bridge for streams/control", "tapo_server.py, CameraGatewayService"],
                    ["Core", "Encryption, ledger, settings, chat, notifications, reports", "Core services and tests"],
                ],
                [2.7, 8.3, 5.2],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 5.5",
                "Laravel modular-monolith implementation map",
                "CH05_FIG_05_Laravel_Modular_Monolith_Implementation_Map.png",
                6.0,
            ),
        },
        {
            "kicker": "Backend layers",
            "title": "Controller, Request, Service, Action, Event, and Job Pattern",
            "paragraphs": [
                (
                    "The backend implementation follows a layered pattern. Routes select "
                    "controllers; controllers validate and authorize requests; services "
                    "or actions perform domain logic; models persist state; events notify "
                    "interested clients; and jobs execute slow or retryable work. This keeps "
                    "HTTP details separate from business decisions.",
                    "[33], [35]",
                ),
                (
                    "The pattern appears repeatedly across the repository. Dispatch is "
                    "implemented through station routes, an IncidentController, an "
                    "IncidentService transaction, the CrimeService, events such as "
                    "IncidentReviewed and CrimeAssigned, notification jobs, and ledger "
                    "entries. This is a software-engineering implementation, not a screen-only prototype.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.6",
                "Backend code-layer implementation pattern",
                ["Layer", "Repository examples", "Engineering benefit"],
                [
                    ["Routes", "station.web.php, api.php, Admin routes, Camera routes, AiModel routes", "Defines surface, guards, and throttles"],
                    ["Controllers", "IncidentController, AiModelController, Camera controllers", "Translate requests to use cases"],
                    ["Requests/DTOs", "Form requests and DTO folders in modules", "Validation and typed transfer"],
                    ["Services", "IncidentService, CameraGatewayService, AlertService", "Reusable domain operations"],
                    ["Actions", "EscalateCrimeAction, import actions", "Explicit multi-step operations"],
                    ["Events", "IncidentCreated, CrimeAssigned, PanicActivated", "Realtime domain notifications"],
                    ["Jobs", "ExtractCrimeScene, MaybeAutoDispatchIncident, SyncCameraGatewayStreamJob", "Retryable asynchronous work"],
                ],
                [3.0, 7.2, 6.0],
                accent=CYAN_DARK,
            ),
            "code": code(
                "Implementation snippet — AI model route chain",
                """Route::prefix('v1/model')->group(function () {
    Route::post('login', [AiModelAuthController::class, 'login'])
        ->middleware('throttle:5,1');

    Route::middleware(['auth:ai_model', 'verify.model_ip'])->group(function () {
        Route::get('cameras', [AiModelController::class, 'cameras']);
        Route::post('heartbeat', [AiModelController::class, 'heartbeat']);

        Route::middleware(['verify.ai_signature'])->group(function () {
            Route::post('alert', [AiModelController::class, 'alert']);
            Route::post('crime', [AiModelController::class, 'crime']);
        });
    });
});""",
            ),
        },
        {
            "kicker": "Persistence",
            "title": "Database, Models, Migrations, and Seeders",
            "section": "5.3",
            "paragraphs": [
                (
                    "The database implementation is built from Laravel migrations and "
                    "Eloquent models. Migrations create the operational schema, factories "
                    "support tests and demo data, and seeders create roles, permissions, "
                    "stations, cameras, officers, incidents, crimes, and presentation data. "
                    "This makes the demo reproducible instead of manually assembled.",
                    "[33]",
                ),
                (
                    "The system uses model casts, enums, relationships, spatial fields, "
                    "JSON/JSONB data, polymorphic relations, and encrypted casts. These "
                    "implementation details connect the ERD from Chapter Four to executable "
                    "code.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.7",
                "Migration and seeding implementation",
                ["Artifact", "Implementation use", "Example"],
                [
                    ["Migrations", "Create tables, pivots, spatial columns, auth infrastructure", "incidents, crimes, cameras, officers, ledger_entries"],
                    ["Models", "Represent domain entities and relationships", "Incident, Crime, Camera, Officer, CitizenTip"],
                    ["Enums", "Represent valid states and types", "IncidentStatus, CrimeStatus, OfficerStatus"],
                    ["Factories", "Generate test/demo records", "CitizenTipFactory and model factories"],
                    ["Seeders", "Load roles, demo data, presentation data", "DatabaseSeeder, RolesAndPermissionsSeeder, DemoSeeder"],
                    ["Presentation seeders", "Create visually rich demo scenarios", "PresentationDemoSeeder"],
                ],
                [3.1, 7.2, 5.9],
                accent=GOLD,
            ),
            "figure": figure(
                "Figure 5.6",
                "Database migration and seeding implementation flow",
                "CH05_FIG_06_Database_Migration_Seeding_Implementation_Flow.png",
                5.7,
            ),
        },
        {
            "kicker": "Routes and APIs",
            "title": "API and Web Route Implementation",
            "paragraphs": [
                (
                    "The implementation exposes separate route groups for each client "
                    "type. Admin and station consoles use web/session routes. Officer and "
                    "station companion clients use token-protected API routes. AI models "
                    "use machine routes under /api/v1/model. Camera gateway routes use "
                    "gateway IP and HMAC middleware. Public citizen-tip routes are constrained "
                    "and triaged before promotion.",
                    "[33]",
                ),
                (
                    "This routing design is more than organization. It is an implementation "
                    "of the trust model: each route group carries the guard, middleware, "
                    "throttle, and controller set appropriate to its actor.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.8",
                "API and web route implementation groups",
                ["Route group", "Primary client", "Implemented controls"],
                [
                    ["/admin", "Admin browser", "admin session guard, admin broadcasting auth"],
                    ["/station", "Station/dispatcher browser", "station guards, force_password_change, station broadcasting auth"],
                    ["/api/v1/officer", "Officer mobile", "officer Sanctum guard, signed media routes"],
                    ["/api/v1/police-station", "Station companion API", "police_station Sanctum guard"],
                    ["/api/v1/model", "AI model server", "ai_model guard, IP check, HMAC for alert"],
                    ["/api/camera", "Camera gateway/control path", "gateway.ip, gateway.hmac, throttle"],
                    ["/tip/{stationCode}", "Citizen reporter", "Public intake, validation, later triage"],
                ],
                [4.0, 4.8, 7.4],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 5.7",
                "Station route slice from browser to service layer",
                "CH05_FIG_07_Station_Route_Slice_Browser_To_Service.png",
                5.8,
            ),
        },
        {
            "kicker": "Web frontend",
            "title": "Inertia, React, TypeScript, and Tailwind Implementation",
            "section": "5.4",
            "paragraphs": [
                (
                    "The web frontends are implemented as Inertia/React applications. "
                    "Admin and station surfaces have separate module entry points, while "
                    "shared utilities live under resources/js. This allows Laravel to keep "
                    "server-side routing and authorization while React handles interactive "
                    "interfaces such as dashboards, monitoring grids, forms, maps, and "
                    "realtime panels.",
                    "[33]",
                ),
                (
                    "The React layer uses TypeScript types, shared hooks, reusable components, "
                    "Echo/Pusher listeners, HLS/WebRTC playback helpers, permission helpers, "
                    "toast helpers, and design tokens. Tailwind CSS v4 supports the visual "
                    "system without moving domain logic into styles.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.9",
                "Inertia and React implementation pattern",
                ["Implementation element", "Repository evidence", "Purpose"],
                [
                    ["Admin entry point", "Modules/Admin/resources/js/admin.tsx", "Bootstraps admin Inertia app"],
                    ["Station entry point", "Modules/Police/resources/js/station.tsx", "Bootstraps station/dispatcher app"],
                    ["Shared utilities", "resources/js/lib", "API helpers, hooks, realtime, media players"],
                    ["Layouts", "StationLayout.tsx and admin layouts", "Consistent navigation and shell"],
                    ["Typed payloads", "resources/js/types", "Safer UI contracts"],
                    ["Browser tests", "tests/Browser and module web tests", "Regression evidence for pages and interactions"],
                ],
                [4.0, 5.5, 6.7],
                accent=BLUE,
            ),
            "code": code(
                "Implementation snippet — Inertia entry-point pattern",
                """createInertiaApp({
    resolve: name => resolvePageComponent(
        `./Pages/${name}.tsx`,
        import.meta.glob('./Pages/**/*.tsx'),
    ),
    setup({ el, App, props }) {
        createRoot(el).render(<App {...props} />);
    },
});""",
            ),
        },
        {
            "kicker": "Admin console",
            "title": "Admin Console Implementation",
            "paragraphs": [
                (
                    "The admin console implements governance features rather than field "
                    "dispatch. It includes police-station management, AI model management, "
                    "camera assignment, analytics, settings, priority-weight dry-run/apply, "
                    "system health, audit export, reports, notifications, simulation, chat, "
                    "camera tamper handling, and a camera gateway test surface.",
                    "[33]",
                ),
                (
                    "The implementation follows the same backend/frontend split as the rest "
                    "of the system. Admin routes map to controllers, controllers call services, "
                    "services prepare snapshots or actions, and React pages render the final "
                    "operator interface.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.10",
                "Admin console implemented features",
                ["Feature group", "Implemented capabilities", "Representative files"],
                [
                    ["Stations", "CRUD, import/export, city support, password reset", "PoliceStationsController and React pages"],
                    ["AI models", "CRUD, camera assignment, analytics, comparison, reset", "AiModelsController and analytics services"],
                    ["Settings", "Firebase, system, camera settings, priority weights", "SettingsController, PriorityWeightsController"],
                    ["Health and audit", "System checks, audit table, CSV export", "SystemHealthService, AuditLogService"],
                    ["Reports and simulation", "Reports snapshot and demo trigger", "ReportsController, DemoSimulationController"],
                    ["Camera health", "Tamper acknowledge/false alarm", "CameraTamperEventsController"],
                ],
                [3.5, 7.0, 5.7],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 5.8",
                "Admin console implementation surface",
                "CH05_FIG_08_Admin_Console_Implementation_Surface.png",
                6.2,
            ),
        },
        {
            "kicker": "Station console",
            "title": "Police Station and Dispatcher Web Implementation",
            "paragraphs": [
                (
                    "The station console implements the operational workflow for the "
                    "station and its dispatchers. The route file includes login, forced "
                    "password change, dispatcher dashboard, incident APIs, claims, release, "
                    "nearest officers, manual incident creation, dispatch, rejection, camera "
                    "stream access, heatmap, monitoring, citizen tips, crimes, officers, "
                    "cameras, users, BOLOs, profile, chat, notifications, and Firebase token "
                    "registration.",
                    "[33]",
                ),
                (
                    "The station web surface remains the main police-station interface. "
                    "Mobile station support exists as companion API capability, but live "
                    "camera monitoring, maps, incident review, and dispatcher collaboration "
                    "are implemented primarily for the browser workspace.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.11",
                "Station and dispatcher implemented features",
                ["Feature", "Implemented actions", "Engineering concern"],
                [
                    ["Incident queue", "Index, show, nearest officers, create, dispatch, reject, link", "State transition and authorization"],
                    ["Claim/release", "Claim, release, stale claim cleanup, presence ping", "Concurrency control"],
                    ["Cameras", "CRUD, streams, filters, alarm, movement, connection test", "Gateway-backed control"],
                    ["Officers", "CRUD, reset password, patrol zone, activity locations", "Field resource management"],
                    ["Citizen tips", "Review, promote, dismiss, reply, signed media", "Untrusted public input triage"],
                    ["Communication", "Chat, voice, notifications, unread counts", "Realtime station awareness"],
                ],
                [3.4, 7.0, 5.8],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Monitoring",
            "title": "Live Monitoring and Camera Control Implementation",
            "paragraphs": [
                (
                    "Live monitoring is implemented through the station web console and "
                    "gateway-backed stream URLs. The web client can request stream metadata, "
                    "play HLS or WebRTC where appropriate, display camera coverage, and send "
                    "authorized commands such as alarm or movement through backend routes. "
                    "The browser never talks directly to the physical camera.",
                    "[33]",
                ),
                (
                    "Camera control is protected both by station authorization and by the "
                    "gateway security layer. Backend routes throttle camera actions; gateway "
                    "routes require IP/HMAC controls; and the Python gateway executes the "
                    "actual device-level interaction.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.12",
                "Live monitoring and camera-control implementation",
                ["Capability", "Implementation path", "Why it is engineered this way"],
                [
                    ["Stream listing", "Station camera stream endpoint", "UI receives role-appropriate stream data"],
                    ["HLS playback", "Signed /gateway/hls/{key}/index.m3u8 route", "Players fetch media without a session cookie dependency"],
                    ["WebRTC relay", "Gateway/MediaMTX relay URLs", "Lower-latency monitoring"],
                    ["Alarm control", "Station route → camera service → gateway command", "Backend authority controls physical device"],
                    ["PTZ movement", "Station route throttle → gateway command", "Prevents direct browser-to-camera control"],
                    ["Connection test", "Station/API controller with gateway validation", "Demo and operator feedback"],
                ],
                [3.4, 6.3, 6.5],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 5.9",
                "Dispatcher console implementation surface",
                "CH05_FIG_09_Dispatcher_Console_Implementation_Surface.png",
                6.2,
            ),
        },
        {
            "kicker": "Incident workflow",
            "title": "Incident and Dispatch Service Implementation",
            "section": "5.5",
            "paragraphs": [
                (
                    "The IncidentService implements the most important domain boundary in "
                    "CrimeLens. Accepted AI alerts and manual reports create pending "
                    "Incidents. Repeated AI alerts from the same camera within three minutes "
                    "reuse the existing pending Incident. A dispatcher then dispatches or rejects the Incident. Dispatch "
                    "uses a database transaction and row lock so the workflow is not corrupted "
                    "by concurrent operators.",
                    "[33]",
                ),
                (
                    "When an Incident is dispatched, the service creates a Crime through "
                    "CrimeService, updates review fields, optionally triggers the camera alarm "
                    "job, writes activity/ledger evidence, and broadcasts IncidentReviewed. "
                    "This implementation expresses the rule that the backend, not the UI, "
                    "owns state transitions.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.13",
                "Incident and dispatch service implementation",
                ["Method / component", "Implementation role", "Important behavior"],
                [
                    ["createFromAiAlert", "Convert suspicious model alert to pending Incident", "Priority context, log, event, maybe auto-dispatch"],
                    ["AlertService duplicate window", "Reuse recent pending AI Incident for the same camera", "Three-minute window, detection log preserved"],
                    ["createManual", "Allow station-created incidents", "Manual source and created_by actor"],
                    ["dispatch", "Approve Incident and create Crime", "DB transaction, lockForUpdate, ledger, event"],
                    ["reject", "Reject false alarm", "Reason code, review fields, event"],
                    ["IncidentCreated/Reviewed", "Broadcast domain updates", "Realtime station queue synchronization"],
                ],
                [3.8, 6.4, 6.0],
                accent=RED,
            ),
            "code": code(
                "Implementation snippet — transaction and row-level lock",
                """return DB::transaction(function () use ($incident, $reviewer, $officer) {
    $lockedIncident = Incident::query()
        ->whereKey($incident->id)
        ->lockForUpdate()
        ->firstOrFail();

    if (! $lockedIncident->isPending()) {
        throw new DomainException('Incident is not pending review.');
    }

    $crime = $this->crimeService->createFromIncident($lockedIncident, $officer);
    IncidentReviewed::dispatch($lockedIncident->refresh(), 'dispatched');
    return $crime;
});""",
            ),
            "figure": figure(
                "Figure 5.10",
                "Incident service transaction flow",
                "CH05_FIG_10_Incident_Service_Transaction_Flow.png",
                5.0,
            ),
        },
        {
            "kicker": "Priority engine",
            "title": "Priority Scoring and Auto-Dispatch Implementation",
            "paragraphs": [
                (
                    "Priority scoring is implemented as a service-level calculation rather "
                    "than a hard-coded UI label. The scoring context includes confidence, "
                    "weapon signal, crime-type weight, time-of-day factor, and repeat-area "
                    "factor. The output stores both the priority score and the factor "
                    "breakdown so a dispatcher can understand why an Incident is high or low.",
                    "[33]",
                ),
                (
                    "Auto-dispatch is implemented as a policy and job path rather than a "
                    "default assumption. This keeps the normal human-in-the-loop workflow "
                    "intact while allowing a controlled policy to be evaluated asynchronously "
                    "for special cases.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.14",
                "Priority and auto-dispatch implementation",
                ["Component", "Implemented responsibility", "Design value"],
                [
                    ["IncidentPriorityService", "Creates context and computes priority output", "Centralizes scoring"],
                    ["PriorityScorer", "Applies configured weights and tier thresholds", "Avoids UI-only priority logic"],
                    ["priority_factors JSON", "Stores explainable breakdown", "Supports review, reports, and audit"],
                    ["Settings/Priority weights", "Admin dry-run and apply behavior", "Tunable without code changes"],
                    ["AutoDispatchPolicy", "Checks narrow auto-dispatch eligibility", "Keeps automation governed"],
                    ["MaybeAutoDispatchIncident", "Queued policy evaluation", "Avoids blocking intake"],
                ],
                [4.1, 6.1, 6.0],
                accent=GOLD,
            ),
            "info": (
                "Engineering principle",
                "A score that affects operations must be computed, stored, and explainable. "
                "It should not exist only as a color or label on a screen.",
                CYAN_DARK,
                "PRINCIPLE",
            ),
        },
        {
            "kicker": "Field workflow",
            "title": "Officer Crime Lifecycle Implementation",
            "paragraphs": [
                (
                    "The field workflow is implemented through officer APIs and mobile "
                    "screens. An officer can receive a Crime assignment, view a tactical "
                    "brief, accept, reject/no-visit, update location and status, activate "
                    "panic, upload body-camera media, use chat/quick replies/voice, view "
                    "active BOLOs, and resolve the Crime.",
                    "[33]",
                ),
                (
                    "Backend authorization protects officer actions. An officer cannot act "
                    "on an unassigned Crime, and signed media routes serve body-camera and "
                    "chat voice files without exposing public storage paths.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.15",
                "Officer field workflow implementation",
                ["Workflow action", "API endpoint family", "Implementation concern"],
                [
                    ["Accept/no-visit/resolve", "/api/v1/officer/crimes/{crime}/...", "Crime status transition and authorization"],
                    ["Pre-arrival brief", "/api/v1/officer/crimes/{crime}/brief", "Tactical context before arrival"],
                    ["Location update", "/api/v1/officer/location", "Redis/PostGIS location synchronization"],
                    ["Status update", "/api/v1/officer/status", "Availability and shift state"],
                    ["Panic/SOS", "/api/v1/officer/panic", "Emergency event broadcast and backup fan-out"],
                    ["Body-cam upload", "/api/v1/officer/crimes/{crime}/body-cam", "Private media and signed serving"],
                    ["Chat and quick reply", "/api/v1/officer/chat/...", "Field communication"],
                ],
                [4.0, 5.4, 6.8],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Mobile app",
            "title": "Flutter Mobile Implementation",
            "section": "5.6",
            "paragraphs": [
                (
                    "The Flutter application is implemented as a feature-oriented mobile "
                    "project. Core infrastructure contains configuration, networking, "
                    "routing, token storage, notification services, location tracking, "
                    "themes, shared widgets, and media viewers. Feature folders contain "
                    "authentication, officer presentation widgets, splash flow, and user "
                    "selection.",
                    "[33]",
                ),
                (
                    "The mobile implementation uses Dio for HTTP communication, GetIt for "
                    "service location, BLoC/Cubit for several state flows, Firebase "
                    "Messaging and local notifications for push delivery, Pusher channels "
                    "for realtime communication, Google Maps and geolocation packages for "
                    "field movement, and media packages for camera/video/audio features.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.16",
                "Flutter mobile implementation structure",
                ["Folder / component", "Purpose", "Examples"],
                [
                    ["core/network", "HTTP client and endpoint definitions", "api_client.dart, api_endpoints.dart"],
                    ["core/storage", "Token persistence", "auth_token_storage.dart"],
                    ["core/services", "Session, FCM, notification, sound, location tracking", "push_notification_service.dart"],
                    ["core/router", "Navigation", "app_router.dart"],
                    ["features/auth", "Login and password reset flow", "data/domain/presentation layers"],
                    ["features/officer", "Officer-specific UI widgets", "pre_arrival_brief_card.dart"],
                    ["core/pages/widgets", "Live stream, crime scene video, shared player widgets", "camera_live_stream_screen.dart"],
                ],
                [3.7, 6.0, 6.5],
                accent=BLUE,
            ),
            "figure": figure(
                "Figure 5.11",
                "Officer mobile implementation architecture",
                "CH05_FIG_11_Officer_Mobile_Implementation_Architecture.png",
                6.2,
            ),
        },
        {
            "kicker": "Mobile integration",
            "title": "Mobile Networking, Push, Location, and Media",
            "paragraphs": [
                (
                    "The mobile client is implemented around authenticated API calls and "
                    "stored tokens. After login, the application persists the session, "
                    "registers a Firebase token, fetches assignments and notifications, "
                    "sends officer location updates, and uses signed URLs for protected "
                    "media such as body-camera footage and chat voice.",
                    "[33]",
                ),
                (
                    "For field work, location and push behavior are implementation-critical. "
                    "An officer may be outside a station workstation, so background push, "
                    "device notification, sound cues, maps, and secure token handling are "
                    "not optional interface details; they are part of the operational workflow.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.17",
                "Mobile networking and notification implementation",
                ["Concern", "Implemented package / component", "Role"],
                [
                    ["HTTP client", "Dio and core API client", "Authenticated REST calls"],
                    ["Session storage", "Shared preferences/token storage", "Retain login state"],
                    ["Push delivery", "firebase_messaging and local notifications", "Background assignments, panic, chat"],
                    ["Realtime", "pusher_channels_flutter", "Live station/officer channels where needed"],
                    ["Maps/location", "google_maps_flutter, geolocator, geocoding", "Navigation, GPS updates, location display"],
                    ["Media", "video_player, flutter_webrtc, image/file picker, record", "Evidence, streams, voice notes"],
                    ["Encryption helpers", "encrypt and crypto", "Support secure payload handling where used"],
                ],
                [3.3, 6.2, 6.7],
                accent=TEAL,
            ),
            "code": code(
                "Implementation snippet — mobile API boundary pattern",
                """final response = await apiClient.post(
  ApiEndpoints.officerLocation,
  data: {'lat': latitude, 'lng': longitude},
);

await fcmTokenService.registerCurrentDeviceToken();
final token = await authTokenStorage.readToken();""",
            ),
        },
        {
            "kicker": "Operational features",
            "title": "Citizen Tips, BOLO, Panic, and Chat Implementation",
            "paragraphs": [
                (
                    "CrimeLens implements several supporting operational features that make "
                    "the dispatch workflow more realistic. Citizen tips provide public intake "
                    "through web and SMS paths. BOLO records broadcast important subject or "
                    "area information. Panic/SOS protects officers in the field. Chat supports "
                    "text, quick replies, image/media, and voice-message workflows.",
                    "[33]",
                ),
                (
                    "These features are implemented as first-class workflows rather than "
                    "loose notes attached to crimes. Each has routes, validation, models, "
                    "events or notifications, and media handling where required.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.18",
                "Citizen tips, BOLO, panic, and chat implementation",
                ["Feature", "Implemented path", "Operational contribution"],
                [
                    ["Citizen tips", "TipIntakeService, CitizenTipService, public/twilio/station routes", "Turns public reports into triaged station work"],
                    ["BOLO", "Station BOLO routes and officer active BOLO API", "Broadcasts area/subject warnings"],
                    ["Panic/SOS", "Officer panic API, panic events, nearby officer notification job", "Protects field officers"],
                    ["Chat", "Core ChatService, station/admin/officer APIs, presence channels", "Coordinates station/officer/admin communication"],
                    ["Voice", "ChatVoiceController and TranscribeChatVoice job", "Supports field-friendly communication"],
                    ["Notifications", "Database notifications and FirebaseService", "Durable and background delivery"],
                ],
                [3.2, 6.9, 6.1],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "AI runtime",
            "title": "AI Model Server Implementation",
            "section": "5.7",
            "paragraphs": [
                (
                    "The AI model runtime is implemented as a Flask-based orchestrator. "
                    "At startup, it loads model artifacts, authenticates with the Laravel "
                    "backend, retrieves the per-session encryption key, fetches assigned "
                    "cameras, decrypts stream material, starts camera-processing threads, "
                    "sends heartbeats, refreshes cameras periodically, and reports alerts "
                    "or confirmed crimes.",
                    "[33]",
                ),
                (
                    "The model server keeps the machine-client responsibility narrow. It "
                    "watches streams and reports observations; it does not dispatch officers, "
                    "create final Crimes, or command cameras through the normal production API.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.19",
                "AI model runtime implementation",
                ["Component", "Implementation responsibility", "Evidence"],
                [
                    ["main.py", "Flask app and ModelServer lifecycle", "start, heartbeat, camera refresh, dashboard"],
                    ["ApiClient", "Login, token, encryption key, HMAC signing, alert posts", "services/api_client.py"],
                    ["CameraManager", "Assigned camera sync and processing threads", "services/camera_processor.py"],
                    ["InferenceService", "Load and run weapon/fire/crime/action models", "services/inference_service.py"],
                    ["EncryptionService", "Decrypt encrypted camera payloads", "services/encryption_service.py"],
                    ["StreamReader", "Read camera streams for inference", "services/stream_reader.py"],
                ],
                [3.5, 7.0, 5.7],
                accent=RED,
            ),
            "figure": figure(
                "Figure 5.12",
                "AI model service runtime lifecycle",
                "CH05_FIG_12_AI_Model_Service_Runtime_Lifecycle.png",
                6.2,
            ),
        },
        {
            "kicker": "AI backend contract",
            "title": "AI Backend Integration Implementation",
            "paragraphs": [
                (
                    "The Laravel AiModel module implements the backend contract for the "
                    "model server. It handles model login, logout, assigned camera retrieval, "
                    "heartbeat, alert reporting, camera filters, detection "
                    "logs, model analytics, and heartbeat monitoring.",
                    "[33]",
                ),
                (
                    "HMAC signing is implemented by the Python client and verified by "
                    "Laravel middleware. Each signed request includes a timestamp and nonce "
                    "to reduce replay risk. This is an example of implementation following "
                    "the security design rather than leaving security as a diagram-only claim.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.20",
                "AI backend integration implementation",
                ["Capability", "Backend component", "Model-side component"],
                [
                    ["Login/session", "AiModelAuthController, ai_model guard", "ApiClient.login"],
                    ["Assigned cameras", "AiModelController.cameras", "ApiClient.fetch_cameras"],
                    ["Heartbeat", "AiModelController.heartbeat, model:check-heartbeats", "ModelServer heartbeat loop"],
                    ["Alert report", "AlertService, IncidentService", "ApiClient.send_alert"],
                    ["Signing", "VerifyAiSignature middleware", "ApiClient._signature_headers"],
                    ["Analytics", "ai_detection_logs and admin analytics services", "Detection decisions and confidence payloads"],
                ],
                [3.6, 6.2, 6.4],
                accent=RED,
            ),
            "code": code(
                "Implementation snippet — AI client HMAC headers",
                """digest = hmac.new(
    self.signing_secret.encode('utf-8'),
    body.encode('utf-8'),
    hashlib.sha256,
).hexdigest()

return {
    'X-Signature': f'sha256={digest}',
    'X-Timestamp': str(int(time.time())),
    'X-Nonce': secrets.token_hex(16),
}""",
            ),
        },
        {
            "kicker": "Gateway runtime",
            "title": "Camera Gateway and Streaming Implementation",
            "section": "5.8",
            "paragraphs": [
                (
                    "The camera gateway is implemented as a persistent Flask service. It "
                    "stores a camera registry, keeps cached Tapo connections, tracks active "
                    "FFmpeg stream processes, produces HLS output, can publish RTSP/WebRTC "
                    "relay URLs through MediaMTX, and protects gateway operations with an "
                    "X-Gateway-Token shared secret.",
                    "[33]",
                ),
                (
                    "Laravel communicates with the gateway through CameraGatewayService. "
                    "The service registers camera credentials, starts and stops streams, "
                    "checks stream status, executes camera commands, checks gateway health, "
                    "normalizes responses, retries selected calls, and translates common "
                    "camera-control errors for the user interface.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.21",
                "Camera gateway and stream implementation",
                ["Gateway feature", "Python implementation", "Laravel integration"],
                [
                    ["Camera registry", "_camera_registry keyed by gateway_stream_key", "registerCamera/registerCameraCredentials"],
                    ["Stream process", "_stream_processes and FFmpeg command", "startStreamByKey/stopStreamByKey/status"],
                    ["HLS output", "GATEWAY_HLS_ROOT and playlist route", "signed Laravel HLS proxy"],
                    ["RTSP/WebRTC relay", "MediaMTX publish/public URL builders", "gateway stream URLs on Camera"],
                    ["Device control", "Tapo connection cache and command endpoints", "executeCommandByKey/executeCameraCommand"],
                    ["Security", "require_gateway_token before_request", "X-Gateway-Token header and gateway middleware"],
                ],
                [3.7, 6.4, 6.1],
                accent=TEAL,
            ),
            "code": code(
                "Implementation snippet — Laravel gateway client header",
                """$client = Http::acceptJson()
    ->asJson()
    ->baseUrl(rtrim($baseUrl, '/'))
    ->connectTimeout(config('services.camera_gateway.connect_timeout', 5))
    ->timeout(config('services.camera_gateway.timeout', 30))
    ->retry(2, 250, throw: false);

return $client->withHeader('X-Gateway-Token', $secret);""",
            ),
            "figure": figure(
                "Figure 5.13",
                "Camera gateway runtime and stream fan-out",
                "CH05_FIG_13_Camera_Gateway_Runtime_Stream_Fanout.png",
                5.7,
            ),
        },
        {
            "kicker": "Evidence media",
            "title": "Scene Extraction, Body-Cam, and Signed Media Implementation",
            "paragraphs": [
                (
                    "Evidence implementation spans camera segments, generated scene clips, "
                    "body-camera uploads, citizen-tip media, tamper sample frames, chat voice "
                    "notes, and HLS playlist/segment serving. Private media is exposed through "
                    "signed routes rather than public storage paths.",
                    "[33]",
                ),
                (
                    "Scene extraction is queued because FFmpeg work can be slow. The design "
                    "keeps media processing outside the dispatch request path, preserving "
                    "operator responsiveness while still producing linked evidence records.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.22",
                "Evidence and media implementation",
                ["Media path", "Implementation component", "Protection / processing"],
                [
                    ["Crime scene", "ExtractCrimeScene job and SceneExtractorService", "Queued FFmpeg and private scene route"],
                    ["Body cam", "BodyCamController", "Upload throttle and signed serve route"],
                    ["Citizen-tip media", "CitizenTipsController media route", "Relative signed URL"],
                    ["Tamper sample", "CameraTamperController and private tamper route", "Signed access"],
                    ["Chat voice", "ChatVoiceController and TranscribeChatVoice", "Signed serve and transcript job"],
                    ["HLS media", "Gateway HLS proxy", "Sessionless signed playback route"],
                ],
                [3.4, 6.8, 6.0],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Realtime",
            "title": "Events, Broadcasting, and Notifications Implementation",
            "section": "5.9",
            "paragraphs": [
                (
                    "Realtime behavior is implemented through Laravel events, private "
                    "broadcast channels, Echo/Pusher subscriptions, Firebase push messages, "
                    "and database notifications. Events such as IncidentCreated, "
                    "IncidentAssigned, IncidentReviewed, CrimeAssigned, PanicActivated, "
                    "CitizenTipReceived, CameraTamperDetected, and AiModelOffline connect "
                    "backend state changes to web and mobile clients.",
                    "[33]",
                ),
                (
                    "The implementation keeps the database authoritative. Broadcasts update "
                    "screens quickly, but a client can still reload and recover the current "
                    "state from API or Inertia payloads. This prevents WebSocket delivery "
                    "from becoming a hidden source of truth.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.23",
                "Realtime event implementation",
                ["Event family", "Events", "Consumers"],
                [
                    ["Incident", "IncidentCreated, IncidentAssigned, IncidentReviewed", "Station dispatcher console"],
                    ["Crime/officer", "CrimeAssigned, CrimeResolved, OfficerLocationUpdated", "Officer app, station map, admin tracking"],
                    ["Safety", "PanicActivated, PanicResolved, OfficerProximityChanged", "Station/officer emergency surfaces"],
                    ["Community", "CitizenTipReceived, BoloBroadcasted, WeaponClusterDetected", "Station queue and officer notifications"],
                    ["Infrastructure", "CameraOffline, CameraTamperDetected, AiModelOffline", "Admin and station health views"],
                    ["Chat", "ChatMessageSent, ChatTranscriptUpdated", "Conversation participants"],
                ],
                [3.2, 7.2, 5.8],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 5.14",
                "Realtime event and notification implementation",
                "CH05_FIG_14_Realtime_Event_Notification_Implementation.png",
                6.0,
            ),
        },
        {
            "kicker": "Background work",
            "title": "Queues, Horizon, and Scheduler Implementation",
            "paragraphs": [
                (
                    "Background work is implemented through Redis queues and Laravel Horizon. "
                    "The Horizon configuration separates default/notifications/reports/health/"
                    "scenes/maintenance work from incident work, broadcast/FCM work, and "
                    "camera-alarm work. This prevents heavy media tasks from blocking urgent "
                    "operational notifications.",
                    "[33]",
                ),
                (
                    "Scheduling is implemented both in the root console routes and module "
                    "service providers. Camera health, AI heartbeat checks, gateway boot, "
                    "recording cleanup, stale dispatcher assignment release, officer route "
                    "processing, daily reports, ledger verification, Horizon snapshots, and "
                    "Telescope pruning are all represented in the scheduler configuration.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.24",
                "Queues and schedules implemented",
                ["Workload", "Implementation location", "Cadence / queue"],
                [
                    ["Incident auto-dispatch", "MaybeAutoDispatchIncident", "incidents queue"],
                    ["Broadcasts and push", "Events, FirebaseService, Horizon supervisors", "broadcasts/fcm queues"],
                    ["Camera alarm", "TriggerCameraAlarmJob", "camera-alarms queue"],
                    ["Scene extraction", "ExtractCrimeScene", "scenes queue"],
                    ["Camera health", "CameraServiceProvider schedule", "every second"],
                    ["AI heartbeat", "AiModelServiceProvider schedule", "every second"],
                    ["Gateway boot", "CameraServiceProvider schedule", "every two minutes"],
                    ["Ledger verification", "routes/console.php", "daily at 02:00"],
                ],
                [4.0, 7.0, 5.2],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 5.15",
                "Horizon queue topology and scheduled workers",
                "CH05_FIG_15_Horizon_Queue_Topology_Scheduled_Workers.png",
                6.0,
            ),
        },
        {
            "kicker": "Operational intelligence",
            "title": "Settings, Reports, Analytics, and Observability Implementation",
            "paragraphs": [
                (
                    "CrimeLens includes operational support features beyond the core dispatch "
                    "path. Settings are implemented as cached key/value configuration. Admin "
                    "reports and snapshots summarize system state. AI analytics use detection "
                    "logs to show acceptance and model behavior. Heatmaps use spatial data. "
                    "Horizon exposes queue metrics, Telescope records request/debug telemetry, "
                    "and Pail supports live log inspection during development.",
                    "[33]",
                ),
                (
                    "These features support the Agile feedback loop. They help the team see "
                    "whether integration is working, whether queues are running, whether "
                    "models are alive, whether cameras are active, and whether the demo data "
                    "is producing understandable scenarios.",
                    "[33], [34]",
                ),
            ],
            "table": table(
                "Table 5.25",
                "Settings, reports, analytics, and observability implementation",
                ["Capability", "Implementation component", "Purpose"],
                [
                    ["Settings", "SettingsService and admin settings routes", "Change operational values without code edits"],
                    ["Priority weights", "SettingsDryRunService and PriorityWeightsController", "Evaluate and apply scoring changes"],
                    ["Reports", "ReportsSnapshotService and GenerateReport/GenerateDailyReportJob", "Summarize operational data"],
                    ["AI analytics", "AiModelAnalyticsService and detection logs", "Monitor model output and drift indicators"],
                    ["Heatmaps", "Heatmap services and spatial data", "Reveal crime/camera/officer patterns"],
                    ["Queue observability", "Horizon configuration and snapshots", "Understand background workload"],
                    ["Debug telemetry", "Telescope and Pail", "Development-time inspection"],
                ],
                [3.6, 6.8, 5.8],
                accent=BLUE,
            ),
        },
        {
            "kicker": "Security implementation",
            "title": "Implemented Security Controls",
            "section": "5.10",
            "paragraphs": [
                (
                    "Security is implemented across middleware, guards, model casts, signed "
                    "routes, services, policies, request validation, rate limits, channel "
                    "authorization, and ledger verification. This chapter does not repeat "
                    "the design theory from Chapter Four; it shows how those controls appear "
                    "in executable code.",
                    "[33]",
                ),
                (
                    "The system uses defense in depth. A machine client may need a token, "
                    "correct source IP, valid HMAC signature, fresh timestamp, unused nonce, "
                    "and assigned-camera authorization. A web user may need the right session "
                    "guard, station scope, role permission, and private channel authorization.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.26",
                "Security controls implemented in code",
                ["Control", "Implementation location", "Protects"],
                [
                    ["Multi-guard authentication", "config/auth.php and route middleware", "Admin, station, officer, AI surfaces"],
                    ["Sanctum tokens", "Mobile and machine API guards", "Officer, station companion, AI model"],
                    ["IP allow-list", "verify.model_ip and gateway.ip middleware", "AI and gateway trust boundaries"],
                    ["HMAC signatures", "verify.ai_signature and gateway.hmac", "Payload integrity and replay resistance"],
                    ["Encrypted casts", "Camera credentials and model secrets", "Sensitive persisted secrets"],
                    ["Signed media routes", "Laravel signed middleware/routes", "Evidence, HLS, body cam, chat voice"],
                    ["Ledger hash chain", "LedgerService and ledger:verify", "Decision accountability"],
                ],
                [3.9, 6.5, 5.8],
                accent=RED,
            ),
        },
        {
            "kicker": "Auth and authorization",
            "title": "Authentication, RBAC, Policies, and Channel Authorization",
            "paragraphs": [
                (
                    "Authentication is implemented with separate guards for admin web, "
                    "station web, individual station user web, police-station API, officer "
                    "API, AI model API, default API, and framework web usage. Authorization "
                    "then adds policies, station scoping, role/permission checks, and channel "
                    "authorization callbacks.",
                    "[33]",
                ),
                (
                    "The station user model and Spatie permission tables support individual "
                    "dispatcher permissions. This matters because a station account can be "
                    "institutional, but dispatch decisions should still be traceable to a "
                    "permissioned operator where individual users are used.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.27",
                "Authentication and authorization implementation",
                ["Implementation mechanism", "Examples", "Purpose"],
                [
                    ["Session guards", "admin, police_station_web, station_user_web", "Browser console authentication"],
                    ["Sanctum guards", "officer, police_station, ai_model", "Mobile and machine authentication"],
                    ["Force password change", "force_password_change middleware", "Initial credential rotation"],
                    ["Policies", "CrimePolicy, OfficerPolicy, IncidentPolicy, CameraPolicy", "Model-level authorization"],
                    ["RBAC", "RolesAndPermissionsSeeder and station user permissions", "Fine-grained dispatcher permissions"],
                    ["Channel auth", "Modules/*/routes/channels.php", "Private realtime tenancy"],
                    ["Signed routes", "body-cam, chat voice, HLS, tip media", "Temporary media authorization"],
                ],
                [4.0, 6.1, 6.1],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 5.16",
                "Security implementation layers",
                "CH05_FIG_16_Security_Implementation_Layers.png",
                5.8,
            ),
        },
        {
            "kicker": "Data protection",
            "title": "Encryption, Signing, Media Protection, and Audit Implementation",
            "paragraphs": [
                (
                    "Data protection is implemented through multiple code paths. Laravel "
                    "encrypted casts protect persisted credentials and signing secrets. "
                    "The AI camera handshake encrypts camera payloads with a session key. "
                    "Signed media routes protect private files. HMAC middleware protects "
                    "machine payloads. The ledger creates a tamper-evident chain for important "
                    "decisions.",
                    "[33]",
                ),
                (
                    "Auditability is implemented both broadly and deeply. Activity logs record "
                    "general actions, while ledger entries focus on consequential decisions "
                    "such as dispatch, rejection, escalation, and promotion. The nightly "
                    "ledger verification command checks whether the hash chain remains intact.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.28",
                "Data protection implementation",
                ["Asset", "Implementation method", "Verification / usage"],
                [
                    ["Camera credentials", "Encrypted Eloquent casts", "Hidden from serialization and decrypted only in trusted code"],
                    ["AI signing secret", "Encrypted model field and HMAC middleware", "Signature verification for alert"],
                    ["AI camera payload", "EncryptionService and per-login key", "Model decrypts assigned camera URLs"],
                    ["Private evidence", "Signed media controllers/routes", "Temporary access to clips and uploads"],
                    ["Citizen media", "Relative signed station media route", "Works across local/tunnel host changes"],
                    ["Decision ledger", "LedgerService, hash fields, ledger:verify", "Tamper-evident audit trail"],
                    ["Machine replay protection", "Timestamp and Redis nonce cache", "Rejects stale/reused signed requests"],
                ],
                [3.5, 6.6, 6.1],
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Configuration",
            "title": "Environment and Configuration Implementation",
            "paragraphs": [
                (
                    "Configuration is implemented through Laravel config files, environment "
                    "variables, module config files, Python gateway environment variables, "
                    "model-server configuration, and Flutter application configuration. This "
                    "keeps credentials, hostnames, ports, timeouts, queue drivers, broadcast "
                    "keys, and external-service tokens outside source logic.",
                    "[33]",
                ),
                (
                    "The implementation also supports demo and local development through "
                    "Composer scripts. composer run setup installs dependencies, creates the "
                    "environment, generates the key, runs migrations, installs Node packages, "
                    "and builds assets. composer run dev starts Laravel, queue listener, Pail, "
                    "Vite, scheduler, and gateway boot behavior together.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.29",
                "Configuration and environment implementation",
                ["Config area", "Files / variables", "Purpose"],
                [
                    ["Laravel application", ".env, config/app.php, config/services.php", "URLs, drivers, external-service credentials"],
                    ["Auth", "config/auth.php, config/sanctum.php", "Guards and token behavior"],
                    ["Queues", "config/queue.php, config/horizon.php", "Redis queues and supervisors"],
                    ["Broadcasting", "config/broadcasting.php and Pusher env vars", "Realtime web delivery"],
                    ["Camera gateway", "services.camera_gateway and gateway env vars", "Gateway base URL, shared secret, timeouts"],
                    ["AI model", "model-server config.py and .env", "Backend URL, model credentials, thresholds"],
                    ["Flutter", "app_config.dart, firebase_options.dart, pubspec.yaml", "API base, Firebase, assets, packages"],
                ],
                [3.4, 6.8, 6.0],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Runtime",
            "title": "Development, Demo, and Deployment Runtime",
            "section": "5.11",
            "paragraphs": [
                (
                    "The local runtime is designed to be repeatable. The Laravel application "
                    "requires PHP, Composer, Node, PostgreSQL/PostGIS, Redis, FFmpeg, and "
                    "external keys for optional services such as Pusher, Firebase, and Twilio. "
                    "The gateway and AI model server run as Python processes with their own "
                    "dependencies.",
                    "[33], [36]",
                ),
                (
                    "Production deployment would supervise PHP-FPM/Nginx, Horizon workers, "
                    "the Laravel scheduler, PostgreSQL, Redis, the Python gateway, MediaMTX, "
                    "and the AI model runtime. Chapter Five describes implementation and "
                    "demo readiness; final measured performance belongs in Chapter Six.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.30",
                "Development and demo commands",
                ["Command / process", "What it runs", "Use"],
                [
                    ["composer run setup", "Composer install, env, key, migrations, npm install, build", "Initial bootstrap"],
                    ["php artisan migrate --seed", "Database migrations and seeders", "Demo/test data preparation"],
                    ["composer run dev", "Serve, queue listener, Pail, Vite, scheduler, gateway boot", "Integrated local development"],
                    ["php artisan horizon", "Horizon queue workers", "Queue processing and monitoring"],
                    ["python Modules/Gateway/tapo_server.py", "Gateway Flask service", "Camera streaming/control"],
                    ["python model-server/main.py", "AI model orchestrator", "Inference and AI reports"],
                    ["npm run build", "Vite production build", "Web assets"],
                ],
                [4.4, 7.0, 4.8],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 5.17",
                "Local development and demo runtime stack",
                "CH05_FIG_17_Local_Development_Demo_Runtime_Stack.png",
                6.0,
            ),
        },
        {
            "kicker": "Quality evidence",
            "title": "Testing and Quality Implementation",
            "section": "5.12",
            "paragraphs": [
                (
                    "Testing is implemented across Laravel, browser, Flutter, and AI client "
                    "areas. The repository contains feature tests, unit tests, browser tests, "
                    "module-specific tests, Flutter tests, and model-server tests. The count "
                    "should be presented as discovered inventory unless a final full-suite "
                    "run is recorded in the target environment.",
                    "[33], [36]",
                ),
                (
                    "The implementation uses tests to protect critical workflows such as "
                    "authorization, cross-station isolation, incident actions, camera gateway "
                    "sync, AI signatures, detection filters, panic, pattern alerts, ledger "
                    "append-only behavior, media serving, notifications, and browser pages.",
                    "[33]",
                ),
            ],
            "table": table(
                "Table 5.31",
                "Testing and quality implementation evidence",
                ["Test area", "Examples", "Quality purpose"],
                [
                    ["Laravel feature/unit", "Module tests under Modules/*/tests and tests/Feature", "Backend behavior and authorization"],
                    ["Browser tests", "tests/Browser and page smoke tests", "Web console regression"],
                    ["Camera tests", "Gateway boot, recording, scene extraction, tamper", "Streaming/evidence reliability"],
                    ["AI tests", "AI signature, model routes, detection filters", "Machine-client security and intake"],
                    ["Ledger tests", "AppendOnly, hash parity, verifier, event wiring", "Audit integrity"],
                    ["Flutter tests", "mobile-app test directory", "Mobile domain/UI behavior where covered"],
                    ["Formatting/static", "Pint, Larastan/PHPStan availability", "Consistency and maintainability"],
                ],
                [3.4, 7.0, 5.8],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 5.18",
                "Testing and quality evidence map",
                "CH05_FIG_18_Testing_Quality_Evidence_Map.png",
                6.0,
            ),
        },
        {
            "kicker": "Engineering discipline",
            "title": "Software-Engineering Practices Applied",
            "paragraphs": [
                (
                    "CrimeLens applies software-engineering practices throughout the "
                    "implementation: modular boundaries, separation of concerns, explicit "
                    "domain services, transaction boundaries, event-driven updates, queued "
                    "side effects, role-based authorization, repeatable seed data, versioned "
                    "API routes, private media access, automated tests, and living internal "
                    "documentation.",
                    "[33], [35]",
                ),
                (
                    "The most important engineering habit is traceability. A feature should "
                    "be traceable from requirement to route, controller, service, model state, "
                    "event/job, interface, and test or demo evidence. This is the difference "
                    "between a graduation demo that merely appears to work and a system that "
                    "can be explained, reviewed, and improved.",
                    "[33], [35]",
                ),
            ],
            "table": table(
                "Table 5.32",
                "Software-engineering practices applied",
                ["Practice", "CrimeLens implementation", "Benefit"],
                [
                    ["Separation of concerns", "Controllers, requests, services, actions, jobs, events", "Maintainable domain logic"],
                    ["Single responsibility", "Modules and services own focused responsibilities", "Less accidental coupling"],
                    ["Fail fast", "Validation, guards, middleware, throttles, exceptions", "Invalid states rejected early"],
                    ["Transactional consistency", "DB transactions and row locks for dispatch", "Safer concurrent operations"],
                    ["Event-driven integration", "Broadcast events and queued notifications", "Responsive UIs without tight coupling"],
                    ["Repeatable demos", "Seeders and presentation data", "Reliable review and presentation"],
                    ["Traceability", "Requirements to tests and documentation", "Academic and engineering accountability"],
                ],
                [3.6, 7.3, 5.3],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Evidence insertion",
            "title": "Screenshots and Implementation Evidence to Add Later",
            "paragraphs": [
                (
                    "The Word file intentionally contains placeholders instead of inserted "
                    "screenshots. Screenshots should be added only when they prove an "
                    "implemented capability. For Chapter Five, the most useful images are "
                    "not generic UI shots; they are evidence of working implementation "
                    "slices: route-to-screen behavior, dispatcher monitoring, mobile field "
                    "actions, AI model dashboard, gateway status, Horizon queues, and test "
                    "runs.",
                    None,
                ),
                (
                    "When inserting screenshots, crop the image to the relevant area, remove "
                    "private credentials, keep text readable on A4, and prefer one clear "
                    "workflow per figure. If a screen contains sensitive or noisy data, use "
                    "demo seed data rather than real personal information.",
                    None,
                ),
            ],
            "table": table(
                "Table 5.33",
                "Chapter Five screenshot and evidence checklist",
                ["Placeholder", "Image to provide", "Purpose"],
                [
                    ["CH05_FIG_08", "Admin console screenshot", "Governance and management evidence"],
                    ["CH05_FIG_09", "Dispatcher monitoring/incident screenshot", "Station operational evidence"],
                    ["CH05_FIG_11", "Officer mobile assignment/status screenshot", "Field workflow evidence"],
                    ["CH05_FIG_12", "AI model dashboard/runtime screenshot", "Inference runtime evidence"],
                    ["CH05_FIG_13", "Gateway stream/status screenshot", "Streaming implementation evidence"],
                    ["CH05_FIG_15", "Horizon queues/supervisors screenshot", "Background work evidence"],
                    ["CH05_FIG_18", "Test result or testing map screenshot", "Quality evidence"],
                ],
                [3.2, 6.2, 6.8],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 5.19",
                "Screenshot insertion checklist for Chapter Five",
                "CH05_FIG_19_Screenshot_Insertion_Checklist.png",
                5.6,
            ),
            "info": (
                "Chapter close",
                "Chapter Five documents the implemented system. Chapter Six should evaluate "
                "it through tests, validation, measured results, and performance evidence.",
                GREEN,
                "NEXT",
            ),
        },
    ]
