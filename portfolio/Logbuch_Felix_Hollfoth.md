# Logbuch — KI1-Projekt 308

**Name:** Felix Hollfoth
**Gruppe:** 308
**Matrikelnummer: 8221324**

---

## Generelle Ideen:

* Spalte longitude negative Werte????!!!!
* Starke Korrelation zwischen BedRomms und Rooms oder Latitude und Langitude, eventuell doppelt gelernt oder sowas?
* starke korrelation zwischen MedInc und median_house_value mal einzelnd betrachten
* vorhandene Analyse: https://medium.com/@advika5109/neural-networks-for-real-estate-predictions-a-comprehensive-analysis-of-the-california-housing-0e79cd642c36

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

## Eintrag 5

**Datum:** 07.03.2026
**Titel:** Bestimmung von Hyperparametern (Aktivierungsfunktion und Skalierung)
**Aus Gruppentreffen:** Gruppentreffen 4 (27.02.2026)

**Arbeitsschritte:**

* Da die Konvergenz eines Verfahrens häufig sehr stark von dem Wertebereich und der dazugehörigen Aktivierungsfunktion abhänkt wird über folgende Kombinationen iteriert:
  * Aktivierungsfunktionen: 'relu', 'tanh', 'sigmoid', 'elu', 'selu', 'leaky_relu'
  * Datenskalierung: keine, standard, min0_max1
* Außer den in den Vorlesung bekannten Aktivierungsfunktionen wird selu mitberücksichtigt, da sie beim Durchlauf die Aktivierungen normalisieren kann. Vorallem für tiefere Netze interessant, falls mehr als zwei hidden layer sich als nützlich erweisen (https://www.geeksforgeeks.org/deep-learning/selu-activation-function-in-neural-network/)
* Im Training-Score, sowie auch bis auf eine Ausnahme im Test-Score ist die Standardisierung die beste Option. Dahingehen sorgt keine Skalierung dafür, dass einige Modelle je nach Aktivierungsfunktion sogar schlechter sind als der Mittelwert. Das kann an den großen Unterschiedenen im Wertebereich der Features liegen
* Beste Test-Score zeigt sich beim tanh mit der Standardisierung mit 0,7668.
* Abweichung zum Trainingsscore liegt bei 3,8 %, welches leichtes overfitting andeutet aber als noch nicht problematisch angesehen wird
* Relu bietet mit 6,1 % Abweichung das größte overfitting an und liefert den zweitbesten score mit 0,7618

---

## Eintrag 6

**Datum:** 09.03.2026
**Titel:** Bestimmung von Hyperparametern (Lernrate, Batch-Size)
**Aus Gruppentreffen:** Gruppentreffen 4 (27.02.2026)

**Arbeitsschritte:**

* Lernrate grob bestimmt (Test von alpha = 1E-6 - 10); Resultat: zwischen 0,001 und 0,01 die einzigen Bereiche, in denen der Score auf den Testdaten über 70 % ist
* Zwischen 0,001 und 0,01 in 50 identischen Schritten durchitteriert -> Ergebnisse schwanken von 0,7177 bis 0,7624
* Lernrate konstant über 0,74 im Intervall [0,0032; 0,0072]
* Bester Einzelwert bei 0,0054 welche aber auch deutlich auf Zufall im Modell hindeutet -> Lernrate bei 0,0054 mehrfach ausgeführt und Schwankung beobachtet
* Schwankung bei erneuter Ausführung von über 3 % erkannt -> Training der Hyperparamter liegt in diesem Schwankungsbereich -> Statistische Untersuchung der Schwankung bei erneuter Ausführung

---

## Eintrag 7

**Datum:** 10.03.2026
**Titel:** Bestimmung von Hyperparametern (Erneute Ausführungen, Epochenanzahl)
**Aus Gruppentreffen:** Gruppentreffen 4 (27.02.2026)

**Arbeitsschritte:**

* Histogramm über 100 Modelle mit konstanten Parametern erstellt -> wenige Modelle 0,7 und 0,72; meisten Modelle liegen zwischen 0,74 und 0,765
  * Mittelwert: 0,7481
  * Varianz: 0,0002
  * Standardabweichung: 0,0124
* Epochen betrachtet bis 10.000 -> ab 500 Epochen wird Overfitting stärker aber bis 500 Epochen verbessert sich auch Test-Score -> Entscheidung einen Verlauf des MAE-Wertes auf den Testdaten pro Epoche ausgeben zu lassen
* MAE-Wert zeigt ein Minimum bei 500, daher bis 1000 Epochen laufen lassen
* Bis 1000 Epochen zeigt sich aber keine weitere Verbesserung mehr -> Minimum hier bei circa 300 Epochen. Vor 300 Epochen sieht man in beiden Plots eine Verringerung des MAE, daher sollten auf jeden Fall mehr als 100 Epochen trainiert werden, eher über 300

---



## Eintrag 8

**Datum:** 10.03.2026
**Titel:** Random Search
**Aus Gruppentreffen:** Gruppentreffen 4 (27.02.2026)

**Arbeitsschritte:**

* Bis jetzt wurden sich nur einzelne Hyperparameter angeschaut, daher mal über verschiedene Hyperparameter testen mittels Random Search (https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf) -> Wegen Rechenzeit und Ergebnissen wird dies GridSearch bevorzugt
* 


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

---
