# ToDo - Projekt

Projektabgabe: 15.03


## Pflicht-Klasse Player.py
Für das Spiel ist verpflichtend eine Klasse `Player` mit folgendem Aufbau zu erstellen:

### Instanzvariablen
Die Klasse `Player` enthält die folgenden privaten Instanzvariablen:

- `name`: Name des Spielers wird dem Konstruktor übergeben
- `health`: Gesundheitszustand des Spielers (soll standardmäßig auf den Wert 100 gesetzt werden)
- `strength`: Stärke des Spielers wird durch den Konstruktor gesetzt (zufällige Zahl zwischen 40 (inkl.) und 80 (inkl.))

### Methoden
Folgende Methoden sind zu implementieren:

- `__str__` soll folgenden String zurückgeben: `"Player <name> has <strength> strength and <health> health."`
- `take_damage(damage)` soll eine Zahl `damage` als Parameter erhalten und diesen vom aktuellen `health`
  Wert abziehen (Minimalwert: 0)
- `regain_health(health_regain)` soll eine Zahl `health_regain` als Parameter erhalten und diese auf die aktuelle
  `health` addieren (Maximalwert ist der Standardwert 100)

Unit-Tests:
Es sollen mindestens eine Test-Datei für die vorgegebene Klasse sowie mindestens eine weitere Test-Datei für eine andere zentrale Komponente Ihres Programms erstellt werden mit jeweils mindestens 3 Testfällen.

Das Spiel soll über eine Hauptdatei main.py gestartet werden und eine passende Startnachricht ausgeben.

Erstellen Sie eine `README.md` Datei, um über Ihren Programmcode angemessen zu informieren. 
  - Kurze Projektbeschreibung: 3–5 Sätze zum Spiel, Setting, Ziel.
  - Installations- und Ausführungsanleitung: Wie startet man das Spiel? Wie führt man die Tests aus? 
  - Strukturübersicht: Kurze Erklärung der wichtigsten Dateien/Module und Klassen. 
  - Bekannte Einschränkungen / Bugs: Falls bekannte Fehler existieren, kurz beschreiben
