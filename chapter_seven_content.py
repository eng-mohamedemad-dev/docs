"""Structured content for CrimeLens Chapter Seven — Conclusion and Future Work."""

from __future__ import annotations


CYAN_DARK = "0E7490"
GOLD = "D4AF37"
GREEN = "22C55E"
PURPLE = "A855F7"
RED = "EF4444"
BLUE = "2563EB"
TEAL = "2DD4BF"
ORANGE = "F59E0B"


CHAPTER_SEVEN_FIGURES = [
    ("Figure 7.1", "Chapter-opening conclusion and future-work background", 214),
    ("Figure 7.2", "CrimeLens outcome and value map", 215),
    ("Figure 7.3", "Objectives-to-achievements matrix", 216),
    ("Figure 7.4", "Technical contribution summary map", 217),
    ("Figure 7.5", "Software-engineering lessons learned", 218),
    ("Figure 7.6", "Limitations-to-roadmap transition map", 219),
    ("Figure 7.7", "Future roadmap timeline", 220),
    ("Figure 7.8", "AI and data improvement roadmap", 221),
    ("Figure 7.9", "Scalability and operations roadmap", 222),
    ("Figure 7.10", "Security, governance, and compliance roadmap", 223),
    ("Figure 7.11", "Productization and deployment roadmap", 224),
    ("Figure 7.12", "Ethical and societal impact map", 225),
    ("Figure 7.13", "Final evidence and defense checklist", 226),
]


CHAPTER_SEVEN_TABLES = [
    ("Table 7.1", "Chapter Seven conclusion scope", 215),
    ("Table 7.2", "Objectives achieved by CrimeLens", 216),
    ("Table 7.3", "Technical and academic contributions", 217),
    ("Table 7.4", "Software-engineering lessons learned", 218),
    ("Table 7.5", "Current limitations and responsible interpretation", 219),
    ("Table 7.6", "Future roadmap overview", 220),
    ("Table 7.7", "AI and data future enhancements", 221),
    ("Table 7.8", "Scalability and operational future enhancements", 222),
    ("Table 7.9", "Security and governance future enhancements", 223),
    ("Table 7.10", "Productization and deployment future enhancements", 224),
    ("Table 7.11", "Ethical and societal considerations", 225),
    ("Table 7.12", "Final defense evidence checklist", 226),
]


CHAPTER_SEVEN_REFERENCES = [
    (
        "[43]",
        "CrimeLens Project Team, CrimeLens final repository, graduation book, "
        "presentation material, diagrams, testing evidence, and demo assets, "
        "Beni-Suef University, Jun. 2026.",
    ),
    (
        "[44]",
        "ISO/IEC, ISO/IEC 25010: Systems and Software Engineering — Systems and "
        "Software Quality Requirements and Evaluation (SQuaRE) — System and Software "
        "Quality Models, International Organization for Standardization, 2011.",
    ),
    (
        "[45]",
        "M. Fowler, Patterns of Enterprise Application Architecture. Boston, MA, "
        "USA: Addison-Wesley, 2002.",
    ),
    (
        "[46]",
        "NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), "
        "National Institute of Standards and Technology, Jan. 2023.",
    ),
    (
        "[47]",
        "OWASP Foundation, OWASP Application Security Verification Standard, "
        "official project documentation, accessed Jun. 2026.",
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


def chapter_seven_page_specs() -> list[dict]:
    return [
        {
            "kicker": "Project closure",
            "title": "Conclusion Chapter Overview",
            "section": "7.1",
            "paragraphs": [
                (
                    "Chapter Seven closes the CrimeLens graduation book by summarizing the "
                    "project outcomes, evaluating the degree to which the original objectives "
                    "were achieved, identifying the most important technical contributions, "
                    "and converting the remaining limitations into a practical future-work "
                    "roadmap. The chapter is not a repetition of the implementation or "
                    "testing chapters; it is the final engineering interpretation of the "
                    "whole project.",
                    "[43]",
                ),
                (
                    "The central conclusion is that CrimeLens successfully demonstrates an "
                    "integrated AI-assisted dispatch workflow. It connects camera evidence, "
                    "AI reporting, human review, priority explanation, field assignment, "
                    "realtime coordination, mobile response, and audit records in one "
                    "coherent system. The project therefore proves the feasibility of the "
                    "principle used throughout the book: AI reports, humans decide, and the "
                    "backend enforces accountable action.",
                    "[43]",
                ),
            ],
            "table": table(
                "Table 7.1",
                "Chapter Seven conclusion scope",
                ["Conclusion area", "What it summarizes", "Why it matters"],
                [
                    ["Project outcome", "What CrimeLens achieved as a complete prototype", "Shows final value"],
                    ["Objectives", "How the original goals were met", "Connects ending to Chapter One"],
                    ["Contributions", "Technical, academic, and engineering additions", "Explains uniqueness"],
                    ["Lessons learned", "Agile, integration, testing, and teamwork insights", "Demonstrates engineering maturity"],
                    ["Limitations", "Current boundaries without weakening the project", "Keeps the book honest"],
                    ["Future work", "AI, scalability, security, deployment, and productization roadmap", "Shows continuity"],
                ],
                [3.2, 7.1, 5.9],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 7.2",
                "CrimeLens outcome and value map",
                "CH07_FIG_02_CrimeLens_Outcome_Value_Map.png",
                5.4,
            ),
        },
        {
            "kicker": "Objective review",
            "title": "Achievement of Project Objectives",
            "paragraphs": [
                (
                    "The project objectives were achieved through a combination of research, "
                    "analysis, design, implementation, testing, documentation, and iterative "
                    "refinement. CrimeLens did not stop at object detection or a dashboard "
                    "mockup. It built the complete operational chain: AI-originated reports, "
                    "dispatcher-controlled incidents, geospatial officer assignment, field "
                    "mobile support, realtime notifications, streaming integration, and "
                    "audit evidence.",
                    "[43]",
                ),
                (
                    "The implementation also achieved an important non-functional objective: "
                    "the system is explainable enough to be defended academically. Actors, "
                    "requirements, diagrams, architecture, database design, security controls, "
                    "software modules, test evidence, and future work are all documented in "
                    "a traceable sequence across the seven chapters.",
                    "[43], [44]",
                ),
            ],
            "table": table(
                "Table 7.2",
                "Objectives achieved by CrimeLens",
                ["Original objective", "Achievement", "Evidence"],
                [
                    ["Connect AI surveillance to dispatch", "AI reports become reviewable incidents", "AI API, Incident layer, dispatcher console"],
                    ["Keep humans in control", "Dispatcher approves, rejects, claims, or dispatches", "Human-in-the-loop workflow"],
                    ["Support field response", "Officer mobile app handles assignments and status", "Flutter app and officer APIs"],
                    ["Provide live monitoring", "Station web console consumes camera stream URLs", "Gateway and monitoring module"],
                    ["Protect authority boundaries", "Multi-guard auth, tenant isolation, signed media", "Security tests and design"],
                    ["Provide auditability", "Activity records and hash-chained decision ledger", "Ledger design and tests"],
                    ["Demonstrate quality", "884 passing Laravel tests and structured evidence", "Chapter Six testing results"],
                ],
                [4.0, 6.5, 5.7],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 7.3",
                "Objectives-to-achievements matrix",
                "CH07_FIG_03_Objectives_To_Achievements_Matrix.png",
                5.5,
            ),
        },
        {
            "kicker": "Contributions",
            "title": "Technical and Academic Contributions",
            "section": "7.2",
            "paragraphs": [
                (
                    "The main contribution of CrimeLens is not a single algorithm or screen. "
                    "It is the integration of multiple engineering concerns into one "
                    "reviewable public-safety workflow. The project combines AI perception, "
                    "backend governance, streaming, realtime events, geospatial assignment, "
                    "mobile field response, security controls, and auditability.",
                    "[43], [45]",
                ),
                (
                    "From an academic perspective, the project demonstrates how software "
                    "engineering can transform AI output into a controlled operational "
                    "process. This distinction matters because a model confidence score is "
                    "not the same as a dispatch decision. CrimeLens explicitly inserts "
                    "system design, policy, validation, and human authority between the two.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.3",
                "Technical and academic contributions",
                ["Contribution", "Description", "Value"],
                [
                    ["Incident governance layer", "AI reports are reviewed before becoming crimes", "Prevents blind automation"],
                    ["Explainable priority engine", "Stored factors explain urgency", "Improves dispatcher trust"],
                    ["Geospatial assignment", "Nearest eligible officer selected from location data", "Speeds response"],
                    ["Streaming gateway", "RTSP, HLS, and WebRTC paths support monitoring", "Connects cameras to web operations"],
                    ["Decision ledger", "Hash-chain records preserve critical decisions", "Supports accountability"],
                    ["Multi-surface system", "Admin web, station web, officer mobile, AI model, gateway", "Demonstrates integration"],
                    ["Testing evidence", "Full Laravel suite and evidence checklist", "Raises project credibility"],
                ],
                [3.7, 7.0, 5.5],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 7.4",
                "Technical contribution summary map",
                "CH07_FIG_04_Technical_Contribution_Summary_Map.png",
                5.4,
            ),
        },
        {
            "kicker": "Lessons learned",
            "title": "Software-Engineering Lessons Learned",
            "paragraphs": [
                (
                    "The most important lesson from CrimeLens is that integration must be "
                    "designed early. Camera streams, AI reports, dispatcher decisions, mobile "
                    "assignments, notifications, queues, and evidence storage all influence "
                    "one another. Treating them as separate final-week integrations would "
                    "have created high risk. The Agile vertical-slice approach reduced this "
                    "risk by connecting thin end-to-end workflows throughout development.",
                    "[43], [45]",
                ),
                (
                    "A second lesson is that testing is not an activity performed only after "
                    "development. In CrimeLens, tests clarified routing ownership, validation "
                    "rules, tenant isolation, media access, and deterministic demo behavior. "
                    "This made testing a design feedback mechanism, not merely a pass/fail "
                    "report.",
                    "[37], [39], [43]",
                ),
            ],
            "table": table(
                "Table 7.4",
                "Software-engineering lessons learned",
                ["Lesson", "How it appeared in CrimeLens", "Future application"],
                [
                    ["Build vertical slices", "Authentication → action → state → UI → test", "Reduce integration risk"],
                    ["Keep AI bounded", "AI creates reports, not final dispatch decisions", "Protect human authority"],
                    ["Design for traceability", "Requirements connect to diagrams, modules, and tests", "Improve review quality"],
                    ["Prefer deterministic demos", "Seeders and factories make screens repeatable", "Avoid presentation surprises"],
                    ["Validate negative paths", "Invalid actors, files, and payloads are rejected", "Strengthen security"],
                    ["Document honestly", "Measured evidence separated from future targets", "Preserve academic credibility"],
                ],
                [3.3, 7.2, 5.7],
                accent=GOLD,
            ),
            "figure": figure(
                "Figure 7.5",
                "Software-engineering lessons learned",
                "CH07_FIG_05_Software_Engineering_Lessons_Learned.png",
                5.4,
            ),
        },
        {
            "kicker": "Responsible boundaries",
            "title": "Current Limitations",
            "section": "7.3",
            "paragraphs": [
                (
                    "A strong conclusion should acknowledge the project’s current boundaries "
                    "without presenting them as failures. CrimeLens is a graduation prototype "
                    "and research-oriented implementation, not a certified national public-"
                    "safety platform. It demonstrates architecture, workflow, integration, "
                    "and evidence, while production deployment would require additional "
                    "testing, compliance review, infrastructure hardening, and operational "
                    "procedures.",
                    "[43], [44], [46]",
                ),
                (
                    "The AI component is also bounded by available data and evaluation "
                    "conditions. Model performance depends on camera angle, lighting, crowd "
                    "density, occlusion, action type, recording quality, and threshold "
                    "configuration. Therefore the system is positioned as decision support, "
                    "not autonomous law-enforcement authority.",
                    "[1], [46]",
                ),
            ],
            "table": table(
                "Table 7.5",
                "Current limitations and responsible interpretation",
                ["Limitation", "Responsible interpretation", "Roadmap direction"],
                [
                    ["Prototype deployment", "Designed for graduation and controlled demo", "Production hardening and DevOps"],
                    ["AI dataset scope", "Metrics depend on available labeled clips", "Larger local datasets and MLOps"],
                    ["Camera environment", "Real devices and networks vary significantly", "Field trials and gateway monitoring"],
                    ["Mobile evidence", "Some validation requires native mobile environment", "Final Flutter evidence screenshots"],
                    ["Scale testing", "Local measurements are not city-scale load tests", "Distributed load and stress testing"],
                    ["Compliance", "No formal legal certification claimed", "Policy, privacy, and governance review"],
                ],
                [3.4, 6.7, 6.1],
                accent=ORANGE,
            ),
            "figure": figure(
                "Figure 7.6",
                "Limitations-to-roadmap transition map",
                "CH07_FIG_06_Limitations_To_Roadmap_Transition_Map.png",
                5.5,
            ),
        },
        {
            "kicker": "Roadmap",
            "title": "Future Work Roadmap Overview",
            "section": "7.4",
            "paragraphs": [
                (
                    "Future work should be organized as a roadmap rather than a wish list. "
                    "The most valuable next steps are those that move CrimeLens from a strong "
                    "graduation prototype toward a field-ready, measurable, maintainable, "
                    "and governable public-safety platform. The roadmap therefore groups "
                    "enhancements into AI/data, scalability, operations, security, product "
                    "experience, deployment, and governance.",
                    "[43], [44]",
                ),
                (
                    "The roadmap should preserve the project’s central principle. Even as "
                    "models become stronger, infrastructure becomes more scalable, and user "
                    "interfaces become richer, the system should continue to separate AI "
                    "evidence from human decision authority and keep auditability as a core "
                    "requirement.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.6",
                "Future roadmap overview",
                ["Roadmap horizon", "Enhancement focus", "Expected value"],
                [
                    ["Short term", "Final screenshots, demo evidence, UI polish, missing native test outputs", "Defense readiness"],
                    ["Short term", "More scenario seeders and demo scripts", "Repeatable presentation"],
                    ["Medium term", "Expanded AI dataset and threshold calibration", "Better detection reliability"],
                    ["Medium term", "Load testing and monitoring dashboards", "Operational confidence"],
                    ["Long term", "Multi-station scaling and deployment automation", "Production readiness"],
                    ["Long term", "Governance, privacy, retention, and compliance workflows", "Responsible operation"],
                ],
                [3.0, 7.0, 6.0],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 7.7",
                "Future roadmap timeline",
                "CH07_FIG_07_Future_Roadmap_Timeline.png",
                5.5,
            ),
        },
        {
            "kicker": "AI direction",
            "title": "AI and Data Future Enhancements",
            "paragraphs": [
                (
                    "The AI roadmap should focus on robustness, explainability, and local "
                    "context. Future versions can expand the dataset, include more camera "
                    "angles, add hard negative examples, calibrate thresholds per camera, "
                    "measure false-alarm patterns, and evaluate models under night, crowd, "
                    "occlusion, and low-resolution conditions.",
                    "[1], [2], [46]",
                ),
                (
                    "A mature version should also introduce Machine Learning Operations "
                    "(MLOps): dataset versioning, model versioning, experiment tracking, "
                    "confidence calibration, drift monitoring, rollback procedures, and "
                    "approval workflows before a new model is used in operational demos or "
                    "real deployments.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.7",
                "AI and data future enhancements",
                ["Enhancement", "Description", "Benefit"],
                [
                    ["Expanded dataset", "More local scenes, lighting conditions, and camera angles", "Improves realism"],
                    ["Hard negatives", "Clips that look suspicious but are harmless", "Reduces false alarms"],
                    ["Per-camera thresholds", "Tune sensitivity per location and model", "Controls alert volume"],
                    ["Model versioning", "Track model files, metrics, and deployment dates", "Improves reproducibility"],
                    ["Drift monitoring", "Detect changes in camera environment or model behavior", "Maintains long-term quality"],
                    ["Explainable evidence", "Store frames, boxes, confidence, and temporal context", "Improves human review"],
                ],
                [3.3, 7.2, 5.7],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 7.8",
                "AI and data improvement roadmap",
                "CH07_FIG_08_AI_Data_Improvement_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Scale and operations",
            "title": "Scalability and Operational Future Enhancements",
            "paragraphs": [
                (
                    "The scalability roadmap should evaluate how CrimeLens behaves as the "
                    "number of stations, cameras, officers, AI reports, notifications, and "
                    "recorded evidence increases. Future work should include load testing, "
                    "queue capacity planning, Redis and database monitoring, stream gateway "
                    "observability, storage lifecycle policies, and multi-node deployment "
                    "experiments.",
                    "[43], [44], [45]",
                ),
                (
                    "Operational maturity also requires observability. Dashboards should "
                    "show queue wait time, failed jobs, camera health, stream status, AI "
                    "model heartbeat, API latency, database load, notification delivery, "
                    "and storage usage. These indicators help the team move from demo "
                    "confidence to operational confidence.",
                    "[43]",
                ),
            ],
            "table": table(
                "Table 7.8",
                "Scalability and operational future enhancements",
                ["Area", "Future enhancement", "Operational value"],
                [
                    ["Queues", "Horizon alerting, retry dashboards, priority queues", "Stable background work"],
                    ["Database", "Indexes, partitioning, archiving, query dashboards", "Sustained performance"],
                    ["Streaming", "Gateway health metrics and fallback monitoring", "Reliable camera feeds"],
                    ["Storage", "Retention policies, evidence lifecycle, backup verification", "Controlled media growth"],
                    ["Notifications", "Delivery tracking and retry audit", "Reliable field communication"],
                    ["Load testing", "Multi-station and high-camera simulations", "Scale readiness"],
                ],
                [3.0, 7.2, 5.8],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 7.9",
                "Scalability and operations roadmap",
                "CH07_FIG_09_Scalability_Operations_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Governance",
            "title": "Security, Privacy, and Governance Future Enhancements",
            "paragraphs": [
                (
                    "Security should continue beyond authentication. Future versions should "
                    "strengthen device identity, rotate secrets, formalize permission reviews, "
                    "document retention rules, protect exported reports, monitor abnormal "
                    "access patterns, and define incident-response procedures for system "
                    "security events.",
                    "[46], [47]",
                ),
                (
                    "Privacy and governance are especially important because CrimeLens "
                    "handles surveillance feeds, geolocation, evidence, dispatch records, "
                    "and citizen reports. Future work should include data minimization, "
                    "retention policies, export approvals, access reviews, privacy impact "
                    "assessment, and a clear distinction between demo data and real data.",
                    "[46], [47]",
                ),
            ],
            "table": table(
                "Table 7.9",
                "Security and governance future enhancements",
                ["Governance area", "Future work", "Reason"],
                [
                    ["Secret management", "Rotation, vault storage, environment separation", "Reduce credential exposure"],
                    ["Access reviews", "Periodic role and permission audits", "Maintain least privilege"],
                    ["Privacy", "Retention, masking, export approval, demo-data policy", "Protect sensitive information"],
                    ["Monitoring", "Security logs, unusual access detection, alerts", "Detect misuse"],
                    ["Incident response", "Runbooks for compromise or data exposure", "Improve readiness"],
                    ["Compliance", "Formal alignment with applicable policies", "Prepare for real deployment"],
                ],
                [3.4, 6.8, 6.0],
                accent=RED,
            ),
            "figure": figure(
                "Figure 7.10",
                "Security, governance, and compliance roadmap",
                "CH07_FIG_10_Security_Governance_Compliance_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Productization",
            "title": "Deployment and Productization Future Enhancements",
            "paragraphs": [
                (
                    "Productization means turning the project from a working prototype into "
                    "a maintainable service. Future work should add Continuous Integration "
                    "and Continuous Deployment (CI/CD), environment-specific configuration, "
                    "containerized services, automated database migrations, health checks, "
                    "backup procedures, monitoring dashboards, release notes, and rollback "
                    "plans.",
                    "[43], [45]",
                ),
                (
                    "A production-oriented version should also refine the user experience. "
                    "Dispatchers need faster review shortcuts, clearer alert grouping, richer "
                    "camera context, better evidence preview, keyboard-friendly workflows, "
                    "and report templates. Officers need stronger offline behavior, simpler "
                    "status updates, and clearer notification recovery.",
                    "[42], [43]",
                ),
            ],
            "table": table(
                "Table 7.10",
                "Productization and deployment future enhancements",
                ["Enhancement", "Description", "Impact"],
                [
                    ["CI/CD", "Automated test, build, and deployment pipeline", "Safer releases"],
                    ["Containers", "Package Laravel, gateway, AI, queues, and dependencies", "Repeatable environments"],
                    ["Health checks", "Service status endpoints and dashboards", "Faster troubleshooting"],
                    ["Backups", "Database and evidence recovery plan", "Data resilience"],
                    ["UX polish", "Shortcuts, grouping, empty states, guided demo mode", "Better operator experience"],
                    ["Documentation", "Admin guide, station guide, officer guide, operations guide", "Maintainability"],
                ],
                [3.2, 7.0, 6.0],
                accent=BLUE,
            ),
            "figure": figure(
                "Figure 7.11",
                "Productization and deployment roadmap",
                "CH07_FIG_11_Productization_Deployment_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Social responsibility",
            "title": "Ethical and Societal Considerations",
            "section": "7.5",
            "paragraphs": [
                (
                    "CrimeLens is built around a sensitive application domain. Surveillance "
                    "and AI can improve response speed and situational awareness, but they "
                    "can also create risks if used without oversight. Ethical operation "
                    "requires proportional use, clear authority, auditability, privacy "
                    "controls, human review, and transparency about model limitations.",
                    "[46], [47]",
                ),
                (
                    "The project’s human-in-the-loop architecture is therefore not only a "
                    "technical choice. It is an ethical design decision. By ensuring that "
                    "AI produces evidence rather than final action, CrimeLens keeps human "
                    "judgment, responsibility, and accountability at the center of public-"
                    "safety decisions.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.11",
                "Ethical and societal considerations",
                ["Consideration", "CrimeLens design response", "Future strengthening"],
                [
                    ["False positives", "Dispatcher reviews AI reports", "Better calibration and hard negatives"],
                    ["Privacy", "Scoped access and signed evidence routes", "Retention and masking policies"],
                    ["Accountability", "Decision records and hash-chain ledger", "Formal audit reports"],
                    ["Bias / domain shift", "Metrics treated as context-dependent", "Diverse local datasets"],
                    ["Operator overload", "Priority scoring and alert filtering", "Alert grouping and fatigue metrics"],
                    ["Transparency", "Stored confidence and evidence context", "Explainability dashboard"],
                ],
                [3.4, 6.8, 6.0],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 7.12",
                "Ethical and societal impact map",
                "CH07_FIG_12_Ethical_Societal_Impact_Map.png",
                5.4,
            ),
        },
        {
            "kicker": "Final conclusion",
            "title": "Final Conclusion and Defense Evidence",
            "section": "7.6",
            "paragraphs": [
                (
                    "CrimeLens demonstrates that a graduation project can combine research, "
                    "software engineering, AI integration, realtime systems, mobile workflows, "
                    "security, testing, and professional documentation into one cohesive "
                    "product story. The project’s value is not only that it detects events, "
                    "but that it explains how a detection becomes a controlled operational "
                    "decision.",
                    "[43]",
                ),
                (
                    "The final defense should emphasize the complete journey: literature "
                    "review, requirements, diagrams, architecture, implementation, tests, "
                    "demo evidence, limitations, and future roadmap. If the team inserts "
                    "the requested screenshots and diagrams into the placeholders, the book "
                    "will show both technical depth and presentation discipline.",
                    "[43]",
                ),
            ],
            "table": table(
                "Table 7.12",
                "Final defense evidence checklist",
                ["Placeholder", "Evidence to insert", "Defense value"],
                [
                    ["CH07_FIG_02", "Outcome/value map summary", "Opens conclusion visually"],
                    ["CH07_FIG_03", "Objectives-to-achievements diagram", "Shows goals were met"],
                    ["CH07_FIG_07", "Future roadmap timeline", "Shows maturity and next steps"],
                    ["CH07_FIG_08", "AI/data roadmap diagram", "Shows research continuity"],
                    ["CH07_FIG_09", "Scalability/operations roadmap", "Shows production thinking"],
                    ["CH07_FIG_10", "Security/governance roadmap", "Shows responsible design"],
                    ["CH07_FIG_13", "Final defense checklist", "Shows project readiness"],
                ],
                [3.0, 7.0, 6.0],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 7.13",
                "Final evidence and defense checklist",
                "CH07_FIG_13_Final_Evidence_Defense_Checklist.png",
                5.4,
            ),
            "info": (
                "Final statement",
                "CrimeLens is a complete, human-supervised, AI-assisted dispatch prototype. "
                "Its strongest achievement is the integration of intelligent sensing, "
                "operational decision-making, field response, security, auditability, and "
                "test evidence into one coherent graduation project.",
                GREEN,
                "END",
            ),
        },
    ]
