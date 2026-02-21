# KI1 - Projekt 308: Neuronales Netz für den kalifornischen Hauspreis-Datensatz

**Modul:** Künstliche Intelligenz I — WS 2025/26  
**Dozenten:** Prof. Dr. Christian Heiliger, Dr. Jan-Matthis Waack  
**Gruppennummer:** 308  
**Abgabetermin:** 15.04.2026

## Aufgabenstellung

Entwicklung eines neuronalen Netzes zur Vorhersage von Hauspreisen anhand des
[California Housing Datensatzes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)
(Scikit-learn). Das Modell wird im Vergleich zur linearen Regression (aus der Vorlesung) eingeordnet.

## Projektstruktur

```
ki-308/
├── data.ipynb                           # Hub-Notebook: Übersicht + Baseline
├── requirements.txt                     # Python-Abhängigkeiten
├── utils/
│   ├── data.py                          # Datenladen, Cleaning, Train/Test-Split
│   ├── plotting.py                      # Einheitliche Visualisierungen
│   └── evaluation.py                    # R², MAE, RMSE + Modellvergleich
├── notebooks/
│   ├── 01_EDA.ipynb                     # Explorative Datenanalyse
│   ├── 02_Baseline_Lineare_Regression.ipynb
│   ├── 03_LASSO_Ridge.ipynb             # P1: Regularisierung, Feature-Selektion
│   ├── 04_Decision_Tree.ipynb           # P2: Regression Trees, Pruning
│   ├── 05_Ensemble.ipynb                # P3: Random Forest, Gradient Boosting
│   ├── 06_kNN_Regression.ipynb          # P4: k-Nearest Neighbors
│   └── 07_Neural_Network.ipynb          # P5: TensorFlow/Keras NN (Kernaufgabe)
├── results/                             # Exportierte Abbildungen (PNG + PDF)
├── portfolio/
│   ├── Logbuch_Template.md              # Vorlage für das individuelle Logbuch
│   └── create_submission_zip.sh         # ZIP-Skript für die Sprecherin
└── PDFs/
    └── Aufgabe.txt / Aufgabe.pdf        # Aufgabenstellung
```

## Schnellstart

### 1. Umgebung einrichten

> **⚠️ Hinweis:** TensorFlow ist nicht mit Python 3.14+ kompatibel. Bitte **Python 3.13** verwenden! für Intel Mac User ist leider auch 3.13 zu neu es muss 3.11.14 genutzt werden deswegen wurde auch Tensorflow auf 2.10 zurückgestuft 

```bash
# Virtuelle Umgebung erstellen (einmalig) – explizit Python 3.13
python3.13 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### 2. Notebooks starten

```bash
jupyter lab
```

Die Notebooks befinden sich im Ordner `notebooks/` und sind nummeriert:
starte mit `01_EDA.ipynb`, dann `02_Baseline_Lineare_Regression.ipynb`.
Das Hub-Notebook `data.ipynb` im Stammverzeichnis gibt eine Gesamtübersicht.

### 3. nbstripout einrichten (Pflicht vor dem ersten Commit)

[nbstripout](https://github.com/kynan/nbstripout) entfernt Notebook-Outputs
vor Git-Commits, damit das Repository sauber bleibt:

```bash
pip install nbstripout
nbstripout --install
```

## Gemeinsame Konventionen

| Konvention | Wert |
|-----------|------|
| `random_state` (überall) | 42 |
| Test-Anteil | 20 % |
| Outlier-Quantil | 98 % |
| Evaluationsmetriken | R², MAE, RMSE (Train + Test) |
| Abbildungsformat | matplotlib-Export als PNG/PDF (kein Screenshot) |

Alle Notebooks importieren aus `utils/` — so sind Daten-Split und Metriken
für alle Modelle direkt vergleichbar.

## Abhängigkeiten

| Paket | Version |
|-------|---------|
| Python | 3.13 (**nicht** 3.14+, TensorFlow-Inkompatibilität) |
| numpy | ≥ 1.24 |
| pandas | ≥ 2.0 |
| matplotlib | ≥ 3.5 |
| seaborn | ≥ 0.12 |
| scikit-learn | ≥ 1.0 |
| tensorflow | ≥ 2.16 |

## Abgabe

**Alle Gruppenmitglieder** laden ihr individuelles e-Portfolio hoch:
(dafür existiert ein vorgefertigtes (Logbuch_Template.md) dieses einmal kopieren und dann in den Orner packen) 
```
KI1_308_<Nachname>_Portfolio.pdf
```

**Sprecherin** erstellt zusätzlich die Code-ZIP und lädt sie hoch:

```bash
bash portfolio/create_submission_zip.sh
# Ausgabe: KI1_308_Code.zip
```

Beide Dateien werden auf **Stud.IP in den vorgesehenen Abgabeordner** hochgeladen.

## Repository

GitLab: https://github.com/FlorianAdamczyk/ki-308

