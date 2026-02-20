## Plan: KI1-Projekt 308 — Masterplan für 5er-Team

**Thema**: Neuronales Netz für den California Housing Datensatz + Vergleich mit Linearer Regression.
**Deadline**: 15.04.2026 | **Workload**: 75h pro Person | **Abgabe**: Individuelle PDF-Portfolios + gemeinsamer Code als ZIP.

Die Aufgabe verlangt explizit **kein fertiges Ergebnis**, sondern einen **begründeten Zwischenstand** mit dokumentiertem Arbeitsprozess. Das größte Bewertungsgewicht liegt auf der individuellen **Zusammenfassung des Logbuchs (40%)** — dort müssen mehrere Methoden erprobt, begründet und iteriert worden sein. Die **Gruppenergebnisse (25%)** sind eine Gruppennote.

---


### Phase 0: Setup & Organisation (Woche 1 — alle)
1. **Sprecherin bestimmen** — verantwortlich für Gruppentreffen-Protokolle, Ergebnisse der Gruppe, und finale Code-Abgabe als ZIP
2. **Repository-Struktur** in ki-308/ anlegen:
   - `notebooks/` — ein Notebook pro Arbeitsbereich (EDA, Baseline, LASSO, Trees/Ensemble, Neural Network)
   - `utils/` — gemeinsame Hilfsfunktionen (`data_loading.py`, `plotting.py`, `evaluation.py`)
   - `results/` — exportierte Abbildungen (matplotlib, kein Screenshot!) und Ergebnis-Tabellen
3. **Gemeinsames Daten-Modul** erstellen: Laden, Cleaning, Train/Test-Split (fester `random_state`) — damit alle auf identischen Daten arbeiten. Vorlage: HA9_10_Aufgabe3_lsg.ipynb (Cut-offs + 98%-Quantil-Outlier-Entfernung)
4. **`nbstripout`** installieren (siehe Ressources.md) und requirements.txt um `pandas`, `seaborn`, `tensorflow` ergänzen
5. **Logbuch-Template** anfertigen (jeder führt ab sofort ein eigenes Logbuch)

### Phase 1: EDA & Baseline (Woche 2–3 — alle gemeinsam)
6. **Jede Person** arbeitet sich selbstständig in den Datensatz ein (Pflicht für individuelle Logbücher):
   - `fetch_california_housing()` laden, Feature-Beschreibungen verstehen
   - Histogramme, Scatterplots (Feature vs. `MedHouseVal`), `df.describe()`
   - Korrelationsmatrix + Heatmap (Vorlage: Blatt 10 Lösung)
7. **Gemeinsame Entscheidung** über Data Cleaning (Gruppentreffen dokumentieren):
   - Cut-off bei `MedHouseVal` = 5.0 und `HouseAge` = 52 entfernen
   - Outlier via 98%-Quantil (AveRooms, AveBedrms, Population, AveOccup)
8. **Baseline: Lineare Regression** (`LinearRegression` auf allen Features) — $R^2$-Score auf Train/Test. Das ist der **Referenzwert** für alle weiteren Modelle.

### Phase 2: Individuelle Methodenbereiche (Woche 3–7 — parallel)

Jede Person bearbeitet ihren Schwerpunkt **eigenständig**, dokumentiert Entscheidungen/Iterationen im Logbuch und vergleicht immer gegen die Baseline:

| Person | Schwerpunkt | Methoden | Vorlagen |
|--------|-------------|----------|----------|
| **P1** | Regularisierte Regression | `LassoCV`, `Ridge`, Feature-Selektion, polynomiale Feature-Transformation ($x^n$), Skalierung (MinMax, Standard) | Blatt 10 Lösung, Blatt 11 Lösung, Kapitel 6 Folien |
| **P2** | Baumbasierte Modelle | `DecisionTreeRegressor`, Pruning (`ccp_alpha`), Feature Importance | Blatt 08 Lösung, Kapitel 4+6 Folien |
| **P3** | Ensemble-Methoden | `RandomForestRegressor`, `GradientBoostingRegressor`, Hyperparameter-Tuning via `GridSearchCV` | Kapitel 7 Folien, Ensemble-Code |
| **P4** | Nicht-parametrische Regression | `KNeighborsRegressor`, Local Regression, Skalierungseffekte | Kap. 6.4 Code, Kapitel 6 Folien |
| **P5** | **Neuronales Netz** (Kernaufgabe) | TensorFlow/Keras `Sequential`, verschiedene Architekturen (Tiefe, Breite), Aktivierungsfunktionen (ReLU, ELU, tanh), Learning Rate, Epochs | Blatt 12 Lösung, Kapitel 8 Folien |

9. **Jede Person dokumentiert im Logbuch**:
   - Welche Hyperparameter getestet (mind. 3–4 Varianten pro Methode)
   - Warum bestimmte Konfigurationen gewählt/verworfen
   - Schwierigkeiten und Lösungen
   - Zwischenergebnisse mit $R^2$-Score (Train + Test)
10. **Evaluation einheitlich**: Alle nutzen denselben Train/Test-Split und berichten $R^2$, MAE, RMSE — so sind Ergebnisse **direkt vergleichbar**

### Phase 3: Vertiefung & Cross-Vergleich (Woche 7–8)
11. **Gruppentreffen**: Ergebnisse zusammentragen, gemeinsame Vergleichstabelle erstellen:
   - Modell | $R^2$ Train | $R^2$ Test | MAE | RMSE | Trainingszeit | #Parameter
12. **Jede Person** probiert mind. eine **Iteration/Variation** ihres Modells basierend auf den Gruppenerkenntnissen (z.B. nur Top-Features nutzen, die LASSO identifiziert hat)
13. **P5 (NN)** vergleicht explizit gegen Lineare Regression (Kernforderung der Aufgabe) und erstellt einen Predicted-vs-Actual-Plot
14. **Gemeinsame Diskussion**: Wo sind Grenzen der Modelle? Warum ist Lat/Lon problematisch? Möglicher Ausblick (z.B. Clustering nach Region, Feature Engineering)

### Phase 4: Portfolio-Erstellung (Woche 8–10)
15. **Jede Person** schreibt ihr individuelles e-Portfolio (PDF):
   - **Titelseite** (1 S.): Thema, Name, Gruppennr. 308, Mitglieder, Sprecherin
   - **Logbuch** (Anhang): chronologisch, mit Datum, Titel, Zusammenfassung pro Eintrag, Verweis auf Gruppentreffen
   - **Zusammenfassung des Logbuchs** (max. 4 S.): Fragestellung → Methoden + Begründung → Ergebnisse → Grenzen/Unsicherheiten → Schlussfolgerungen/Ausblick. Mit nummerierten Abbildungen und Tabellen, klickbare Verweise ins Logbuch
   - **Einschätzung der Gruppenmitglieder** (1 S.): je 1 Stärke + 1 Schwäche, respektvoll, 2–4 Sätze pro Person
   - **Quellen & Hilfsmittel** (~1 S.): URLs mit Datum, Bücher, KI-Prompts transparent
16. **Sprecherin** zusätzlich:
   - **Ergebnisse der Gruppe** (max. 3 S.): Alle Methoden gegenübergestellt, nicht aneinandergereiht — Vergleichstabelle, Interpretation, Grenzen, Ausblick
   - **Protokoll der Gruppentreffen** (1–2 S.): Datum, Teilnehmer, besprochene Inhalte, vereinbarte Aufgaben, Anpassungen
17. **Abbildungen**: matplotlib-Export (kein Screenshot!), beschriftet, nummeriert, im Text referenziert
18. **Dateinamen**: `KI1_308_<Nachname>_Portfolio.pdf` + Sprecherin: `KI1_308_Code.zip`

---

**Verification**
- Alle Notebooks laufen fehlerfrei auf gemeinsamer Umgebung (requirements.txt)
- Gemeinsame Vergleichstabelle (Modell vs. Metriken) ist konsistent über alle Portfolios
- Jedes Portfolio enthält alle 7 Pflichtabschnitte (Tabelle I der Aufgabe)
- $R^2$-Werte sind plausibel (Baseline ~0.6, NN/Ensemble sollte ~0.7–0.85 erreichen)
- Gegenlesen: jede Person liest ein anderes Portfolio gegen (Vollständigkeit, Abbildungsqualität)

**Decisions**
- **5 Methodenbereiche statt weniger**: Jede Person hat einen klar eigenen Schwerpunkt → individuelle Logbuch-Einträge sind unterscheidbar und zeigen eigenständige Transferleistung (wichtig für 40%-Bewertung)
- **Gemeinsamer Daten-Split**: Identischer `random_state` und Cleaning → Ergebnisse direkt vergleichbar für die Gruppenübersicht
- **Mehrere Notebooks statt einem**: Saubere Trennung, weniger Merge-Konflikte in Git, aber gemeinsames `utils/`-Modul für Konsistenz
- **NN als Kernstück bei P5**: Die Aufgabenstellung fordert explizit ein NN + Vergleich mit Linearer Regression — P5 ist daher die Schlüsselrolle, aber alle profitieren vom Vergleich

Projektstruktur:

```
ki-308/
├── data.ipynb                          ← Hub-Notebook mit Übersicht + Baseline
├── requirements.txt                    ← + pandas, seaborn, tensorflow
├── .gitignore                          ← Python/Jupyter/IDE Ignores
├── utils/
│   ├── __init__.py                     ← Zentrale Imports
│   ├── data.py                         ← Laden, Cleaning, Train/Test-Split (random_state=42)
│   ├── plotting.py                     ← Pred-vs-Actual, Residuen, Heatmap, Histogramme
│   └── evaluation.py                   ← R², MAE, RMSE + Modellvergleichstabelle
├── notebooks/
│   ├── 01_EDA.ipynb                    ← Explorative Datenanalyse (alle)
│   ├── 02_Baseline_Lineare_Regression.ipynb  ← Referenzmodell (alle)
│   ├── 03_LASSO_Ridge.ipynb            ← P1: Regularisierung + Feature-Selektion
│   ├── 04_Decision_Tree.ipynb          ← P2: Pruning, Feature Importance
│   ├── 05_Ensemble.ipynb               ← P3: Random Forest, Gradient Boosting
│   ├── 06_kNN_Regression.ipynb         ← P4: k-Nearest Neighbors
│   └── 07_Neural_Network.ipynb         ← P5: TF/Keras NN + Vergleich mit LR (Kernaufgabe)
└── results/                            ← Exportierte Abbildungen (PNG+PDF)
```
