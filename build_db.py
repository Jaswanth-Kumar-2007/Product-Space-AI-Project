from sentence_transformers import SentenceTransformer
import chromadb
import os
import textwrap

model = SentenceTransformer("all-MiniLM-L6-v2")

# Persistent DB
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create collection (only if not exists)
try:
    collection = chroma_client.get_collection("docs")
except:
    collection = chroma_client.create_collection("docs")

docs_folder = "docs"

for filename in os.listdir(docs_folder):
    with open(os.path.join(docs_folder, filename), "r", encoding="utf-8") as f:
        text = f.read()

        # Split into smaller chunks (better retrieval)
        chunks = textwrap.wrap(text, width=800)  # 800 chars ~ 150 tokens

        for i, chunk in enumerate(chunks):
            doc_id = f"{filename}_{i}"

            # If already exists → delete
            try:
                collection.delete(ids=[doc_id])
            except:
                pass

            embedding = model.encode(chunk).tolist()
            collection.add(documents=[chunk], embeddings=[embedding], ids=[doc_id])

        print(f"✅ Processed {filename} ({len(chunks)} chunks)")

print("🎉 All docs added to ChromaDB")
