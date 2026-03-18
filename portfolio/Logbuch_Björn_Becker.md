# Logbuch — KI1-Projekt 308

**Name:** Björn Philipp Becker  
**Gruppe:** 308  
**Zeitraum:** 20.02.2026 – 15.04.2026
**Matrikelnummer** ...
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

**Datum:** 19.02.2026 & 20.02.2026  
**Titel:** Projektstart — Aufgabe lesen, Repository einrichten  
**Aus Gruppentreffen:** Gruppentreffen 1 (20.02.2026)

**Arbeitsschritte:**
- Aufgabenstellung gelesen und verstanden
- Recherche, wie man an den Datensatz kommt (Am Ende aus Übung)
- Über GitLab informiert (im Gruppentreffen dann aber anders entschieden, da keiner sich wirklich damit auskennt, aber Florian ordentlich mit GutHub)
- Wiederholung der Vorlesungsfolien
- Repository geklont
- `nbstripout --install` eingerichtet
- Erste Übersicht über den California Housing Datensatz verschafft


**Schwierigkeiten / offene Fragen:**
- Wie kann das Projekt funktionieren, wenn wir so verschiedene Zeitfenster haben
---

## Eintrag 2

**Datum:** 17.03.2026
**Titel:** Wiederholung von Vorlesung und Einlesen in Ergebnisse der Gruppenmitglieder  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
* Aufgrund von Tensorflow musste die Python Version von 3.14 auf 3.12 hueruntergestuft werden. 
* Nachvollziehen des Aufbaus des Git-Workspace. Requirements installiert.
* Lesen und Verstehen der Notebooks vor den Neuronalen Netzwerken, die später zum Ensemble-learning beitragen könnten.
* Nochmals Vorlesung wiederholen und dabei vorläufig Ideen entwickeln, an welche Aufgaben ich mich setzen möchte. (Pooling der geographischen Lage, Transformation der Daten, Learning-Rate-Scheduler. Ich weiß aus vorherigen Gruppentreffen, dass Hyperparameter wie Form, Lernrate oder Aktivierungsfunktionen schon ausführlich behandelt wurden).
zusätzliche Recherche mit Google
* Einlesen in Fortschritt der Gruppenmitglieder (NN-Notbooks) 
  * dabei wird klar, dass einige Ideen schon umgesetzt wurden
* Überfliegen von Felix H. Logbuch


**Entscheidungen:**
- ich möchte mich nicht so sehr mit der Form des NN auseinandersetzen, sondern an genannten Dingen arbeiten
  - Pooling (auch wenn Aussicht auf Erfolg nicht so groß ist)
ich lege mir eine kleine Analoge Formelsammlung für das Projekt und die Umgebung an.

**Schwierigkeiten / offene Fragen:**
- Das Ausführen der Notebooks der anderen Gruppenmitglieder dauert sehr lange - sollte ich es im JupiterHub der Uni probieren, welchem ich mehr Rechenleistung adhästiere.

---

## Eintrag 4

**Datum:** [18.03.2026]  
**Titel:** [Anfänge und erste Erkenntnisse]  
**Aus Gruppentreffen:** [Angelehnt an Gruppentreffen 5 am 17.03.]

**Arbeitsschritte:**
- Aus den Ergebnissen von Kolja und Felix H. haben wir Schlüsse über die Größenordnung von Parametern gezogen. Außerdem war ergebnis, dass die Aktivierungsfunktion kaum Einfluss auf die Ergebnisse hat, weswegen ich heute nur ReLu nutzte, da diese effizient ist(vgl. [StudySmarter](https://www.studysmarter.de/studium/ingenieurwissenschaften/maschinelles-lernen-studium/aktivierungsfunktion/#:~:text=Eine%20der%20gr%C3%B6%C3%9Ften%20St%C3%A4rken%20der%20ReLU%20ist,einer%20Standardwahl%20in%20Deep%20Learning%20Anwendungen%20macht.)).
- Ich wollte mich zuerst mit dem Grundsätzlichen Coden eines einfachen Neuronalen Netzes auseinandersetzen. Dazu habe ich Modulimporte und Skalierung der bereinigten Daten aus den Gruppenergebnissen übernommen. Da Felix H. herausfand, dass nur ["MedInc", "AveOccup", "Latitude", "Longitude"] Informationsgewinn bieten und die anderen Daten eher zum Rauschen beitragen, entschied ich mich, nur diese 4 zu benutzen. 
- Meine ersten beiden kleinen Netze, die ich mit einer L2 Regularisierung zur Vermeidung von Overfitting (Die Nützlichkeit hatte Kolja beim Gruppentreffen eingebracht), kleinem Dropout und mit EarlyStopping ausgestattet hatte, ergaben ordentliche Ergebnisse mit einem R2 von knapp über 0.7 und wenig Overfitting. 
- Wie im Gruppentreffen besprochen, ist die erste Aufgabe, ein sehr gutes Netz aus den bisherigen Erkenntnissen zu bauen. Ich erwartete, da bisher die Hyperparameter eher einzeln getestet wurden, Probleme mit lokalen Minima zu bekommen. Deswegen nutze ich Random-Search. Hyperparametereingrenzung ergaben sich aus den Ergbnissen der Anderen mit Abgleich mit ChatGPT: Ergebnis: 
  - Neuronen:        32, 64, 128
  - Layer:           2, 3
  - Learning Rate:   1e-4 – 1e-2 (log)
  - L2:              1e-5 – 1e-3
  - Dropout:         0.1 – 0.3
  - Batch Size:      16, 32, 64
  - Epochs:          max 100 (EarlyStopping)
  - Aktivierung:     ReLU
- Ich erwartete eine enorme Rechenzeit und deswegen informierte ich mich über Parallelisierung
- Ergebnis: <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>run_id</th>
      <th>R² Val</th>
      <th>R² Test</th>
      <th>units</th>
      <th>depth</th>
      <th>lr</th>
      <th>l2</th>
      <th>dropout</th>
      <th>batch_size</th>
      <th>epochs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>0.757183</td>
      <td>0.743349</td>
      <td>128</td>
      <td>2</td>
      <td>0.000343</td>
      <td>0.000052</td>
      <td>0.156997</td>
      <td>16</td>
      <td>81</td>
    </tr>
    <tr>
      <th>33</th>
      <td>33</td>
      <td>0.751369</td>
      <td>0.736966</td>
      <td>128</td>
      <td>2</td>
      <td>0.001588</td>
      <td>0.000024</td>
      <td>0.163947</td>
      <td>16</td>
      <td>66</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>0.750405</td>
      <td>0.736433</td>
      <td>128</td>
      <td>2</td>
      <td>0.000395</td>
      <td>0.000017</td>
      <td>0.256285</td>
      <td>64</td>
      <td>93</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>0.747135</td>
      <td>0.733957</td>
      <td>64</td>
      <td>3</td>
      <td>0.000941</td>
      <td>0.000284</td>
      <td>0.116963</td>
      <td>16</td>
      <td>77</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>0.746669</td>
      <td>0.733977</td>
      <td>128</td>
      <td>3</td>
      <td>0.001095</td>
      <td>0.000016</td>
      <td>0.195057</td>
      <td>32</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>

- Ich hoffte Zusammenänge sehen zu können, aber das ist nicht der Fall. Deswegen werde ich den Code erneut Ausführen und die besten Ergebnisse sammeln. Ich erhoffe mir mit einer größeren Menge an Daten eine gescheite lineare Regression durchzuführen, um Zusammenhänge zu verstehen. 

- Beim Nochmal drüber Nachdenken bin ich nun nicht mehr so überzeugt, dass die lin. reg so viel bringt. Frage ChatGPT: Welche anderen Möglichkeiten gibt es, die Daten in eine verständliche Form zu bringen? - PDP mit RandomForestGenerator
  - die PDP sind schwer nachzuvollziehen, aber,
  - so wie Florian die Feature Importance herausgefunden hat, kann man jetzt die Hyperparameter Importance aus dem Random Forest ausgeben lassen


**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 

---

---

## Eintrag 3

**Datum:** [Datum]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 

---

## Eintrag 3

**Datum:** [Datum]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 

---

## Eintrag 3

**Datum:** [Datum]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 

---

## Eintrag 3

**Datum:** [Datum]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 

<!-- Weitere Einträge nach dem gleichen Schema -->
