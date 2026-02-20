"""
Visualisierungsfunktionen für das KI1-Projekt 308.

Einheitliche Plots für alle Notebooks — Abbildungen werden als Vektorgrafik
exportiert (kein Screenshot!) gemäß Aufgabenstellung.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"


def save_fig(fig, name: str, dpi: int = 150):
    """Speichere Abbildung als PNG und PDF in results/."""
    RESULTS_DIR.mkdir(exist_ok=True)
    fig.savefig(RESULTS_DIR / f"{name}.png", dpi=dpi, bbox_inches="tight")
    fig.savefig(RESULTS_DIR / f"{name}.pdf", bbox_inches="tight")
    print(f"Gespeichert: results/{name}.png und results/{name}.pdf")


def plot_predicted_vs_actual(y_true, y_pred, title: str = "Predicted vs. Actual",
                              ax=None, save_name: str | None = None):
    """Scatterplot: Vorhersage gegen tatsächlichen Wert mit Diagonale.

    Args:
        y_true: Tatsächliche Werte.
        y_pred: Vorhergesagte Werte.
        title: Titel des Plots.
        ax: Matplotlib Axes (optional, sonst neue Figure).
        save_name: Dateiname zum Speichern (optional).
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 7))
    else:
        fig = ax.get_figure()

    ax.scatter(y_true, y_pred, alpha=0.3, s=10, edgecolors="none")
    lims = [
        min(y_true.min(), y_pred.min()) - 0.1,
        max(y_true.max(), y_pred.max()) + 0.1,
    ]
    ax.plot(lims, lims, "r--", linewidth=1.5, label="Ideal")
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_xlabel("Tatsächlicher Hauspreis (MedHouseVal)")
    ax.set_ylabel("Vorhergesagter Hauspreis")
    ax.set_title(title)
    ax.legend()
    ax.set_aspect("equal")

    if save_name:
        save_fig(fig, save_name)

    return fig, ax


def plot_residuals(y_true, y_pred, title: str = "Residuen",
                   ax=None, save_name: str | None = None):
    """Residuenplot: Vorhersage vs. Fehler.

    Args:
        y_true: Tatsächliche Werte.
        y_pred: Vorhergesagte Werte.
        title: Titel des Plots.
        ax: Matplotlib Axes (optional).
        save_name: Dateiname zum Speichern (optional).
    """
    residuals = y_true - y_pred
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    else:
        fig = ax.get_figure()

    ax.scatter(y_pred, residuals, alpha=0.3, s=10, edgecolors="none")
    ax.axhline(y=0, color="r", linestyle="--", linewidth=1.5)
    ax.set_xlabel("Vorhergesagter Hauspreis")
    ax.set_ylabel("Residuum (Actual - Predicted)")
    ax.set_title(title)

    if save_name:
        save_fig(fig, save_name)

    return fig, ax


def plot_feature_importances(importances, feature_names, title: str = "Feature Importances",
                              ax=None, save_name: str | None = None):
    """Horizontales Balkendiagramm für Feature-Wichtigkeiten.

    Args:
        importances: Array der Wichtigkeiten.
        feature_names: Liste der Feature-Namen.
        title: Titel.
        ax: Matplotlib Axes (optional).
        save_name: Dateiname zum Speichern (optional).
    """
    idx = np.argsort(importances)
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    else:
        fig = ax.get_figure()

    ax.barh(range(len(idx)), importances[idx])
    ax.set_yticks(range(len(idx)))
    ax.set_yticklabels([feature_names[i] for i in idx])
    ax.set_xlabel("Importance")
    ax.set_title(title)

    if save_name:
        save_fig(fig, save_name)

    return fig, ax


def plot_correlation_heatmap(df, title: str = "Korrelationsmatrix",
                              save_name: str | None = None):
    """Seaborn-Heatmap der Korrelationsmatrix.

    Args:
        df: DataFrame mit numerischen Spalten.
        title: Titel.
        save_name: Dateiname zum Speichern (optional).
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
                center=0, square=True, ax=ax)
    ax.set_title(title)

    if save_name:
        save_fig(fig, save_name)

    return fig, ax


def plot_histograms(df, bins: int = 40, save_name: str | None = None):
    """Histogramme aller Spalten eines DataFrames.

    Args:
        df: DataFrame.
        bins: Anzahl der Bins.
        save_name: Dateiname zum Speichern (optional).
    """
    n_cols = len(df.columns)
    n_rows = (n_cols + 2) // 3
    fig, axes = plt.subplots(n_rows, 3, figsize=(15, 4 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(df.columns):
        axes[i].hist(df[col], bins=bins, edgecolor="black", alpha=0.7)
        axes[i].set_title(col)
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Häufigkeit")

    # Leere Subplots ausblenden
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle("Verteilung aller Features", fontsize=14, y=1.02)
    fig.tight_layout()

    if save_name:
        save_fig(fig, save_name)

    return fig, axes


def plot_features_vs_target(df, target_col: str = "MedHouseVal",
                             save_name: str | None = None):
    """Scatterplots jedes Features gegen die Zielvariable.

    Args:
        df: DataFrame mit Features und Target.
        target_col: Name der Zielvariable.
        save_name: Dateiname zum Speichern (optional).
    """
    features = [c for c in df.columns if c != target_col]
    n_features = len(features)
    n_rows = (n_features + 2) // 3
    fig, axes = plt.subplots(n_rows, 3, figsize=(15, 4 * n_rows))
    axes = axes.flatten()

    for i, feat in enumerate(features):
        axes[i].scatter(df[feat], df[target_col], alpha=0.1, s=5, edgecolors="none")
        axes[i].set_xlabel(feat)
        axes[i].set_ylabel(target_col)
        axes[i].set_title(f"{feat} vs. {target_col}")

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle("Features vs. Hauspreis", fontsize=14, y=1.02)
    fig.tight_layout()

    if save_name:
        save_fig(fig, save_name)

    return fig, axes
