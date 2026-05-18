import pandas as pd

def load_data():
    return pd.read_csv("data/student_info.csv")


if __name__ == "__main__":
    df = load_data()

    print("----- BASIC DATA INFO -----")
    print(df.info())

    print("\n----- MISSING VALUES -----")
    print(df.isnull().sum())

    print("\n----- STATISTICAL SUMMARY -----")
    print(df.describe())

    print("\n----- TARGET INSPECTION (CGPA) -----")
    print(df['What is your current CGPA?'].describe())
    
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def load_data():
    return pd.read_csv("data/student_info.csv")


def preprocess_data(df):
    """
    Perform preprocessing:
    - Create target variable
    - Handle missing values
    - Encode categorical features
    - Split train and test data
    """

    # -------------------------------
    # 1. Create Target Variable
    # Academic Risk: CGPA < 3.0 → 1, else 0
    # -------------------------------
    df['Academic_Risk'] = df['What is your current CGPA?'].apply(
        lambda x: 1 if x < 3.0 else 0
    )

    # -------------------------------
    # 2. Remove Leakage Columns
    # -------------------------------
    df = df.drop([
        'What is your current CGPA?',
        'What was your previous SGPA?'
    ], axis=1)

    # -------------------------------
    # 3. Handle Missing Values
    # -------------------------------
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(include='object').columns

    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    # -------------------------------
    # 4. One-Hot Encode Categorical Data
    # -------------------------------
    df = pd.get_dummies(df, drop_first=True)

    # -------------------------------
    # 5. Feature–Target Split
    # -------------------------------
    X = df.drop('Academic_Risk', axis=1)
    y = df['Academic_Risk']

    # -------------------------------
    # 6. Train–Test Split
    # -------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("Preprocessing completed successfully ✅")
    print("Training data shape:", X_train.shape)
    print("Testing data shape:", X_test.shape)
    print("\nClass distribution (Training set):")
    print(y_train.value_counts(normalize=True))
