import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# -----------------------------
# 1. Load dataset
# -----------------------------

df = pd.read_csv(
    "data/student-mat.csv",
    sep=";"
)

print("Dataset shape:", df.shape)


# -----------------------------
# 2. Select features
# -----------------------------

features = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2",
    "sex",
    "school",
    "internet"
]

target = "G3"

X = df[features]
y = df[target]


# -----------------------------
# 3. Identify columns
# -----------------------------

categorical_features = [
    "sex",
    "school",
    "internet"
]

numeric_features = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]


# -----------------------------
# 4. Preprocessing
# -----------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# -----------------------------
# 5. Create model pipeline
# -----------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=200,
                random_state=42
            )
        )
    ]
)


# -----------------------------
# 6. Train/test split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------
# 7. Train
# -----------------------------

model.fit(X_train, y_train)


# -----------------------------
# 8. Predict
# -----------------------------

predictions = model.predict(X_test)


# -----------------------------
# 9. Evaluate
# -----------------------------

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nModel Results")
print("----------------")
print("MAE:", mae)
print("R²:", r2)


# -----------------------------
# 10. Save model
# -----------------------------

joblib.dump(
    model,
    "model.pkl"
)

print("\nModel saved as model.pkl")