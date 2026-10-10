# 🚀 AI-Powered Space Mission Knowledge Explorer

An AI-powered application that uses **Retrieval-Augmented Generation (RAG)** to answer questions from uploaded space mission PDF documents.

## 📌 About the Project

The Space Mission Knowledge Explorer allows users to upload multiple PDF documents about space missions and ask questions about their content.

It retrieves relevant information from the uploaded documents using semantic search and uses the Gemini API to generate natural-language answers based on the retrieved context.

## ✨ Features

- Upload multiple PDF documents.
- Extract text from PDFs.
- Split text into smaller chunks.
- Generate embeddings for semantic search.
- Store and retrieve document chunks using ChromaDB.
- Generate answers using the Gemini API.
- Display source document names alongside answers.

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Streamlit** – User interface
- **PyPDF** – PDF text extraction
- **Sentence Transformers** – Text embeddings
- **ChromaDB** – Vector database
- **Google Gemini API** – Answer generation

## 🔄 How It Works

1. Upload space mission PDF documents.
2. Extract text from the PDFs.
3. Split the extracted text into chunks.
4. Generate embeddings using `all-MiniLM-L6-v2`.
5. Store the chunks and embeddings in ChromaDB.
6. Retrieve relevant chunks based on the user's question.
7. Send the retrieved context and question to Gemini.
8. Display the generated answer and source document names.

## 📂 Project Structure

```text
space-mission-rag-explorer/
├── app.py
├── rag.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

**Note:** `.env` contains your API key and must not be uploaded to GitHub.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sowmya161207/space-mission-rag-explorer.git
cd space-mission-rag-explorer
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Gemini API key.

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 🪐 Example Use Case

**Question:** What are the main objectives of the Chandrayaan-2 and Chandrayaan-3 missions?

The application retrieves relevant information from the uploaded mission PDFs and generates an answer using the retrieved context.

## 📚 What I Learned

- Understanding the Retrieval-Augmented Generation (RAG) pipeline.
- Working with text embeddings and semantic search.
- Using a vector database for document retrieval.
- Integrating an LLM API into a Python application.
- Building an interactive document question-answering system.

## 🔮 Future Improvements

- Display page numbers for source references.
- Improve chunking and retrieval accuracy.
- Add relevance checks to reduce unsupported answers.
- Add support for more document formats.

## 👩‍💻 Author

**Sowmya S**

Machine Learning and Artificial Intelligence Student

## 🔖 Tags

`RAG` `Generative AI` `Machine Learning` `Python` `Streamlit` `ChromaDB` `Gemini API`
