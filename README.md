# 🧠 AI Powered Product Analysis Dashboard

An AI-driven **Streamlit** web app that analyzes **bottle product images** and provides detailed predictions for multiple attributes such as **category, subtype, morphological features, functional factors, and real-world traits**.
It integrates **TensorFlow models** for classification and **Gemini AI** for intelligent visual reasoning and natural language analysis.

---

## 🚀 Live Demo

You can provide your live demo link here after deployment. Example placeholder:

👉 [Click here to try the app](https://ai-product-analysis-dashboard.streamlit.app)

---

## 🚀 Features

### 🔍 Intelligent Product Classification

* **Master Category Prediction** (e.g., Beverage, Cosmetic, Medical, etc.)
* **Subtype Detection** using Gemini AI (e.g., Plastic, Glass, Steel, Copper, Aluminum bottles)
* **Morphological Feature Detection** (Tall, Slim, Curved, etc.)
* **Functional Factor Analysis** (Durability, Hygiene Design, Ergonomics)
* **Real World Usage Prediction** (Eco-friendly, Reusable, Affordable, etc.)

### 🤖 Integrated AI Assistant

* Ask **Gemini AI** about bottle features, product insights, or suggestions.
* Get expert-level analysis powered by **Google Generative AI (Gemini 2.5 Flash)**.

### 🆚 Comparison Module

* Upload two bottle images and compare AI predictions side-by-side.

### 📊 Interactive Visualization

* Confidence bar charts and visual feature analysis using **Matplotlib** and **Seaborn**.

### 💬 Feedback System

* Users can submit suggestions or comments directly via a built-in form.

---

## 🧩 Tech Stack

| Component        | Technology                       |
| ---------------- | -------------------------------- |
| Frontend UI      | Streamlit                        |
| AI Models        | TensorFlow / Keras               |
| Image Processing | Pillow, NumPy                    |
| Visualization    | Matplotlib, Seaborn              |
| LLM Integration  | Google Gemini (Generative AI)    |
| Data Download    | gdown (Google Drive integration) |

---

## 📦 Project Structure

```
AI-Powered-Product-Analysis-Dashboard-using-TensorFlow-and-Gemini-AI/
│
│
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## 🧠 Model Information

All trained **TensorFlow/Keras models** are hosted on **Google Drive** and automatically downloaded on first run using `gdown`.

Optional manual setup: place the following files in `models/`:

| Model Name                          | Description                           | Google Drive ID                     |
| ----------------------------------- | ------------------------------------- | ----------------------------------- |
| `MasterCategories_model.keras`      | Predicts the master product category  | `1TE8cMcmI9HIKINYSVqSCWXx-sNR6FmlI` |
| `MorphologicalFeatures_model.keras` | Detects bottle shape and structure    | `1nCSYG8b0nrArMhdHV2JoO43E91kjSjTF` |
| `FunctionalFactors_model.keras`     | Identifies key functional attributes  | `1MTbld9R0Vvm9sDcmuBB0gYqup4b3fILh` |
| `RealWorldUsage_model.keras`        | Evaluates real-world usage and traits | `1gkx3-cjRQX_VTGEynJItfY7qJRL4GGV6` |

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/iamDeepakHR/AI-Powered-Product-Analysis-Dashboard-using-TensorFlow-and-Gemini-AI.git
cd AI-Product-Analysis-Dashboard
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Gemini API Key

Open `app.py` and replace:

```python
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

Get your key from:
🔗 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧾 Example Workflow

1. Go to **Upload & Predict** section.
2. Upload a bottle image (`.jpg`, `.jpeg`, `.png`).
3. The app will:

   * Run TensorFlow models for feature prediction
   * Use **AI** for intelligent subtype reasoning
   * Display all predictions, reasoning, and confidence scores
4. Check **Compare Bottles** to analyze two products side by side
5. Use **AI Assistant** to chat with Gemini about bottle materials or improvements

---

## 📸 Sample Output

**Predictions Example:**

```
Master Category: Beverage (98.6%)
Subtype: Steel Bottle (95.0%)
Morphological Feature: Slim (87.2%)
Functional Factor: Durability (91.3%)
Real World Usage: Reusable (89.4%)
```

**AI Reasoning:**

> The bottle has a metallic silver shine, opaque surface, and cylindrical design with a steel lid.
> Final Classification: Steel Bottle

---

## 🧪 Requirements

```text
streamlit
tensorflow
numpy
pillow
matplotlib
seaborn
gdown
google-generativeai
```

---

## 🧑‍💻 Developer

**Deepak H R**
📍 BE in Computer Science and Engineering, Nagarjuna College of Engineering, Bangalore
🌐 [GitHub](https://github.com/iamDeepakHR) | [LinkedIn](https://linkedin.com/in/iamdeepakhr)

---

## 🪄 Future Enhancements

* Add **bottle defect detection** using YOLOv8
* Support **multi-product batch predictions**
* Integrate **cloud model hosting** (TensorFlow Serving / Vertex AI)
* Add **database for user feedback & analysis reports**

---

## 🏁 License

This project is **open-source under the MIT License**.
You are free to use, modify, and distribute with attribution.

