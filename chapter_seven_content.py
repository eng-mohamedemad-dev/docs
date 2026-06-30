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
    ("Figure 7.3", "Objectives-to-Achievements Matrix", 216),
    ("Figure 7.4", "Technical Contribution Summary Map", 217),
    ("Figure 7.5", "Software Engineering Lessons Learned", 218),
    ("Figure 7.6", "Limitations-to-Roadmap Transition Map", 219),
    ("Figure 7.7", "Future Roadmap Timeline", 220),
    ("Figure 7.8", "AI and Data Improvement Roadmap", 221),
    ("Figure 7.9", "Scalability and Operations Roadmap", 223),
    ("Figure 7.10", "Security, Governance, and Compliance Roadmap", 224),
    ("Figure 7.11", "Productization and Deployment Roadmap", 225),
    ("Figure 7.12", "Ethical and Societal Impact Map", 226),
    ("Figure 7.13", "Final Evidence and Defense Checklist", 227),
]


CHAPTER_SEVEN_TABLES = [
    ("Table 7.1", "Scope of the Chapter Seven Conclusion", 215),
    ("Table 7.2", "CrimeLens Objectives and Achievements", 216),
    ("Table 7.3", "Technical and Academic Contributions", 217),
    ("Table 7.4", "Software Engineering Lessons Learned", 218),
    ("Table 7.5", "Current Limitations and Responsible Interpretation", 219),
    ("Table 7.6", "Future Roadmap Overview", 220),
    ("Table 7.7", "AI and Data Future Enhancements", 221),
    ("Table 7.8", "AI Audio and Wanted-Person Matching Features", 222),
    ("Table 7.9", "Scalability and Operational Future Enhancements", 223),
    ("Table 7.10", "Security and Governance Future Enhancements", 224),
    ("Table 7.11", "Productization and Deployment Future Enhancements", 225),
    ("Table 7.12", "Ethical and Societal Considerations", 226),
]


CHAPTER_SEVEN_REFERENCES = [
    (
        "[43]",
        "CrimeLens Project Team, CrimeLens final repository, graduation project "
        "documentation, presentation materials, diagrams, testing evidence, and "
        "demo assets, unpublished project materials, Beni-Suef University, Jun. 2026.",
    ),
    (
        "[44]",
        "ISO/IEC, ISO/IEC 25010:2023 — Systems and Software Engineering — Systems "
        "and Software Quality Requirements and Evaluation (SQuaRE) — Product Quality "
        "Model. Geneva, Switzerland: International Organization for Standardization, "
        "2023.",
    ),
    (
        "[45]",
        "M. Fowler, Patterns of Enterprise Application Architecture. Boston, MA, "
        "USA: Addison-Wesley, 2002.",
    ),
    (
        "[46]",
        "National Institute of Standards and Technology, Artificial Intelligence Risk "
        "Management Framework (AI RMF 1.0), NIST AI 100-1, Jan. 2023.",
    ),
    (
        "[47]",
        "OWASP Foundation, OWASP Application Security Verification Standard (ASVS), "
        "Version 5.0.0, official project documentation, May 2025, accessed Jun. 2026.",
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
                    "Chapter Seven closes the CrimeLens graduation project documentation by summarizing the "
                    "project outcomes, evaluating the extent to which the original objectives "
                    "were achieved, identifying the most important technical contributions, "
                    "and converting the remaining limitations into a practical future-work "
                    "roadmap. This chapter is not a repetition of the implementation or "
                    "testing chapters; rather, it represents the final engineering "
                    "interpretation of the entire project.",
                    "[43]",
                ),
                (
                    "The central conclusion is that CrimeLens successfully demonstrates an "
                    "integrated AI-assisted dispatch workflow. It connects camera evidence, "
                    "AI reporting, human review, priority explanation, field assignment, "
                    "real-time coordination, mobile response, and audit records within one "
                    "coherent system. The project therefore proves the feasibility of the "
                    "principle used throughout the documentation: AI reports, humans make "
                    "the final decision, and the backend enforces accountable and traceable "
                    "action.",
                    "[43]",
                ),
            ],
            "table": table(
                "Table 7.1",
                "Scope of the Chapter Seven Conclusion",
                ["Conclusion area", "What it summarizes", "Why it matters"],
                [
                    ["Project outcome", "What CrimeLens achieved as a complete prototype", "Shows final value"],
                    ["Objectives", "How the original goals were met", "Connects the ending to Chapter One"],
                    ["Contributions", "Technical, academic, and engineering additions", "Explains uniqueness"],
                    ["Lessons learned", "Agile, integration, testing, and teamwork insights", "Demonstrates engineering maturity"],
                    ["Limitations", "Current boundaries without weakening the project", "Maintains academic credibility"],
                    ["Future work", "AI, scalability, security, deployment, and productization roadmap", "Shows continuity"],
                ],
                [3.2, 7.1, 5.9],
                accent=CYAN_DARK,
            ),
            "figure": figure(
                "Figure 7.2",
                "CrimeLens outcome and value map",
                "chapter7/CH07_FIG_02_CrimeLens_Outcome_Value_Map.png",
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
                    "mockup. Instead, it built the complete operational chain: AI-originated "
                    "reports, dispatcher-controlled incidents, geospatial officer assignment, "
                    "field mobile support, real-time notifications, streaming integration, "
                    "and audit evidence.",
                    "[43]",
                ),
                (
                    "The implementation also satisfied an important non-functional objective: "
                    "the system is explainable enough to be defended academically. Actors, "
                    "requirements, diagrams, architecture, database design, security controls, "
                    "software modules, test evidence, and future work are all documented in "
                    "a traceable sequence across the seven chapters.",
                    "[43], [44]",
                ),
            ],
            "table": table(
                "Table 7.2",
                "CrimeLens Objectives and Achievements",
                ["Original objective", "Achievement", "Evidence"],
                [
                    ["Connect AI surveillance to dispatch", "AI reports become reviewable incidents", "AI API, Incident layer, dispatcher console"],
                    ["Keep humans in control", "Dispatcher approves, rejects, claims, or dispatches", "Human-in-the-loop workflow"],
                    ["Support field response", "Officer mobile app handles assignments and status updates", "Flutter app and officer APIs"],
                    ["Provide live monitoring", "Station web console consumes camera stream URLs", "Gateway and monitoring module"],
                    ["Protect authority boundaries", "Multi-guard authentication, tenant isolation, and signed media", "Security tests and design"],
                    ["Provide auditability", "Activity records and a hash-chained decision ledger", "Ledger design and tests"],
                    ["Demonstrate quality", "884 passing Laravel test cases and structured evidence", "Chapter Six testing results"],
                ],
                [4.0, 6.5, 5.7],
                accent=GREEN,
            ),
            "figure": figure(
                "Figure 7.3",
                "Objectives-to-Achievements Matrix",
                "chapter7/CH07_FIG_03_Objectives_To_Achievements_Matrix.png",
                5.5,
            ),
        },
        {
            "kicker": "Contributions",
            "title": "Technical and Academic Contributions",
            "section": "7.2",
            "paragraphs": [
                (
                    "The main contribution of CrimeLens is not limited to a single algorithm "
                    "or user interface. Rather, it lies in integrating multiple engineering "
                    "concerns into one reviewable public safety workflow. The project combines "
                    "AI-based detection and analysis, backend governance, streaming, real-time "
                    "events, geospatial assignment, mobile field response, security controls, "
                    "and auditability.",
                    "[43], [45]",
                ),
                (
                    "From an academic perspective, the project demonstrates how software "
                    "engineering can transform AI output into a controlled operational "
                    "process. This distinction is important because a model confidence score "
                    "is not equivalent to a dispatch decision. CrimeLens explicitly places "
                    "system design, policy rules, validation mechanisms, and human authority "
                    "between automated detection and operational action.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.3",
                "Technical and Academic Contributions",
                ["Contribution", "Description", "Value"],
                [
                    ["Incident governance layer", "AI reports are reviewed before being escalated into operational incidents", "Prevents blind automation"],
                    ["Explainable priority engine", "Stored decision factors explain urgency levels", "Improves dispatcher trust"],
                    ["Geospatial assignment", "The nearest eligible officer is selected using location data", "Speeds response"],
                    ["Streaming gateway", "RTSP, HLS, and WebRTC pathways support live monitoring", "Connects cameras to web operations"],
                    ["Decision ledger", "Hash-chain records preserve critical decisions", "Supports accountability"],
                    ["Multi-surface system", "Admin web, station web, officer mobile app, AI model, and gateway", "Demonstrates integration"],
                    ["Testing evidence", "Full Laravel test suite and structured evidence checklist", "Strengthens project credibility"],
                ],
                [3.7, 7.0, 5.5],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 7.4",
                "Technical Contribution Summary Map",
                "chapter7/CH07_FIG_04_Technical_Contribution_Summary_Map.png",
                5.4,
            ),
        },
        {
            "kicker": "Lessons learned",
            "title": "Software Engineering Lessons Learned",
            "paragraphs": [
                (
                    "The most important lesson from CrimeLens is that integration must be "
                    "planned early. Camera streams, AI reports, dispatcher decisions, mobile "
                    "assignments, notifications, queues, and evidence storage all influence "
                    "one another. Treating these elements as separate integrations to be "
                    "addressed only at the end of development would have introduced "
                    "significant risk. The Agile vertical-slice approach reduced this risk "
                    "by connecting small end-to-end workflows throughout the development "
                    "process.",
                    "[43], [45]",
                ),
                (
                    "A second lesson is that testing is not an activity performed only after "
                    "development. In CrimeLens, tests helped clarify route responsibilities, "
                    "validation rules, tenant isolation, media access, and predictable "
                    "behavior during demonstrations. This turned testing into a design "
                    "feedback mechanism rather than merely a pass/fail report.",
                    "[37], [39], [43]",
                ),
            ],
            "table": table(
                "Table 7.4",
                "Software Engineering Lessons Learned",
                ["Lesson", "How it appeared in CrimeLens", "Future application"],
                [
                    ["Build vertical slices", "Authentication → action → state → user interface → test", "Reduce integration risk"],
                    ["Keep AI bounded", "AI creates reports, not final dispatch decisions", "Protect human authority"],
                    ["Design for traceability", "Requirements connect to diagrams, modules, and tests", "Improve review quality"],
                    ["Prefer deterministic demos", "Seeders and factories make screens repeatable", "Avoid presentation surprises"],
                    ["Validate negative paths", "Invalid actors, files, and payloads are rejected", "Strengthen security"],
                    ["Document honestly", "Measured evidence is separated from future targets", "Preserve academic credibility"],
                ],
                [3.3, 7.2, 5.7],
                accent=GOLD,
            ),
            "figure": figure(
                "Figure 7.5",
                "Software Engineering Lessons Learned",
                "chapter7/CH07_FIG_05_Software_Engineering_Lessons_Learned.png",
                5.4,
            ),
        },
        {
            "kicker": "Current limitations",
            "title": "Current Limitations",
            "section": "7.3",
            "paragraphs": [
                (
                    "A strong conclusion should acknowledge the project’s current limitations "
                    "without presenting them as failures. CrimeLens is a graduation prototype "
                    "and a research-oriented system implementation, not a certified national "
                    "public safety platform. It demonstrates architecture, workflow, integration, "
                    "and supporting evidence, while real-world production deployment would "
                    "require additional testing, compliance review, infrastructure hardening, "
                    "and formal operational procedures.",
                    "[43], [44], [46]",
                ),
                (
                    "The AI component is also constrained by the available data and evaluation "
                    "conditions. Model performance depends on camera angle, lighting, crowd "
                    "density, occlusion, action type, recording quality, and threshold "
                    "configuration. Therefore, the system is positioned as a decision-support "
                    "tool rather than an autonomous law-enforcement system.",
                    "[1], [46]",
                ),
            ],
            "table": table(
                "Table 7.5",
                "Current Limitations and Responsible Interpretation",
                ["Limitation", "Responsible interpretation", "Roadmap direction"],
                [
                    ["Prototype deployment", "Designed for graduation use and controlled demonstrations", "Production hardening and DevOps"],
                    ["AI dataset scope", "Metrics depend on the availability of labeled clips", "Larger local datasets and MLOps"],
                    ["Camera environment", "Real devices and networks vary significantly", "Field trials and gateway monitoring"],
                    ["Mobile evidence", "Some validation requires a native mobile environment", "Final Flutter validation evidence"],
                    ["Scale testing", "Local performance measurements do not represent city-scale load testing", "Distributed load and stress testing"],
                    ["Compliance", "No formal legal certification is claimed", "Policy, privacy, and governance review"],
                ],
                [3.4, 6.7, 6.1],
                accent=ORANGE,
            ),
            "figure": figure(
                "Figure 7.6",
                "Limitations-to-Roadmap Transition Map",
                "chapter7/CH07_FIG_06_Limitations_To_Roadmap_Transition_Map.png",
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
                    "and well-governed public safety platform. The roadmap therefore groups "
                    "enhancements into AI and data, scalability, operations, security, "
                    "product experience, deployment, and governance.",
                    "[43], [44]",
                ),
                (
                    "The roadmap should preserve the project’s central principle. Even as "
                    "models become stronger, infrastructure becomes more scalable, and user "
                    "interfaces become more refined, the system should continue to separate "
                    "AI-generated evidence from human decision authority and retain "
                    "auditability as a core system requirement.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.6",
                "Future Roadmap Overview",
                ["Roadmap horizon", "Enhancement focus", "Expected value"],
                [
                    ["Short term", "Final screenshots, demo evidence, UI polish, and pending native test evidence", "Defense readiness"],
                    ["Short term", "Additional scenario seeders and structured demo scripts", "Repeatable presentation"],
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
                "Future Roadmap Timeline",
                "chapter7/CH07_FIG_07_Future_Roadmap_Timeline.png",
                5.5,
            ),
        },
        {
            "kicker": "AI direction",
            "title": "AI and Data Future Enhancements",
            "paragraphs": [
                (
                    "The AI roadmap should focus on robustness, explainability, and adaptation "
                    "to local context. Future versions can expand the dataset, include more "
                    "camera angles, add hard negative examples, calibrate alert thresholds "
                    "for each camera, measure false-alarm patterns, and evaluate models under "
                    "night, crowd, occlusion, and low-resolution conditions.",
                    "[1], [2], [46]",
                ),
                (
                    "A more mature version should also introduce Machine Learning Operations "
                    "(MLOps), including dataset versioning, model versioning, experiment "
                    "tracking, confidence calibration, drift monitoring, rollback procedures, "
                    "and approval workflows before a new model is used in operational "
                    "demonstrations or real-world deployments.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.7",
                "AI and Data Future Enhancements",
                ["Enhancement", "Description", "Benefit"],
                [
                    ["Expanded dataset", "More local scenes, lighting conditions, and camera angles", "Improves realism"],
                    ["Hard negatives", "Clips that appear suspicious but are actually harmless", "Reduces false alarms"],
                    ["Per-camera thresholds", "Tune sensitivity for each location and model", "Controls alert volume"],
                    ["Model versioning", "Track model files, metrics, and deployment dates", "Improves reproducibility"],
                    ["Drift monitoring", "Detect changes in camera environments or model behavior", "Maintains long-term quality"],
                    ["Explainable evidence", "Store key frames, bounding boxes, confidence scores, and temporal context", "Improves human review"],
                ],
                [3.3, 7.2, 5.7],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 7.8",
                "AI and Data Improvement Roadmap",
                "chapter7/CH07_FIG_08_AI_Data_Improvement_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "AI evidence extensions",
            "title": "AI Audio Analysis and Wanted-Person Matching Support",
            "paragraphs": [
                (
                    "CrimeLens can be extended with two additional AI-assisted evidence "
                    "modules: audio-based incident detection and wanted-person visual "
                    "matching. These modules are designed to support the dispatcher with "
                    "additional evidence, not to replace human judgment or make final "
                    "enforcement decisions automatically.",
                    "[43], [46]",
                ),
                (
                    "The audio analysis module focuses on detecting suspicious sound patterns "
                    "and abusive or profane speech indicators within monitored areas. When "
                    "the system identifies aggressive language, shouting, abnormal noise "
                    "levels, or other configured audio signals, it creates an audio-based "
                    "alert containing the camera or microphone source, timestamp, detected "
                    "category, confidence score, and related evidence snippet. This alert is "
                    "then sent to the dispatcher for review before any operational action is "
                    "taken.",
                    "[43], [46]",
                ),
                (
                    "The wanted-person matching module compares live camera frames with "
                    "reference images of wanted or person-of-interest records stored in the "
                    "database. During live monitoring, the system extracts visual features "
                    "from detected faces and compares them with stored reference profiles. "
                    "If the similarity score exceeds a predefined threshold, the system "
                    "generates a potential wanted-person match alert. The alert includes "
                    "the matched record reference, camera location, timestamp, confidence "
                    "score, and captured evidence frame.",
                    "[43], [46], [47]",
                ),
                (
                    "CrimeLens does not declare a person guilty or automatically classify "
                    "someone as a criminal. Instead, it presents a possible match that must "
                    "be verified by an authorized human dispatcher. This design keeps the "
                    "system aligned with the project’s core principle: AI provides evidence, "
                    "humans make the final decision, and the backend records accountable "
                    "actions.",
                    "[43], [46], [47]",
                ),
            ],
            "table": table(
                "Table 7.8",
                "AI Audio and Wanted-Person Matching Features",
                ["Feature", "Input Source", "AI Output", "Human Role", "Stored Evidence"],
                [
                    ["Audio profanity and aggression detection", "Live audio stream or microphone input", "Suspicious audio/profanity alert with confidence score", "Dispatcher reviews and confirms relevance", "Timestamp, source, category, confidence, audio snippet"],
                    ["Wanted-person visual matching", "Live camera stream and database reference images", "Potential wanted-person match", "Dispatcher verifies the match before escalation", "Camera frame, matched record ID, confidence, location, timestamp"],
                    ["Alert prioritization", "AI result, confidence score, and context", "Suggested priority level", "Dispatcher accepts, modifies, or rejects priority", "Priority factors and decision record"],
                    ["Audit trail", "Dispatcher actions and system-generated alerts", "Traceable decision history", "Supervisor or admin can review actions", "Activity logs and decision ledger"],
                ],
                [3.0, 3.5, 3.4, 3.2, 3.9],
                accent=PURPLE,
                font_size=7.7,
            ),
            "post_table_paragraphs": [
                (
                    "This approach improves situational awareness while preserving "
                    "accountability, privacy, and human supervision. It also reduces the "
                    "risk of blind automation by ensuring that AI-generated audio or visual "
                    "alerts are treated as reviewable evidence rather than final operational "
                    "conclusions.",
                    "[43], [46], [47]",
                ),
            ],
        },
        {
            "kicker": "Scale and operations",
            "title": "Scalability and Operational Future Enhancements",
            "paragraphs": [
                (
                    "The scalability roadmap should assess how CrimeLens performs as the "
                    "number of stations, cameras, officers, AI reports, notifications, and "
                    "recorded evidence increases. Future work should include load testing, "
                    "queue capacity planning, Redis and database monitoring, observability "
                    "of the streaming gateway, storage lifecycle policies, and multi-node "
                    "deployment experiments.",
                    "[43], [44], [45]",
                ),
                (
                    "Operational maturity also requires observability. Dashboards should "
                    "display queue wait times, failed jobs, camera health, stream status, "
                    "AI service heartbeat, API latency, database load, notification delivery, "
                    "and storage usage. These indicators help move the system from "
                    "demonstration confidence to operational confidence.",
                    "[43]",
                ),
            ],
            "table": table(
                "Table 7.9",
                "Scalability and Operational Future Enhancements",
                ["Area", "Future enhancement", "Operational value"],
                [
                    ["Queues", "Laravel Horizon alerting, retry dashboards, and priority queues", "Stable background processing"],
                    ["Database", "Indexes, partitioning, archiving, and query dashboards", "Sustained performance"],
                    ["Streaming", "Gateway health metrics and fallback-path monitoring", "Reliable camera feeds"],
                    ["Storage", "Retention policies, evidence lifecycle management, and backup verification", "Controlled media growth"],
                    ["Notifications", "Delivery tracking and retry auditing", "Reliable field communication"],
                    ["Load testing", "Multi-station and high-camera-count simulations", "Scale readiness"],
                ],
                [3.0, 7.2, 5.8],
                accent=TEAL,
            ),
            "figure": figure(
                "Figure 7.9",
                "Scalability and Operations Roadmap",
                "chapter7/CH07_FIG_09_Scalability_Operations_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Governance",
            "title": "Security, Privacy, and Governance Future Enhancements",
            "paragraphs": [
                (
                    "Security must extend beyond authentication mechanisms. Future versions "
                    "should strengthen device identity controls, implement secret rotation, "
                    "formalize permission reviews, document retention rules, protect exported "
                    "reports and evidence, monitor abnormal access patterns, and define "
                    "incident-response procedures for system security events.",
                    "[46], [47]",
                ),
                (
                    "Privacy and governance are especially important because CrimeLens "
                    "handles surveillance feeds, geolocation data, evidence, dispatch records, "
                    "and citizen reports. Future work should include data minimization, "
                    "retention policies, export approvals, access reviews, privacy impact "
                    "assessments, and a clear distinction between demo data and real "
                    "operational data.",
                    "[46], [47]",
                ),
            ],
            "table": table(
                "Table 7.10",
                "Security and Governance Future Enhancements",
                ["Governance area", "Future work", "Reason"],
                [
                    ["Secret management", "Rotation, secure vault storage, and environment separation", "Reduce credential exposure"],
                    ["Access reviews", "Periodic role and permission audits", "Maintain least privilege"],
                    ["Privacy", "Retention, masking, export approval, and demo-data policy", "Protect sensitive information"],
                    ["Monitoring", "Security logging, unusual access detection, and alerting", "Detect misuse"],
                    ["Incident response", "Runbooks for compromise or data exposure", "Improve readiness"],
                    ["Compliance", "Formal alignment with applicable policies", "Prepare for real deployment"],
                ],
                [3.4, 6.8, 6.0],
                accent=RED,
            ),
            "figure": figure(
                "Figure 7.10",
                "Security, Governance, and Compliance Roadmap",
                "chapter7/CH07_FIG_10_Security_Governance_Compliance_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Productization",
            "title": "Deployment and Productization Future Enhancements",
            "paragraphs": [
                (
                    "Productization means transforming the project from a working prototype "
                    "into a maintainable and deployable service. Future work should add "
                    "CI/CD pipelines, environment-specific configuration management, "
                    "containerized services, automated database migrations, health checks, "
                    "backup procedures, monitoring dashboards, release notes, and rollback "
                    "plans.",
                    "[43], [45]",
                ),
                (
                    "A production-oriented version should also refine the user experience. "
                    "Dispatchers need faster review actions, clearer alert grouping, richer "
                    "camera context, better evidence previews, keyboard-efficient workflows, "
                    "and report templates. Officers need stronger offline behavior, simpler "
                    "status updates, and clearer recovery from missed notifications.",
                    "[42], [43]",
                ),
            ],
            "table": table(
                "Table 7.11",
                "Productization and Deployment Future Enhancements",
                ["Enhancement", "Description", "Impact"],
                [
                    ["CI/CD", "Automated testing, build, and deployment pipeline", "Safer releases"],
                    ["Containerization", "Containerize Laravel, the gateway, AI services, queue workers, and dependencies", "Repeatable environments"],
                    ["Health checks", "Service status endpoints and dashboards", "Faster troubleshooting"],
                    ["Backups", "Database backup and evidence recovery plan", "Data resilience"],
                    ["UX polish", "Shortcuts, grouping, empty states, and guided demo mode", "Better operator experience"],
                    ["Documentation", "Admin guide, station guide, officer guide, and operations guide", "Maintainability"],
                ],
                [3.2, 7.0, 6.0],
                accent=BLUE,
            ),
            "figure": figure(
                "Figure 7.11",
                "Productization and Deployment Roadmap",
                "chapter7/CH07_FIG_11_Productization_Deployment_Roadmap.png",
                5.4,
            ),
        },
        {
            "kicker": "Social responsibility",
            "title": "Ethical and Societal Considerations",
            "section": "7.5",
            "paragraphs": [
                (
                    "CrimeLens is built for a sensitive public-safety domain. Surveillance "
                    "and AI can improve response speed and situational awareness, but they "
                    "can also introduce risks if used without proper oversight. Ethical "
                    "operation requires proportional use, clear authority boundaries, "
                    "auditability, privacy controls, human review, and transparency "
                    "regarding model limitations.",
                    "[46], [47]",
                ),
                (
                    "The project’s human-in-the-loop architecture is therefore not only a "
                    "technical choice, but also an ethical design decision. By ensuring that "
                    "AI produces evidence rather than making final operational decisions, "
                    "CrimeLens keeps human judgment, responsibility, and accountability at "
                    "the center of public-safety decision-making.",
                    "[43], [46]",
                ),
            ],
            "table": table(
                "Table 7.12",
                "Ethical and Societal Considerations",
                ["Consideration", "CrimeLens design response", "Future strengthening"],
                [
                    ["False positives", "Dispatcher reviews AI reports", "Better calibration and hard negatives"],
                    ["Privacy", "Scoped access and signed evidence routes", "Retention and masking policies"],
                    ["Accountability", "Decision records and a hash-chained ledger", "Formal audit reports"],
                    ["Bias and domain shift", "Metrics are treated as context-dependent", "Diverse local datasets"],
                    ["Operator overload", "Priority scoring and alert filtering", "Alert grouping and fatigue metrics"],
                    ["Transparency", "Stored confidence scores and evidence context", "Explainability dashboard"],
                ],
                [3.4, 6.8, 6.0],
                accent=PURPLE,
            ),
            "figure": figure(
                "Figure 7.12",
                "Ethical and Societal Impact Map",
                "chapter7/CH07_FIG_12_Ethical_Societal_Impact_Map.png",
                5.4,
            ),
        },
        {
            "kicker": "Final conclusion",
            "title": "Final Conclusion",
            "section": "7.6",
            "paragraphs": [
                (
                    "CrimeLens demonstrates that a graduation project can successfully "
                    "combine research, software engineering, AI integration, real-time "
                    "systems, mobile workflows, security, testing, and professional "
                    "documentation into one cohesive project narrative. The project’s value "
                    "lies not only in detecting events, but in showing how detection is "
                    "transformed into a controlled operational decision.",
                    "[43]",
                ),
                (
                    "The final defense should emphasize the complete project journey: "
                    "literature review, requirements, diagrams, architecture, implementation, "
                    "testing, demonstration evidence, limitations, and a future roadmap. "
                    "Together these elements demonstrate both technical depth and "
                    "engineering discipline.",
                    "[43]",
                ),
            ],
            "figure": figure(
                "Figure 7.13",
                "Final Evidence and Defense Checklist",
                "chapter7/CH07_FIG_13_Final_Evidence_Defense_Checklist.png",
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
