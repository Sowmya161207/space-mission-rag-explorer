import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("space_missions")

model = SentenceTransformer("all-MiniLM-L6-v2")
gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def clear_collection():
    data = collection.get()
    if data["ids"]:
        collection.delete(ids=data["ids"])


def store_chunks(chunks, source):
    embeddings = model.encode(chunks).tolist()

    ids = [source + "_" + str(i) for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"source": source} for i in chunks]
    )

    return len(chunks)


def search_document(question, source):
    embedding = model.encode([question]).tolist()

    return collection.query(
        query_embeddings=embedding,
        n_results=4,
        where={"source": source}
    )


def generate_answer(question, sources):

    documents = []
    source_names = []

    for source in sources:
        result = search_document(question, source)

        for doc in result["documents"][0]:
            documents.append(doc)
            source_names.append(source)

    if not documents:
        return "Information not found.", []

    context = ""

    for i in range(len(documents)):
        context += "Source: " + source_names[i] + "\n"
        context += documents[i] + "\n\n"

    prompt = f"""
Answer the question using only the context.

Context:
{context}

Question:
{question}

Give a simple answer.
"""

    response = gemini.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text, list(set(source_names))