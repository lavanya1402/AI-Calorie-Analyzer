# 🥗 AI Calorie Analyzer (NutriVision)

**AI Calorie Analyzer** (codename *NutriVision*) is an intelligent food analysis system powered by **Groq Llama 4 Vision** and **Streamlit**.
It uses multimodal deep learning to visually interpret meal images, identify ingredients, and estimate total calorie intake — bridging **computer vision**, **nutrition science**, and **AI accessibility**.

🌐 **Live Demo:** [https://ai-calorie-analyzer.streamlit.app](https://ai-calorie-analyzer.streamlit.app)
👩‍💻 **Author:** [Lavanya Srivastava](https://github.com/lavanya1402)

---

## 🚀 Overview

This project demonstrates how generative and vision-based AI can analyze food imagery and deliver contextual insights such as:

* 🍽️ Recognizing food items from photos
* 🔢 Estimating calories per item and total meal calories
* 🧠 Explaining assumptions and nutrient composition
* 🌿 Supporting health tracking, dietary planning, and wellness education

---

## 🧩 Architecture

```text
User Uploads Image  →  Streamlit UI  →  Groq Llama 4 Vision API
       │                         │
       │                         └──> Encodes image → Sends to model
       │
       └── Receives structured AI output:
           ├─ Food item list
           ├─ Calorie estimates
           ├─ Nutritional comments
           └─ Aggregated meal summary
```

### 🔍 Key Components

| Layer                    | Technology                 | Purpose                             |
| ------------------------ | -------------------------- | ----------------------------------- |
| **Frontend**             | Streamlit                  | Interactive web interface           |
| **AI Core**              | Groq Llama 4 Vision API    | Multimodal reasoning (text + image) |
| **Middleware**           | Python + Requests          | API orchestration & JSON parsing    |
| **Environment Handling** | dotenv / Streamlit Secrets | Secure key management               |
| **Visualization**        | Pillow + Streamlit UI      | Image rendering & display           |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/lavanya1402/AI-Calorie-Analyzer.git
cd AI-Calorie-Analyzer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Environment Key

Create a `.env` file:

```
GROQ_API_KEY=sk_your_groq_key_here
```

### 4️⃣ Run Locally

```bash
streamlit run app.py
```

### 5️⃣ Deploy to Streamlit Cloud

* Go to **Advanced settings → Secrets**
* Paste:

  ```toml
  GROQ_API_KEY = "sk_your_groq_key_here"
  ```
* Set **Python 3.10**
* Click **Deploy**

---

## 🌍 Real-World Applications

| Domain                      | Example Use                                            |
| --------------------------- | ------------------------------------------------------ |
| 🏥 **Healthcare**           | Calorie tracking for diabetes and obesity management   |
| 📱 **Fitness & Wearables**  | Integration with fitness apps for smart nutrition      |
| 🏫 **Education**            | Teaching AI + health awareness through visual projects |
| 🛒 **Food Industry**        | Restaurant menu digitization, smart calorie labeling   |
| 🧑‍🍳 **Personal Wellness** | Personalized meal planning and diet assistance         |

---

## 🔮 Future Prospects

* **Mobile Extension:** Deploy as a cross-platform Flutter/PWA app for instant food logging.
* **Multilingual Support:** Nutrition reports in 10+ global languages.
* **Diet Recommendation Engine:** Integrate with LLM-based diet planners for personalized plans.
* **Global Datasets:** Fine-tuning with Food-101 / Indian Food-Dataset for region-specific accuracy.
* **Sustainability Insights:** Estimate carbon footprint of meals.

---

## 🧠 Tech Stack

| Category            | Stack                                       |
| ------------------- | ------------------------------------------- |
| **Framework**       | Streamlit 1.50 + Python 3.10                |
| **AI Model**        | Groq Llama 4 Vision (Maverick/Scout series) |
| **Libraries**       | Requests, Pillow, Python-Dotenv             |
| **Deployment**      | Streamlit Cloud                             |
| **Version Control** | Git + GitHub                                |

---

## 🏗️ Project Goals

1. Democratize **AI-driven nutrition analysis** using open tools.
2. Demonstrate **multimodal model integration** with Groq APIs.
3. Serve as a **teaching reference** for AI, data science, and health tech learners worldwide.

---

## 📸 Demo Preview

*(Replace with your screenshot)*
![App Screenshot](https://github.com/lavanya1402/AI-Calorie-Analyzer/assets/demo_screenshot.png)

---

## 💬 Citation & Attribution

If you use or reference this work, please cite:

> **Lavanya Srivastava (2025)**. *AI Calorie Analyzer — Multimodal Nutrition Estimation using Groq Vision + Streamlit.*
> GitHub Repository: [https://github.com/lavanya1402/AI-Calorie-Analyzer](https://github.com/lavanya1402/AI-Calorie-Analyzer)

---

## ❤️ Acknowledgments

* **Groq Inc.** for providing open access to Llama-Vision APIs.
* **Streamlit Community** for seamless rapid deployment.
* **Open-source ecosystem** powering this innovation.

---

### 🌟 Vision Statement

> “To make nutrition intelligence universally accessible — empowering every individual to see, understand, and improve what’s on their plate.”

---

Happy learning
**Best regards,**
**Lavanya Srivastava**
*(AI Developer | Educator | Health-Tech Innovator)*

## License

MIT, see [LICENSE](LICENSE). Built by [Lavanya Srivastava](https://github.com/lavanya1402), Lavanya AI Consultancy.
