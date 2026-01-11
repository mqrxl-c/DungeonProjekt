# Planung

Projektabgabe: 15.03

## OOP und Coding Conventions
Zeilenlänge: 
- max. 79 Zeichen pro Zeile

Imports: 
- separate Zeilen,
- Standardbibliothek zuerst, dann Drittanbieter, dann
eigene Module

Benennungskonventionen:
- Variablen/Funktionen: snake case
- Klassen: CamelCase
- Konstanten: UPPER CASE

Leere Zeilen:
- 2 Leerzeilen vor Klassen/Funktionen auf Modulebene
- 1 Leerzeile innerhalb von Methoden

Kommentare: 
- klar, prägnant, Inline nur wenn nötig

Docstrings: 
- dreifache Anfuhrungszeichen 
- für Module, Klassen, Funktionen

## Anforderungen funktional:
Planung für die Umsetzung der Anforderungen

main.py → start + Startnachricht

Wenn Player durch alle Räume ist → Erfolgsnachricht

### Unit-Tests:
  - Es sollen mindestens eine Test-Datei für die vorgegebene Klasse sowie mindestens eine weitere Test-Datei für eine 
     andere zentrale Komponente Ihres Programms erstellt werden mit jeweils mindestens 3 Testfällen.
  - Verwenden Sie das Python-Framework unittest oder pytest.
  - Die Tests sollen sowohl typische Fälle als auch Randfälle abdecken.

### Klasse: Monster
Voragabe: Für den Fall, dass der Spieler das Monster besiegt, erhält er Lebenspunkte in Höhe der Hälfte des vom Monsters erlittenen Schadens. Z.B.: In einem Kampf erleidet ein Monster 60 Schadenspunkte. Hat der Spieler das Monster geschlagen, so erhält der Spieler 60/2 = 30 Lebenspunkte auf seinen Gesundheitszustand gutgeschrieben.
Unsicher: gilt auch für wenn das monster nur 59 HP anfangs hatte?

Init Funktion:
- name: vom Player gegeben
- HP: 40 - 80 (zufällig)
- max HP: Anfangs HP
- Stärke: 20 - 40 (zufällig)

str Funktion:
- return: Das Monster names "..", hat .. HP und .. Stärke
- (eventuell stärke unbekannt lassen)

Sterben Funktion:
- falls HP unter 0 -> Ausgabe oder so?


### Klasse: Player
PLayer erhält bei einem besiegten Monster, häfte des ausgeteilten Schaden.

Init Funktion:
- name: Basierend auf Spieler Input
- HP: 100 
- MaxHP: 100
- Stärke: 40 - 80 zufällig

str Funktion:
- return "Player <name> has <strength> strength and <health> health."

take_damage(damage) Funktion:
- soll schaden von HP abziehen

regain_health(health_regain) Funktion:
- gibt HP zurück (maximal 100 HP)

## Anforderungen nicht-funktional:

### README.md
- Projektbeschreibung: 3-4 Sätze, Spiel, Setting, Ziel
- Installations- und Ausführungsanleitung: (Wie führt man Tests aus)
- Strukturübersicht: Kurze Erklärung der Wichtigsten Sachen
- Bekannte Einschränkungen / Bugs: Falls fehler existieren, beschreiben

### Dokumentation (PDF)
Namensschema der Datei: `INF25_Matrikelnummer_Name_Dokumentation.pdf`

1. Konzeptbeschreibung: Kurzbeschreibung der Spielidee, Spiellogik und des typischen Spielablaufs.
2. Struktur- / Designskizze: Übersicht über die wichtigsten Klassen und Funktionen (z.B. als Text oder einfache Grafik).
3. Für jede zentrale Klasse: Zweck, Attribute und Methoden.
4. Testkonzept: 
   1. Welche Teile der Anwendung werden getestet? 
   2. Welche Arten von Fällen (Normalfälle, Randfälle) werden abgedeckt?
   3. Wie führen Sie die Tests aus?
5. Reflexion:
   1. Was waren Ihre größten Herausforderungen?
   2. Welche Fehler/Bugs sind aufgetreten und wie haben Sie diese gelöst?
   3. Wie sind Sie beim Entwurf der Klassen/Struktur vorgegangen?
   4. Welche Hilfsmittel (z.B. Foren, Google, IDE-Hilfestellung, ...) haben Sie verwendet (ein kurzer Absatz je Hilfsmittel):
      - Wie genau wurden diese eingesetzt?
      - Was haben Sie übernommen, was verworfen?
      - Was haben Sie dabei gelernt?

Wichtig: Bei Fehlern Hilfsmittel Dokumentieren!!

Eigenständigkeitserklärung (Ende des Dokuments)


## Abgabe
Geben Sie die folgenden Ergebnisse Ihrer Arbeit im Moodle Kursraum ab:

- Projektarchiv
  - .zip Datei Ihres Codes
  - Test-Dateien
  - README.md
  - keine unnötigen temporären Dateien, keine virtuellen Umgebungen
- Dokumentation (PDF Datei) strukturiert nach den oben vorgegebenen Kapiteln.
- Abgabeformat: alles zusammen als .zip-Datei im Moodle-Kurs abgeben.
      Namensschema der zip-Datei: `INF25_Matrikelnummer_Name_Abgabe.zip

## Bewertungsschema
Die Bewertung achtet auf folgende Aspekte (jeweils mit angegebener Maximalpunktzahl). 
In Summe können maximal 100 Punkte erreicht werden.
[]()
| Bewertungskategorie                        | Maximalpunkte |
|--------------------------------------------|---------------|
| Spiellogik und Funktionalität              | 30            |
| Pflichtklasse Player.py                    | 10            |
| OOP Design & Code-Struktur                 | 15            |
| Konsoleninteraktion und Eingabevalidierung | 10            |
| Unit-Tests                                 | 15            |
| Readme.md                                  | 5             |
| Projektdoku                                | 10            |
| Projektstruktur und Abgabeformalitäten     | 5             |


## Eigene Ideen:
pyQt:
- GUI Bibliothek
- Anleitungen etc Link Speichern

Highscore:
- Json Highscore speichern und Vor game Start anzeigbar



https://www.youtube.com/watch?v=46ICy1VgM5s