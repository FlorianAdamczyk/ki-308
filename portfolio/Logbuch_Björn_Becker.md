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
**Aus Gruppentreffen:** Eigenständig und Gruppentreffen 1 (20.02.2026)

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
**Titel:** Wiederholung der Vorlesung und Einlesen in Ergebnisse der Gruppenmitglieder  
**Aus Gruppentreffen:** Eigenständig

**Arbeitsschritte:**
* Aufgrund von Tensorflow musste die Python Version von 3.14 auf 3.12 heruntergestuft werden. 
* Nachvollziehen des Aufbaus des Git-Workspace. Requirements installiert.
* Lesen und Verstehen der Notebooks vor den Neuronalen Netzwerken, die später zum Ensemble-learning beitragen könnten.
* Nochmals Vorlesung wiederholen und dabei vorläufig Ideen entwickeln, an welche Aufgaben ich mich setzen möchte. (Pooling der geographischen Lage, Transformation der Daten(Feature Engineering), Learning-Rate-Scheduler. Ich weiß aus vorherigen Gruppentreffen, dass Hyperparameter wie Form, Lernrate oder Aktivierungsfunktionen schon ausführlich behandelt wurden).
zusätzliche Recherche mit Google
* Einlesen in Fortschritt der Gruppenmitglieder (NN-Notebooks) 
  * dabei wird klar, dass einige Ideen schon umgesetzt wurden
* Überfliegen von Felix H. Logbuch


**Entscheidungen:**
- ich möchte mich nicht so sehr mit der Form des NN auseinandersetzen, sondern an genannten Dingen arbeiten
  - Pooling (auch wenn Aussicht auf Erfolg nicht so groß ist)
ich lege mir eine kleine Analoge Formelsammlung für das Projekt und die Umgebung an.

**Schwierigkeiten / offene Fragen:**
- Das Ausführen der Notebooks der anderen Gruppenmitglieder dauert sehr lange - sollte ich es im JupiterHub der Uni probieren, welchem ich mehr Rechenleistung adhästiere.

---

## Eintrag 3

**Datum:** 18.03.2026
**Titel:** Anfänge und erste Erkenntnisse
**Aus Gruppentreffen:** Angelehnt an Gruppentreffen 5 am 17.03.

**Arbeitsschritte:**
- Aus den Ergebnissen von Kolja und Felix H. haben wir Schlüsse über die Größenordnung von Parametern gezogen. Außerdem war Ergebnis, dass die Aktivierungsfunktion kaum Einfluss auf die Ergebnisse hat, weswegen ich heute nur ReLu nutzte, da diese effizient ist (vgl. [StudySmarter](https://www.studysmarter.de/studium/ingenieurwissenschaften/maschinelles-lernen-studium/aktivierungsfunktion/#:~:text=Eine%20der%20gr%C3%B6%C3%9Ften%20St%C3%A4rken%20der%20ReLU%20ist,einer%20Standardwahl%20in%20Deep%20Learning%20Anwendungen%20macht.)).
- Ich wollte mich zuerst mit dem grundsätzlichen Coden eines einfachen Neuronalen Netzes auseinandersetzen. Dazu habe ich Modulimporte und Skalierung der bereinigten Daten aus den Gruppenergebnissen übernommen. Da Felix H. herausfand, dass nur ["MedInc", "AveOccup", "Latitude", "Longitude"] Informationsgewinn bieten und die anderen Daten eher zum Rauschen beitragen, entschied ich mich, nur diese 4 zu benutzen. 
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

- Beim nochmaligen darüber Nachdenken bin ich nun nicht mehr so überzeugt, dass die lin. reg so viel bringt. Frage ChatGPT: Welche anderen Möglichkeiten gibt es, die Daten in eine verständliche Form zu bringen? - PDP (Partial Dependence Plots) mit RandomForestGenerator
  - die PDP grenzen die Hyperparameter weiter ein
  - so wie Florian die Feature Importance herausgefunden hat, kann man jetzt die Hyperparameter Importance aus dem Random Forest ausgeben lassen
    - Jetzt kann man iterativ Random-/ oder Grid-Search machen und die Hyperparameter weiter eingrenzen

![Hyperparameter Importance](C:\KI_2026\KI_308\ki-308\results\Hyperparameters_Feature_Importance.png)
![PDP](C:\KI_2026\KI_308\ki-308\results\pdp.png)


**Entscheidungen:**
- Morgen mache ich das ganze nochmal mit einem größeren Datensatz
- Ich möchte schauen, wie gut die Netze werden, wenn man den Vorgang mehrfach Wiederholt

**Schwierigkeiten / offene Fragen:**
- Macht es Sinn, die Zeit aufzuwenden mehr Daten anzusammeln? Wie gut kann das werden? Laufe ich in eine Sackgasse?

---

---

## Eintrag 4

**Datum:** 19.03.2026  
**Titel:** erste Iterationen 
**Aus Gruppentreffen:** 5 vom 17.03.

**Arbeitsschritte:**
- Ich erweitere meinen Datensatz, um bei den PDP und Hyperparameter-Importances klare Schlüsse ziehen zu können. Bisher besteht mein Datensatz nur aus den 30 besten Eintägen der vorherigen Runs.
  - zu sehr werde ich es nicht erweitern, da ich das Gefühl bekomme, Tendenzen jetzt schon abschätzen zu können. Es braucht sehr viel Rechenzeit
- Es hat sich gelohnt zu warten. Der neue Datensatz mit nun 50 Einträgen zeigt eine andere Tendenz für die Batchsize. (Vorher 32, jetzt 16). Die Tiefe scheint ziemlich egal zu sein. Bei der Hyperparameter-Importance gewinnt die Batchsize stark an Einfluss. Es lässt sich nur mit schwacher Sicherheit sagen, dass die Anzahl der Units pro Layer und die Tiefe eine vergleichbar kleine Rolle spielen. Dagegen sind wahrscheinlich "dropout", "Lernrate" und "L2-Regularisierungsfaktor" von großer Bedeutung. 
  - ich finde es etwas Überraschend, dass hier "L2" wichtig ist
  - Das ganze Vorgehen entspricht nicht meiner Intuition. Ich bin mir unsicher, wie die Ergebnisse zu interpretieren sind
- Ich werde nun trotzdem die Hyperparameter anhand der PDP eingrenzen.
  - Units: bleibt - aber Zufallsverteilung eher Richtung 128
  - depth: das Ergbnis ist ziemlich waagerecht. Ich nehme mal noch die 4 hinzu und schaue was passiert
  - batch size nur noch 16 und 32
  - dropout: Nur noch 0.1 - 0.16
  - lr: bleibt
  - l2: bleibt
  - ich hatte vorher noch die Möglichkeit, dass auch Netze über 50 Epochen gerechnet werden konnten. In den Ergebnissen ist kein Abbruch vor 50 Epochen zu sehen, daher wird es entfernt und auf 100 festgelegt (mit Earlystop).
    - mit den Ergebnissen der anderen Gruppenmitgliedern im Kopf, sind mehr Epochen sehr wahrscheinlich besser, aber die Rechenzeit ist einfach zu enorm, als das ich es ausprobieren könnte. Vielleicht mal über Nacht.
- Nun habe ich die Ergebnisse:
  - Die neuen Netze neigen maginal weniger zum Overfitting, was auch vorher kein großes problem war. In der Spitze sind die neuen Netze laut dem R2 Wert tatsächlich nicht besser. Der Vergleich ist aber unfair, da jetzt ca. 400 Netze mit 200 Netzen verglichen werden 
  - auf Platz 20 für den besten Testscore ist aber eine leichte Verbesserung zu sehen, trotz ungerechtem Vergleich.
    - In der Breite ist es nun besser geworden
- Aus PDP und Hyperparameter-Importance kann man nun sehen, dass 4 Layer nicht gut sind und eine Einschränkung des Dropouts auf 0.115 - 0.15 Sinn machen könnte. Ich werde nun die Parameter nochmal verändern und das Ergebnis dann zu meinem neuen Datensatz hinzufügen. Außerdem werde ich mal 200 Epochen als Maximalwert ausprobieren
- 200 Epochen zu nutzen war sehr gut. Die Hyperparameter-Importance zeigt nun, dass der wichtigste Parameter nun die Lernrate ist. ![Hyperparameter-Importance](C:\KI_2026\KI_308\ki-308\results\Hyperparameters_Feature_Importance_3.png)
- ![PDP Nr.3](C:\KI_2026\KI_308\ki-308\results\PDP_3.png) Mit Blick auf die Lernrate stellt sich die Frage, ob das erlaubte Intervall optimal angesezt ist. Speziell werde ich mir kleinere Lernraten ansehen ab 10^-6.
  - Die Ergebnisse werden nicht besser


**Entscheidungen:**
- Ensemble aus Netzen mit den gesamten California Housing testen. Ich habe noch Baysche Netze im Kopf(ohne genau zu wissen was das ist, aber das passt glaube ich zu dem Thema.
Das ist eher eine Rechercheaufgabe)

**Schwierigkeiten / offene Fragen:**
- Der heutige Tag war vor allem von warten geprägt. Die Ausführung des Codes dauert jeweils mehr als eine Stunde.

---

## Eintrag 5

**Datum:** 20.03.  
**Titel:** erstes Ensemble
**Aus Gruppentreffen:** 5 vom 17.03.

**Arbeitsschritte:**
- Jetzt ein letztes mal Parameteranpassung. Lernrate (logarytmisch) wird auf Intervall [-3.3; -2] begrenzt. 
- Über Nacht habe ich darüber nachgedacht, ob es eine gute Entscheidung war, immer wieder die schlechten Netze zu löschen. Vielleicht könnten diese Ergebnisse das Gesamtergebnis verbessern.
- Die Verbesserung hat gute Ergebnisse erziehlt. Ich werde die Epochen auf 500 hochschrauben, da viele Netze die 200 max Epochen zum lernen nutzen. Diese Netze sind wirklich gut, aber kaum entschieden besser als vorher. 
- Ich hatte vorher schon die Units gewichtet. Vorher war es stark favorisiert in Richtung 128, jetzt immer noch, aber weniger stark. Ich möchte mehr diversifizieren, da ich nur NN für die späteren Ensembles benutze, was sehr wichtig ist (vgl. Vorlesung 7, S.11). Ich nehme eine Hand voll der Netze und benötige noch ein paar schwächere mit stark anderen Hyperparametern
- ich dachte eigentlich, dass wir einen gemeinsamen Speicher von unseren besten Netzen haben, aber das einzige, dass ich fand, war eine leere Liste, die nur Einträge im Arbeitsspeicher vermerkt.
- Ich habe jetzt ein Ensemble gebaut. Leider ist das Ergebnis mit R2 = 0.7499 nur wenig besser als der Durchschnitt der einzelnen Netze. 
- 


**Entscheidungen:**
- Aufgrund der nicht so bereichernden Ergebnisse heute, möchte ich morgen das gleiche mit allen Features machen. 
  - entweder der Score wird besser, oder der Score wird schlechter. Im zweiten Fall müsste ich dann die Hyperparameter nochmal neu anpassen. - Also wieder Random-Search
- Außerdem finde ich spannend die Features zu verknüpfen 

**Schwierigkeiten / offene Fragen:**
- Es ist schwer die Ergebnisse einzuornen, da nicht hinreichend unterschieden werden kann zwischen statistischen Schwankungen und Wahrheit.

---

## Eintrag 6

**Datum:** 21.03.
**Titel:** Titel  
**Aus Gruppentreffen:** Eigenständig, aber aufbauend aud Gruppentreffen 5

**Arbeitsschritte:**
- Ich trainiere das Ensemble nun auf den gesamten California Housing Datensatz. Der Score ist 0.78 und damit deutlich besser als zuvor. Ich werde das Ensemble noch ein paar mal ausführen, um abzuschätzen, wie groß das Rauschen ist. (Ergebnisse: 0.778, 07795, 0.788, 0.7807, 0.7809)
- Fragte ChatGPT: welche Features des California Housing Datensatz kann man verbinden, sodass ein bessers NN entsteht? - ... Diese sind besonders effektiv: AveRooms / AveOccup, AveBedrms / AveRooms,Population / AveOccup, MedInc / AveOccup ... Es sollten die normierten Daten verwendet werden. 
- Ich habe heute keine Lust mehr mich mit Python Fehlern auseinander zu setzen
**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 

---

## Eintrag 7

**Datum:** 23.03. 
**Titel:** Anfang Dokumentation 
**Aus Gruppentreffen:** Treffen X oder "Eigenständig"

**Arbeitsschritte:**
- Habe einen schwer zu identifizierenden Fehler. Der Score des aktuellen Ensembles ist ?negativ?. 
  - in meinen Daten ist ein eiziger Wert nicht Non-Null. Grund könnte ein geteilt durch 0 Problem beim Feature Engineering sein, dass ich durch das Hinzufügen eines kleinen Wertes in den Nenner zu beheben versuche.
    - Der score ist nun 0.65
  - Außerdem ist die Skalierung im Eimer. Wahrscheinlich macht es Sinn, erst Feature Engineering mit den Ursprungsdaten zu machen und dann alle gemeinsam zu skalieren.
    - Der Score von nun 0.765 ist etwas enttäuschend
- Nach einer längeren Lagebesprechung mit Felix N. haben wir uns für heute dazu entschieden, wie auch im Gruppentreffen 5 vereinbart, schonmal die Ergebnisse des Projektes zusammen zu fassen. Gesprächsthemen waren außerdem der aktuelle Stand und formale Themen. Außerdem werde ich mich im Verlauf des heutigen Tages mit meinem Notebook beschäftigen in Sachen Lesbarkeit und Dokumentation.

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**
- 


---

<!-- Weitere Einträge nach dem gleichen Schema -->
## Eintrag 7

**Datum:** [23.03.]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**## Eintrag 7

**Datum:** [23.03.]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**## Eintrag 7

**Datum:** [23.03.]  
**Titel:** [Titel]  
**Aus Gruppentreffen:** [Treffen X oder "Eigenständig"]

**Arbeitsschritte:**
- 

**Entscheidungen:**
- 

**Schwierigkeiten / offene Fragen:**