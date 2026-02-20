# Logbuch – Florian Adamczyk
**Matrikelnummer:** 8105234  
**Kurs:** KI 1 – Projekt, WS 2025/26  
**Gruppe:** 308  

---

## Eintrag 1 – Gruppentreffen 1
**Datum:** 11.02.2026  
**Zeitraum:** 13:30 – 15:45 Uhr  
**Anwesende:** Björn, Kolja, Florian, Felix H. (alle Mitglieder)

### Arbeitsschritte
- Gegenseitige Vorstellung aller Gruppenmitglieder
- Technische Rahmenbedingungen besprochen und abgestimmt:
  - Python-Version (zunächst 3.14.3 vereinbart, später auf 3.13 geändert – siehe Eintrag 3)
  - GitHub Education Accounts eingerichtet
  - Gemeinsames Git-Repository auf GitHub angelegt
- Gruppensprecher bestimmt
- Programmierstil abgestimmt: **funktionaler Ansatz** (Funktionen statt Klassen)
- Erste Aufgabenteilung erstellt:
  - **Florian + Kolja:** Datenbereinigung (auf Basis der Vorlesungsinhalte)
  - Weitere Aufgaben noch nicht endgültig verteilt
- Erste gemeinsame Aufgabenliste erstellt

### Entscheidungen
| Entscheidung | Ergebnis |
|---|---|
| Programmierstil | Funktional |
| Versionskontrolle | Git / GitHub |
| Python-Version (vorläufig) | 3.14.3 |
| Meine Aufgabe | Datenbereinigung (gemeinsam mit Kolja) |

### Schwierigkeiten
- Keine technischen Probleme; das Treffen diente primär der Organisation.

### Nächstes Treffen
Di. 17.02.2026, 11:00 Uhr

## Eintrag 0.5 – Git-Workflow & nbstripout-Integration
**Datum:** 11.02.2026  
**Zeitraum:** 16:00 – 18:30 Uhr (Selbststudium)  
**Anwesende / Kontext:** Eigenständige Recherche

### Arbeitsschritte
1. **Recherche zu Teammanagement und Versionskontrolle:**
   - 2–3 Stunden Studium zu Best Practices für Entwicklergruppen
   - Fokus auf Probleme bei Git-Integration mit Jupyter Notebooks
2. **Problem identifiziert:** Outputs und Metadaten von Notebooks erschweren Code-Reviews und erzeugen unnötige Merge-Konflikte
3. **Lösung gefunden: `nbstripout`**
   - Tool zur automatischen Bereinigung von Notebook-Outputs vor Commits
   - Installation und Konfiguration als Git-Hook (Pre-Commit)
4. **Dokumentation erstellt** in `Ressourcen.md`:
   - Installation via `pip install nbstripout`
   - Setup: `nbstripout --install`
   - Automatische Ausführung beim Commit
5. **Team informiert** – nbstripout wird als verpflichtender Standard etabliert

### Entscheidungen
| Entscheidung | Ergebnis |
|---|---|
| Ausgabe-Verwaltung für Notebooks | `nbstripout` (Git-Hook) |
| Dokumentation | Im Team-Repository (Ressourcen.md) |

### Schwierigkeiten
- Keine; erfolgreiche Identifikation einer etablierten Lösung

### Nächster Schritt
Alle Teamkollegen informieren, `nbstripout` lokal installieren und als Standard etablieren

---

## Eintrag 2 – Gruppentreffen 2
**Datum:** 17.02.2026  
**Zeitraum:** 11:00 – 12:30 Uhr  
**Anwesende:** Björn, Kolja, Florian, Felix H.

### Arbeitsschritte
- Besprechung des Workflows mit Jupyter Notebooks:
  - **`nbstripout`** soll verwendet werden, damit Zell-Outputs nicht automatisch committet werden
- Einführung in **VS Code** und die GitHub-Integration für alle Mitglieder
- Diskussion über den **JLU JupyterHub** für rechenintensive Modelle → Entscheidung: Punkt wird auf spätere Treffen verschoben (relevant wenn Modelltraining startet)
- **Einheitliche Code-Beschriftung** festgelegt: Kommentare und Erklärungen sollen direkt im Notebook als Python-Kommentar oder Markdown-Zelle erfolgen

### Arbeitsziele bis zum nächsten Treffen
| Person | Aufgabe |
|---|---|
| Florian + Kolja | Datenbereinigung und Datenanalyse |
| Felix | Datentransformation |

### Entscheidungen
| Entscheidung | Ergebnis |
|---|---|
| Output-Bereinigung | `nbstripout` obligatorisch vor Commits |
| Code-Kommentierung | Direkt im Notebook (Markdown oder `#`-Kommentar) |
| JupyterHub JLU | Später, wenn Modelltraining relevant wird |

### Schwierigkeiten
- Keine grundlegenden Probleme; Workflow-Details mussten noch abgestimmt werden.

### Nächstes Treffen
27.02.2026, 15:00 Uhr auf Discord

---

## Eintrag 3 – Projektstart & Python-Umgebung
**Datum:** 20.02.2026  
**Zeitraum:** Selbststudium

### Arbeitsschritte
1. **Python-Versionsproblem entdeckt:** TensorFlow ist nicht mit Python 3.14 kompatibel.  
   → Beim Versuch `pip install tensorflow` zu installieren, scheitert die Installation an fehlenden Wheels für Python 3.14.  
   → TensorFlow unterstützt offiziell bis Python 3.12/3.13 (ab v2.18 mit Python 3.13).
2. **Lösung:** Systemweit war `/usr/bin/python3.13` bereits installiert; kein gesonderter Download notwendig.
3. **Virtuelle Umgebung neu erstellt** mit Python 3.13:
   ```bash
   rm -rf .venv
   python3.13 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. **TensorFlow 2.20.0** erfolgreich installiert und getestet (`import tensorflow as tf` → OK).
5. **Projektstruktur angelegt:**
   - `utils/data.py` – Datenladen, Bereinigung, Train/Test-Split
   - `utils/evaluation.py` – einheitliche Metriken (R², MAE, RMSE) für alle Teammitglieder
   - `utils/plotting.py` – Matplotlib-Exporte (PNG + PDF) nach `results/`
6. **Notebooks erstellt** (01–07): EDA, Baseline, LASSO/Ridge, Decision Tree, Ensemble, kNN, Neuronales Netz
7. **Baseline-Modell (lineare Regression) berechnet:**
   - R² Test = **0.633**, MAE = **0.434**, RMSE = **0.578**
   - Datensatz nach Bereinigung: 17.386 Samples

### Entscheidungen
| Entscheidung | Ergebnis |
|---|---|
| Python-Version | 3.13 (statt 3.14 – TF-Inkompatibilität) |
| TensorFlow-Version | 2.20.0 |
| RANDOM_STATE | 42 (alle Notebooks) |
| Test-Split | 20 % |
| Ausreißer-Grenze | 98. Perzentil (AveRooms, AveBedrms, Population, AveOccup) |

### Schwierigkeiten
- **TensorFlow + Python 3.14:** pip findet keine kompatiblen Wheels. Lösung: Python 3.13 verwenden (bereits systemweit installiert).  
- **`utils` als lokales Modul:** Die `requirements.txt` enthielt fälschlicherweise `utils>=0.1.0` (PyPI-Paket). Entfernt – das lokale `utils/`-Modul wird über `sys.path` oder `pip install -e .` eingebunden.

### Ergebnis
Vollständige Entwicklungsumgebung funktioniert. Erste Baseline steht.  
Nächster Schritt: Datenanalyse (01_EDA.ipynb) und LASSO/Ridge (03).

---

## Eintrag 4 – (Vorlage für weitere Einträge)
**Datum:** TT.MM.JJJJ  
**Zeitraum:**  
**Anwesende / Kontext:**

### Arbeitsschritte
-

### Entscheidungen
| Entscheidung | Ergebnis |
|---|---|
| | |

### Schwierigkeiten
-

### Nächstes Treffen / nächster Schritt
