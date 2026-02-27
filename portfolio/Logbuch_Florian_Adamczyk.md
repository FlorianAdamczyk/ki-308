# Logbuch – Florian Adamczyk
**Matrikelnummer:** 8105234  
**Kurs:** KI 1 – Projekt, WS 2025/26  
**Gruppe:** 308  

---

## Eintrag 1 – Recherche: Git-Workflow & nbstripout
**Datum:** 11.02.2026  
**Zeitraum:** ca. 16:00 – 20:00 Uhr (Selbststudium, im Anschluss an Gruppentreffen 1)  
**Gesamtzeit: ca. 4 h**

### Arbeitsschritte
- Im Gruppentreffen 1 (11.02.) wurde u. a. die Nutzung von Git/GitHub beschlossen. Im Anschluss habe ich eigenständig recherchiert, wie man Jupyter Notebooks sinnvoll versionieren kann. *(ca. 30 min)*
- **Problem identifiziert:** Notebook-Outputs und Metadaten erzeugen unnötige Merge-Konflikte und erschweren Code-Reviews erheblich. Lektüre von Blogposts und Stack-Overflow-Threads zu Jupyter + Git. *(ca. 45 min)*
- **Lösung gefunden: `nbstripout`** — ein Tool, das Zell-Outputs automatisch vor jedem Commit entfernt (Git-Hook). Offizielle Dokumentation und GitHub-Repo gelesen, mehrere Alternativen verglichen (`nbconvert --clear-output`, manuelle Pre-Commit-Hooks). *(ca. 45 min)*
- GitHub-Repository initial eingerichtet (`git init`, Remote angelegt, README aus dem GitLab-Kursrepo übernommen). *(ca. 30 min)*
- `nbstripout` lokal installiert und als Git-Hook ausprobiert; initialer Testcommit mit einem Notebook erstellt und Diff auf saubere Ausgabe geprüft. *(ca. 30 min)*
- Dokumentation in `Ressources.md` erstellt: Installationsanleitung, Einrichtung als Git-Hook, Links zu den relevanten Repositories (Arbeitsrepo, Kurs-GitLab, Vorlesungsfolien, Lösungen). *(ca. 60 min)*

### Entscheidungen
| Entscheidung | Begründung |
|---|---|
| `nbstripout` als verpflichtender Git-Hook | Vermeidet Merge-Konflikte durch Notebook-Outputs |
| Zentrale Dokumentation in `Ressources.md` | Alle Teammitglieder können Installationsschritte dort nachschlagen |

### Schwierigkeiten
- Keine direkten Schwierigkeiten; die Recherche war erfolgreich.

---

## Eintrag 2 – Erste Repository-Strukturierung
**Datum:** 17.02.2026  
**Zeitraum:** Im Anschluss an Gruppentreffen 2, ca. 3 h  
**Gesamtzeit: ca. 3 h**

### Arbeitsschritte
- Wie am Gruppentreffen 2 am 17.02. besprochen: `nbstripout` im Team als Standard vorgestellt; Fragen der anderen Teammitglieder zur Installation beantwortet. *(ca. 30 min)*
- `PDFs/`-Ordner im Repository angelegt, Aufgabenstellung (PDF) heruntergeladen und eingecheckt. *(ca. 20 min)*
- Alte Test-Dateien und überflüssige Artefakte aus der initialen Repo-Einrichtung aufgeräumt (Branches bereinigt, überflüssige Commits analysiert). *(ca. 45 min)*
- `.gitattributes` konfiguriert, um Notebooks korrekt mit `nbstripout` zu behandeln; Konfiguration durch einen Test-Commit verifiziert. *(ca. 45 min)*
- **Meine Aufgabe bis zum nächsten Treffen** (wie am Gruppentreffen besprochen): Datenbereinigung und Datenanalyse gemeinsam mit Kolja — erste Planung der Vorgehensweise notiert. *(ca. 40 min)*

### Schwierigkeiten
- Keine nennenswerten Probleme.

---

## Eintrag 3 – Projektstruktur, Utils-Modul, Notebooks & erste Modelle
**Datum:** 20.02.2026  
**Zeitraum:** ca. 07:00 – 22:00 Uhr (ganztägig, inkl. Gruppentreffen 3 von 9:00–11:30 Uhr)  
**Gesamtzeit: ca. 35 h** *(verteilt auf 20.02. und nachfolgende Abende bis 25.02.)*

Dies war der zentrale Arbeitsblock, in dem ich die gesamte Projektgrundstruktur aufgebaut habe. Ausgangspunkt waren die Aufgaben, die am Gruppentreffen 2 (17.02.) vereinbart wurden: Datenbereinigung und Datenanalyse. Im Zuge dessen habe ich über die reine Datenbereinigung hinaus einen vollständigen Masterplan sowie die gemeinsame Code-Infrastruktur für das gesamte Projekt erstellt.

### Arbeitsschritte

#### 0. Gruppentreffen 3 *(ca. 2,5 h)*
- Teilnahme am Gruppentreffen 3 (09:00–11:30 Uhr): Präsentation des bisherigen Stands, Diskussion der Aufgabenverteilung P1–P5, Abstimmung über Projektstruktur und Zeitplan. *(ca. 2,5 h)*

#### 1. Masterplan und Aufgabenverteilung *(ca. 3 h)*
- **`Masterplan.md`** geschrieben: Projektphasen (Setup → EDA/Baseline → Individuelle Methoden → Vertiefung → Portfolio), Zuordnung der Methoden zu fünf Personen (P1–P5), Bewertungshinweise, Projektstruktur. *(ca. 90 min)*
- **`Aufgabenübersicht.md`** erstellt: Für jede der fünf Aufgaben eine kurze Beschreibung (Was macht man? Schwierigkeiten? Schwierigkeitsgrad?), damit sich die Teammitglieder orientiert eine Aufgabe auswählen können. *(ca. 60 min)*
- Die Idee hinter der Aufteilung: Jede Person bearbeitet einen eigenen methodischen Schwerpunkt (Regularisierung, Decision Trees, Ensemble, kNN, Neuronales Netz), sodass sich die individuellen Logbücher inhaltlich unterscheiden — wichtig für die 40 %-Bewertung der Logbuch-Zusammenfassung laut Aufgabenstellung. Konzept schriftlich ausgearbeitet und im Masterplan dokumentiert. *(ca. 30 min)*

#### 2. Python-Umgebung & TensorFlow *(ca. 3 h)*
- **Python-Versionsproblem entdeckt:** Am Gruppentreffen 1 hatten wir Python 3.14.3 vereinbart. Beim Versuch, TensorFlow zu installieren, scheiterte `pip install tensorflow` — es existieren keine Wheels für Python 3.14. TensorFlow unterstützt offiziell bis Python 3.13 (ab TF 2.18). Fehleranalyse und Recherche der offiziellen TF-Kompatibilitätsmatrix. *(ca. 60 min)*
- **Lösung:** Auf meinem System (Arch Linux) war `python3.13` bereits installiert. Virtuelle Umgebung neu erstellt:
  ```bash
  python3.13 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
  *(ca. 30 min)*
- TensorFlow 2.20.0 erfolgreich installiert und mit einem kurzen Testskript verifiziert (`tf.__version__`, einfaches Dense-Modell). *(ca. 30 min)*
- **`requirements.txt`** erstellt mit allen benötigten Paketen: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`, `jupyter`, `ipykernel`, `nbstripout`. Versionen recherchiert und auf Kompatibilität geprüft. *(ca. 60 min)*

#### 3. Gemeinsames Utils-Modul (`utils/`) *(ca. 12 h)*
Damit alle Teammitglieder auf identischen Daten und einheitlichen Metriken arbeiten, habe ich ein zentrales Python-Modul erstellt:

- **`utils/data.py`** — Laden des California-Housing-Datensatzes, Datenbereinigung (Cut-offs bei `MedHouseVal = 5.001` und `HouseAge = 52`, Ausreißer über 98. Perzentil bei `AveRooms`, `AveBedrms`, `Population`, `AveOccup`), standardisierter Train/Test-Split (80/20, `random_state=42`), optionale Skalierung (MinMax / Standard). *(ca. 4 h)*
  - Die Bereinigungsschritte orientieren sich an den Vorlesungsunterlagen (Blatt 9/10 Lösung). Lösung nachvollzogen, Cut-off-Werte reproduziert und im Code kommentiert. *(in obigen 4 h enthalten)*
- **`utils/evaluation.py`** — Einheitliche Auswertung: R², MAE, RMSE für Train- und Testdaten. Globale Ergebnis-Sammlung (`add_result()`, `compare_models()`), damit am Ende eine gemeinsame Vergleichstabelle über alle Modelle entsteht. *(ca. 2 h)*
- **`utils/plotting.py`** — Standardisierte Visualisierungen: Predicted-vs-Actual-Plot, Residuenplot, Feature-Importances, Korrelations-Heatmap, Histogramme, Features-vs-Target-Scatterplots. Alle Plots werden automatisch als PNG und PDF nach `results/` exportiert (wie in der Aufgabenstellung gefordert: keine Screenshots). Design und Formatierung iterativ angepasst. *(ca. 5 h)*
- **`utils/__init__.py`** — Re-Export der wichtigsten Funktionen für einfachen Import in den Notebooks. Testen aller Importe in einem Scratch-Notebook. *(ca. 60 min)*

#### 4. Notebooks erstellt *(ca. 8 h)*
Acht Notebooks angelegt, die den Phasen des Masterplans entsprechen. Für jedes Notebook: Grundstruktur aufgebaut, Imports eingerichtet, `sys.path`-Eintrag gesetzt, Datenladen-Zelle vorbereitet, Platzhalter-Abschnitte für Methodik und Auswertung angelegt, abschließende Ergebniszelle mit `add_result()`-Aufruf vorbereitet. *(ca. 1 h pro Notebook)*

| Notebook | Inhalt |
|---|---|
| `0a_EDA.ipynb` | Explorative Datenanalyse: Histogramme, Scatterplots, Korrelationsheatmap (roh und bereinigt) |
| `0b_Baseline_Lineare_Regression.ipynb` | Lineare Regression als Referenzmodell (alle Features, nur MedInc), Pred-vs-Actual, Residuen |
| `0c_Scaling_Data.ipynb` | Vergleich verschiedener Skalierungsmethoden (MinMax, Standard) mit Visualisierung |
| `01_LASSO_Ridge.ipynb` | P1: LassoCV/RidgeCV mit/ohne Skalierung, polynomiale Features |
| `02_Decision_Tree.ipynb` | P2: Entscheidungsbaum, Depth-Tuning, Pruning, Feature Importances |
| `03_Ensemble.ipynb` | P3: Random Forest, Gradient Boosting, GridSearchCV |
| `04_kNN_Regression.ipynb` | P4: kNN-Regression, Skalierungseffekt, k-Optimierung |
| `05_Neural_Network.ipynb` | P5: TensorFlow/Keras NN, verschiedene Architekturen, Vergleich mit LR |

- Jedes Notebook importiert die gemeinsamen Funktionen aus `utils/` und arbeitet auf demselben bereinigten Datensatz mit identischem Split. *(in obigen 8 h enthalten)*
- Die Notebooks sind inhaltlich so vorbereitet, dass jedes Teammitglied direkt mit seinem Schwerpunkt starten kann — die Grundstruktur (Daten laden, Ergebnis speichern, Plots exportieren) ist in jedem Notebook bereits angelegt. *(in obigen 8 h enthalten)*

#### 5. EDA & Baseline durchgeführt *(ca. 5 h)*
- **EDA (`0a_EDA.ipynb`):** Rohdaten untersucht (20.640 Samples, 8 Features, keine fehlenden Werte), Histogramme vor und nach Bereinigung erstellt, Korrelationsheatmap zeigt stärkste Korrelation zwischen `MedInc` und `MedHouseVal`. Nach Bereinigung verbleiben ca. 17.386 Samples. Plots exportiert und Interpretation schriftlich festgehalten. *(ca. 3 h)*
- **Baseline (`0b_Baseline_Lineare_Regression.ipynb`):** Lineare Regression auf allen 8 Features: **R² Test ≈ 0.633**, MAE ≈ 0.434, RMSE ≈ 0.578. Residuenplot zeigt systematische Muster → nicht-lineare Zusammenhänge, die lineare Regression nicht erfassen kann. Interpretation und Kommentare im Notebook ergänzt. *(ca. 2 h)*

#### 6. nbstripout & .gitignore-Konfiguration *(ca. 2 h)*
- Mehrere Versuche, `nbstripout` und `.gitignore` korrekt zu konfigurieren. `nbstripout` funktionierte zunächst nicht zuverlässig als Git-Hook (Outputs wurden trotzdem committet). Problem lag an fehlender `.gitattributes`-Konfiguration. Debugging und erneute Einrichtung. *(ca. 90 min)*
- `.gitignore` für `results/*.pdf` eingerichtet, dann wieder angepasst, da einige PDFs doch versioniert werden sollten. Mehrere Commits nötig. *(ca. 30 min)*

### Entscheidungen
| Entscheidung | Begründung |
|---|---|
| Python 3.13 statt 3.14 | TensorFlow-Inkompatibilität mit Python 3.14 |
| TensorFlow 2.20.0 | Neueste Version, kompatibel mit Python 3.13 |
| `RANDOM_STATE = 42` (global) | Reproduzierbare Ergebnisse, identischer Split für alle Teammitglieder |
| Test-Split 20 % | Standard-Aufteilung, wie in Vorlesung verwendet |
| Ausreißer-Grenze: 98. Perzentil | Orientierung an der Vorlesung (Blatt 9/10 Lösung) |
| Getrennte Notebooks pro Methode | Weniger Merge-Konflikte in Git, klare Zuordnung zu Personen |
| Gemeinsames `utils/`-Modul | Einheitliche Daten, Metriken und Plots für alle Teammitglieder |

### Schwierigkeiten
- **TensorFlow + Python 3.14:** Keine kompatiblen Wheels verfügbar. Lösung: Wechsel auf Python 3.13.
- **`utils` als lokales Modul:** `requirements.txt` enthielt zunächst `utils>=0.1.0` (ein fremdes PyPI-Paket). Entfernt — das lokale `utils/`-Modul wird über den Notebook-internen `sys.path`-Eintrag eingebunden.
- **`nbstripout`-Konfiguration:** Mehrere Anläufe nötig, bis der Git-Hook zuverlässig funktionierte.
- **`.gitignore` für PDFs:** Zunächst alle PDFs ignoriert, dann einzelne wieder freigegeben — erforderte mehrere Commits, um die gewünschte Konfiguration zu erreichen.

### Offene Fragen
- Aufgabenverteilung P1–P5 steht noch nicht fest; soll im nächsten Gruppentreffen besprochen werden.

---

## Eintrag 4 – Python-Versionskonflikt auf macOS (Intel)
**Datum:** 20.02.2026  
**Zeitraum:** Während und nach Gruppentreffen 3 (9:00–11:30 Uhr)  
**Gesamtzeit: ca. 2 h**

### Arbeitsschritte
- Während des Gruppentreffens 3 am 20.02. hat Kolja versucht, die Umgebung auf seinem Intel-Mac einzurichten. Problem live beobachtet und gemeinsam analysiert. *(ca. 30 min)*
- **Problem:** TensorFlow ab Version 2.17 unterstützt keine Intel-Macs mehr (nur Apple Silicon oder Linux/Windows). Python 3.13 + TensorFlow 2.20 (mein Setup auf Arch Linux) lässt sich auf Koljas Mac nicht installieren. Recherche der offiziellen TF-Release-Notes und PyPI-Paketmetadaten. *(ca. 45 min)*
- Kolja hat als Workaround die `requirements.txt` auf Python 3.11 und TensorFlow 2.16.2 angepasst — diese Version unterstützt noch Intel-Macs. Änderung geprüft und im Repository nachvollzogen. *(ca. 20 min)*
- **Offene Entscheidung:** Es steht noch aus, ob wir einheitlich auf Python 3.11 + TF 2.16 wechseln oder ob unterschiedliche lokale Umgebungen akzeptiert werden. Optionen schriftlich festgehalten und Vor-/Nachteile abgewogen. *(ca. 25 min)*

### Schwierigkeiten
- Inkompatibilität von TensorFlow ≥ 2.17 mit macOS auf Intel-Prozessoren.
- Falls auf TF 2.16 gewechselt wird, muss geprüft werden, ob alle Notebook-Features kompatibel bleiben.

### Nächster Schritt
- Klärung der Python-/TensorFlow-Version im nächsten Gruppentreffen.
- Mögliche Alternativen: JLU JupyterHub für rechenintensive Aufgaben (wurde bereits am Gruppentreffen 2 am 17.02. als Option angesprochen).

---

## Eintrag 5 – Auswertung und derzeitiges Fazit: Neuronales Netz (`05_Neural_Network.ipynb`)
**Datum:** 23.02.–26.02.2026  
**Zeitraum:** Selbststudium, verteilt auf mehrere Abende  
**Gesamtzeit: ca. 11 h**

### Arbeitsschritte
- Kursunterlagen zu Neuronalen Netzen (Kapitel 3.3, Blatt 11/12) sowie TensorFlow/Keras-Dokumentation zur Auffrischung durchgelesen. *(ca. 90 min)*
- Notebook-Struktur aufgebaut: Abschnitte für Datenloading, Modellarchitektur, Training, Auswertung und Fazit angelegt; Imports und `sys.path`-Eintrag eingerichtet. *(ca. 45 min)*
- Grundmodell (einzelnes Dense-Layer) implementiert, kompiliert und trainiert; erste Metriken abgelesen und mit der Baseline verglichen. *(ca. 60 min)*
- Verschiedene Architekturen (Modell 1–5) systematisch implementiert und getestet: schrittweise tiefere Netze ([64], [128,64], [128,64,32], [128,64,32,16], [128,64,32,16] + Dropout). Pro Modell: Training über 300 Epochen, Loss-Kurven betrachtet, R² / MAE / RMSE notiert. *(ca. 4 h)*
- Dropout-Regularisierung eingebaut; Overfitting-Verhalten von Modell 3 vs. Modell 5 analysiert und im Notebook kommentiert. *(ca. 45 min)*
- **Zusammenfassungszelle in `05_Neural_Network.ipynb` ausgefüllt:** Die zuvor mit *„eintragen"* platzhalterten Felder in der Vergleichstabelle (Abschnitt 7.10) wurden mit den tatsächlichen Messwerten aus den Notebook-Outputs befüllt. *(ca. 30 min)*
- **Ergebnisse abgelesen** aus den Zell-Outputs der bereits ausgeführten Modellzellen:

| Aspekt | Lineare Regression | Bestes NN ([128,64,32,16] + Dropout) |
|---|---|---|
| R² Test | 0.6326 | 0.7795 |
| MAE Test | 0.4341 | 0.3066 |
| Trainingszeit | < 1 s | ~1–2 min (300 Epochs, CPU) |

- **Fazit formuliert:** Das NN übertrifft die lineare Regression um ~18 Prozentpunkte R² und ~0.13 MAE (in 100.000 USD). Als Begründung wurde der nichtlineare Charakter des California-Housing-Datensatzes herausgearbeitet. Grenzen (Overfitting ohne Regularisierung, fehlende Interpretierbarkeit, hoher Tuning-Aufwand) sowie mögliche Verbesserungen (Early Stopping, LR-Scheduling, Ensembling) wurden dokumentiert. *(ca. 90 min)*
- Logbuch-Eintrag verfasst, Ergebnisse strukturiert zusammengefasst, Entscheidungen begründet. *(ca. 60 min)*

### Entscheidungen
| Entscheidung | Begründung |
|---|---|
| Modell 5 ([128,64,32,16] + Dropout) als bestes Modell | Höchster R² Test (0.7795) bei gleichzeitig geringster Generalisierungslücke dank Dropout |
| Overfitting-Vergleich Modell 3 vs. Modell 5 explizit erwähnt | Zeigt konkret den Nutzen von Dropout-Regularisierung |

### Schwierigkeiten
- Keine; Metrikwerte lagen bereits als Notebook-Output vor.

---

## Zeitübersicht (Gesamtprojekt)

| Eintrag | Datum | Tätigkeit | Zeit |
|---|---|---|---|
| 1 | 11.02.2026 | Recherche Git-Workflow & nbstripout | ca. 4 h |
| 2 | 17.02.2026 | Repository-Strukturierung | ca. 3 h |
| 3 | 20.–25.02.2026 | Projektstruktur, Utils, Notebooks, EDA, Baseline | ca. 35 h |
| 4 | 20.02.2026 | Python-Versionskonflikt macOS | ca. 2 h |
| 5 | 23.–26.02.2026 | Neuronales Netz & Auswertung | ca. 11 h |
| **Gesamt** | | | **ca. 55 h** |
