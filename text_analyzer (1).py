import streamlit as st
import re
from collections import Counter
import math

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Advanced Text Analyzer",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------- Sidebar for Dark Mode Info ----------------
st.sidebar.header("Settings")
st.sidebar.info(
    "💡 You can toggle Streamlit dark/light theme in Settings → Theme."
)

# ---------------- Title ----------------
st.markdown(
    "<h1 style='text-align: center; color: #4B0082;'>📝 Advanced Text Analyzer</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Analyze text with detailed statistics and smart insights.</p>",
    unsafe_allow_html=True
)

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader("Upload a .txt file (optional)", type="txt")

text = ""
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

# ---------------- Text Input ----------------
with st.container():
    st.markdown("## ✏️ Input Section", unsafe_allow_html=True)
    paragraph = st.text_area(
        "Enter your paragraph:",
        value=text,
        height=200
    )

# ---------------- Dropdown ----------------
option = st.selectbox(
    "Select details to display:",
    ("None", "Words", "Characters", "Sentences", "All")
)

if paragraph.strip():
    # ---------------- Processing ----------------
    words = re.findall(r'\b\w+\b', paragraph.lower())
    word_count = len(words)

    characters = list(paragraph)
    char_count = len(paragraph)

    raw_sentences = re.split(r'[.!?]+', paragraph)
    sentences = [s.strip() for s in raw_sentences if s.strip()]
    sentence_count = len(sentences)

    reading_time = math.ceil(word_count / 200) if word_count else 0
    avg_sentence_length = round(word_count / sentence_count, 2) if sentence_count else 0

    word_freq = Counter(words).most_common(5)

    # ---------------- Summary Counts (Middle Section) ----------------
    with st.container():
        st.markdown("## 📊 Summary Counts", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color:#E6E6FA; padding:15px; border-radius:10px'>",
            unsafe_allow_html=True
        )
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Words", word_count)
        c2.metric("Characters", char_count)
        c3.metric("Sentences", sentence_count)
        c4.metric("Reading Time", f"{reading_time} min")
        st.markdown(f"**Average Sentence Length:** {avg_sentence_length} words")
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ---------------- Top 5 Frequent Words ----------------
    with st.container():
        st.markdown("## 🔁 Top 5 Repeated Words", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color:#F0FFF0; padding:10px; border-radius:10px'>",
            unsafe_allow_html=True
        )
        if word_freq:
            st.table(word_freq)
        else:
            st.write("No repeated words found.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ---------------- Detailed View (Bottom Section) ----------------
    with st.container():
        st.markdown("## 📌 Detailed View", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color:#FFF0F5; padding:10px; border-radius:10px'>",
            unsafe_allow_html=True
        )

        if option == "Words":
            st.subheader("🔤 All Words")
            st.table(list(enumerate(words, start=1)))

        elif option == "Characters":
            st.subheader("🔠 All Characters")
            st.write("".join(characters))

        elif option == "Sentences":
            st.subheader("📃 All Sentences")
            for i, s in enumerate(sentences, start=1):
                st.write(f"{i}. {s}")

        elif option == "All":
            st.subheader("🔤 Words")
            st.table(list(enumerate(words, start=1)))

            st.subheader("🔠 Characters")
            st.write("".join(characters))

            st.subheader("📃 Sentences")
            for i, s in enumerate(sentences, start=1):
                st.write(f"{i}. {s}")

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Please enter text or upload a file to analyze.")
