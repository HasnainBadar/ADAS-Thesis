\# ADAS Thesis — Progress Log

\# GitHub: https://github.com/HasnainBadar/ADAS-Thesis



═══════════════════════════════════════════════

SESSION 1 | 27 February 2026

═══════════════════════════════════════════════



COMPLETED:

\- GitHub repository created (ADAS-Thesis, public)

\- Git configured on local PC

\- Project folder structure created

\- Map location selected: A270 Helmond, Netherlands



WORKFLOW:

\- RoadRunner: University PC via NoMachine + FortiClient VPN

\- SUMO + esmini + GitHub: Local PC (my machine)

\- File transfer method: TBD next session



FOLDER STRUCTURE:

  map/            RoadRunner exports (.xodr files)

  sumo/           Traffic simulation files

  scenarios/aeb/  AEB test scenarios

  scenarios/lka/  LKA test scenarios

  scenarios/acc/  ACC test scenarios

  results/        Validation outputs and pass/fail data

  docs/           This log and all documentation



WHY A270 HELMOND:

  Real European ADAS test corridor. Used in Grand Cooperative

  Driving Challenge (GCDC). Operated by Siemens with full

  sensor infrastructure. Contains highway, transition zone,

  and urban grid — covers all 11 Euro NCAP scenarios.



PROBLEMS FACED: None

NEXT SESSION: Connect to university PC, open RoadRunner,

              draw Zone 1 highway stretch, export map1.xodr



═══════════════════════════════════════════════



═══════════════════════════════════════════════

SESSION 1 CONTINUED | Virtual Environment Done

═══════════════════════════════════════════════



COMPLETED:

\- venv recreated cleanly using --clear --upgrade-deps flag

\- Activated successfully via activate.bat

\- Installed: lxml, numpy, pandas, matplotlib, sumolib, traci

\- requirements.txt saved

\- .gitignore created



ROOT CAUSE OF EARLIER PROBLEM:

  First venv creation was incomplete - Scripts/activate

  file was missing. Fixed by using --clear --upgrade-deps

  flag forces a clean rebuild.



HOW TO START EVERY SESSION FROM NOW:

  1. Open Command Prompt

  2. cd Desktop\\ADAS-Thesis

  3. venv\\Scripts\\activate.bat

  4. (venv) appears = ready to work

  5. At end: git add . → git commit → git push → deactivate



PROBLEMS FACED:

  venv\\Scripts\\activate missing on first creation.

  Fixed with --clear --upgrade-deps flag.



═══════════════════════════════════════════════

SESSION 2 | 28 February 2026

PHASE 1 — Map Creation (RoadRunner)

═══════════════════════════════════════════════



COMPLETED:

\- Connected to university PC via FortiClient VPN + NoMachine

\- Opened RoadRunner R2024b, created project ADAS-Thesis

\- Created new scene: Map1.rrscene

\- Drew first road: 500m straight highway stretch

\- Configured 4-lane layout (2 forward, 2 backward)

\- Lane widths: 3.75m each (Dutch motorway standard)

\- Shoulders: 3.0m each side

\- Median: 2x 1.5m restricted lanes (symmetric)

\- Speed: 81mph (130 km/h) per lane

\- Material: Asphalt1

\- Exported: Map1.xodr (OpenDRIVE 1.4, Driving Side: Right)

\- Transferred file to local PC via GitHub

\- Pushed map1.xodr to repository



WHY THESE SPECIFICATIONS:

&nbsp; Based on Dutch RONA motorway standards matching real

&nbsp; A270 Helmond corridor. 3.75m lane width and 3.0m

&nbsp; shoulders are standard for 130 km/h motorways in NL.



WARNINGS ENCOUNTERED:

&nbsp; "Scene is not geolocated" — safe to ignore for now.

&nbsp; GeoJSON coordinates centered at (0,0). Will add real

&nbsp; GPS coordinates when full map is complete.



PROBLEMS FACED:

&nbsp; 1. Road Plan Tool uses RIGHT-CLICK not left-click to

&nbsp;    place points — caused confusion initially.

&nbsp; 2. venv activation failed first time — fixed with

&nbsp;    --clear --upgrade-deps flag.

&nbsp; 3. Single median lane caused asymmetric road — fixed

&nbsp;    by using 2x 1.5m restricted lanes instead.



NEXT SESSION:

&nbsp; - Validate map1.xodr opens correctly in esmini

&nbsp; - Then build Zone 2: highway entry/exit ramps

&nbsp; - Then build Zone 3: urban grid



═══════════════════════════════════════════════

