# Gruppentreffen 4

**Anwesend:** [alle / Florian, Kolja, Felix, Björn, ...]  
**Datum:** 27.02.2026  
**Uhrzeit:** 15:00 Uhr  
**Ort:** Discord

---

## Agenda

### 1. Aufgabenverteilung P1–P5 (offen seit 20.02.)
Jede Person wählt einen Methodenschwerpunkt. Zur Auswahl stehen:

| Nr. | Aufgabe | Schwierigkeit |
|-----|---------|--------------|
| P1  | Regularisierte Regression (LASSO, Ridge, polynomiale Features) | ⭐⭐ |
| P2  | Decision Tree (Pruning, Feature Importances) | ⭐⭐⭐ |
| P3  | Ensemble-Methoden (Random Forest, Gradient Boosting, GridSearchCV) | ⭐⭐⭐⭐ |
| P4  | kNN-Regression (Skalierungseffekt, k-Optimierung) | ⭐⭐ |
| P5  | Neuronales Netz (TensorFlow/Keras, Architekturen, Vergleich mit LR) | ⭐⭐⭐ |

> Hinweis: P3 (Ensemble) ist rechenintensiv — ggf. JupyterHub der JLU nutzen (s. Punkt 3).

### 2. Python-/TensorFlow-Versionskonflikt (Intel-Mac, offen seit 20.02.)
- **Problem:** TensorFlow ≥ 2.17 unterstützt keine Intel-Macs mehr. Kolja arbeitet mit Python 3.11 + TF 2.16.2, Felix mit Python 3.10.13, Florian mit Python 3.13 + TF 2.20.0.
- **Entscheidung notwendig:** Einheitliche Umgebung (Python 3.11 + TF 2.16.2) oder heterogene lokale Setups akzeptieren?
  - Option A: Alle wechseln auf Python 3.11 + TF 2.16.2 → einheitliche `requirements.txt`, einfachere Fehlersuche
  - Option B: Jede Person nutzt ihre lokale Umgebung → `requirements.txt` bleibt wie sie ist, Kompatibilität muss jeder selbst sicherstellen

### 3. JupyterHub der JLU (verschoben aus Gruppentreffen 2, 17.02.)
- Für rechenintensive Aufgaben (insbesondere P3: GridSearchCV über Random Forest / Gradient Boosting) wurde der JLU JupyterHub als Option angesprochen.
- Klären: Wer hat Zugang? Ist er für unser Projekt nutzbar?

### 4. Status-Update: Arbeitsziele aus Gruppentreffen 3 (20.02.)
- **Florian & Kolja** — Datenbereinigung und Datenanalyse: EDA (`0a_EDA.ipynb`) und Baseline (`0b_Baseline_Lineare_Regression.ipynb`) sind fertig (Florian); Status Kolja?
- **Felix** — Datentransformation (`0c_Scaling_Data.ipynb`): Status?
- **Kolja** — TensorFlow-Problem lösen: Status (s. Punkt 2)?

### 5. Nächste Schritte: Individuelle Notebooks starten
- Nach Aufgabenverteilung: Jede Person beginnt mit ihrem Methoden-Notebook.
- Gemeinsame Basis: `utils/data.py`, `utils/evaluation.py`, `utils/plotting.py` sind fertig und einsatzbereit.
- Erinnerung: `nbstripout --install` in jeder lokalen Umgebung einrichten (`.gitattributes` liegt bereits im Repo).

---

## Besprochene Punkte

- 

## Entscheidungen

| Entscheidung | Ergebnis |
|---|---|
| Aufgabenverteilung P1–P5 | |
| Python-/TF-Version (einheitlich oder heterogen) | |
| JupyterHub JLU nutzen | |

## Arbeitsziele bis zum nächsten Treffen

- 

**Nächstes Treffen:** [Datum, Uhrzeit, Ort]

---

*Protokoll erstellt am 27.02.2026*
