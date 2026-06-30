# Chapter 03 — Diagram and Image Requirements

This checklist maps every placeholder in Chapter Three to its editable
Diagrams.net/Draw.io page and final image filename.

## Source File

- Editable multi-page source:
  `diagrams/chapter-03/CrimeLens_Chapter_03_Diagrams.drawio`
- The source is native, uncompressed Draw.io XML. Open it with Diagrams.net,
  draw.io Desktop, or the Draw.io VS Code extension.
- Do not redraw the diagrams in Word. Edit the source page, export it, and
  replace the matching Word placeholder.

## Export Settings

- Export only the current Draw.io page.
- Format: PNG.
- Background: white; transparency disabled.
- Crop: enabled.
- Border width: 20 px.
- Scale: 2x minimum; 3x preferred when labels remain readable.
- Keep the exact filenames below so each image can be located immediately.
- In Word, use **In Line with Text**, preserve the aspect ratio, and fit the
  image inside the existing placeholder without stretching.

## Chapter-Opening Background

| Word page | Required filename | Requirement |
|---|---|---|
| 60 | `CH03_System_Analysis_Background.jpg` | Vertical A4 or 4:5 image, minimum 2480 × 3000 px. Professional software-analysis workspace containing UML, Data Flow Diagram (DFD), requirements, actor, and dispatch-flow motifs. Avoid readable third-party logos and avoid an AI-generated “fake interface.” |

## Draw.io Diagram Exports

| Figure | Word page | Draw.io page | Required filename |
|---|---:|---|---|
| Figure 3.1 — CrimeLens system context and external entities | 63 | `01 - System Context` | `CH03_FIG_01_System_Context.png` |
| Figure 3.2 — Actor authority and interface-surface map | 64 | `02 - Actor Authority and Surface Map` | `CH03_FIG_02_Actor_Authority_Map.png` |
| Figure 3.3 — Data Flow Diagram — Context Level 0 | 85 | `03 - DFD Context Level 0` | `CH03_FIG_03_DFD_Context_Level_0.png` |
| Figure 3.4 — Data Flow Diagram — Level 1 | 86 | `04 - DFD Level 1` | `CH03_FIG_04_DFD_Level_1.png` |
| Figure 3.5 — Data Flow Diagram — Level 2 detection intake and priority | 87 | `05 - DFD L2 Detection Intake and Priority` | `CH03_FIG_05_DFD_L2_Detection_Priority.png` |
| Figure 3.6 — Data Flow Diagram — Level 2 dispatch and field response | 88 | `06 - DFD L2 Dispatch and Field Response` | `CH03_FIG_06_DFD_L2_Dispatch_Response.png` |
| Figure 3.7 — Data Flow Diagram — Level 2 supporting services | 89 | `07 - DFD L2 Supporting Services` | `CH03_FIG_07_DFD_L2_Supporting_Services.png` |
| Figure 3.8 — CrimeLens use-case overview | 91 | `08 - Use Case Overview` | `CH03_FIG_08_Use_Case_Overview.png` |
| Figure 3.9 — System-administrator use cases | 92 | `09 - Administrator Use Cases` | `CH03_FIG_09_Admin_Use_Cases.png` |
| Figure 3.10 — Police-station management use cases | 93 | `10 - Station Management Use Cases` | `CH03_FIG_10_Station_Management_Use_Cases.png` |
| Figure 3.11 — Dispatcher operational use cases | 94 | `11 - Dispatcher Use Cases` | `CH03_FIG_11_Dispatcher_Use_Cases.png` |
| Figure 3.12 — Field-officer mobile use cases | 95 | `12 - Field Officer Use Cases` | `CH03_FIG_12_Officer_Use_Cases.png` |
| Figure 3.13 — AI, camera, citizen, and worker use cases | 96 | `13 - Machine, Citizen and Worker Use Cases` | `CH03_FIG_13_Machine_Citizen_Worker_Use_Cases.png` |
| Figure 3.14 — Sequence diagram — AI detection to Incident | 112 | `14 - Sequence AI Detection to Incident` | `CH03_FIG_14_Sequence_AI_To_Incident.png` |
| Figure 3.15 — Sequence diagram — claim, review, and dispatch | 113 | `15 - Sequence Claim, Review and Dispatch` | `CH03_FIG_15_Sequence_Claim_Dispatch.png` |
| Figure 3.16 — Sequence diagram — officer response and escalation | 114 | `16 - Sequence Officer Response and Escalation` | `CH03_FIG_16_Sequence_Officer_Response.png` |
| Figure 3.17 — Activity diagram — Incident lifecycle | 115 | `17 - Activity Incident Lifecycle` | `CH03_FIG_17_Activity_Incident_Lifecycle.png` |
| Figure 3.18 — Activity diagram — citizen tip and evidence flow | 116 | `18 - Activity Citizen Tip and Evidence` | `CH03_FIG_18_Activity_Tip_Evidence.png` |
| Figure 3.19 — Incident, Crime, and Panic state machines | 117 | `19 - State Machines` | `CH03_FIG_19_State_Machines.png` |
| Figure 3.20 — Conceptual class diagram | 118 | `20 - Conceptual Class Diagram` | `CH03_FIG_20_Conceptual_Class_Diagram.png` |
| Figure 3.21 — Requirements traceability map | 119 | `21 - Requirements Traceability Map` | `CH03_FIG_21_Requirements_Traceability.png` |

## Modeling Quality Rules

- **Use-case diagrams:** actors stay outside the system boundary; use cases
  express actor goals. `<<include>>` is mandatory reused behavior,
  `<<extend>>` is conditional behavior, and generalization means inheritance.
- **Sequence diagrams:** time runs from top to bottom; participants use
  lifelines; calls are solid arrows; returns are dashed; alternatives and loops
  stay inside their proper combined fragments.
- **Activity diagrams:** include initial and final nodes, action nodes,
  decisions with guarded outgoing branches, and forks/joins only for real
  parallel behavior. Partitions identify responsibility.
- **State machines:** state transitions use
  `trigger [guard] / effect` where those elements exist.
- **Data Flow Diagrams:** use only external entities, processes, data stores,
  and named data flows. Do not add control-flow decision diamonds. Child
  diagrams must preserve the parent process inputs and outputs.
- **Conceptual class diagram:** show domain concepts, meaningful attributes,
  associations, multiplicities, inheritance, and composition where justified.
  Database columns and implementation-only details remain for Chapter Four.

## Final Review Before Inserting

- Confirm that labels remain readable at the final Word size.
- Confirm no connector crosses a label or terminates at empty space.
- Confirm every action in the related requirements/specification tables is
  represented by the appropriate actor, process, message, transition, or
  relationship.
- Confirm filenames and figure numbers match this checklist.
- Update the Word List of Figures after replacing all placeholders.
