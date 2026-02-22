"""
Datenlade- und Bereinigungsmodul für den California Housing Datensatz.

Einheitlicher Daten-Split und Cleaning für alle Teammitglieder,
damit die Ergebnisse direkt vergleichbar sind.

Vorlage: HA10.ipynb (Cut-offs + 98%-Quantil-Outlier-Entfernung)
"""

import numpy as np
import pandas as pd
from typing import Union
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Fester Random State für Reproduzierbarkeit über alle Notebooks
RANDOM_STATE = 42
TEST_SIZE = 0.2
QUANTILE_THRESHOLD = 0.98


def load_raw_data() -> pd.DataFrame:
    """Lade den California Housing Datensatz als DataFrame.

    Returns:
        pd.DataFrame mit allen 8 Features + Zielvariable 'MedHouseVal'.
    """
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df["MedHouseVal"] = housing.target
    return df


def clean_data(df: pd.DataFrame, quantile: float = QUANTILE_THRESHOLD) -> pd.DataFrame:
    """Bereinige den Datensatz: Cut-offs und Outlier entfernen.

    1. Entferne Cut-off-Werte bei MedHouseVal (= 5.001) und HouseAge (= 52.0)
    2. Entferne Outlier über dem 98%-Quantil bei AveRooms, AveBedrms, Population, AveOccup

    Args:
        df: Roher DataFrame.
        quantile: Quantil-Schwelle für Outlier-Entfernung (Standard: 0.98).

    Returns:
        Bereinigter DataFrame.
    """
    df_clean = df[
        (df["MedHouseVal"] < df["MedHouseVal"].max())
        & (df["HouseAge"] < df["HouseAge"].max())
    ].copy()

    df_clean = df_clean[
        (df_clean["AveRooms"] < df_clean["AveRooms"].quantile(quantile))
        & (df_clean["AveBedrms"] < df_clean["AveBedrms"].quantile(quantile))
        & (df_clean["Population"] < df_clean["Population"].quantile(quantile))
        & (df_clean["AveOccup"] < df_clean["AveOccup"].quantile(quantile))
    ].copy()

    return df_clean


def load_and_clean_data(quantile: float = QUANTILE_THRESHOLD) -> pd.DataFrame:
    """Lade und bereinige den California Housing Datensatz in einem Schritt.

    Args:
        quantile: Quantil-Schwelle für Outlier-Entfernung.

    Returns:
        Bereinigter DataFrame.
    """
    df = load_raw_data()
    return clean_data(df, quantile=quantile)


def get_train_test_split(
    df: pd.DataFrame | None = None,
    target_col: str = "MedHouseVal",
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
    scaler: str | None = None,
):
    """Erstelle einheitlichen Train/Test-Split.

    Args:
        df: DataFrame (wenn None, wird load_and_clean_data() aufgerufen).
        target_col: Name der Zielvariable.
        test_size: Anteil der Testdaten.
        random_state: Seed für Reproduzierbarkeit.
        scaler: 'minmax', 'standard' oder None.

    Returns:
        (X_train, X_test, y_train, y_test) — bei scaler werden X skaliert,
        zusätzlich wird der fitted scaler als 5. Element zurückgegeben.
    """
    if df is None:
        df = load_and_clean_data()

    X = df.drop(columns=[target_col]).values
    y = df[target_col].values
    feature_names = [c for c in df.columns if c != target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    if scaler is not None:
        if scaler == "minmax":
            sc = MinMaxScaler()
        elif scaler == "standard":
            sc = StandardScaler()
        else:
            raise ValueError(f"Unbekannter Scaler: {scaler}. Nutze 'minmax' oder 'standard'.")
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        return X_train, X_test, y_train, y_test, sc, feature_names

    return X_train, X_test, y_train, y_test, feature_names




def Min_Max_Scaler(input: Union[pd.DataFrame, np.ndarray], min_val: float = 0.0, max_val: float = 1.0) -> Union[pd.DataFrame, np.ndarray]:
    """Skaliere Datensatz mit Min-Max-Scaler.

    Args:
        input: DataFrame oder NumPy-Array mit dem zu skalierendem Datensatz.
        min_val: Minimaler Wert nach Skalierung.
        max_val: Maximaler Wert nach Skalierung.


    Returns:
        Skaliertes DataFrame oder NumPy-Array mit denselben Dimensionen und Datentyp wie input.
    """
 
    input = input.copy()

    scaler = MinMaxScaler(feature_range=(min_val, max_val))

    if isinstance(input, pd.DataFrame):
        features = input.iloc[:, :-1]
        target_feature = input.iloc[:, -1]
        
        x_scaled = scaler.fit_transform(features)
        x_scaled_df = pd.DataFrame(x_scaled, columns=input.columns[:-1])
        y_df = pd.DataFrame(target_feature, columns=[input.columns[-1]])
        output_df = pd.concat([x_scaled_df, y_df], axis=1)
        return output_df
    
    if isinstance(input, np.ndarray):
        features = input[:, :-1]
        target_feature = input[:, -1].reshape(-1, 1)
        
        x_scaled = scaler.fit_transform(features)
        output_np = np.concatenate([x_scaled, target_feature], axis=1)
        return output_np




def Feature_Min_Max_Scaler(input: pd.DataFrame, feature: str, min_val: float = 0.0, max_val: float = 1.0) -> pd.DataFrame:
    """Skaliere einzelnes Feature mit Min-Max-Scaler.

    Args:
        input: DataFrame mit dem zu skalierendem Datensatz.
        target_feature: Name des Features, das skaliert werden soll.
        min_val: Minimaler Wert nach Skalierung.
        max_val: Maximaler Wert nach Skalierung.


    Returns:
        Skaliertes NumPy-Array aus dem target_feature und dem durchschnittlichem Hauspreis.
    """
    input = input.copy()

    if not isinstance(input, pd.DataFrame):
        raise TypeError("Input muss ein DataFrame sein, um Feature_Min_Max_Scaler zu verwenden.")

    values = input[[feature]].values

    scaler = MinMaxScaler(feature_range=(min_val, max_val))    
    x_scaled = scaler.fit_transform(values)
    input[feature] = x_scaled
    return input
        
        


def Standard_Scaler(input: Union[pd.DataFrame, np.ndarray]) -> Union[pd.DataFrame, np.ndarray]:
    """Skaliere Datensatz mit StandardScaler.

    Args:
        input: DataFrame oder NumPy-Array mit dem zu skalierendem Datensatz.

    Returns:
        Skaliertes DataFrame oder NumPy-Array mit denselben Dimensionen und Datentyp wie input.
    """
    
    input = input.copy()

    scaler = StandardScaler()

    if isinstance(input, pd.DataFrame):
        features = input.iloc[:, :-1]
        target_feature = input.iloc[:, -1]
        
        x_scaled = scaler.fit_transform(features)
        x_scaled_df = pd.DataFrame(x_scaled, columns=input.columns[:-1])
        y_df = pd.DataFrame(target_feature, columns=[input.columns[-1]])
        output_df = pd.concat([x_scaled_df, y_df], axis=1)
        return output_df
    
    if isinstance(input, np.ndarray):
        features = input[:, :-1]
        target_feature = input[:, -1].reshape(-1, 1)
        
        x_scaled = scaler.fit_transform(features)
        output_np = np.concatenate([x_scaled, target_feature], axis=1)
        return output_np