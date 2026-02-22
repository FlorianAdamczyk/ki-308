# Logbuch — KI1-Projekt 308

**Name:** Felix Hollfoth
**Gruppe:** 308
**Matrikelnummer: 8221324**

---

## Anleitung

Ein Eintrag enthält mindestens:

- **Datum**
- **Titel** (kurz und prägnant)
- **Arbeitsschritte** (stichpunktartig ist ausreichend)
- Verweis auf das Gruppentreffen, aus dem die Aufgabe hervorgegangen ist
- Ggf. Abweichungen vom vereinbarten Vorgehen (mit Begründung)

Screenshots im Logbuch sind erlaubt. Abbildungen müssen nicht vollständig ausgearbeitet sein.

---

## Eintrag 1

**Datum:** 16.02.2026
**Titel:** Repository einrichten und Ideen für Gruppeneinteilung aufstellen
**Aus Gruppentreffen:** Gruppentreffen 1 (11.02.2026)

**Arbeitsschritte:**

- Repository geklont, Abhängigkeiten installiert (`pip install -r requirements.txt`)
- `nbstripout --install` eingerichtet
- Python 3.14.3 installiert
- Erste Übersicht über den California Housing Datensatz verschafft
  (`fetch_california_housing()`, 8 Features, Zielvariable: `MedHouseVal`)
- Vorlesungsfolien nach relevanten Methoden untersucht
- Übergordnete Aufgaben zusammengetragen (Datenbereinigung, -analyse, -transformation, Lernen des neuronalen Netztes (layers, units, Aktivierungsfkt. etc., Prüfen auf Overfitting, Validierungsmethoden, Parameterreduzierung, Regularisierung, Vergleich mit linearer Regression) für Vorstellung in nächstem Gruppentreff

---

## Eintrag 2

**Datum:** 22.02.2026
**Titel:** Programmierumgebung geschaffen und Datenskalierung
**Aus Gruppentreffen:** Gruppentreffen 1 (11.02.2026) und Gruppentreffen 2 (17.02.2026)

**Arbeitsschritte:**

* Auf Hinweis von Gruppenmitglied Kolja musste Python 3.14 für tensorflow gedowngradet werden. Nach Recherche geht dies nur mit Python 3.10 oder niedriger, daher Python 3.10.13 über pyvenv installiert und bei VS Code als Interpreter und Kernel festlegen
* Funktionen geschrieben um den Datensatz zu Skalieren mittels MinMaxScaler und Standardscaler (aus Gruppentreff 2 17.02.2026)
  * wichtig da einige Features sehr große und andere sehr kleine Werte haben -> Probleme beim Gradientenverfahren (Backpropagation)
  * Intervall kann auf die Aktivierungsfunktion abgestimmt werden
  * Funktionen resistent gemacht gegen die Eingabe von DataFrames und Array -> Eingabedatentyp wird auch wieder ausgegeben
  * target_values werden nicht skaliert für die Stabilität und Interpretierbarkeit des Netzes


---

## Eintrag 3

**Datum:** [Datum]
**Titel:** [Titel]
**Aus Gruppentreffen:** Gruppentreffen 1 (11.02.2026) und Gruppentreffen 2 (17.02.2026)

**Arbeitsschritte:**

---



<!-- Weitere Einträge nach dem gleichen Schema -->
