import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Load model
# -----------------------------

model = joblib.load("model.pkl")


# -----------------------------
# Title
# -----------------------------

st.title("🎓 Student Performance Predictor")

st.write(
    "Enter student information to estimate the final grade."
)


# -----------------------------
# Input section
# -----------------------------

st.subheader("Student Information")


age = st.number_input(
    "Age",
    min_value=15,
    max_value=25,
    value=17
)


studytime = st.selectbox(
    "Weekly Study Time",
    options=[1, 2, 3, 4],
    index=1
)


failures = st.number_input(
    "Past Class Failures",
    min_value=0,
    max_value=4,
    value=0
)


absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=5
)


g1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)


g2 = st.number_input(
    "Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)


sex = st.selectbox(
    "Sex",
    ["F", "M"]
)


school = st.selectbox(
    "School",
    ["GP", "MS"]
)


internet = st.selectbox(
    "Internet Access at Home",
    ["yes", "no"]
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Final Grade"):

    input_data = pd.DataFrame(
        {
            "age": [age],
            "studytime": [studytime],
            "failures": [failures],
            "absences": [absences],
            "G1": [g1],
            "G2": [g2],
            "sex": [sex],
            "school": [school],
            "internet": [internet]
        }
    )


    prediction = model.predict(
        input_data
    )[0]


    prediction = max(
        0,
        min(20, prediction)
    )


    st.success(
        f"Predicted Final Grade: {prediction:.2f} / 20"
    )


    # -------------------------
    # Performance interpretation
    # -------------------------

    if prediction >= 16:

        st.info("🌟 Excellent predicted performance")

    elif prediction >= 12:

        st.info("👍 Good predicted performance")

    elif prediction >= 10:

        st.warning("📚 Average predicted performance")

    else:

        st.error("⚠️ Student may need additional support")