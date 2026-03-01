\# esmini — Environment Simulator



This folder contains the esmini simulation engine used to run

OpenSCENARIO test scenarios for ADAS validation.



\## Structure

bin/                  esmini executables (not tracked by Git)

&nbsp; esmini.exe          Main scenario runner

&nbsp; odrviewer.exe       OpenDRIVE road viewer

&nbsp; odrviewer.exe       Replay recorded scenarios

&nbsp; dat2csv.exe         Convert output data to CSV

&nbsp; esminiLib.dll       Required runtime library



resources/

&nbsp; Catalogs/           Vehicle and pedestrian catalogs

&nbsp; models/             3D models (not tracked by Git)

&nbsp; schema/             OpenSCENARIO schema validation files

&nbsp; traffic\_signals/    Traffic signal definitions



\## How to Run

From project root:

&nbsp; esmini\\bin\\odrviewer.exe --window 60 60 800 400 --odr map\\map1.xodr



\## esmini Version

Source: https://github.com/esmini/esmini

