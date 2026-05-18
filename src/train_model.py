# import joblib
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from imblearn.over_sampling import SMOTE

# from preprocessing import load_data, preprocess_data


# def train_models():

#     # --------------------------------
#     # Load and preprocess data
#     # --------------------------------
#     df = load_data()
#     X_train, X_test, y_train, y_test = preprocess_data(df)

#     print("\nBefore SMOTE:")
#     print(y_train.value_counts())

#     # --------------------------------
#     # Apply SMOTE (Balance Training Data)
#     # --------------------------------
#     smote = SMOTE(random_state=42)
#     X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

#     print("\nAfter SMOTE:")
#     print(pd.Series(y_train_balanced).value_counts())

#     # --------------------------------
#     # Random Forest (Final Model)
#     # --------------------------------
#     rf = RandomForestClassifier(
#         n_estimators=300,
#         random_state=42,
#         n_jobs=-1
#     )

#     rf.fit(X_train_balanced, y_train_balanced)

#     y_pred_rf = rf.predict(X_test)

#     print("\n----- Random Forest Results -----")
#     print("Accuracy:", round(accuracy_score(y_test, y_pred_rf), 4))
#     print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
#     print("Classification Report:\n", classification_report(y_test, y_pred_rf))

#     # --------------------------------
#     # Save Model
#     # --------------------------------
#     joblib.dump(rf, "model/earlyrisk_model.pkl")
#     joblib.dump(X_train.columns, "model/feature_columns.pkl")

#     print("\nFinal Model Selected: Random Forest (SMOTE Balanced)")
#     print("Model and feature columns saved successfully ✅")

#     # --------------------------------
#     # Show Full Dataset Distribution (Aligned with 3.0 threshold)
#     # --------------------------------
#     print("\nFull Dataset Risk Distribution:")
#     df_full = load_data()
#     df_full['Academic_Risk'] = df_full['What is your current CGPA?'].apply(
#         lambda x: 1 if x < 3.0 else 0
#     )
#     print(df_full['Academic_Risk'].value_counts(normalize=True))


# if __name__ == "__main__":
#     train_models()



import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from preprocessing import load_data, preprocess_data


def train_models():

    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("\nBefore SMOTE:")
    print(y_train.value_counts())

    # Apply SMOTE
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

    print("\nAfter SMOTE:")
    print(pd.Series(y_train_balanced).value_counts())

    # Train Random Forest
    rf = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    )

    rf.fit(X_train_balanced, y_train_balanced)

    y_pred = rf.predict(X_test)

    print("\n----- Random Forest Results -----")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save model
    joblib.dump(rf, "model/earlyrisk_model.pkl")
    joblib.dump(X_train.columns, "model/feature_columns.pkl")

    # Feature Importance
    importances = rf.feature_importances_
    feature_importance_df = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    joblib.dump(feature_importance_df, "model/feature_importance.pkl")

    print("\nTop 5 Important Features:")
    print(feature_importance_df.head(5))


if __name__ == "__main__":
    train_models()
