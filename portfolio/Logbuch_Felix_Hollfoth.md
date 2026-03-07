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

**Datum:** 02.03.2026 und 03.03.2026
**Titel:** virtuelle Pythonumgebung neu aufgesetzt
**Aus Gruppentreffen:** Gruppentreffen 4 (27.02.2026)

**Arbeitsschritte:**

* mit der installierten Tensorflow Version aus Eintrag 2 konnto 05_flo_NN.ipynb nicht ausgeführt werden. Numpy ≥ 1.21.1 lies sich unter python < 3.11 nicht installieren.
* Bei dem wechsel auf Python 3.11. wurde .git verändert und das Repro musste neu geclont werden
* Durch Konflikte mehrerer Python, .venv und .pyenv Konfigurationen wurden alle komplett gelöscht und ein neues Setup erstellt:
  * TensorFlow Version: 2.10.1
  * Numpy Version: 1.26.4
  * Pandas Version: 2.3.3
  * Matplotlib Version: 3.10.8
  * Python Version: 3.10.11

---

## Eintrag 4

**Datum:** 07.03.2026
**Titel:** Probleme mit Not a Number (NaN) beim erstellen des Neuronalen Netzes
**Aus Gruppentreffen:** Gruppentreffen 2 (17.02.2026)

**Arbeitsschritte:**

* Beim erstellen eines ersten neuronalen Netzes kam der Fehler NaN. Fehlerursache (Vermutungen):
  * Das Dataframe ist nach dem skalieren intern beschädigt, trotz bzw. wegen eingebauter Rückumwandlung
  * Beim Konventieren in Numpy entstehen echte NaNs, die im Dataframe enthalten bleiben
* Gruppenmitglied Florian hat in der Funktion: get_train_test_split() ebenfalls einen scaler miteinprogrammiert, welcher diesen Fehler nicht enthält, weshalb dieser absofort genutzt wird

---



## Eintrag 4

**Datum:** 03.03.2026
**Titel:** [Titel]
**Aus Gruppentreffen:** Gruppentreffen 1 (11.02.2026) und Gruppentreffen 2 (17.02.2026)

**Arbeitsschritte:**`<!-- Weitere Einträge nach dem gleichen Schema -->`

* Spalte longitude negative Werte????!!!!!

---



## Eintrag 4

**Datum:** 03.03.2026
**Titel:** [Titel]
**Aus Gruppentreffen:** Gruppentreffen 1 (11.02.2026) und Gruppentreffen 2 (17.02.2026)

**Arbeitsschritte:**`<!-- Weitere Einträge nach dem gleichen Schema -->`

---



## Eintrag 4

**Datum:** 03.03.2026
**Titel:** [Titel]
**Aus Gruppentreffen:** Gruppentreffen 1 (11.02.2026) und Gruppentreffen 2 (17.02.2026)

**Arbeitsschritte:**`<!-- Weitere Einträge nach dem gleichen Schema -->`
