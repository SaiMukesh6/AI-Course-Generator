# 📚 AI Course Generator

An AI-powered web application that generates structured learning courses using Large Language Models (LLMs). The application also allows users to download courses as PDF files, save course history, and chat with uploaded PDF documents using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 🤖 AI-powered course generation
- 🌍 Multiple languages (English, Hindi, Telugu)
- 📊 Adjustable difficulty levels
- 📚 Custom number of modules
- 📄 Download generated course as PDF
- 💾 Persistent course history using SQLite
- 📑 Upload any PDF
- 💬 Chat with uploaded PDFs using RAG
- 🔍 Semantic search using FAISS
- 🎨 Responsive Streamlit interface

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- HTML/CSS (Custom Styling)

### Backend
- Python

### AI
- Groq API
- Llama 3.3 70B
- Prompt Engineering

### RAG
- LangChain
- FAISS
- Sentence Transformers
- HuggingFace Embeddings

### Database
- SQLite

### PDF
- ReportLab
- PyPDF

---

## 📂 Project Structure

```text
AI-Course-Generator
│
├── app.py
├── backend
│   ├── ai_generator.py
│   ├── database.py
│   ├── pdf_generator.py
│   └── rag.py
│
├── pages
│   └── 2_PDF_Chat.py
│
├── assets
│   └── style.css
│
├── data
│   └── courses.db
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd AI-Course-Generator
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_API_KEY
```

Run the project

```bash
streamlit run app.py
```

---

## 💡 How It Works

### AI Course Generator

1. User enters a course topic.
2. A prompt is created dynamically.
3. Groq API generates the course using Llama 3.3.
4. Course is displayed.
5. Course is stored in SQLite.
6. Course can be downloaded as a PDF.

---

### PDF Chat (RAG)

1. Upload a PDF.
2. PDF is split into smaller chunks.
3. Embeddings are generated.
4. Chunks are stored in a FAISS vector database.
5. User asks a question.
6. Relevant chunks are retrieved.
7. Llama 3.3 generates an answer using only the retrieved context.

---

## ✨ Future Improvements

- User authentication
- Cloud database integration
- Save PDF chat history
- Export chat as PDF
- Voice-based interaction
- Course chatbot
- Cloud vector database (Pinecone/Chroma)

---

## 👨‍💻 Developer

**Mukesh**

Built as an AI Engineering placement project to demonstrate:

- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Vector Databases
- Streamlit Development
- Python Backend Development

---

## 📄 License

This project is for educational and portfolio purposes.