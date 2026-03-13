# DungeonProjekt
***
Programmieren Projekt 2026 DHBW  
 
Das Ziel des Spiels ist es, das Ende des Dungeons zu erreichen. 
Dabei muss der Spieler durch mehrere Räume und Überleben. 
In jedem Raum gibt es ein Monster, gegen das der Spieler kämpfen oder wegrennen kann. 
Vor dem Spielstart entscheidet der Spieler, wie viele Räume er spielen will. 

___
### Installation und Ausführung
Einfach:  
1. in den Ordner "dist" navigieren
2. main.exe ausführen

Komplizierter:
1. Dependencies installieren
   1. im Terminal in den root ordner Navigieren (DungeonProjekt)
   2. "pip install ." ausführen
   3. Die Setup.py Datei übernimmt dann die Installation aller Dependencies
2. Spiel Starten
    1. über den root Ordner: "py src/main.py" ausführen
   2. oder erst in src navigieren, mit "cd src" und dann "py main.py" ausführen

___
### Tests Ausführen
Um die Unittests auszuführen muss man zuerst Schritt 1 (Dependencies installieren)
aus der Anleitung zur Spielausführung befolgen.
1. im Terminal in den root Ordner navigieren (oder direkt in den test ordner)
2. "py tests/dateiname.py" ausführen

___
### Strukturübersicht




---
### Einschränkungen
Wenn das Programm über die .exe auf einem älteren Gerät ausgeführt wird,
kann es sein das die visuelle Lebensanzeige der Monster und des Spielers nicht angezeigt wird.
Dann werden "?" als Ersatz für die Herzen verwendet. Die Zahlenanzeige Funktioniert immer.

---

