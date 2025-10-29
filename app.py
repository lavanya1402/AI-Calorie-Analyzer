# app.py
# NutriVision — Local food & calorie analyzer (Ollama + Streamlit)

import io
import base64
import requests
from PIL import Image
import streamlit as st

# -------------------------
# Config
# -------------------------
OLLAMA_HOST = "http://localhost:11434"
CHAT_URL = f"{OLLAMA_HOST}/api/chat"
DEFAULT_MODEL = "llava:13b"   # change to "llava:7b", "minicpm-v:8b", or "moondream:latest"
REQUEST_TIMEOUT = 600         # seconds (first call can be slow while model loads)

st.set_page_config(page_title="NutriVision (Local Ollama)")
st.title("🥗 NutriVision — AI-Powered Food & Calorie Analyzer (Local)")

# -------------------------
# Sidebar controls
# -------------------------
st.sidebar.header("Model Settings")
model_name = st.sidebar.selectbox(
    "Select a vision model installed in Ollama",
    options=[DEFAULT_MODEL, "llava:7b", "minicpm-v:8b", "moondream:latest"],
    index=0
)
temperature = st.sidebar.slider("Creativity (temperature)", 0.0, 1.0, 0.2, 0.05)

# -------------------------
# Helper functions
# -------------------------
def encode_image_to_b64(image: Image.Image) -> str:
    """Encode a PIL image to base64 PNG."""
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def call_ollama_chat(model: str, prompt: str, image_b64: str) -> str:
    """Call Ollama /api/chat with a user message that includes an image."""
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": [image_b64]
            }
        ],
        "options": {"temperature": temperature},
        "stream": False
    }
    r = requests.post(CHAT_URL, json=payload, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    data = r.json()
    # Newer Ollama returns {"message":{"content":"..."}}
    if isinstance(data, dict):
        if "message" in data and isinstance(data["message"], dict):
            return (data["message"].get("content") or "").strip()
        # Older shape (fallback)
        return (data.get("response") or "").strip()
    return ""

# -------------------------
# UI
# -------------------------
default_instruction = (
    "You are a professional nutritionist. Identify each visible food item in the image. "
    "Estimate approximate calories per item and provide a total in this format:\n"
    "1) Item — ~calories\n2) Item — ~calories\nTotal — ~calories\n"
    "If uncertain, state brief assumptions."
)

user_instruction = st.text_area(
    "Instruction to the AI",
    value=default_instruction,
    height=140,
)

uploaded = st.file_uploader("Upload a meal photo (JPG/PNG)", type=["jpg", "jpeg", "png"])

img = None
if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

analyze = st.button("Analyze")

# -------------------------
# Inference
# -------------------------
if analyze:
    if img is None:
        st.error("Please upload an image first.")
    else:
        img_b64 = encode_image_to_b64(img)
        with st.spinner("🧠 Analyzing image... (first run can take a few minutes while the model loads)"):
            try:
                result = call_ollama_chat(model_name, user_instruction, img_b64)
                if result:
                    st.subheader("🍽️ AI Analysis")
                    st.write(result)
                else:
                    st.warning("No text returned by the model.")
            except requests.exceptions.ReadTimeout:
                st.error("⏱️ Ollama took too long to respond. Try again; the first call is the slowest.")
            except requests.exceptions.ConnectionError:
                st.error("🔌 Could not connect to Ollama. Ensure `ollama serve` is running.")
            except Exception as e:
                st.error(f"⚠️ Error connecting to Ollama: {e}")

# -------------------------
# Footer help
# -------------------------
with st.expander("Having trouble? Quick checks"):
    st.markdown(
        """
1. In a separate terminal, keep **`ollama serve`** running.
2. Pull a vision model (pick one you installed):  
   `ollama pull llava:13b`  •  `ollama pull llava:7b`  •  `ollama pull minicpm-v:8b`  •  `ollama pull moondream:latest`
3. Verify install: `ollama list` should show the model you selected.
4. First request may take **2–5 min** as the model loads into memory; we use a **600s** timeout.
5. If your GPU/VRAM is limited, try `llava:7b` or `moondream:latest`.
        """
    )
