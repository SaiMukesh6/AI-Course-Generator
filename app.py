import streamlit as st

# ---------------- LOAD CSS ---------------- #

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------- IMPORTS ---------------- #

from backend.ai_generator import generate_ai_course
from backend.pdf_generator import create_pdf

from backend.database import (
    create_table,
    save_course,
    get_courses,
    delete_all_courses
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Course Generator",
    page_icon="📚",
    layout="wide"
)

# ---------------- DATABASE ---------------- #

create_table()
# ---------- SESSION STATE ----------

if "generated_course" not in st.session_state:
    st.session_state.generated_course = ""

# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://img.icons8.com/color/96/artificial-intelligence.png",
    width=80
)

st.sidebar.title("AI Course Generator")
st.sidebar.caption("Generate AI-powered courses instantly")

st.sidebar.divider()

page = st.sidebar.radio(
    "📂 Navigation",
    [
        "🏠 Generate Course",
        "📜 Course History",
        "ℹ About"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("📊 Statistics")

st.sidebar.metric(
    "Courses Generated",
    len(get_courses())
)

st.sidebar.divider()

st.sidebar.subheader("⚙ Tech Stack")

st.sidebar.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 🤖 Groq API
- 🦙 Llama 3.3
- 🗄 SQLite
- 📄 ReportLab
- 🔍 FAISS
""")

# ===========================================================
#                 GENERATE COURSE PAGE
# ===========================================================

if page == "🏠 Generate Course":

    st.title("📚 AI Course Generator")

    st.markdown("""
### 🚀 Build complete AI-powered courses in seconds

Generate structured courses with:

- 🤖 Llama 3.3 (Groq)
- 📄 Download as PDF
- 💾 SQLite Course History
- 🌍 Multi-language Support
- 🔍 PDF Question Answering (RAG)

---
""")

    topic = st.text_input(
        "Enter Course Topic",
        placeholder="Example: Machine Learning"
    )

    col1, col2 = st.columns(2)

    with col1:

        difficulty = st.selectbox(
            "Select Difficulty",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        reading_time = st.selectbox(
            "Reading Time",
            [
                "5 Minutes",
                "10 Minutes",
                "15 Minutes"
            ]
        )

    with col2:

        modules = st.slider(
            "Number of Modules",
            min_value=2,
            max_value=10,
            value=5
        )

        language = st.selectbox(
            "Course Language",
            [
                "English",
                "Hindi",
                "Telugu"
            ]
        )

    if st.button(
        "🚀 Generate AI Course",
        use_container_width=True
    ):

        if not topic.strip():

            st.warning("Please enter a course topic.")

        else:

            with st.spinner(
                "🤖 AI is generating your course..."
            ):

                course = generate_ai_course(
                    topic,
                    difficulty,
                    modules,
                    reading_time,
                    language
                )

            save_course(
                topic,
                course
            )
            st.session_state.generated_course = course

            st.success(
                "🎉 Your AI course has been generated successfully!"
            )

            st.info("""
You can now:

✅ Read the generated course

📥 Download it as a PDF

📜 Access it later from Course History
""")

           

            pdf_file = create_pdf(
                course,
                "generated_course.pdf"
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📥 Download Course PDF",
                    data=file,
                    file_name=f"{topic}.pdf",
                    mime="application/pdf"
                )
    if st.session_state.generated_course:

        st.divider()

        st.subheader("📚 Generated Course")

        st.markdown(st.session_state.generated_course)

# ===========================================================
#                  COURSE HISTORY PAGE
# ===========================================================

elif page == "📜 Course History":

    st.title("📜 Course History")
    st.write("Previously generated AI courses.")

    st.divider()

    courses = get_courses()

    if len(courses) == 0:

        st.info("No courses generated yet.")

    else:

        for topic, course in courses:

            with st.expander(f"📘 {topic}"):

                st.markdown(course)

        st.divider()

        if st.button(
            "🗑 Clear History",
            use_container_width=True
        ):

            delete_all_courses()

            st.success("History cleared successfully!")

            st.rerun()

# ===========================================================
#                     ABOUT PAGE
# ===========================================================

elif page == "ℹ About":

    st.title("ℹ About")

    st.markdown("""
# 📚 AI Course Generator

An AI-powered application that generates
complete learning courses using Large Language Models.

---

## 🚀 Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B
- SQLite
- ReportLab
- FAISS
- Prompt Engineering
- RAG (PDF Chat)

---

## ✨ Features

✅ AI Course Generation

✅ Adjustable Modules

✅ Multiple Difficulty Levels

✅ Multi-language Support

✅ Course History (SQLite)

✅ Download Course as PDF

✅ PDF Chat using RAG

---

## 👨‍💻 Developer

Mukesh

Built as an AI Engineering placement project.
""")

# ===========================================================
#                        FOOTER
# ===========================================================

st.markdown("---")

st.caption(
    "Built with ❤️ using Python • Streamlit • Groq • SQLite • ReportLab • FAISS"
)
