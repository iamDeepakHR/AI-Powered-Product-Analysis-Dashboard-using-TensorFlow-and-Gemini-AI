import streamlit as st

import tensorflow as tf

from tensorflow.keras.models import load_model

from PIL import Image, UnidentifiedImageError

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

import os

import google.generativeai as genai

from datetime import datetime

---------------------------- CONFIGURATION ----------------------------

GEMINI_API_KEY = "AIzaSyAU9WBV5MvyTs5fKTmsRwhQlIvGHWclj6c"

genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(

page_title="🧠 AI Powered Product Analysis Dashboard",

layout="wide"

)

---------------------------- TITLE ----------------------------

st.title("🧠 AI Powered Product Analysis Dashboard")

st.markdown("""

Upload a bottle image and receive predictions for:

🧾 Master Category

🧴 Subtype

🔬 Morphological Features

🧪 Functional Factors

🌍 Real World Usage


Includes AI-powered visual comparison and difference analysis.

""")

---------------------------- SIDEBAR ----------------------------

st.sidebar.header("📁 Navigation")

section = st.sidebar.radio("Go to", [

"Upload & Predict",

"Compare Bottles",

"AI Assistant",

"Feedback Form"

])

---------------------------- MODEL PATHS ----------------------------

MODEL_PATHS = {

"master": r"C:\Users\Gagan gowda\Downloads\MasterCategories_model.keras",

"morph": r"C:\Users\Gagan gowda\Downloads\MorphologicalFeatures_model.keras",

"factors": r"C:\Users\Gagan gowda\Downloads\FunctionalFactors_model.keras",

"realworld": r"C:\Users\Gagan gowda\Downloads\RealWorldUsage_model.keras",

}

---------------------------- LOAD MODELS ----------------------------

@st.cache_resource

def load_all_models():

models = {}

for name, path in MODEL_PATHS.items():

    if not os.path.exists(path):

        st.error(f"❌ Missing model: {path}")

        st.stop()

    models[name] = load_model(path)

return models

models = load_all_models()

---------------------------- LABELS ----------------------------

labels = {

"master": ['Beverage', 'Cosmetic & Personal Care', 'Household & Cleaning', 'Medical & Baby', 'Specialty & Niche'],

"morph": ['Tall', 'Short', 'Wide', 'Slim', 'Curved'],

"factors": ['Thermal Insulation', 'Durability', 'Hygiene Design', 'Chemical Safety', 'Ergonomics'],

"realworld": ['User Friendly', 'Eco Friendly', 'Reusable', 'Affordable', 'Premium Grade']

}

---------------------------- IMAGE PREPROCESS ----------------------------

def preprocess_image(image, model):

h, w = model.input_shape[1:3]

image = image.convert("RGB").resize((w, h))

img = np.array(image) / 255.0

return img.reshape(1, h, w, 3)

---------------------------- GEMINI SUBTYPE ----------------------------

def predict_subtype_with_gemini(image):

model = genai.GenerativeModel("gemini-2.5-flash")



prompt = """

You are a bottle material classification expert.

Classify the bottle as:

Plastic Bottle / Steel Bottle / Glass Bottle / Copper Bottle / Aluminum Bottle

End response with:

Final Classification: <type>

"""

response = model.generate_content([prompt, image])

text = response.text.strip()



final = "Unknown"

for line in text.splitlines():

    if "Final Classification:" in line:

        final = line.split(":")[-1].strip()



return {

    "prediction": final,

    "confidence": 0.95,

    "full_scores": {final: 0.95},

    "reason": text

}

---------------------------- FEATURE VISUALIZATION ----------------------------

def visualize_bottle_features(reason):

features = {

    "Color": 0.5,

    "Texture": 0.5,

    "Reflectivity": 0.5,

    "Transparency": 0.5,

    "Shape": 0.5

}



text = reason.lower()

if "metal" in text: features["Reflectivity"] = 0.9

if "transparent" in text: features["Transparency"] = 0.9

if "opaque" in text: features["Transparency"] = 0.1

if "smooth" in text: features["Texture"] = 0.9

if "curved" in text or "cylindrical" in text: features["Shape"] = 0.8



fig, ax = plt.subplots(figsize=(4, 3))

sns.barplot(

    x=list(features.values()),

    y=list(features.keys()),

    ax=ax

)

ax.set_xlim(0, 1)

ax.set_title("Visual Feature Strength")

return fig

---------------------------- PREDICTION PIPELINE ----------------------------

def predict_all_models(image):

results = {}



for key, model in models.items():

    processed = preprocess_image(image, model)

    pred = model.predict(processed, verbose=0)[0]

    idx = np.argmax(pred)



    results[key] = {

        "prediction": labels[key][idx],

        "confidence": float(pred[idx]),

        "full_scores": {

            labels[key][i]: float(pred[i]) for i in range(len(pred))

        }

    }



results["subtype"] = predict_subtype_with_gemini(image)

return results

---------------------------- SINGLE BOTTLE VIEW ----------------------------

def show_single_bottle_analysis(title, image, predictions):

st.markdown(f"## 🧴 {title}")

st.image(image, use_column_width=True)



for key, val in predictions.items():

    st.markdown(

        f"### {key.upper()}: {val['prediction']} ({val['confidence']*100:.1f}%)"

    )



    if key == "subtype":

        colA, colB = st.columns(2)



        with colA:

            st.markdown("**🧠 Gemini Explanation**")

            st.caption(val["reason"])

            st.markdown("**📈 Visual Feature Strength**")

            fig = visualize_bottle_features(val["reason"])

            st.pyplot(fig)



        with colB:

            pass



# -------- Confidence graphs (2 per row) --------

st.subheader("📊 Confidence Scores")



items = list(predictions.items())



for i in range(0, len(items), 2):

    col1, col2 = st.columns(2)



    k1, v1 = items[i]

    fig1, ax1 = plt.subplots(figsize=(4, 3))

    sns.barplot(

        x=list(v1["full_scores"].values()),

        y=list(v1["full_scores"].keys()),

        ax=ax1

    )

    ax1.set_xlim(0, 1)

    ax1.set_title(k1.upper())

    col1.pyplot(fig1)



    if i + 1 < len(items):

        k2, v2 = items[i + 1]

        fig2, ax2 = plt.subplots(figsize=(4, 3))

        sns.barplot(

            x=list(v2["full_scores"].values()),

            y=list(v2["full_scores"].keys()),

            ax=ax2

        )

        ax2.set_xlim(0, 1)

        ax2.set_title(k2.upper())

        col2.pyplot(fig2)

---------------------------- DIFFERENCE ANALYSIS ----------------------------

def show_bottle_differences(pred1, pred2):

st.subheader("🔍 Key Differences Between Bottles")



for key in pred1.keys():

    v1 = pred1[key]["prediction"]

    v2 = pred2[key]["prediction"]



    if v1 == v2:

        st.success(f"✅ **{key.upper()}**: Same → **{v1}**")

    else:

        st.error(

            f"❌ **{key.upper()} Difference**\n\n"

            f"- Bottle 1: **{v1}**\n"

            f"- Bottle 2: **{v2}**"

        )

---------------------------- SECTIONS ----------------------------

if section == "Upload & Predict":

uploaded = st.file_uploader("Upload Bottle Image", type=["jpg", "png", "jpeg"])

if uploaded:

    try:

        img = Image.open(uploaded)

        with st.spinner("Analyzing..."):

            results = predict_all_models(img)

        show_single_bottle_analysis("Bottle", img, results)

    except UnidentifiedImageError:

        st.error("❌ Invalid image file")

elif section == "Compare Bottles":

st.header("🔄 Bottle Comparison")



col1, col2 = st.columns(2)

up1 = col1.file_uploader("Upload Bottle 1", type=["jpg","png","jpeg"])

up2 = col2.file_uploader("Upload Bottle 2", type=["jpg","png","jpeg"])



if up1 and up2:

    img1 = Image.open(up1)

    img2 = Image.open(up2)



    with st.spinner("Comparing bottles..."):

        r1 = predict_all_models(img1)

        r2 = predict_all_models(img2)



    c1, c2 = st.columns(2)

    with c1:

        show_single_bottle_analysis("Bottle 1", img1, r1)

    with c2:

        show_single_bottle_analysis("Bottle 2", img2, r2)



    st.markdown("---")

    show_bottle_differences(r1, r2)

elif section == "AI Assistant":

st.header("🤖 Ask Gemini AI")

q = st.text_input("Ask about the product")

if q:

    with st.spinner("Analyzing..."):

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(q)

        st.markdown(response.text)

elif section == "Feedback Form":

with st.form("feedback"):

    st.text_input("Name")

    st.text_input("Email")

    st.text_area("Feedback")

    if st.form_submit_button("Submit"):

        st.success("Thank you ❤️")

---------------------------- FOOTER ----------------------------

year = datetime.now().year

st.markdown("---")

st.caption(f"AI Powered Product Analysis Dashboard by Gagan Gowda K S • {year}")
