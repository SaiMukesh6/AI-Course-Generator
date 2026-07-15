import streamlit as st
import tempfile

from backend.rag import (
    process_pdf,
    ask_pdf
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="PDF Chat",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Chat with your PDF")

st.write("Upload a PDF and ask questions based on its content.")

st.divider()

# ---------------- SESSION STATE ---------------- #

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = ""

# ---------------- PDF UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    # Clear chat only if a NEW PDF is uploaded
    if uploaded_file.name != st.session_state.current_pdf:

        st.session_state.current_pdf = uploaded_file.name
        st.session_state.chat_history = []

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_file.read())

        pdf_path = temp_file.name

    with st.spinner("📄 Processing PDF..."):

        st.session_state.vector_store = process_pdf(pdf_path)

    st.success("✅ PDF Processed Successfully!")

    st.info(f"📄 Current PDF: {st.session_state.current_pdf}")

# ---------------- CHAT ---------------- #

if st.session_state.vector_store is not None:

    st.divider()

    # Display previous chat
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    question = st.chat_input(
        "Ask anything from your PDF..."
    )

    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        with st.spinner("🤖 Searching PDF..."):

            answer = ask_pdf(
                st.session_state.vector_store,
                question
            )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):

            st.markdown(answer)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):

            st.session_state.chat_history = []

            st.rerun()

    with col2:

        st.caption(
            f"Current PDF: **{st.session_state.current_pdf}**"
        )