import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
import os

# Embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Groq client

client_groq = Groq(api_key=groq_api_key)

# Persistent Chroma setup
chroma_client = chromadb.PersistentClient(path="./chroma_db")

try:
    collection = chroma_client.get_collection("docs")
except:
    collection = chroma_client.create_collection("docs")

st.title("📑 Internal Docs Q&A Agent ")

question = st.text_input("Ask a question:")

if question:
    # Step 1: Encode query and search in docs
    query_emb = embedder.encode(question).tolist()
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=1,
        include=["documents", "distances"]
    )

    doc = results["documents"][0][0] if results["documents"][0] else None
    distance = results["distances"][0][0] if results["distances"][0] else None

    # 🔧 Similarity threshold (tune between 0.2–0.35)
    threshold = 0.8

    st.write(f"🔍 Best match distance: {distance}")  # debug info

    if doc and distance is not None and distance < threshold:
        # ✅ Good doc match → answer directly
        st.write("💡 *Answer :*", doc)
    else:
        # ❌ Weak or no match → fallback to Groq
        prompt = f"Question: {question}\nAnswer:"

        response = client_groq.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )

        answer = response.choices[0].message.content
        st.write("🤖 *Answer :*", answer)
