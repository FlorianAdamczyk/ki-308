# Überblick: Aufgaben P1–P5

### P1 — Regularisierte Regression (Notebook 03)
**Was macht man?**
LASSO und Ridge Regression ausprobieren, verschiedene Skalierungen vergleichen (keine / MinMax / Standard), polynomiale Features (Grad 2) hinzufügen, Feature-Selektion dokumentieren.

**Das Tolle daran:**
- Sehr direkter Bezug zur Vorlesung (Kapitel 6)
- LASSO gibt automatisch eine "Rangliste" der Features — das ist ein schönes, interpretierbares Ergebnis
- Polynomiale Features sind ein "Aha-Moment": aus 8 Features werden 44

**Schwierigkeiten:**
- Skalierung muss *vor* dem Split passieren (Datenleck vermeiden) — konzeptuell wichtig
- `PolynomialFeatures` + `LassoCV` dauert etwas länger
- Man muss verstehen, *warum* LASSO manche Features auf 0 setzt

**Benötigte Fähigkeiten:** Grundlegendes Python, Vorlesungsstoff Kapitel 6 verstanden haben
**Schwierigkeit:** ⭐⭐ (eher leicht)

---

### P2 — Decision Tree (Notebook 04)
**Was macht man?**
Einen Entscheidungsbaum ohne Einschränkung trainieren (Overfitting beobachten), dann `max_depth` systematisch variieren, dann Pruning via `ccp_alpha` ausprobieren, Feature Importances visualisieren.

**Das Tolle daran:**
- Overfitting ist hier *extrem* sichtbar: Train R²=1.0, Test R²≈0.6 — sehr lehrreich
- Bias-Varianz-Tradeoff wird konkret erfahrbar
- Feature Importance gibt ein schönes Balkendiagramm

**Schwierigkeiten:**
- `cost_complexity_pruning_path` ist etwas unbekannter als die Standard-API
- GridSearchCV dauert länger als bei linearen Modellen
- Kombination von `max_depth` *und* `ccp_alpha` gleichzeitig kann verwirrend sein

**Benötigte Fähigkeiten:** Vorlesung Kapitel 4 (Bäume), Geduld beim Tuning
**Schwierigkeit:** ⭐⭐⭐ (mittel)

---

### P3 — Ensemble-Methoden (Notebook 05)
**Was macht man?**
Random Forest und Gradient Boosting trainieren, jeweils mit `GridSearchCV` optimieren (Achtung: viele Hyperparameter), Feature Importances vergleichen, beide Methoden gegenüberstellen.

**Das Tolle daran:**
- Liefert mit Abstand die **besten R²-Werte** (~0.82–0.87) — das macht Spaß
- Random Forest ist konzeptuell elegant (viele schlechte Bäume → ein gutes Modell)
- `n_jobs=-1` macht es schnell

**Schwierigkeiten:**
- `GridSearchCV` über RF + GB ist **sehr rechenintensiv** (3×4×3 = 36 Fits × 5 Folds = 180 Modelle für RF allein!)
- Gradient Boosting reagiert sensitiv auf `learning_rate` × `n_estimators` — Kombination verstehen
- GridSearch muss notfalls auf kleineres Paramgitter reduziert werden

**Benötigte Fähigkeiten:** Kapitel 7 Folien, etwas Erfahrung mit `sklearn`, guter Rechner (oder JupyterHub)
**Schwierigkeit:** ⭐⭐⭐⭐ (anspruchsvoll, vor allem zeitlich)

---

### P4 — kNN Regression (Notebook 06)
**Was macht man?**
kNN *ohne* und *mit* Skalierung vergleichen, das optimale k (1–50) durch Iteration finden, uniform vs. distance-Gewichtung testen, Skalierungseffekt erklären.

**Das Tolle daran:**
- **Skalierungseffekt** ist dramatisch sichtbar: ohne Skalierung funktioniert kNN kaum
- Konzeptuell sehr intuitiv ("die k ähnlichsten Häuser")
- k-Tuning-Plot ist didaktisch sehr schön (klassischer Bias-Varianz-Tradeoff)
- Kürzestes Notebook — überschaubar

**Schwierigkeiten:**
- kNN bei k=1 auf 17.000 Samples und 50 Iterationen ist etwas langsam
- `GridSearchCV` auf kNN mit vielen Features kann deutlich langsamer sein als erwartet
- Inhaltlich relativ schmale Aufgabe — man muss für 4 Seiten Portfolio-Zusammenfassung aktiv nach Tiefe suchen (z.B. geografische Features Lat/Lon besonders diskutieren)

**Benötigte Fähigkeiten:** Kapitel 6.4 Folien, Grundverständnis Distanzmetriken
**Schwierigkeit:** ⭐⭐ (leicht bis mittel)

---

### P5 — Neuronales Netz (Notebook 07)
**Was macht man?**
Das ist die **Kernaufgabe** laut Aufgabenstellung. TensorFlow/Keras Modelle bauen, 5 verschiedene Architekturen testen (Tiefe, Breite, Aktivierungsfunktionen, Dropout), Lernkurven analysieren, **expliziten Vergleich mit linearer Regression** als Pflicht-Abschnitt.

**Das Tolle daran:**
- Das ist der Kern des Projekts — P5 hat die "Hauptrolle"
- TensorFlow/Keras ist modern und praxisrelevant
- Lernkurven sind visuell sehr eindrucksvoll
- Man lernt Dropout, Aktivierungsfunktionen, Early Stopping kennen

**Schwierigkeiten:**
- **Trainingszeit** ist deutlich höher als alle anderen Notebooks
- Python 3.13 + TF-Venv muss korrekt eingerichtet sein
- Viele Freiheitsgrade → man kann sich verlieren; sinnvolle Dokumentation der Entscheidungen ist Pflicht
- Overfitting bei tiefen Netzen ohne Regularisierung ist ein echtes Problem, nicht nur ein theoretisches
- Der Pflicht-Vergleich mit LR muss inhaltlich begründet sein, nicht nur "NN ist besser"

**Benötigte Fähigkeiten:** Kapitel 8 Folien, Blatt 12 Lösung, Bereitschaft sich in TensorFlow einzulesen
**Schwierigkeit:** ⭐⭐⭐⭐⭐ (anspruchsvollste Aufgabe, aber auch die inhaltlich reichhaltigste)

---

## Schnellvergleich

| | P1 LASSO/Ridge | P2 Dec. Tree | P3 Ensemble | P4 kNN | P5 Neural Net |
|---|---|---|---|---|---|
| **Schwierigkeit** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Rechenzeit** | gering | mittel | **hoch** | mittel | **hoch** |
| **Vorlesungsbezug** | Kap. 6 | Kap. 4+6 | Kap. 7 | Kap. 6.4 | Kap. 8 |
| **Ergebnis-Qualität (R²)** | ~0.65 | ~0.70 | **~0.85** | ~0.72 | ~0.78 |
| **Portfolio-Stoff** | gut | gut | sehr gut | eher knapp | sehr gut |
| **Für wen geeignet** | Einsteiger | Solide Grundlage | Erfahren + Geduld | Einsteiger | Am meisten Interesse/Erfahrung |

> **Empfehlung:** P5 sollte die Person übernehmen, die am meisten Interesse und/oder Vorkenntnisse mitbringt — es ist die Kernaufgabe. P3 sollte jemand mit gutem Rechner oder Zugriff auf den JupyterHub machen.