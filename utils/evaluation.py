"""
Evaluationsmodul für das KI1-Projekt 308.

Einheitliche Metriken für alle Modelle:
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
"""

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


def evaluate_model(model, X_train, X_test, y_train, y_test, model_name: str = "Modell"):
    """Evaluiere ein trainiertes Modell auf Train- und Testdaten.

    Args:
        model: Trainiertes sklearn-kompatibles Modell (muss .predict() haben).
        X_train, X_test: Feature-Matrizen.
        y_train, y_test: Zielvariablen.
        model_name: Name für die Ausgabe.

    Returns:
        dict mit allen Metriken.
    """
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    results = {
        "Modell": model_name,
        "R² Train": r2_score(y_train, y_train_pred),
        "R² Test": r2_score(y_test, y_test_pred),
        "MAE Train": mean_absolute_error(y_train, y_train_pred),
        "MAE Test": mean_absolute_error(y_test, y_test_pred),
        "RMSE Train": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "RMSE Test": np.sqrt(mean_squared_error(y_test, y_test_pred)),
    }

    print(f"\n{'='*50}")
    print(f"  {model_name}")
    print(f"{'='*50}")
    print(f"  R² Score:  Train = {results['R² Train']:.4f}  |  Test = {results['R² Test']:.4f}")
    print(f"  MAE:       Train = {results['MAE Train']:.4f}  |  Test = {results['MAE Test']:.4f}")
    print(f"  RMSE:      Train = {results['RMSE Train']:.4f}  |  Test = {results['RMSE Test']:.4f}")
    print(f"{'='*50}")

    return results


def evaluate_predictions(y_train, y_train_pred, y_test, y_test_pred, model_name: str = "Modell"):
    """Evaluiere direkt aus Vorhersagen (z.B. für TensorFlow-Modelle).

    Args:
        y_train, y_test: Tatsächliche Werte.
        y_train_pred, y_test_pred: Vorhergesagte Werte.
        model_name: Name für die Ausgabe.

    Returns:
        dict mit allen Metriken.
    """
    results = {
        "Modell": model_name,
        "R² Train": r2_score(y_train, y_train_pred),
        "R² Test": r2_score(y_test, y_test_pred),
        "MAE Train": mean_absolute_error(y_train, y_train_pred),
        "MAE Test": mean_absolute_error(y_test, y_test_pred),
        "RMSE Train": np.sqrt(mean_squared_error(y_train, y_train_pred)),
        "RMSE Test": np.sqrt(mean_squared_error(y_test, y_test_pred)),
    }

    print(f"\n{'='*50}")
    print(f"  {model_name}")
    print(f"{'='*50}")
    print(f"  R² Score:  Train = {results['R² Train']:.4f}  |  Test = {results['R² Test']:.4f}")
    print(f"  MAE:       Train = {results['MAE Train']:.4f}  |  Test = {results['MAE Test']:.4f}")
    print(f"  RMSE:      Train = {results['RMSE Train']:.4f}  |  Test = {results['RMSE Test']:.4f}")
    print(f"{'='*50}")

    return results


# Globaler Speicher für Modellvergleiche
_results_list: list[dict] = []


def add_result(result: dict):
    """Füge ein Evaluationsergebnis zur Vergleichsliste hinzu."""
    _results_list.append(result)


def compare_models(results: list[dict] | None = None) -> pd.DataFrame:
    """Erstelle eine Vergleichstabelle aller evaluierten Modelle.

    Args:
        results: Liste von Ergebnis-Dicts (optional, sonst interner Speicher).

    Returns:
        pd.DataFrame mit allen Modellen und Metriken.
    """
    if results is None:
        results = _results_list

    if not results:
        print("Keine Ergebnisse vorhanden. Nutze evaluate_model() + add_result() zuerst.")
        return pd.DataFrame()

    df = pd.DataFrame(results)
    df = df.set_index("Modell")
    df = df.sort_values("R² Test", ascending=False)
    return df


def reset_results():
    """Leere die globale Ergebnisliste."""
    _results_list.clear()
