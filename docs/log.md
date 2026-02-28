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

&nbsp; First venv creation was incomplete - Scripts/activate

&nbsp; file was missing. Fixed by using --clear --upgrade-deps

&nbsp; flag forces a clean rebuild.



HOW TO START EVERY SESSION FROM NOW:

&nbsp; 1. Open Command Prompt

&nbsp; 2. cd Desktop\\ADAS-Thesis

&nbsp; 3. venv\\Scripts\\activate.bat

&nbsp; 4. (venv) appears = ready to work

&nbsp; 5. At end: git add . → git commit → git push → deactivate



PROBLEMS FACED:

&nbsp; venv\\Scripts\\activate missing on first creation.

&nbsp; Fixed with --clear --upgrade-deps flag.

