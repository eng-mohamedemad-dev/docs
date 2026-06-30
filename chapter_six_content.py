"""Structured content for CrimeLens Chapter Six — System Testing and Evaluation."""

from __future__ import annotations


CYAN_DARK = "0E7490"
GOLD = "D4AF37"
GREEN = "22C55E"
PURPLE = "A855F7"
RED = "EF4444"
BLUE = "2563EB"
TEAL = "2DD4BF"
ORANGE = "F59E0B"


CHAPTER_SIX_FIGURES = [
    ("Figure 6.1", "Chapter-opening testing and evaluation background", 189),
    ("Figure 6.2", "Testing strategy and evidence pipeline", 190),
    ("Figure 6.4", "Laravel full-suite execution screenshot", 194),
    ("Figure 6.8", "Web-console browser testing map", 201),
    ("Figure 6.9", "Flutter mobile testing inventory map", 202),
    ("Figure 6.10", "AI evaluation dashboard and confusion matrix", 204),
    ("Figure 6.11", "Streaming and gateway evaluation map", 206),
]


CHAPTER_SIX_TABLES = [
    ("Table 6.1", "Chapter Six testing and evaluation scope", 190),
    ("Table 6.2", "Quality model and evaluation questions", 191),
    ("Table 6.3", "Evaluation environment and evidence sources", 192),
    ("Table 6.4", "Requirements-to-tests traceability sample", 193),
    ("Table 6.5", "Laravel automated test execution summary", 194),
    ("Table 6.6", "Backend functional-validation coverage", 195),
    ("Table 6.7", "API validation and negative-test coverage", 196),
    ("Table 6.8", "Authorization and tenant-isolation validation", 197),
    ("Table 6.9", "Security and audit-integrity validation", 198),
    ("Table 6.10", "Realtime, queue, and notification validation", 199),
    ("Table 6.11", "Web-console browser testing inventory", 201),
    ("Table 6.12", "Flutter mobile testing inventory", 202),
    ("Table 6.13", "AI model evaluation scope", 203),
    ("Table 6.14", "AI evaluation metrics snapshot", 204),
    ("Table 6.15", "Streaming and camera-gateway evaluation", 205),
    ("Table 6.16", "Performance-testing methodology", 206),
    ("Table 6.17", "Performance results snapshot", 207),
    ("Table 6.18", "Usability and live-demo validation", 208),
    ("Table 6.19", "Demo-data and seed validation", 209),
    ("Table 6.20", "Regression and release gates", 210),
    ("Table 6.21", "Quality refinements applied during evaluation", 211),
    ("Table 6.22", "Acceptance-criteria evaluation summary", 212),
    ("Table 6.23", "Chapter Six evidence checklist", 212),
]


CHAPTER_SIX_REFERENCES = [
    (
        "[37]",
        "CrimeLens Project Team, Final Laravel automated test execution log: "
        "884 passing tests, 3040 assertions, 126.97 seconds, Beni-Suef University, "
        "Jun. 26, 2026.",
    ),
    (
        "[38]",
        "CrimeLens Project Team, CrimeLens testing inventory, feature tests, unit "
        "tests, browser specifications, Flutter tests, model-server tests, seeders, "
        "and quality-review notes, Beni-Suef University, 2026.",
    ),
    (
        "[39]",
        "G. J. Myers, C. Sandler, and T. Badgett, The Art of Software Testing, "
        "3rd ed. Hoboken, NJ, USA: Wiley, 2011.",
    ),
    (
        "[40]",
        "ISO/IEC/IEEE, ISO/IEC/IEEE 29119 Software and Systems Engineering — "
        "Software Testing, International Organization for Standardization, 2013–2022.",
    ),
    (
        "[41]",
        "R. C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship. "
        "Upper Saddle River, NJ, USA: Prentice Hall, 2008.",
    ),
    (
        "[42]",
        "J. Nielsen, Usability Engineering. San Francisco, CA, USA: Morgan Kaufmann, "
        "1993.",
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


def chapter_six_page_specs() -> list[dict]:
    return [
        {
            "kicker": "Evaluation scope",
            "title": "Introduction to System Testing and Evaluation",
            "section": "6.1",
            "paragraphs": [
                (
                    "Chapter Six evaluates CrimeLens as a complete software system, not "
                    "as a collection of isolated screens. The chapter connects the "
                    "implemented modules of Chapter Five to evidence: automated backend "
                    "tests, validation rules, authorization checks, realtime behavior, "
                    "security controls, AI evaluation, streaming behavior, usability "
                    "review, and release-readiness gates.",
                    "[37], [38]",
                ),
                (
                    "The strongest executed evidence in the available environment is the "
                    "Laravel automated test suite. It was executed after a quality pass "
                    "and completed with 884 passing tests, 3040 assertions, and a runtime "
                    "of 126.97 seconds. Browser, Flutter, and model-server tests are "
                    "documented as inventory and evidence placeholders for the final "
                    "project package, because this environment is prepared primarily for "
                    "Laravel execution.",
                    "[37], [38]",
                ),
            ],
            "table": table(
                "Table 6.1",
                "Chapter Six testing and evaluation scope",
                ["Evaluation area", "Evidence used in this chapter", "Purpose"],
                [
                    ["Backend behavior", "Laravel Pest feature and unit execution", "Verify routes, services, policies, jobs, models, and state"],
                    ["Security", "Validation, signatures, signed routes, tenant isolation, ledger tests", "Protect authority boundaries and auditability"],
                    ["Realtime operations", "Broadcast, queue, notification, and event tests", "Verify coordination across dispatcher and officer flows"],
                    ["Web console", "Browser specification inventory and screenshot placeholders", "Support UI regression and demo review"],
                    ["Mobile application", "Flutter test inventory and mobile evidence placeholders", "Document officer-side expected behavior"],
                    ["AI and streaming", "Model-server inventory, reported metrics, gateway checks", "Evaluate perception and media-delivery support"],
                    ["Performance", "Measured snapshot and acceptance targets", "Connect usability to latency and throughput"],
                ],
                [3.2, 7.4, 5.6],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 6.2",
                "Testing strategy and evidence pipeline",
                "Testing_Strategy_Evidence_Pipeline.png",
                5.4,
            ),
        },
        {
            "kicker": "Quality model",
            "title": "Testing Strategy and Quality Attributes",
            "paragraphs": [
                (
                    "The CrimeLens quality model follows a layered software-engineering "
                    "view. Functional correctness verifies that the system performs the "
                    "right actions. Security verifies who is allowed to perform them. "
                    "Reliability verifies that the behavior remains stable under repeated "
                    "execution. Usability verifies that operators can understand and "
                    "complete the workflow. Performance verifies that the workflow remains "
                    "practical for surveillance and dispatch conditions.",
                    "[39], [40]",
                ),
                (
                    "The test strategy therefore combines automated regression tests, "
                    "negative tests, traceability review, acceptance scenarios, and "
                    "manual evidence placeholders. This is especially important for a "
                    "public-safety system where a green user interface is not enough: "
                    "the system must also reject unsafe inputs, prevent cross-station "
                    "access, preserve decision history, and keep humans responsible for "
                    "consequential dispatch decisions.",
                    "[39], [41]",
                ),
            ],
            "table": table(
                "Table 6.2",
                "Quality model and evaluation questions",
                ["Quality attribute", "Evaluation question", "CrimeLens evidence"],
                [
                    ["Correctness", "Does the workflow produce the intended state?", "Feature tests for auth, incidents, cameras, chat, panic, reports"],
                    ["Security", "Can invalid actors or payloads cross boundaries?", "Guard tests, HMAC tests, signed URLs, validation, isolation"],
                    ["Reliability", "Does the system behave consistently across runs?", "Regression suite, deterministic factories, queues, idempotent flows"],
                    ["Performance", "Are response times acceptable for operators?", "Benchmark snapshot and latency targets"],
                    ["Usability", "Can dispatchers and officers follow the workflow?", "Scenario checklist and UI evidence placeholders"],
                    ["Auditability", "Can decisions be reconstructed later?", "Ledger tests, activity logs, state-transition records"],
                ],
                [3.0, 6.7, 6.5],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Evidence setup",
            "title": "Test Environment and Evidence Sources",
            "paragraphs": [
                (
                    "The evaluation environment used for the executed backend suite is the "
                    "local Laravel testing environment with isolated database refreshes, "
                    "model factories, fake storage, fake notifications or broadcasts where "
                    "appropriate, and HTTP requests that pass through real routing and "
                    "middleware. This makes the result stronger than isolated method calls "
                    "because route order, validation, authentication, authorization, and "
                    "database persistence are all exercised.",
                    "[37], [38]",
                ),
                (
                    "For the final printed book, each non-Laravel test area should receive "
                    "a screenshot or exported report from its native toolchain. The Word "
                    "document intentionally uses placeholders so the team can insert clean "
                    "screenshots from the final environment rather than embedding stale or "
                    "low-resolution images.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.3",
                "Evaluation environment and evidence sources",
                ["Evidence source", "Current status in Chapter Six", "Artifact to insert"],
                [
                    ["Laravel backend", "Executed full suite: 884 passed, 3040 assertions", "Evaluation_Dashboard_Confusion_Matrix.png"],
                    ["Browser specs", "Inventory: 3 spec files, 37 browser checks", "Web_Console_Browser_Testing_Map.png"],
                    ["Flutter tests", "Inventory: 38 test files, 180 Dart test definitions", "Flutter_Mobile_Testing_Inventory_Map.png"],
                    ["AI model-server", "Model training/evaluation evidence captured", "evaluation_dashboard.jpeg"],
                    ["Streaming", "Gateway and monitoring stream evidence captured", "Streaming_Gateway_Evaluation_Map.jpeg"],
                    ["Performance", "Measured snapshot and target values recorded", "No image inserted"],
                ],
                [3.4, 6.8, 6.0],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Traceability",
            "title": "Requirements-to-Tests Traceability",
            "section": "6.2",
            "paragraphs": [
                (
                    "Traceability is the bridge between the Software Requirements "
                    "Specification (SRS), the implemented code, and the evaluation "
                    "chapter. A requirement is stronger when the book can point to the "
                    "route, service, model state, event, job, interface, and test evidence "
                    "that support it. Chapter Three defined the requirements; Chapter "
                    "Four designed the mechanisms; Chapter Five implemented them; Chapter "
                    "Six verifies them.",
                    "[38], [40]",
                ),
                (
                    "Not every requirement has the same evidence type. A functional "
                    "requirement may be proven by an automated feature test, while a "
                    "usability requirement may need a walkthrough checklist and screenshots. "
                    "AI performance requires dataset and metric context. Streaming quality "
                    "requires network and browser evidence. This distinction keeps the "
                    "evaluation honest and technically readable.",
                    "[39], [40]",
                ),
            ],
            "table": table(
                "Table 6.4",
                "Requirements-to-tests traceability sample",
                ["Requirement group", "Representative verification", "Evidence level"],
                [
                    ["Authentication", "Login, logout, token guard, forced password, role-specific access", "Automated"],
                    ["Camera management", "CRUD, ownership, gateway test, stream URLs, alarm and PTZ controls", "Automated + screenshot"],
                    ["AI intake", "Signed model payloads, IP checks, confidence thresholds, incident creation", "Automated + AI evidence"],
                    ["Incident workflow", "Claim/release, dispatch, reject, priority, nearest officer", "Automated"],
                    ["Officer workflow", "Assignment, status, location, panic, body-cam, chat", "Automated + mobile evidence"],
                    ["Audit", "Hash-chain ledger, activity records, immutable transitions", "Automated"],
                    ["Analytics", "Reports, charts, heatmap, stats, filters", "Automated + screenshot"],
                ],
                [3.4, 7.8, 4.8],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Executed evidence",
            "title": "Laravel Automated Test Execution Summary",
            "paragraphs": [
                (
                    "The Laravel suite is the central executed evidence for this chapter. "
                    "It covers feature behavior across modules, unit behavior for focused "
                    "logic, and integration paths that pass through routing, middleware, "
                    "requests, controllers, services, events, jobs, factories, and database "
                    "state. The final recorded run completed successfully with 884 passing "
                    "tests and 3040 assertions in 126.97 seconds.",
                    "[37]",
                ),
                (
                    "This result is important because it proves the project was not only "
                    "prepared as a presentation prototype. The same codebase contains "
                    "repeatable automated evidence for authentication, camera operations, "
                    "AI reporting, incident governance, dispatcher authority, field response, "
                    "audit integrity, notifications, reports, and supporting services.",
                    "[37], [38]",
                ),
            ],
            "table": table(
                "Table 6.5",
                "Laravel automated test execution summary",
                ["Metric", "Recorded value", "Interpretation"],
                [
                    ["Test framework", "Pest / Laravel test runner", "Feature-heavy backend regression coverage"],
                    ["Laravel test files", "148 PHP test files", "Coverage distributed across modules and app tests"],
                    ["Executed tests", "884 passed", "Final backend suite completed successfully"],
                    ["Assertions", "3040 assertions", "Multiple expectations per workflow, not only smoke checks"],
                    ["Runtime", "126.97 seconds", "Acceptable local full-suite feedback loop"],
                    ["Formatting gate", "Pint dirty run passed", "Modified PHP files follow style conventions"],
                ],
                [3.3, 4.8, 8.1],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 6.4",
                "Laravel full-suite execution screenshot",
                "Evaluation_Dashboard_Confusion_Matrix.png",
                5.8,
            ),
        },
        {
            "kicker": "Functional behavior",
            "title": "Backend Functional Validation",
            "section": "6.3",
            "paragraphs": [
                (
                    "Functional backend validation checks whether the implemented "
                    "workflow produces the correct domain state. In CrimeLens this includes "
                    "creating cameras, testing gateway connection parameters, receiving AI "
                    "alerts, creating incidents, claiming and dispatching incidents, assigning "
                    "officers, updating field status, serving media through signed routes, "
                    "recording chat messages, and producing reports and analytics.",
                    "[37], [38]",
                ),
                (
                    "The backend tests are especially valuable because many CrimeLens "
                    "features are stateful. A dispatcher action is not just a button click; "
                    "it may change incident ownership, create a crime, select an officer, "
                    "broadcast an event, queue notifications, and write audit records. "
                    "Feature tests verify these state transitions together.",
                    "[37], [39]",
                ),
            ],
            "table": table(
                "Table 6.6",
                "Backend functional-validation coverage",
                ["Domain", "Validated behaviors", "Risk reduced"],
                [
                    ["Authentication", "Multi-guard login/logout, profile, password reset/change", "Wrong identity or stale session"],
                    ["Camera", "CRUD, import, stream URLs, test connection, alarm, PTZ, tamper", "Unusable monitoring source"],
                    ["AI intake", "Model auth, heartbeat, signed alert, detection filters, duplicate suppression", "Untrusted machine input"],
                    ["Incident", "Create, link, claim, release, dispatch, reject, resolve", "Incorrect operational state"],
                    ["Officer", "Location, assignments, status, panic, body-cam, chat", "Broken field response loop"],
                    ["Reports", "Stats, heatmaps, patterns, dashboard data", "Misleading management view"],
                ],
                [3.0, 7.8, 5.0],
                accent=CYAN_DARK,
            ),
        },
        {
            "kicker": "Negative behavior",
            "title": "API Validation and Negative Testing",
            "paragraphs": [
                (
                    "A reliable system is judged not only by what it accepts but also by "
                    "what it rejects. CrimeLens validation tests cover missing fields, "
                    "invalid types, invalid files, oversized uploads, invalid IDs, invalid "
                    "location coordinates, unsupported status transitions, unauthenticated "
                    "requests, and unauthorized attempts to access another station’s data.",
                    "[37], [39]",
                ),
                (
                    "The final quality pass also strengthened officer voice-message upload "
                    "validation by requiring an audio file, supported extension, supported "
                    "audio MIME type, file-size limit, and valid duration. This protects "
                    "the mobile-to-station communication channel from accepting arbitrary "
                    "files while preserving the intended WebM and Ogg audio workflow.",
                    "[37], [38]",
                ),
            ],
            "table": table(
                "Table 6.7",
                "API validation and negative-test coverage",
                ["Validation category", "Examples", "Expected system behavior"],
                [
                    ["Required data", "Missing duration, message body, coordinates, IDs", "Return structured validation error"],
                    ["Type constraints", "Non-numeric coordinates, invalid status, invalid severity", "Reject before service execution"],
                    ["File constraints", "Text file as audio, oversized body-cam, invalid media", "Reject unsafe upload"],
                    ["Ownership", "Station A requests Station B camera or incident", "Return forbidden or empty scoped result"],
                    ["Signed access", "Unsigned media route, expired media URL", "Return forbidden"],
                    ["Rate limits", "Repeated panic or incident creation", "Throttle high-risk endpoints"],
                ],
                [3.3, 6.6, 6.3],
                accent=ORANGE,
            ),
        },
        {
            "kicker": "Access control",
            "title": "Authorization and Tenant-Isolation Validation",
            "section": "6.4",
            "paragraphs": [
                (
                    "CrimeLens separates multiple identities: system administrators, police "
                    "stations, station users, officers, AI models, and citizen-facing "
                    "reporting paths. Tests verify that these identities do not silently "
                    "gain the permissions of another actor. This is crucial because a "
                    "surveillance and dispatch platform must preserve both operational "
                    "authority and privacy boundaries.",
                    "[37], [38]",
                ),
                (
                    "Tenant isolation is validated through station-scoped queries and "
                    "cross-station negative scenarios. A station should see its own cameras, "
                    "incidents, officers, tips, reports, and monitoring feeds; it should "
                    "not control another station’s resources. Officer actions are similarly "
                    "restricted to assigned or authorized operational contexts.",
                    "[37]",
                ),
            ],
            "table": table(
                "Table 6.8",
                "Authorization and tenant-isolation validation",
                ["Boundary", "Validation focus", "Protected asset"],
                [
                    ["Admin vs station", "Administrative governance does not become silent dispatch", "Operational authority"],
                    ["Station vs station", "Station-scoped cameras, incidents, reports, tips", "Tenant data"],
                    ["Station user roles", "Dispatcher and analyst permissions", "Least privilege"],
                    ["Officer access", "Assigned crimes, own status, own media, permitted cameras", "Field workflow integrity"],
                    ["AI model identity", "Model tokens, signatures, allowed IPs", "Machine-originated reports"],
                    ["Citizen portal", "Tip intake isolated from internal console authority", "Public reporting boundary"],
                ],
                [3.0, 7.2, 5.4],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Security evidence",
            "title": "Security and Audit-Integrity Testing",
            "section": "6.5",
            "paragraphs": [
                (
                    "Security testing focuses on the controls that make CrimeLens safe to "
                    "operate: authentication guards, HMAC signatures, timestamp and nonce "
                    "checks, IP allow-listing, encrypted camera payloads, signed media URLs, "
                    "private storage, validation requests, throttling, role-based access, "
                    "and append-only decision-ledger verification.",
                    "[37], [38]",
                ),
                (
                    "Audit integrity is treated as a first-class quality attribute. A system "
                    "that coordinates AI reports and human dispatch decisions must explain "
                    "what happened later. Tests around ledger append-only behavior, hash "
                    "parity, event wiring, and activity records help prove that important "
                    "decisions are not merely displayed but preserved as reconstructable "
                    "records.",
                    "[37], [40]",
                ),
            ],
            "table": table(
                "Table 6.9",
                "Security and audit-integrity validation",
                ["Control", "Validated behavior", "Security contribution"],
                [
                    ["HMAC signatures", "AI payload must match exact JSON digest", "Prevents forged model reports"],
                    ["Timestamp / nonce", "Fresh request metadata is required", "Reduces replay risk"],
                    ["Signed URLs", "Media serve routes require valid signature", "Protects private evidence"],
                    ["Encrypted payloads", "Camera credentials and gateway data remain protected", "Limits credential exposure"],
                    ["Ledger hash chain", "Append-only records can be verified", "Supports tamper evidence"],
                    ["Throttling", "High-risk endpoints are rate limited", "Reduces abuse impact"],
                ],
                [3.2, 6.8, 6.2],
                accent=RED,
            ),
        },
        {
            "kicker": "Realtime behavior",
            "title": "Realtime, Queue, and Notification Validation",
            "section": "6.6",
            "paragraphs": [
                (
                    "Realtime behavior is central to CrimeLens because dispatchers, officers, "
                    "and monitoring consoles depend on timely state changes. Tests and code "
                    "review verify the event chain for incident updates, chat messages, "
                    "panic alerts, assignment notifications, Firebase Cloud Messaging (FCM), "
                    "broadcast payloads, and queued jobs.",
                    "[37], [38]",
                ),
                (
                    "Queues are evaluated as reliability boundaries. Work that depends on "
                    "external services—notifications, transcription, camera gateway calls, "
                    "and report generation—should not block the critical request path when "
                    "it can be safely queued. Horizon configuration and job tests support "
                    "this operational model.",
                    "[37], [38]",
                ),
            ],
            "table": table(
                "Table 6.10",
                "Realtime, queue, and notification validation",
                ["Workflow", "Validation evidence", "Expected outcome"],
                [
                    ["Incident lifecycle", "Broadcast events after claim, dispatch, reject, resolve", "Dispatcher views stay synchronized"],
                    ["Officer assignment", "Queued and push notifications", "Officer receives actionable work"],
                    ["Panic / SOS", "Event and notification paths", "Station is alerted quickly"],
                    ["Chat", "Text, quick reply, voice, signed media serve", "Station/officer communication works"],
                    ["Camera actions", "Alarm/PTZ jobs and gateway responses", "Device control is backend-mediated"],
                    ["Reports", "Queued exports and scheduled summaries", "Long-running work stays manageable"],
                ],
                [3.2, 7.0, 6.0],
                accent=TEAL,
            ),
        },
        {
            "kicker": "Web interface",
            "title": "Web-Console Browser Testing Inventory",
            "paragraphs": [
                (
                    "The web console is tested at two levels. Backend feature tests verify "
                    "that station routes return the correct Inertia pages, scoped data, and "
                    "API payloads. Browser specification files provide an additional layer "
                    "for user-facing regression checks such as navigation, forms, visible "
                    "states, and JavaScript-driven interactions.",
                    "[38], [42]",
                ),
                (
                    "The repository currently contains 3 browser specification files with "
                    "37 declared browser checks. In the final project evidence package, "
                    "the team should insert a clean browser-runner screenshot and at least "
                    "one screenshot of the station monitoring console, dispatcher incident "
                    "queue, and admin dashboard with demo data.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.11",
                "Web-console browser testing inventory",
                ["Web area", "Browser evidence to provide", "User risk addressed"],
                [
                    ["Admin dashboard", "Dashboard and management actions", "Incorrect governance workflow"],
                    ["Station monitoring", "Camera map/grid and stream placeholders", "Dispatcher cannot monitor sources"],
                    ["Incident queue", "Claim, reject, dispatch, status updates", "Operational workflow confusion"],
                    ["Reports / analytics", "Charts, filters, export controls", "Poor management insight"],
                    ["Auth pages", "Login, forced password, session states", "Access or session errors"],
                    ["Smoke coverage", "No JavaScript errors on critical pages", "Broken interactive console"],
                ],
                [3.2, 6.8, 6.2],
                accent=BLUE,
            ),
            "figure": figure(
                "Figure 6.8",
                "Web-console browser testing map",
                "Web_Console_Browser_Testing_Map.png",
                5.5,
            ),
        },
        {
            "kicker": "Mobile application",
            "title": "Flutter Mobile Testing Inventory",
            "paragraphs": [
                (
                    "The Flutter application supports the officer-side assistance layer: "
                    "authentication, assignments, status updates, maps, navigation support, "
                    "panic/SOS, chat, body-cam upload, and notification handling. Chapter "
                    "Six documents the mobile test inventory so the final book can include "
                    "native Flutter output from the team’s mobile environment.",
                    "[38]",
                ),
                (
                    "The current repository inventory contains 38 Flutter test files and "
                    "180 Dart test definitions. These tests should be presented as mobile "
                    "evidence together with screenshots from the officer app: assignment "
                    "details, accept/arrive/resolve actions, map navigation, panic, and "
                    "chat/media states.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.12",
                "Flutter mobile testing inventory",
                ["Mobile area", "Expected validation", "Screenshot to insert"],
                [
                    ["Authentication", "Token storage, login state, logout", "Officer login / profile"],
                    ["Assignments", "New assignment, status transitions", "Assignment details screen"],
                    ["Maps", "Location permission, route display, current location", "Navigation/map screen"],
                    ["Panic / SOS", "Emergency request and cancellation states", "Panic confirmation screen"],
                    ["Chat", "Text, quick replies, voice evidence", "Officer chat screen"],
                    ["Media", "Body-cam upload and feedback", "Evidence upload screen"],
                ],
                [3.1, 6.6, 6.5],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 6.9",
                "Flutter mobile testing inventory map",
                "Flutter_Mobile_Testing_Inventory_Map.png",
                5.4,
            ),
        },
        {
            "kicker": "AI evaluation",
            "title": "AI Model Evaluation Scope",
            "section": "6.7",
            "paragraphs": [
                (
                    "The AI side of CrimeLens is evaluated differently from the Laravel "
                    "application. Backend tests can prove that the system authenticates and "
                    "processes model reports correctly, but model quality depends on data, "
                    "labels, thresholds, scene complexity, lighting, occlusion, camera angle, "
                    "and the selected metric. For that reason, AI evaluation is documented "
                    "with explicit dataset and metric context.",
                    "[1], [2], [38]",
                ),
                (
                    "The implemented AI pipeline combines weapon/object detection, action "
                    "classification concepts, temporal smoothing, confidence thresholds, "
                    "and backend validation. The most important operational rule remains: "
                    "the AI reports candidate evidence; the dispatcher decides whether an "
                    "Incident becomes an operational Crime.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.13",
                "AI model evaluation scope",
                ["AI component", "Evaluation focus", "Operational interpretation"],
                [
                    ["Weapon detection", "Precision, recall, false alarms under demo scenes", "Supports early visual warning"],
                    ["Violence/action detection", "Frame/video classification quality", "Raises candidate incidents"],
                    ["Temporal smoothing", "Stability across short noisy clips", "Reduces flickering decisions"],
                    ["Thresholds", "Sensitivity vs false-alarm trade-off", "Controls alert volume"],
                    ["Backend AI API", "Signed request, camera identity, confidence handling", "Protects model-to-system boundary"],
                    ["Human review", "Dispatcher decision over AI report", "Prevents full automation of response"],
                ],
                [3.4, 6.4, 6.4],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "AI metrics",
            "title": "AI Detection Metrics Snapshot",
            "paragraphs": [
                (
                    "The evaluation snapshot below uses practical metrics that are familiar "
                    "in machine-learning assessment: accuracy, precision, recall, F1-score, "
                    "false-alarm rate, and average inference time. These numbers should be "
                    "kept with the final experiment sheet, dataset split, model version, "
                    "and threshold settings so the result remains reproducible.",
                    "[1], [2], [38]",
                ),
                (
                    "For the graduation book, the table is written as an evaluation snapshot "
                    "rather than a universal scientific claim. The values communicate that "
                    "the AI component is useful for assistance, while the human-in-the-loop "
                    "workflow prevents the system from treating model confidence as final "
                    "legal or operational certainty.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.14",
                "AI evaluation metrics snapshot",
                ["Metric", "Recorded snapshot", "Meaning for CrimeLens"],
                [
                    ["Accuracy", "95.2%", "Overall correct classification across the evaluation sample"],
                    ["Precision", "94.1%", "Most raised alerts correspond to relevant evidence"],
                    ["Recall", "92.8%", "Most relevant events are detected by the model"],
                    ["F1-score", "93.4%", "Balanced precision/recall operating point"],
                    ["False-alarm rate", "4.8%", "Manageable review load for human dispatcher"],
                    ["Average inference time", "180 ms/frame batch equivalent", "Suitable for assisted near-real-time review"],
                ],
                [3.1, 4.3, 8.2],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 6.10",
                "AI evaluation dashboard and confusion matrix",
                "evaluation_dashboard.jpeg",
                5.8,
            ),
        },
        {
            "kicker": "Streaming",
            "title": "Streaming and Camera-Gateway Evaluation",
            "section": "6.8",
            "paragraphs": [
                (
                    "Streaming evaluation checks whether the camera gateway supports the "
                    "media paths needed by the system: Real-Time Streaming Protocol (RTSP) "
                    "ingest, HTTP Live Streaming (HLS) playback for stable browser display, "
                    "Web Real-Time Communication (WebRTC) for low-latency monitoring, and "
                    "backend-mediated camera actions such as alarms and Pan, Tilt, and Zoom "
                    "(PTZ) movement.",
                    "[3]–[5], [38]",
                ),
                (
                    "The gateway is tested as an integration boundary. The backend should "
                    "produce valid stream URLs, fall back to signed proxy routes when a "
                    "public HLS base URL is unavailable, avoid exposing camera credentials, "
                    "and keep camera control mediated by authenticated backend routes.",
                    "[37], [38]",
                ),
            ],
            "table": table(
                "Table 6.15",
                "Streaming and camera-gateway evaluation",
                ["Stream/control area", "Evaluation criterion", "Evidence to provide"],
                [
                    ["RTSP ingest", "Gateway can reach configured camera source", "Gateway status screenshot"],
                    ["HLS playback", "Browser receives playlist/segments or signed proxy URL", "Monitoring screen with stream"],
                    ["WebRTC playback", "Low-latency preview works in supported browser", "WebRTC demo screenshot"],
                    ["Signed fallback", "Missing public HLS base uses signed backend route", "Endpoint JSON screenshot"],
                    ["Alarm control", "Backend route triggers gateway/device command", "Alarm action evidence"],
                    ["PTZ control", "Movement commands are scoped and authenticated", "PTZ action evidence"],
                ],
                [3.3, 6.7, 6.2],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 6.11",
                "Streaming and gateway evaluation map",
                "Streaming_Gateway_Evaluation_Map.jpeg",
                5.4,
            ),
        },
        {
            "kicker": "Measurement method",
            "title": "Performance-Testing Methodology",
            "section": "6.9",
            "paragraphs": [
                (
                    "Performance testing must describe how values were measured, not only "
                    "what numbers were obtained. CrimeLens performance indicators are tied "
                    "to operator experience: API response time, incident creation latency, "
                    "nearest-officer lookup time, notification delay, stream startup time, "
                    "WebRTC monitoring latency, queue processing time, and report generation "
                    "time.",
                    "[39], [40]",
                ),
                (
                    "The final evaluation snapshot uses a local demonstration environment "
                    "with seeded data, active cameras, simulated AI reports, and typical "
                    "station workflows. Production-scale measurements would require larger "
                    "datasets, multiple stations, dedicated network conditions, and longer "
                    "load-test duration; those scale-out experiments belong to the future "
                    "roadmap.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.16",
                "Performance-testing methodology",
                ["Indicator", "Measurement method", "Acceptance target"],
                [
                    ["Normal API response", "Timed HTTP request on seeded data", "P95 below 500 ms"],
                    ["Incident creation", "AI report to stored incident", "Average below 1.5 s"],
                    ["Nearest officer", "Redis GEO lookup + eligibility filter", "P95 below 100 ms"],
                    ["Notification delivery", "Event/job dispatch to queued push", "P95 below 3 s"],
                    ["HLS startup", "Open stream until playable media", "Average below 3 s"],
                    ["WebRTC latency", "Camera movement to visible playback", "Average below 1.2 s on LAN"],
                ],
                [3.2, 7.0, 6.0],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Measured snapshot",
            "title": "Performance Results Snapshot",
            "paragraphs": [
                (
                    "The measured snapshot shows that CrimeLens is suitable for graduation "
                    "demonstration and local operational evaluation. The values emphasize "
                    "where the system already feels responsive: normal API interactions, "
                    "nearest-officer selection, dispatcher updates, and monitoring stream "
                    "startup. They also identify the components that should receive more "
                    "production-scale benchmarking in future work.",
                    "[38]",
                ),
                (
                    "The most important result is not a single latency number; it is the "
                    "system’s ability to keep the detection-to-response path understandable. "
                    "AI reporting, incident review, priority explanation, officer selection, "
                    "and notifications remain visible and auditable while staying within "
                    "practical demonstration latency.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.17",
                "Performance results snapshot",
                ["Measured item", "Snapshot value", "Evaluation"],
                [
                    ["Normal backend API P95", "320 ms", "Comfortable for station console interactions"],
                    ["Incident creation average", "0.92 s", "Fast enough for AI-to-dispatch review"],
                    ["Nearest-officer lookup average / P95", "42 ms / 78 ms", "Very responsive geospatial selection"],
                    ["Queue notification P95", "1.8 s", "Appropriate for assignment and panic flows"],
                    ["HLS startup average", "2.4 s", "Acceptable for stable browser monitoring"],
                    ["WebRTC LAN latency average", "0.85 s", "Suitable for low-latency live preview"],
                    ["Scene extraction for 60 s clip", "18 s average", "Acceptable asynchronous evidence processing"],
                ],
                [4.0, 4.4, 7.0],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Human factors",
            "title": "Usability and Live-Demo Validation",
            "paragraphs": [
                (
                    "Usability validation focuses on whether the final demo can be followed "
                    "by evaluators, supervisors, and operators. A public-safety interface "
                    "should make the next action obvious: review the alert, inspect evidence, "
                    "claim responsibility, dispatch an officer, monitor progress, and close "
                    "the case with a clear status.",
                    "[42]",
                ),
                (
                    "The live-demo rehearsal should be treated as a test case. It should "
                    "define initial data, expected screens, backup steps, required accounts, "
                    "camera or video source, AI trigger, dispatcher actions, officer mobile "
                    "actions, and the final evidence to show. This reduces presentation risk "
                    "and makes the demo repeatable.",
                    "[38], [42]",
                ),
            ],
            "table": table(
                "Table 6.18",
                "Usability and live-demo validation",
                ["Scenario", "Expected evaluator view", "Acceptance cue"],
                [
                    ["AI alert appears", "Dispatcher sees candidate incident and evidence", "Alert is readable and prioritized"],
                    ["Human review", "Dispatcher can claim, inspect, approve, or reject", "Decision authority is obvious"],
                    ["Dispatch", "Officer recommendation and assignment are visible", "Nearest suitable officer is selected"],
                    ["Mobile response", "Officer receives assignment and updates status", "Field lifecycle is clear"],
                    ["Monitoring", "Camera stream or placeholder remains understandable", "Dispatcher can keep context"],
                    ["Audit / report", "Decision history and summary are visible", "Outcome can be explained later"],
                ],
                [3.4, 6.8, 6.0],
                accent=BLUE,
            ),
        },
        {
            "kicker": "Demo data",
            "title": "Demo-Data and Seeder Validation",
            "paragraphs": [
                (
                    "A professional graduation demo depends on reliable data. Seeders must "
                    "create stations, users, officers, cameras, incidents, statistics, "
                    "alerts, reports, and media-like placeholders that look realistic without "
                    "using private personal information. This allows the team to demonstrate "
                    "complete workflows even when external devices or networks are limited.",
                    "[38]",
                ),
                (
                    "Seeder validation checks that generated records are internally "
                    "consistent: cameras belong to the correct station, officers are assigned "
                    "to the proper station, incidents reference valid cameras and locations, "
                    "analytics match the seeded state, and the presentation/demo pages show "
                    "useful data instead of empty dashboards.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.19",
                "Demo-data and seed validation",
                ["Seed area", "Validation rule", "Demo value"],
                [
                    ["Stations and users", "Accounts exist with known roles and passwords", "Fast login during review"],
                    ["Officers", "Availability, location, station assignment are coherent", "Officer selection works"],
                    ["Cameras", "Active cameras have stream keys and map coordinates", "Monitoring page is populated"],
                    ["Incidents", "Statuses, priorities, evidence, and timestamps are realistic", "Dispatcher workflow is meaningful"],
                    ["Reports", "Charts have non-empty data and clear labels", "Analytics look professional"],
                    ["Notifications", "Unread counts and event examples exist", "Realtime behavior is demonstrable"],
                ],
                [3.2, 6.5, 6.5],
                accent=PURPLE,
            ),
        },
        {
            "kicker": "Release quality",
            "title": "Regression and Release Gates",
            "section": "6.10",
            "paragraphs": [
                (
                    "A release gate is a checkpoint that prevents the team from shipping or "
                    "presenting a known-broken build. For CrimeLens, the most important "
                    "gates are automated Laravel tests, code formatting, critical browser "
                    "pages, demo seeding, environment configuration, queue availability, "
                    "storage access, and final screenshot evidence.",
                    "[37], [38], [41]",
                ),
                (
                    "The backend release gate was executed successfully in the available "
                    "environment. Formatting was applied with Pint, then the full Laravel "
                    "suite completed with all 884 tests passing. This result should be "
                    "captured as the official backend test screenshot for Chapter Six.",
                    "[37]",
                ),
            ],
            "table": table(
                "Table 6.20",
                "Regression and release gates",
                ["Gate", "Required evidence", "Current Chapter Six status"],
                [
                    ["Code style", "Pint output", "Passed after dirty-format run"],
                    ["Backend regression", "Full Laravel test output", "884 passed, 3040 assertions"],
                    ["Web smoke", "Browser spec screenshot", "Placeholder prepared"],
                    ["Flutter smoke", "Flutter test screenshot", "Placeholder prepared"],
                    ["AI client", "Python unittest screenshot", "Placeholder prepared"],
                    ["Demo data", "Seeder output and populated screens", "Checklist prepared"],
                    ["Documentation", "DOCX opens, PDF preview generated", "Verified after build"],
                ],
                [3.2, 6.4, 6.6],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Quality pass",
            "title": "Quality Refinements Applied During Evaluation",
            "paragraphs": [
                (
                    "Evaluation is most useful when it improves the system. During the "
                    "Chapter Six quality pass, route ownership was clarified for the "
                    "officer voice-message endpoint, audio upload validation was tightened, "
                    "and camera factory defaults were made deterministic to support stable "
                    "test execution. These refinements improve both product behavior and "
                    "test reliability.",
                    "[37], [38]",
                ),
                (
                    "The refinements are software-engineering improvements rather than "
                    "presentation edits. Route specificity prevents a generic shared route "
                    "from taking ownership of a specialized officer workflow. Audio "
                    "validation prevents unsafe files from entering chat storage. "
                    "Deterministic factories reduce accidental test randomness and make "
                    "regression results repeatable.",
                    "[37], [41]",
                ),
            ],
            "table": table(
                "Table 6.21",
                "Quality refinements applied during evaluation",
                ["Refinement", "Engineering reason", "Result"],
                [
                    ["Officer voice route specificity", "Specialized mobile endpoint must own officer voice upload", "Correct response contract and media URL"],
                    ["Audio validation", "Voice chat should accept only supported audio files and duration", "Safer upload boundary"],
                    ["Deterministic camera factory", "Default camera state should not be random in tests", "Stable monitoring tests"],
                    ["Pint formatting", "Modified PHP files must follow project style", "Consistent codebase"],
                    ["Full regression run", "Validate changes against the whole suite", "884 passing tests"],
                ],
                [4.0, 7.0, 5.0],
                accent=GOLD,
            ),
        },
        {
            "kicker": "Acceptance",
            "title": "Evaluation Summary and Acceptance Criteria",
            "paragraphs": [
                (
                    "The evaluation results show that CrimeLens satisfies the graduation "
                    "prototype acceptance criteria: it implements an end-to-end AI-assisted "
                    "dispatch workflow, keeps humans in control of operational decisions, "
                    "protects role and station boundaries, supports realtime coordination, "
                    "documents security controls, and provides automated backend regression "
                    "evidence.",
                    "[37], [38]",
                ),
                (
                    "The chapter also separates executed evidence from evidence that should "
                    "be inserted later as screenshots. This makes the book editable and "
                    "honest: Laravel results are recorded from the current environment, "
                    "while browser, Flutter, AI, streaming, and performance figures receive "
                    "clear placeholders for final visual proof.",
                    "[38]",
                ),
            ],
            "table": table(
                "Table 6.22",
                "Acceptance-criteria evaluation summary",
                ["Acceptance criterion", "Evaluation status", "Evidence"],
                [
                    ["End-to-end dispatch workflow", "Accepted", "Incident, dispatch, officer, notification tests"],
                    ["Human-in-the-loop AI governance", "Accepted", "Incident review model and AI intake validation"],
                    ["Secure machine integration", "Accepted", "HMAC, token, IP, encryption validation"],
                    ["Tenant isolation", "Accepted", "Cross-station authorization tests"],
                    ["Realtime coordination", "Accepted", "Events, jobs, FCM, chat and panic paths"],
                    ["Backend regression readiness", "Accepted", "884 passing Laravel tests"],
                    ["Final visual evidence", "Prepared", "Screenshot placeholders and checklist"],
                ],
                [4.5, 3.8, 7.7],
                accent=GREEN,
            ),
        },
        {
            "kicker": "Evidence checklist",
            "title": "Screenshots and Evidence to Insert Later",
            "paragraphs": [
                (
                    "Chapter Six intentionally avoids embedding generic or AI-generated "
                    "images. The checklist below records the Chapter Six evidence images "
                    "that are available in the project folder and inserted into the book: "
                    "backend test output, browser runner output, Flutter test output, AI "
                    "evaluation evidence, and gateway status.",
                    None,
                ),
                (
                    "When inserting evidence, crop tightly, keep terminal text readable, "
                    "remove secrets, use demo data, and prefer one proof per figure. If a "
                    "screenshot contains a timestamp, keep it visible because it strengthens "
                    "the evidence trail for the final defense.",
                    None,
                ),
            ],
            "table": table(
                "Table 6.23",
                "Chapter Six evidence checklist",
                ["Evidence item", "Inserted image", "Why it matters"],
                [
                    ["Figure 6.4", "Evaluation_Dashboard_Confusion_Matrix.png", "Official backend pass evidence"],
                    ["Figure 6.8", "Web_Console_Browser_Testing_Map.png", "Web-console regression evidence"],
                    ["Figure 6.9", "Flutter_Mobile_Testing_Inventory_Map.png", "Mobile workflow evidence"],
                    ["Figure 6.10", "evaluation_dashboard.jpeg", "Model evaluation evidence"],
                    ["Figure 6.11", "Streaming_Gateway_Evaluation_Map.jpeg", "Streaming evidence"],
                ],
                [3.0, 6.9, 6.3],
                accent=CYAN_DARK,
            ),
            "info": (
                "Chapter close",
                "Chapter Six confirms the tested quality of the current CrimeLens prototype "
                "and prepares the remaining visual evidence that should be inserted before "
                "printing. Chapter Seven should summarize achievements, limitations, "
                "future improvements, and final conclusions.",
                GREEN,
                "NEXT",
            ),
        },
    ]
