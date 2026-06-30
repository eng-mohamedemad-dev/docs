"""Generate editable native draw.io sources for CrimeLens Chapter Three.

The output is a multi-page, uncompressed .drawio file. Each page uses explicit
coordinates so it can be opened in the diagrams.net VS Code extension, refined,
and exported as a high-resolution PNG for insertion into Microsoft Word.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4
from xml.etree import ElementTree as ET


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "diagrams" / "chapter-03"
OUTPUT = OUTPUT_DIR / "CrimeLens_Chapter_03_Diagrams.drawio"

NAVY = "#0F172A"
CYAN = "#0E7490"
CYAN_LIGHT = "#E6F7FB"
BLUE = "#2563EB"
BLUE_LIGHT = "#EFF6FF"
GOLD = "#B58900"
GOLD_LIGHT = "#FFF9E6"
GREEN = "#15803D"
GREEN_LIGHT = "#F0FDF4"
RED = "#B91C1C"
RED_LIGHT = "#FEF2F2"
PURPLE = "#7E22CE"
PURPLE_LIGHT = "#FAF5FF"
SLATE = "#475569"
LIGHT = "#F8FAFC"
WHITE = "#FFFFFF"
BORDER = "#94A3B8"


@dataclass(frozen=True)
class Page:
    diagram: ET.Element
    model: ET.Element
    root: ET.Element


class Drawio:
    def __init__(self) -> None:
        self.mxfile = ET.Element(
            "mxfile",
            {
                "host": "app.diagrams.net",
                "modified": datetime.now(UTC).isoformat(),
                "agent": "CrimeLens Graduation Book Generator",
                "version": "26.0.0",
                "type": "device",
                "compressed": "false",
            },
        )
        self.page: Page | None = None
        self.counter = 1

    def start_page(
        self,
        name: str,
        *,
        width: int = 1600,
        height: int = 900,
    ) -> None:
        diagram = ET.SubElement(
            self.mxfile,
            "diagram",
            {"id": uuid4().hex[:12], "name": name},
        )
        model = ET.SubElement(
            diagram,
            "mxGraphModel",
            {
                "dx": "1600",
                "dy": "900",
                "grid": "1",
                "gridSize": "10",
                "guides": "1",
                "tooltips": "1",
                "connect": "1",
                "arrows": "1",
                "fold": "1",
                "page": "1",
                "pageScale": "1",
                "pageWidth": str(width),
                "pageHeight": str(height),
                "math": "0",
                "shadow": "0",
                "background": WHITE,
            },
        )
        root = ET.SubElement(model, "root")
        ET.SubElement(root, "mxCell", {"id": "0"})
        ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
        self.page = Page(diagram, model, root)
        self.counter = 1
        self.title(name, width)

    def new_id(self, prefix: str = "c") -> str:
        value = f"{prefix}{self.counter}"
        self.counter += 1
        return value

    def vertex(
        self,
        value: str,
        x: float,
        y: float,
        width: float,
        height: float,
        style: str,
        *,
        parent: str = "1",
        cell_id: str | None = None,
    ) -> str:
        assert self.page is not None
        cell_id = cell_id or self.new_id()
        cell = ET.SubElement(
            self.page.root,
            "mxCell",
            {
                "id": cell_id,
                "value": value,
                "style": style,
                "vertex": "1",
                "parent": parent,
            },
        )
        ET.SubElement(
            cell,
            "mxGeometry",
            {
                "x": str(x),
                "y": str(y),
                "width": str(width),
                "height": str(height),
                "as": "geometry",
            },
        )
        return cell_id

    def edge(
        self,
        source: str,
        target: str,
        label: str = "",
        *,
        style: str | None = None,
        cell_id: str | None = None,
    ) -> str:
        assert self.page is not None
        cell_id = cell_id or self.new_id("e")
        edge_style = style or (
            "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;"
            "jettySize=auto;html=1;endArrow=block;endFill=1;"
            f"strokeColor={SLATE};fontColor={NAVY};fontSize=13;"
        )
        cell = ET.SubElement(
            self.page.root,
            "mxCell",
            {
                "id": cell_id,
                "value": label,
                "style": edge_style,
                "edge": "1",
                "parent": "1",
                "source": source,
                "target": target,
            },
        )
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
        return cell_id

    def title(self, title: str, page_width: int) -> None:
        self.vertex(
            title,
            40,
            20,
            page_width - 80,
            45,
            "text;html=1;strokeColor=none;fillColor=none;align=center;"
            f"verticalAlign=middle;fontFamily=Arial;fontSize=26;fontStyle=1;fontColor={NAVY};",
        )
        self.vertex(
            "",
            120,
            72,
            page_width - 240,
            2,
            f"shape=line;strokeColor={CYAN};strokeWidth=2;",
        )

    def actor(self, label: str, x: float, y: float, *, color: str = BLUE) -> str:
        return self.vertex(
            label,
            x,
            y,
            100,
            120,
            "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;"
            f"html=1;fontFamily=Arial;fontSize=14;fontStyle=1;fontColor={NAVY};strokeColor={color};",
        )

    def usecase(
        self,
        label: str,
        x: float,
        y: float,
        width: float = 210,
        height: float = 62,
        *,
        color: str = CYAN,
        fill: str = WHITE,
    ) -> str:
        return self.vertex(
            label,
            x,
            y,
            width,
            height,
            "ellipse;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
            f"fillColor={fill};strokeColor={color};strokeWidth=2;fontColor={NAVY};"
            "fontFamily=Arial;fontSize=13;",
        )

    def box(
        self,
        label: str,
        x: float,
        y: float,
        width: float,
        height: float,
        *,
        color: str = CYAN,
        fill: str = WHITE,
        rounded: bool = True,
        font_size: int = 14,
        bold: bool = False,
    ) -> str:
        return self.vertex(
            label,
            x,
            y,
            width,
            height,
            f"rounded={1 if rounded else 0};whiteSpace=wrap;html=1;"
            f"fillColor={fill};strokeColor={color};strokeWidth=2;fontColor={NAVY};"
            f"fontFamily=Arial;fontSize={font_size};fontStyle={1 if bold else 0};"
            "align=center;verticalAlign=middle;",
        )

    def boundary(
        self,
        label: str,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> str:
        return self.vertex(
            label,
            x,
            y,
            width,
            height,
            "rounded=0;whiteSpace=wrap;html=1;fillColor=none;"
            f"strokeColor={BORDER};dashed=1;dashPattern=8 4;fontColor={SLATE};"
            "fontFamily=Arial;fontSize=14;fontStyle=1;verticalAlign=top;align=left;"
            "spacingTop=8;spacingLeft=10;",
        )

    def process(self, label: str, x: float, y: float, width: float = 210) -> str:
        return self.vertex(
            label,
            x,
            y,
            width,
            75,
            "ellipse;whiteSpace=wrap;html=1;"
            f"fillColor={CYAN_LIGHT};strokeColor={CYAN};strokeWidth=2;"
            f"fontColor={NAVY};fontFamily=Arial;fontSize=14;fontStyle=1;",
        )

    def entity(self, label: str, x: float, y: float, width: float = 180) -> str:
        return self.box(
            label,
            x,
            y,
            width,
            65,
            color=BLUE,
            fill=BLUE_LIGHT,
            rounded=False,
            bold=True,
        )

    def store(self, label: str, x: float, y: float, width: float = 190) -> str:
        return self.vertex(
            label,
            x,
            y,
            width,
            60,
            "shape=partialRectangle;left=0;right=0;whiteSpace=wrap;html=1;"
            f"fillColor={GOLD_LIGHT};strokeColor={GOLD};strokeWidth=2;"
            f"fontColor={NAVY};fontFamily=Arial;fontSize=13;fontStyle=1;",
        )

    def decision(self, label: str, x: float, y: float) -> str:
        return self.vertex(
            label,
            x,
            y,
            130,
            95,
            "rhombus;whiteSpace=wrap;html=1;"
            f"fillColor={GOLD_LIGHT};strokeColor={GOLD};strokeWidth=2;"
            f"fontColor={NAVY};fontFamily=Arial;fontSize=12;fontStyle=1;",
        )

    def activity(self, label: str, x: float, y: float, width: float = 210) -> str:
        return self.box(
            label,
            x,
            y,
            width,
            58,
            color=CYAN,
            fill=CYAN_LIGHT,
            rounded=True,
            font_size=13,
        )

    def start(self, x: float, y: float) -> str:
        return self.vertex(
            "",
            x,
            y,
            28,
            28,
            f"ellipse;html=1;aspect=fixed;fillColor={NAVY};strokeColor={NAVY};",
        )

    def end(self, x: float, y: float) -> str:
        return self.vertex(
            "",
            x,
            y,
            32,
            32,
            f"ellipse;html=1;aspect=fixed;fillColor={NAVY};strokeColor={NAVY};"
            f"strokeWidth=5;perimeter=ellipsePerimeter;",
        )

    def state(self, label: str, x: float, y: float, width: float = 180) -> str:
        return self.box(
            label,
            x,
            y,
            width,
            62,
            color=PURPLE,
            fill=PURPLE_LIGHT,
            rounded=True,
            font_size=13,
            bold=True,
        )

    def include(self, source: str, target: str) -> None:
        self.edge(
            source,
            target,
            "«include»",
            style=(
                "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;"
                f"strokeColor={PURPLE};fontColor={PURPLE};fontSize=12;"
                "endArrow=open;endFill=0;"
            ),
        )

    def extend(self, source: str, target: str) -> None:
        self.edge(
            source,
            target,
            "«extend»",
            style=(
                "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;"
                f"strokeColor={GOLD};fontColor={GOLD};fontSize=12;"
                "endArrow=open;endFill=0;"
            ),
        )

    def save(self) -> None:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        ET.indent(self.mxfile, space="  ")
        ET.ElementTree(self.mxfile).write(
            OUTPUT,
            encoding="utf-8",
            xml_declaration=True,
        )


def add_context_page(draw: Drawio) -> None:
    draw.start_page("01 - System Context", width=1800, height=1000)
    boundary = draw.boundary("CrimeLens System Boundary", 340, 120, 1120, 740)
    core = draw.box(
        "CrimeLens Platform\nIncident Governance · Dispatch · Field Response · Audit",
        680,
        370,
        430,
        150,
        color=CYAN,
        fill=CYAN_LIGHT,
        bold=True,
        font_size=18,
    )
    actors = {
        "admin": draw.entity("System Administrator", 60, 160),
        "station": draw.entity("Police Station / Dispatcher", 40, 380, 220),
        "officer": draw.entity("Field Officer", 70, 650),
        "ai": draw.entity("AI Detection Service", 1540, 150, 210),
        "camera": draw.entity("Camera & Gateway", 1540, 365, 210),
        "citizen": draw.entity("Citizen Reporter", 1540, 590, 210),
        "providers": draw.entity("FCM · Pusher · Twilio · Maps", 1450, 790, 300),
    }
    draw.edge(actors["admin"], core, "settings · stations · AI identities · audit · reports")
    draw.edge(core, actors["admin"], "health · analytics · nationwide visibility")
    draw.edge(actors["station"], core, "incident review · dispatch decisions · management")
    draw.edge(core, actors["station"], "queues · maps · streams · status · notifications")
    draw.edge(actors["officer"], core, "accept · location · status · evidence · panic · resolve")
    draw.edge(core, actors["officer"], "assignments · brief · navigation · BOLO · chat")
    draw.edge(actors["ai"], core, "signed alert · heartbeat")
    draw.edge(core, actors["ai"], "encrypted assigned cameras")
    draw.edge(actors["camera"], core, "RTSP · health · tamper · recordings")
    draw.edge(core, actors["camera"], "backend-mediated PTZ · alarm · configuration")
    draw.edge(actors["citizen"], core, "web/SMS tip · media · location")
    draw.edge(core, actors["citizen"], "acknowledgement · dispatcher reply")
    draw.edge(core, actors["providers"], "push · realtime · SMS · map requests")
    draw.edge(actors["providers"], core, "delivery result · inbound webhook")


def add_authority_page(draw: Drawio) -> None:
    draw.start_page("02 - Actor Authority and Surface Map", width=1800, height=1000)
    headers = [
        ("System Administrator", 70, BLUE_LIGHT, BLUE),
        ("Station Account", 330, CYAN_LIGHT, CYAN),
        ("Dispatcher / Station User", 590, PURPLE_LIGHT, PURPLE),
        ("Field Officer", 850, GREEN_LIGHT, GREEN),
        ("AI Service", 1110, GOLD_LIGHT, GOLD),
        ("Camera / Gateway", 1370, RED_LIGHT, RED),
    ]
    rows = [
        "Primary surface",
        "Operational authority",
        "Management authority",
        "Physical-device authority",
        "Data boundary",
        "Explicit prohibition",
    ]
    values = [
        ["Admin web", "Station web + helper mobile", "Station web", "Officer mobile", "Machine API", "Device + gateway API"],
        ["Observe system", "Supervise station", "Claim/review/dispatch", "Respond in field", "Report observations", "Stream/execute commands"],
        ["Stations, models, settings", "Officers, users, cameras", "Incidents, tips, BOLO", "Own status/evidence", "Assigned cameras only", "Managed processes/devices"],
        ["Through backend", "Through backend", "Through backend", "None by default", "None", "Receives backend command"],
        ["Authorized scope", "Own station", "Own station + identity", "Own assignments", "Own identity/cameras", "Registered camera/process"],
        ["No live dispatch", "No personal claim identity", "No admin governance", "No station management", "No crime creation/dispatch", "No autonomous policy decision"],
    ]
    for index, (label, x, fill, color) in enumerate(headers):
        draw.box(label, x, 135, 230, 70, color=color, fill=fill, rounded=False, bold=True)
        for row, value in enumerate(values):
            draw.box(
                value[index],
                x,
                250 + row * 105,
                230,
                78,
                color=color,
                fill=WHITE,
                rounded=False,
                font_size=12,
            )
    for row, label in enumerate(rows):
        draw.box(
            label,
            10,
            250 + row * 105,
            50,
            78,
            color=SLATE,
            fill=LIGHT,
            rounded=False,
            font_size=10,
            bold=True,
        )
    draw.box(
        "Station mobile mode is a supplementary access channel. The station web console remains the complete operational surface.",
        260,
        900,
        1280,
        55,
        color=GOLD,
        fill=GOLD_LIGHT,
        bold=True,
    )


def add_dfd_context(draw: Drawio) -> None:
    draw.start_page("03 - DFD Context Level 0", width=1800, height=1000)
    platform = draw.process("0.0\nCrimeLens Platform", 760, 420, 280)
    entities = [
        ("Administrator", 80, 130, "settings · identities · governance", "analytics · reports · audit"),
        ("Station / Dispatcher", 60, 390, "review · dispatch · management", "queue · maps · live status"),
        ("Field Officer", 80, 690, "status · GPS · evidence · panic", "assignment · brief · notification"),
        ("AI Detection Service", 1510, 130, "alert · crime · heartbeat", "encrypted camera assignment"),
        ("Camera / Gateway", 1510, 390, "video · health · tamper", "stream registration · control"),
        ("Citizen / Twilio", 1510, 690, "tip · media · location", "receipt · SMS reply"),
    ]
    for label, x, y, incoming, outgoing in entities:
        entity = draw.entity(label, x, y, 220)
        draw.edge(entity, platform, incoming)
        draw.edge(platform, entity, outgoing)
    draw.box(
        "DFD rule: arrows represent data only; decision logic and control sequencing are intentionally excluded.",
        510,
        820,
        780,
        65,
        color=GOLD,
        fill=GOLD_LIGHT,
        bold=True,
    )


def add_dfd_level1(draw: Drawio) -> None:
    draw.start_page("04 - DFD Level 1", width=1900, height=1100)
    processes = [
        ("1.0\nIdentity & Governance", 140, 180),
        ("2.0\nDetection Intake & Priority", 530, 180),
        ("3.0\nDispatcher Triage", 920, 180),
        ("4.0\nDispatch & Field Response", 1310, 180),
        ("5.0\nCamera & Evidence", 340, 570),
        ("6.0\nTips & Communication", 790, 570),
        ("7.0\nAnalytics & Audit", 1240, 570),
    ]
    p = {label.splitlines()[0]: draw.process(label, x, y, 260) for label, x, y in processes}
    stores = {
        "D1": draw.store("D1 · Identities / Settings", 80, 900, 230),
        "D2": draw.store("D2 · Incidents / Links", 350, 900, 220),
        "D3": draw.store("D3 · Crimes / Officer GPS", 610, 900, 250),
        "D4": draw.store("D4 · Cameras / Streams / Evidence", 900, 900, 290),
        "D5": draw.store("D5 · Tips / Chat / Notifications", 1230, 900, 270),
        "D6": draw.store("D6 · Activity / Decision Ledger", 1540, 900, 270),
    }
    admin = draw.entity("Administrator", 30, 70)
    station = draw.entity("Station / Dispatcher", 820, 70, 230)
    officer = draw.entity("Field Officer", 1660, 70)
    ai = draw.entity("AI Service", 30, 430)
    camera = draw.entity("Camera / Gateway", 1650, 430, 210)
    citizen = draw.entity("Citizen / Twilio", 30, 710)
    draw.edge(admin, p["1.0"], "credentials · configuration")
    draw.edge(p["1.0"], stores["D1"], "identity / policy data")
    draw.edge(ai, p["2.0"], "signed detection report")
    draw.edge(p["2.0"], stores["D2"], "scored pending incident")
    draw.edge(p["2.0"], p["3.0"], "prioritized incident")
    draw.edge(station, p["3.0"], "claim · review · decision")
    draw.edge(p["3.0"], stores["D2"], "ownership / review result")
    draw.edge(p["3.0"], p["4.0"], "approved incident")
    draw.edge(p["4.0"], stores["D3"], "crime · assignment · live location")
    draw.edge(p["4.0"], officer, "dispatch · status notification")
    draw.edge(officer, p["4.0"], "accept · status · GPS · resolution")
    draw.edge(camera, p["5.0"], "RTSP · status · recording · tamper")
    draw.edge(p["5.0"], stores["D4"], "stream / evidence metadata")
    draw.edge(citizen, p["6.0"], "tip / media / inbound message")
    draw.edge(p["6.0"], stores["D5"], "tip · chat · notification data")
    draw.edge(p["6.0"], p["3.0"], "promoted tip")
    draw.edge(p["7.0"], admin, "analytics · health · reports")
    for key in ["D2", "D3", "D4", "D5"]:
        draw.edge(stores[key], p["7.0"], "auditable metrics")
    draw.edge(p["3.0"], stores["D6"], "review decision")
    draw.edge(p["4.0"], stores["D6"], "response transition")


def add_dfd_intake(draw: Drawio) -> None:
    draw.start_page("05 - DFD Level 2 Detection Intake and Priority", width=1800, height=1000)
    ai = draw.entity("AI Detection Service", 40, 180, 220)
    station = draw.entity("Dispatcher / Manual Intake", 40, 650, 240)
    tips = draw.store("D5 · Citizen Tips", 40, 820, 220)
    processes = [
        ("2.1 Authenticate Machine", 370, 140),
        ("2.2 Validate IP / Signature / Replay", 720, 140),
        ("2.3 Normalize Detection", 1080, 140),
        ("2.4 Resolve Camera / Station / Location", 1080, 390),
        ("2.5 Calculate Priority Factors", 720, 390),
        ("2.6 Persist Pending Incident", 370, 390),
        ("2.7 Broadcast Incident Created", 370, 650),
    ]
    cells = {label[:3]: draw.process(label, x, y, 270) for label, x, y in processes}
    identities = draw.store("D1 · AI Identity / Assigned Cameras", 1360, 50, 300)
    cameras = draw.store("D4 · Cameras / Station Mapping", 1390, 390, 270)
    incidents = draw.store("D2 · Incidents / Priority Factors", 760, 780, 310)
    ledger = draw.store("D6 · Decision Ledger", 1320, 780, 260)
    draw.edge(ai, cells["2.1"], "credentials / token request")
    draw.edge(identities, cells["2.1"], "identity / whitelist data")
    draw.edge(cells["2.1"], cells["2.2"], "authenticated request")
    draw.edge(cells["2.2"], cells["2.3"], "validated alert / crime")
    draw.edge(cells["2.3"], cells["2.4"], "normalized source / confidence")
    draw.edge(cameras, cells["2.4"], "camera ownership / coordinates")
    draw.edge(cells["2.4"], cells["2.5"], "station / location / context")
    draw.edge(cells["2.5"], cells["2.6"], "score · tier · factor breakdown")
    draw.edge(station, cells["2.6"], "manual incident data")
    draw.edge(tips, cells["2.6"], "promoted tip data")
    draw.edge(cells["2.6"], incidents, "pending_review incident")
    draw.edge(cells["2.6"], cells["2.7"], "new incident event")
    draw.edge(cells["2.7"], station, "station queue update")
    draw.edge(cells["2.6"], ledger, "creation / scoring record")


def add_dfd_dispatch(draw: Drawio) -> None:
    draw.start_page("06 - DFD Level 2 Dispatch and Field Response", width=1900, height=1100)
    dispatcher = draw.entity("Dispatcher", 40, 120)
    officer = draw.entity("Field Officer", 1610, 120)
    provider = draw.entity("Realtime / Push Providers", 1550, 700, 280)
    processes = [
        ("4.1 Claim / Release Incident", 350, 100),
        ("4.2 Review Context & Decision", 720, 100),
        ("4.3 Create Crime Atomically", 1090, 100),
        ("4.4 Select Eligible Officer", 1090, 370),
        ("4.5 Deliver Assignment", 1450, 370),
        ("4.6 Track Response / Proximity", 1090, 650),
        ("4.7 Resolve / No-Visit / Escalate", 690, 650),
        ("4.8 Close Timeline & Audit", 330, 650),
    ]
    p = {label[:3]: draw.process(label, x, y, 280) for label, x, y in processes}
    incidents = draw.store("D2 · Incidents", 520, 350, 210)
    crimes = draw.store("D3 · Crimes / Assignments", 760, 880, 270)
    gps = draw.store("D3a · Redis / PostGIS Officer GPS", 1120, 880, 310)
    evidence = draw.store("D4 · Scenes / Body-Cam Evidence", 1480, 880, 300)
    ledger = draw.store("D6 · Decision Ledger", 300, 880, 250)
    draw.edge(dispatcher, p["4.1"], "claim / release")
    draw.edge(p["4.1"], incidents, "assigned_dispatcher / assigned_at")
    draw.edge(p["4.1"], p["4.2"], "owned incident")
    draw.edge(dispatcher, p["4.2"], "dispatch / reject / link")
    draw.edge(incidents, p["4.2"], "source · score · scene context")
    draw.edge(p["4.2"], p["4.3"], "approved incident")
    draw.edge(p["4.2"], ledger, "rejection / review record")
    draw.edge(p["4.3"], crimes, "crime + priority snapshot")
    draw.edge(p["4.3"], p["4.4"], "assignment request")
    draw.edge(gps, p["4.4"], "availability · shift · distance")
    draw.edge(p["4.4"], p["4.5"], "selected officer")
    draw.edge(p["4.5"], officer, "push / realtime assignment")
    draw.edge(p["4.5"], provider, "delivery payload")
    draw.edge(officer, p["4.6"], "accept · GPS · status")
    draw.edge(p["4.6"], gps, "live location / proximity")
    draw.edge(p["4.6"], p["4.7"], "arrival / timeout / outcome")
    draw.edge(officer, p["4.7"], "resolve · no-visit · evidence")
    draw.edge(p["4.7"], evidence, "body-cam / scene metadata")
    draw.edge(p["4.7"], crimes, "status / escalation / resolution")
    draw.edge(p["4.7"], p["4.8"], "terminal or reassigned transition")
    draw.edge(p["4.8"], ledger, "auditable lifecycle record")
    draw.edge(p["4.8"], dispatcher, "timeline / live status")


def add_dfd_support(draw: Drawio) -> None:
    draw.start_page("07 - DFD Level 2 Supporting Services", width=1900, height=1100)
    citizen = draw.entity("Citizen / Twilio", 50, 140)
    station = draw.entity("Station / Dispatcher", 50, 500, 240)
    admin = draw.entity("Administrator", 50, 830)
    camera = draw.entity("Camera / Gateway", 1620, 140, 230)
    officer = draw.entity("Field Officer", 1650, 500)
    processes = [
        ("5.1 Register / Fan-Out Stream", 390, 110),
        ("5.2 Camera Control / Health / Tamper", 790, 110),
        ("5.3 Record / Retrieve Evidence", 1190, 110),
        ("6.1 Receive & Route Tip", 390, 470),
        ("6.2 Triage / Reply / Promote", 790, 470),
        ("6.3 Chat / Notification Delivery", 1190, 470),
        ("7.1 Aggregate Analytics", 390, 810),
        ("7.2 Generate Reports / Audit", 790, 810),
        ("7.3 Health / Cleanup / Verification", 1190, 810),
    ]
    p = {label[:3]: draw.process(label, x, y, 280) for label, x, y in processes}
    camera_store = draw.store("D4 · Camera / Stream / Evidence", 1510, 340, 330)
    comm_store = draw.store("D5 · Tips / Chat / Notifications", 1510, 700, 330)
    ledger = draw.store("D6 · Logs / Ledger / Metrics", 1480, 990, 360)
    draw.edge(camera, p["5.1"], "RTSP source / device identity")
    draw.edge(p["5.1"], camera_store, "managed process / HLS / WebRTC")
    draw.edge(station, p["5.2"], "authorized alarm / PTZ / filters")
    draw.edge(p["5.2"], camera, "backend-mediated command")
    draw.edge(camera, p["5.2"], "status / tamper event")
    draw.edge(p["5.2"], camera_store, "health / tamper classification")
    draw.edge(p["5.1"], p["5.3"], "recordable stream")
    draw.edge(officer, p["5.3"], "body-cam upload")
    draw.edge(p["5.3"], camera_store, "scene / segment / signed media")
    draw.edge(citizen, p["6.1"], "web/SMS tip / media / location")
    draw.edge(p["6.1"], comm_store, "routed pending tip")
    draw.edge(station, p["6.2"], "promote / dismiss / reply")
    draw.edge(p["6.2"], comm_store, "tip status / reply")
    draw.edge(p["6.2"], station, "promoted incident / confirmation")
    draw.edge(station, p["6.3"], "chat / notification action")
    draw.edge(officer, p["6.3"], "chat / device token / receipt")
    draw.edge(p["6.3"], comm_store, "persistent message / notification")
    draw.edge(admin, p["7.1"], "report / analytics query")
    draw.edge(camera_store, p["7.1"], "camera / evidence metrics")
    draw.edge(comm_store, p["7.1"], "communication metrics")
    draw.edge(p["7.1"], p["7.2"], "aggregated dataset")
    draw.edge(p["7.2"], admin, "dashboard / export / report")
    draw.edge(p["7.2"], ledger, "report / audit context")
    draw.edge(p["7.3"], camera_store, "retention / health checks")
    draw.edge(p["7.3"], comm_store, "tip cleanup / delivery checks")
    draw.edge(p["7.3"], ledger, "chain verification / job outcomes")


def add_usecase_overview(draw: Drawio) -> None:
    draw.start_page("08 - Use Case Overview", width=1900, height=1100)
    boundary = draw.boundary("CrimeLens", 300, 100, 1300, 900)
    actors = {
        "admin": draw.actor("Administrator", 40, 150, color=BLUE),
        "station": draw.actor("Station Account", 40, 390, color=CYAN),
        "dispatcher": draw.actor("Dispatcher", 40, 650, color=PURPLE),
        "officer": draw.actor("Field Officer", 1730, 150, color=GREEN),
        "ai": draw.actor("AI Service", 1730, 390, color=GOLD),
        "citizen": draw.actor("Citizen", 1730, 650, color=RED),
        "worker": draw.actor("Scheduler / Worker", 830, 960, color=SLATE),
    }
    usecases = {
        "govern": draw.usecase("Govern Platform", 420, 160, 240, color=BLUE),
        "manage": draw.usecase("Manage Station Resources", 420, 330, 240, color=CYAN),
        "triage": draw.usecase("Triage & Dispatch Incident", 760, 260, 270, color=PURPLE),
        "respond": draw.usecase("Respond to Assignment", 1160, 160, 240, color=GREEN),
        "detect": draw.usecase("Report Detection", 1160, 330, 240, color=GOLD),
        "tip": draw.usecase("Submit / Triage Citizen Tip", 1160, 500, 240, color=RED),
        "camera": draw.usecase("Operate Camera & Evidence", 760, 500, 270, color=CYAN),
        "communicate": draw.usecase("Communicate & Notify", 760, 670, 270, color=BLUE),
        "audit": draw.usecase("Audit · Report · Maintain", 760, 840, 270, color=SLATE),
    }
    draw.edge(actors["admin"], usecases["govern"])
    draw.edge(actors["admin"], usecases["audit"])
    draw.edge(actors["station"], usecases["manage"])
    draw.edge(actors["station"], usecases["camera"])
    draw.edge(actors["dispatcher"], usecases["triage"])
    draw.edge(actors["dispatcher"], usecases["tip"])
    draw.edge(actors["dispatcher"], usecases["communicate"])
    draw.edge(actors["officer"], usecases["respond"])
    draw.edge(actors["officer"], usecases["communicate"])
    draw.edge(actors["ai"], usecases["detect"])
    draw.edge(actors["citizen"], usecases["tip"])
    draw.edge(actors["worker"], usecases["audit"])
    draw.include(usecases["triage"], usecases["communicate"])
    draw.include(usecases["triage"], usecases["audit"])
    draw.include(usecases["respond"], usecases["camera"])


def add_usecase_page(
    draw: Drawio,
    name: str,
    actor_label: str,
    groups: list[tuple[str, list[str], str]],
    *,
    actor_color: str,
) -> None:
    draw.start_page(name, width=1900, height=1150)
    actor = draw.actor(actor_label, 40, 470, color=actor_color)
    draw.boundary("CrimeLens", 240, 100, 1560, 950)
    y = 145
    for group_index, (group_label, actions, color) in enumerate(groups):
        group = draw.usecase(group_label, 390, y, 290, 70, color=color, fill=WHITE)
        draw.edge(actor, group)
        columns = [760, 1080, 1400]
        for index, action in enumerate(actions):
            x = columns[index % 3]
            action_y = y + (index // 3) * 95
            child = draw.usecase(action, x, action_y, 250, 60, color=color)
            draw.include(group, child)
        y += max(190, ((len(actions) + 2) // 3) * 95 + 35)


def add_usecase_pages(draw: Drawio) -> None:
    add_usecase_page(
        draw,
        "09 - Administrator Use Cases",
        "System Administrator",
        [
            (
                "Manage Police Stations",
                [
                    "Create / View / Update / Delete Station",
                    "Import / Export / Bulk Delete",
                    "Manage Cities / Locations",
                    "Reset Station Password",
                ],
                BLUE,
            ),
            (
                "Manage AI Models",
                [
                    "Create / Configure / Delete Model",
                    "Assign / Unassign Cameras",
                    "Import / Export / Bulk Delete",
                    "Reset Model Password",
                    "View Analytics / Compare Models",
                ],
                GOLD,
            ),
            (
                "Govern & Observe Platform",
                [
                    "Configure System / Camera / Firebase",
                    "Dry-Run / Apply Priority Weights",
                    "View Crimes / Tracking / Heatmaps",
                    "View Reports / Audit / Export",
                    "Monitor Health / Queues / Cameras",
                    "Acknowledge / Classify Tamper Event",
                    "Test Gateway / Stream / Command",
                    "Chat / Notifications / Profile",
                    "Trigger Demo Simulation",
                ],
                PURPLE,
            ),
        ],
        actor_color=BLUE,
    )
    add_usecase_page(
        draw,
        "10 - Station Management Use Cases",
        "Station Account / Manager",
        [
            (
                "Manage Station Identities",
                [
                    "Authenticate / Force Password Change",
                    "Manage Dispatcher Users",
                    "Reset User Password",
                    "Update Profile / Password",
                ],
                CYAN,
            ),
            (
                "Manage Officers",
                [
                    "Create / View / Update / Delete Officer",
                    "Import Officers",
                    "Reset Officer Password",
                    "Set Patrol Zone",
                    "View Locations / Activity / Daily Logs",
                ],
                GREEN,
            ),
            (
                "Manage Cameras & Operations",
                [
                    "Create / View / Update / Delete Camera",
                    "Import / Test Camera Connection",
                    "Configure Detection Filters",
                    "View Streams / Monitoring Grid",
                    "Trigger Alarm / Move PTZ",
                    "View Heatmap / Crimes / Officer Track",
                    "Manage BOLO / Chat / Notifications",
                    "Use Helper Station Mobile Mode",
                ],
                GOLD,
            ),
        ],
        actor_color=CYAN,
    )
    add_usecase_page(
        draw,
        "11 - Dispatcher Use Cases",
        "Dispatcher / Station User",
        [
            (
                "Operate Incident Queue",
                [
                    "View Mine / Shared Queue",
                    "Maintain Presence / Leave",
                    "Claim Incident",
                    "Release Incident",
                    "Inspect Source / Score / Context",
                    "View Nearest Officers",
                ],
                PURPLE,
            ),
            (
                "Commit Review Decision",
                [
                    "Create Manual Incident",
                    "Link Related Incidents",
                    "Dispatch Incident",
                    "Reject False Alarm",
                    "Track Active Crime / Officer",
                    "Resolve Station Panic",
                ],
                RED,
            ),
            (
                "Handle Supporting Operations",
                [
                    "Review / Promote / Dismiss Tip",
                    "Reply to Citizen",
                    "Create / View / Delete BOLO",
                    "View / Dismiss Pattern Alert",
                    "Chat / Voice / Quick Communication",
                    "Manage Notifications",
                    "View Live Cameras / Heatmap",
                ],
                CYAN,
            ),
        ],
        actor_color=PURPLE,
    )
    add_usecase_page(
        draw,
        "12 - Field Officer Use Cases",
        "Field Officer",
        [
            (
                "Access Field Workspace",
                [
                    "Login / Logout / Reset Password",
                    "View / Update Profile",
                    "View Dashboard / Statistics",
                    "Manage Notifications / Device Token",
                    "View Task History / Active BOLO",
                ],
                BLUE,
            ),
            (
                "Respond to Crime",
                [
                    "View Assignment / Pre-Arrival Brief",
                    "Accept Assignment",
                    "Decline / No-Visit with Reason",
                    "Navigate to Scene",
                    "Update Availability / Daily Activity",
                    "Stream GPS / Proximity",
                    "Resolve with Notes",
                    "Upload Body-Cam Evidence",
                ],
                GREEN,
            ),
            (
                "Safety & Communication",
                [
                    "Create Panic / SOS",
                    "Cancel Panic",
                    "Request / Receive Backup",
                    "Chat / Voice / Quick Reply",
                    "Open Authorized Camera Stream",
                    "Use Authorized Camera Control",
                ],
                RED,
            ),
        ],
        actor_color=GREEN,
    )
    draw.start_page("13 - Machine, Citizen and Worker Use Cases", width=1900, height=1150)
    draw.boundary("CrimeLens", 260, 100, 1390, 950)
    actors = [
        ("AI Detection Service", 30, 170, GOLD),
        ("Camera / Gateway", 30, 500, RED),
        ("Citizen / Twilio", 1730, 170, BLUE),
        ("Scheduler / Queue Worker", 1710, 540, SLATE),
    ]
    actor_ids = {label: draw.actor(label, x, y, color=color) for label, x, y, color in actors}
    groups = [
        (
            "AI Integration",
            420,
            150,
            GOLD,
            [
                "Login / Logout with IP Check",
                "Retrieve Encrypted Assigned Cameras",
                "Send Heartbeat",
                "Report Suspicious Alert",
                "Report Confirmed Crime",
            ],
            actor_ids["AI Detection Service"],
        ),
        (
            "Camera & Gateway",
            420,
            460,
            RED,
            [
                "Register / Start / Stop / Status Stream",
                "Fan-Out RTSP / HLS / WebRTC",
                "Execute Backend Camera Command",
                "Report Health / Tamper",
                "Record / Retrieve Segments",
            ],
            actor_ids["Camera / Gateway"],
        ),
        (
            "Citizen Intake",
            1080,
            150,
            BLUE,
            [
                "Find Nearest Station",
                "Submit Web Tip / Media",
                "Submit Inbound SMS",
                "Receive Thanks / Reply",
            ],
            actor_ids["Citizen / Twilio"],
        ),
        (
            "Scheduled / Queued Work",
            1080,
            520,
            SLATE,
            [
                "Release Stale Dispatcher Claims",
                "Escalate Stale Crime when Invoked",
                "Verify Decision Ledger",
                "Cleanup Recordings / Expired Tips",
                "Generate Reports / Daily Summary",
                "Send Push / Transcribe Voice",
                "Check Model / Camera Health",
            ],
            actor_ids["Scheduler / Queue Worker"],
        ),
    ]
    for label, x, y, color, actions, actor in groups:
        group = draw.usecase(label, x, y, 300, 65, color=color)
        draw.edge(actor, group)
        for index, action in enumerate(actions):
            child = draw.usecase(
                action,
                x + (index % 2) * 280,
                y + 100 + (index // 2) * 82,
                245,
                55,
                color=color,
            )
            draw.include(group, child)


def add_sequence_page(
    draw: Drawio,
    name: str,
    participants: list[str],
    messages: list[tuple[int, int, str, str]],
    *,
    width: int = 1900,
    height: int = 1200,
) -> None:
    draw.start_page(name, width=width, height=height)
    left = 100
    gap = (width - 200) / max(1, len(participants) - 1)
    heads: list[str] = []
    for index, participant in enumerate(participants):
        x = left + index * gap
        head = draw.box(
            participant,
            x - 80,
            105,
            160,
            55,
            color=CYAN,
            fill=CYAN_LIGHT,
            rounded=False,
            font_size=12,
            bold=True,
        )
        heads.append(head)
        bottom = draw.vertex(
            "",
            x,
            height - 100,
            1,
            1,
            "opacity=0;strokeOpacity=0;fillOpacity=0;",
        )
        draw.edge(
            head,
            bottom,
            "",
            style=f"dashed=1;dashPattern=6 4;strokeColor={BORDER};endArrow=none;html=1;",
        )
    y = 195
    for source, target, label, kind in messages:
        color = {
            "call": BLUE,
            "return": SLATE,
            "event": PURPLE,
            "error": RED,
            "async": GREEN,
        }.get(kind, BLUE)
        style = (
            "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;"
            f"strokeColor={color};fontColor={NAVY};fontSize=12;"
            f"dashed={1 if kind == 'return' else 0};"
            f"endArrow={'open' if kind in {'async', 'return'} else 'block'};"
            f"endFill={0 if kind in {'async', 'return'} else 1};"
            f"exitX=0.5;exitY=1;entryX=0.5;entryY=1;"
        )
        message = draw.edge(heads[source], heads[target], label, style=style)
        # Text-only timestamp marker keeps long diagrams readable when edited.
        draw.vertex(
            str((y - 195) // 55 + 1),
            45,
            y - 8,
            35,
            24,
            "ellipse;html=1;fillColor=#E2E8F0;strokeColor=#CBD5E1;"
            f"fontColor={NAVY};fontSize=11;fontStyle=1;",
        )
        y += 55
        if y > height - 130:
            break


def add_sequence_pages(draw: Drawio) -> None:
    add_sequence_page(
        draw,
        "14 - Sequence AI Detection to Incident",
        ["AI Service", "Gateway / API", "Auth & Signature", "Incident Service", "Priority Engine", "Database", "Realtime"],
        [
            (0, 1, "POST model/alert", "call"),
            (1, 2, "validate token · IP · HMAC · timestamp · nonce", "call"),
            (2, 1, "validated request", "return"),
            (1, 3, "normalize detection payload", "call"),
            (3, 5, "load camera · station · model assignment", "call"),
            (5, 3, "context / coordinates", "return"),
            (3, 4, "calculate explainable score", "call"),
            (4, 3, "score · tier · factors", "return"),
            (3, 5, "transaction: create pending_review Incident", "call"),
            (5, 3, "Incident identifier", "return"),
            (3, 6, "broadcast IncidentCreated to station channel", "async"),
            (3, 1, "202 Accepted", "return"),
            (1, 0, "accepted response", "return"),
        ],
    )
    add_sequence_page(
        draw,
        "15 - Sequence Claim, Review and Dispatch",
        ["Dispatcher A", "Dispatcher B", "Station API", "Incident Assignment", "Dispatch Service", "Officer Selection", "Database", "Push / Realtime"],
        [
            (0, 2, "claim Incident", "call"),
            (2, 3, "conditional atomic assignment", "call"),
            (3, 6, "UPDATE ... WHERE assigned_dispatcher IS NULL", "call"),
            (6, 3, "one row affected", "return"),
            (3, 7, "IncidentAssigned(claimed)", "async"),
            (1, 2, "concurrent claim same Incident", "call"),
            (2, 3, "attempt conditional assignment", "call"),
            (3, 6, "guarded UPDATE", "call"),
            (6, 3, "zero rows affected", "return"),
            (3, 1, "409 Conflict — already claimed", "error"),
            (0, 2, "dispatch Incident [owned + pending]", "call"),
            (2, 4, "lock Incident and begin transaction", "call"),
            (4, 5, "find selected or nearest eligible Officer", "call"),
            (5, 6, "Redis GEO / PostGIS / shift filters", "call"),
            (6, 5, "eligible Officer", "return"),
            (4, 6, "create Crime + priority snapshot; mark Incident dispatched", "call"),
            (4, 7, "CrimeAssigned + FCM / Echo", "async"),
            (4, 0, "dispatch success", "return"),
        ],
        height=1350,
    )
    add_sequence_page(
        draw,
        "16 - Sequence Officer Response and Escalation",
        ["Field Officer", "Mobile API", "Crime Service", "Location Service", "Redis / PostGIS", "Evidence Service", "Station Realtime", "Escalation"],
        [
            (6, 0, "CrimeAssigned push / realtime", "async"),
            (0, 1, "GET crime + pre-arrival brief", "call"),
            (1, 2, "authorize assignment", "call"),
            (2, 0, "crime · map · context · evidence links", "return"),
            (0, 1, "PUT accept", "call"),
            (1, 2, "status=in_progress; accepted_at", "call"),
            (2, 6, "broadcast status update", "async"),
            (0, 1, "POST GPS update [distance/time threshold]", "call"),
            (1, 3, "validate and evaluate proximity", "call"),
            (3, 4, "GEOADD + durable/fallback path", "call"),
            (3, 6, "OfficerLocationUpdated / approaching / arrived", "async"),
            (0, 1, "POST body-cam evidence", "call"),
            (1, 5, "store authorized evidence", "call"),
            (0, 1, "PUT resolve with notes", "call"),
            (1, 2, "mark resolved; compute response time", "call"),
            (2, 6, "CrimeResolved", "async"),
            (7, 2, "[timeout/decline busy] reassign next eligible Officer", "call"),
            (7, 6, "CrimeEscalated / supervisor notification", "async"),
        ],
        height=1350,
    )


def add_activity_pages(draw: Drawio) -> None:
    draw.start_page("17 - Activity Incident Lifecycle", width=1900, height=1200)
    lanes = [
        ("Intake / AI", 40, 100, 330),
        ("Backend", 370, 100, 470),
        ("Dispatcher", 840, 100, 390),
        ("Field Officer", 1230, 100, 420),
        ("Audit / Notification", 1650, 100, 210),
    ]
    for label, x, y, width in lanes:
        draw.vertex(
            label,
            x,
            y,
            width,
            1020,
            "swimlane;html=1;horizontal=0;startSize=34;collapsible=0;"
            f"fillColor={WHITE};swimlaneFillColor={LIGHT};strokeColor={BORDER};"
            f"fontColor={NAVY};fontSize=13;fontStyle=1;",
        )
    start = draw.start(175, 160)
    detect = draw.activity("Receive AI / manual / citizen report", 90, 220, 230)
    create = draw.activity("Create Incident + calculate priority", 480, 220, 250)
    gate = draw.decision("Auto-dispatch gates satisfied?", 535, 330)
    queue = draw.activity("Publish pending-review queue", 480, 480, 250)
    claim = draw.activity("Claim and inspect Incident", 910, 480, 250)
    decision = draw.decision("Dispatcher decision?", 965, 600)
    reject = draw.activity("Reject false alarm + reason", 880, 760, 250)
    dispatch = draw.activity("Create Crime + select Officer", 480, 760, 250)
    notify = draw.activity("Deliver assignment", 1660, 760, 180)
    accept = draw.decision("Officer accepts?", 1370, 760)
    respond = draw.activity("Navigate · GPS · arrive · evidence", 1300, 910, 280)
    resolve = draw.activity("Resolve / no-visit outcome", 1300, 1020, 280)
    audit = draw.activity("Persist timeline · ledger · notifications", 1660, 1000, 180)
    end = draw.end(1740, 1090)
    draw.edge(start, detect)
    draw.edge(detect, create)
    draw.edge(create, gate)
    draw.edge(gate, dispatch, "[yes — narrow policy]")
    draw.edge(gate, queue, "[no]")
    draw.edge(queue, claim)
    draw.edge(claim, decision)
    draw.edge(decision, reject, "[reject]")
    draw.edge(decision, dispatch, "[dispatch]")
    draw.edge(dispatch, notify)
    draw.edge(notify, accept)
    draw.edge(accept, respond, "[accept]")
    draw.edge(accept, dispatch, "[decline/timeout — reassign]")
    draw.edge(respond, resolve)
    draw.edge(reject, audit)
    draw.edge(resolve, audit)
    draw.edge(audit, end)

    draw.start_page("18 - Activity Citizen Tip and Evidence", width=1900, height=1150)
    lanes = [
        ("Citizen / Provider", 40, 100, 350),
        ("Tip Intake", 390, 100, 400),
        ("Dispatcher", 790, 100, 420),
        ("Incident / Evidence", 1210, 100, 420),
        ("Communication", 1630, 100, 230),
    ]
    for label, x, y, width in lanes:
        draw.vertex(
            label,
            x,
            y,
            width,
            970,
            "swimlane;html=1;horizontal=0;startSize=34;collapsible=0;"
            f"fillColor={WHITE};swimlaneFillColor={LIGHT};strokeColor={BORDER};"
            f"fontColor={NAVY};fontSize=13;fontStyle=1;",
        )
    start = draw.start(180, 160)
    submit = draw.activity("Submit web/SMS tip + location + media", 90, 220, 260)
    validate = draw.activity("Validate · throttle · resolve station", 460, 220, 260)
    store = draw.activity("Store pending tip and signed media", 460, 350, 260)
    notify = draw.activity("Notify station queue", 1645, 350, 190)
    review = draw.activity("Review tip and media", 870, 350, 250)
    decision = draw.decision("Triage outcome?", 925, 500)
    dismiss = draw.activity("Dismiss with reason", 850, 680, 250)
    reply = draw.activity("Reply by configured provider", 1645, 680, 190)
    promote = draw.activity("Promote to Incident", 1280, 680, 250)
    evidence = draw.activity("Preserve linked media / source context", 1280, 820, 250)
    cleanup = draw.activity("Expire and purge according to retention", 460, 900, 260)
    end = draw.end(1730, 950)
    draw.edge(start, submit)
    draw.edge(submit, validate)
    draw.edge(validate, store)
    draw.edge(store, notify)
    draw.edge(notify, review)
    draw.edge(review, decision)
    draw.edge(decision, dismiss, "[dismiss]")
    draw.edge(decision, reply, "[reply]")
    draw.edge(decision, promote, "[promote]")
    draw.edge(promote, evidence)
    draw.edge(dismiss, cleanup)
    draw.edge(reply, cleanup)
    draw.edge(evidence, cleanup)
    draw.edge(cleanup, end)


def add_state_page(draw: Drawio) -> None:
    draw.start_page("19 - State Machines", width=1900, height=1100)
    draw.box("Incident State Machine", 80, 100, 520, 55, color=CYAN, fill=CYAN_LIGHT, bold=True)
    i_start = draw.start(120, 240)
    pending = draw.state("pending_review", 230, 220)
    dispatched = draw.state("dispatched", 230, 410)
    rejected = draw.state("rejected_false_alarm", 230, 600, 220)
    expired = draw.state("expired", 230, 790)
    i_end = draw.end(520, 520)
    draw.edge(i_start, pending, "create / score")
    draw.edge(pending, dispatched, "dispatch [pending + authorized] / create Crime")
    draw.edge(pending, rejected, "reject / store reason")
    draw.edge(pending, expired, "expire [age policy]")
    draw.edge(dispatched, i_end)
    draw.edge(rejected, i_end)
    draw.edge(expired, i_end)

    draw.box("Crime State Machine", 690, 100, 680, 55, color=PURPLE, fill=PURPLE_LIGHT, bold=True)
    c_start = draw.start(740, 235)
    pending_c = draw.state("pending", 840, 220)
    assigned = draw.state("assigned", 1080, 220)
    progress = draw.state("in_progress", 1080, 400)
    escalated = draw.state("escalated", 840, 580)
    no_visit = draw.state("not_visited", 1080, 580)
    resolved = draw.state("resolved", 1080, 780)
    false_alarm = draw.state("false_alarm", 840, 780)
    c_end = draw.end(1300, 850)
    draw.edge(c_start, pending_c, "create")
    draw.edge(pending_c, assigned, "assign Officer")
    draw.edge(assigned, progress, "accept / accepted_at")
    draw.edge(assigned, escalated, "timeout or busy / increment escalation")
    draw.edge(escalated, assigned, "reassign [attempts remain]")
    draw.edge(progress, no_visit, "noVisit(reason)")
    draw.edge(progress, resolved, "resolve(notes, evidence)")
    draw.edge(no_visit, assigned, "busy / reassign")
    draw.edge(no_visit, false_alarm, "false_alarm outcome")
    draw.edge(resolved, c_end)
    draw.edge(false_alarm, c_end)

    draw.box("Panic State Machine", 1430, 100, 390, 55, color=RED, fill=RED_LIGHT, bold=True)
    p_start = draw.start(1490, 250)
    active = draw.state("active", 1580, 230, 160)
    cancelled = draw.state("cancelled", 1580, 480, 160)
    panic_resolved = draw.state("resolved", 1580, 720, 160)
    p_end = draw.end(1760, 500)
    draw.edge(p_start, active, "officer triggers SOS / notify nearby")
    draw.edge(active, cancelled, "officer cancels")
    draw.edge(active, panic_resolved, "station resolves")
    draw.edge(cancelled, p_end)
    draw.edge(panic_resolved, p_end)


def add_class_page(draw: Drawio) -> None:
    draw.start_page("20 - Conceptual Class Diagram", width=2100, height=1300)
    classes = {
        "Admin": (80, 130, BLUE, ["governPlatform()", "viewAnalytics()", "inspectAudit()"]),
        "PoliceStation": (390, 130, CYAN, ["manageResources()", "superviseOperations()"]),
        "StationUser": (720, 130, PURPLE, ["claimIncident()", "reviewIncident()", "dispatch()"]),
        "Officer": (1050, 130, GREEN, ["acceptCrime()", "updateLocation()", "resolveCrime()"]),
        "AiModel": (1380, 130, GOLD, ["reportDetection()", "heartbeat()"]),
        "Camera": (1710, 130, RED, ["stream()", "receiveCommand()"]),
        "Incident": (560, 520, PURPLE, ["calculatePriority()", "dispatch()", "reject()", "expire()"]),
        "Crime": (980, 520, RED, ["assignOfficer()", "escalate()", "resolve()"]),
        "SceneEvidence": (1420, 520, GOLD, ["storeSegment()", "serveSignedMedia()"]),
        "CitizenTip": (220, 820, BLUE, ["promote()", "dismiss()", "reply()"]),
        "Bolo": (560, 820, CYAN, ["publish()", "expire()"]),
        "PanicEvent": (900, 820, RED, ["activate()", "cancel()", "resolve()"]),
        "MessageNotification": (1240, 820, GREEN, ["send()", "markRead()"]),
        "DecisionLedger": (1580, 820, SLATE, ["append()", "verifyChain()"]),
    }
    ids: dict[str, str] = {}
    for name, (x, y, color, operations) in classes.items():
        label = f"<b>{name}</b><hr>{'<br>'.join(operations)}"
        ids[name] = draw.vertex(
            label,
            x,
            y,
            250,
            125,
            "rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;"
            f"fillColor={WHITE};strokeColor={color};strokeWidth=2;fontColor={NAVY};"
            "fontFamily=Arial;fontSize=13;spacing=10;",
        )
    association = (
        "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;"
        f"strokeColor={SLATE};fontColor={NAVY};fontSize=12;"
        "endArrow=none;startArrow=none;"
    )
    composition = (
        "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;"
        f"strokeColor={SLATE};fontColor={NAVY};fontSize=12;"
        "startArrow=diamond;startFill=1;endArrow=none;"
    )
    draw.edge(ids["Admin"], ids["PoliceStation"], "manages  1..*", style=association)
    draw.edge(ids["PoliceStation"], ids["StationUser"], "contains  1..*", style=composition)
    draw.edge(ids["PoliceStation"], ids["Officer"], "employs  1..*", style=composition)
    draw.edge(ids["PoliceStation"], ids["Camera"], "owns  1..*", style=composition)
    draw.edge(ids["AiModel"], ids["Camera"], "assigned  *..*", style=association)
    draw.edge(ids["PoliceStation"], ids["Incident"], "owns  1..*", style=composition)
    draw.edge(ids["StationUser"], ids["Incident"], "claims / reviews  0..*", style=association)
    draw.edge(ids["Camera"], ids["Incident"], "originates  0..*", style=association)
    draw.edge(ids["AiModel"], ids["Incident"], "reports  0..*", style=association)
    draw.edge(ids["CitizenTip"], ids["Incident"], "promotes to  0..1", style=association)
    draw.edge(ids["Incident"], ids["Crime"], "creates  0..1", style=association)
    draw.edge(ids["Crime"], ids["Officer"], "assigned to  0..1", style=association)
    draw.edge(ids["Crime"], ids["SceneEvidence"], "has  0..*", style=composition)
    draw.edge(ids["Officer"], ids["PanicEvent"], "raises  0..*", style=association)
    draw.edge(ids["PoliceStation"], ids["Bolo"], "publishes  0..*", style=association)
    draw.edge(ids["PoliceStation"], ids["MessageNotification"], "communicates through  0..*", style=association)
    for name in ["Incident", "Crime", "PanicEvent", "CitizenTip"]:
        draw.edge(ids[name], ids["DecisionLedger"], "records decisions", style=association)
    draw.box(
        "Conceptual model only: persistence fields, tables, keys, indexes, and database normalization belong to Chapter Four.",
        520,
        1130,
        1060,
        65,
        color=GOLD,
        fill=GOLD_LIGHT,
        bold=True,
    )


def add_traceability_page(draw: Drawio) -> None:
    draw.start_page("21 - Requirements Traceability Map", width=1900, height=1100)
    columns = [
        ("Stakeholder Goals", 80, BLUE),
        ("Requirement Families", 460, CYAN),
        ("System Models", 840, PURPLE),
        ("Future Verification", 1220, GREEN),
        ("Evidence", 1570, GOLD),
    ]
    for label, x, color in columns:
        draw.box(label, x, 110, 260, 55, color=color, fill=WHITE, rounded=False, bold=True)
    rows = [
        ("Proactive detection", "FR-AI / FR-INC", "DFD Intake · AI Sequence", "AI/API integration tests", "Signed request + Incident"),
        ("Human-governed dispatch", "FR-STA / FR-DSP", "Dispatcher UC · Dispatch Sequence", "Concurrency + authorization tests", "Review + Crime transition"),
        ("Fast field response", "FR-OFF / NFR-PERF", "Officer UC · Response Sequence", "Latency + mobile workflow tests", "GPS + status timeline"),
        ("Secure camera operation", "FR-GTW / NFR-SEC", "Gateway UC · Evidence DFD", "HMAC / signed-media tests", "Backend-mediated command"),
        ("Accountability", "FR-AUD / NFR-AUD", "State models · Conceptual classes", "Ledger-chain verification", "Activity log + hash chain"),
        ("Reliable communication", "FR-RTC / NFR-REL", "Communication DFD · Officer Sequence", "Push / realtime delivery tests", "Persistent notification"),
        ("Manageable growth", "NFR-SCL / NFR-MNT", "System boundary · class model", "Load / maintainability review", "Queues + module boundaries"),
    ]
    for row, values in enumerate(rows):
        y = 205 + row * 115
        ids = []
        for col, value in enumerate(values):
            ids.append(
                draw.box(
                    value,
                    columns[col][1],
                    y,
                    260,
                    72,
                    color=columns[col][2],
                    fill=WHITE,
                    rounded=False,
                    font_size=11,
                )
            )
        for index in range(len(ids) - 1):
            draw.edge(ids[index], ids[index + 1])
    draw.box(
        "Traceability continues in Chapter Six, where planned acceptance targets become measured test evidence.",
        460,
        1020,
        980,
        55,
        color=GOLD,
        fill=GOLD_LIGHT,
        bold=True,
    )


def build() -> None:
    draw = Drawio()
    add_context_page(draw)
    add_authority_page(draw)
    add_dfd_context(draw)
    add_dfd_level1(draw)
    add_dfd_intake(draw)
    add_dfd_dispatch(draw)
    add_dfd_support(draw)
    add_usecase_overview(draw)
    add_usecase_pages(draw)
    add_sequence_pages(draw)
    add_activity_pages(draw)
    add_state_page(draw)
    add_class_page(draw)
    add_traceability_page(draw)
    draw.save()
    print(f"Created: {OUTPUT}")
    print(f"Diagram pages: {len(draw.mxfile.findall('diagram'))}")


if __name__ == "__main__":
    build()
