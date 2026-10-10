import streamlit as st
from pypdf import PdfReader
from rag import store_chunks, generate_answer, clear_collection

st.title("AI-Powered Space Mission Knowledge Explorer")

files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

if files and st.button("Process PDFs"):

    clear_collection()

    for file in files:

        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        chunks = [
            text[i:i+1000]
            for i in range(0, len(text), 1000)
            if text[i:i+1000].strip()
        ]

        n = store_chunks(chunks, file.name)

        st.success(
            file.name + " processed - " + str(n) + " chunks"
        )


st.subheader("Ask a Question")

question = st.text_input("Enter your question")

if st.button("Ask AI"):

    if question and files:

        names = [file.name for file in files]

        answer, sources = generate_answer(
            question, names
        )

        st.write("### Answer")
        st.write(answer)

        st.write("### Sources")
        for source in sources:
            st.write("📄", source)

    else:
        st.warning("Please upload PDFs and enter a question.")