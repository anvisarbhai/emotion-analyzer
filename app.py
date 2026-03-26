import streamlit as st
from model import detect_emotion

# page config
st.set_page_config(
    page_title="Emotion Analyzer",
    page_icon="🧠",
    layout="centered"
)

# custom styling
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
    }
    h1 {
        text-align: center;
        color: #38bdf8;
    }
    .stTextArea textarea {
        border-radius: 12px;
        padding: 10px;
    }
    .stButton button {
        background-color: #38bdf8;
        color: black;
        border-radius: 10px;
        padding: 8px 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# title
st.title("🧠 Emotion-Aware Text Analyzer")
st.caption("Detect emotions using Deep Learning (Transformer Model)")

# input box
text = st.text_area("Enter your text here", height=150)

# button
if st.button("Analyze Emotion"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        emotion, score = detect_emotion(text)

        st.markdown("---")

        st.subheader("✨ Result")

        # emoji mapping
        emoji_map = {
            "joy": "😊",
            "sadness": "😢",
            "anger": "😠",
            "fear": "😨",
            "love": "❤️",
            "surprise": "😲"
        }

        emoji = emoji_map.get(emotion.lower(), "🙂")

        st.success(f"{emoji} Detected Emotion: **{emotion.upper()}**")
        st.info(f"Confidence: **{round(score * 100, 2)}%**")