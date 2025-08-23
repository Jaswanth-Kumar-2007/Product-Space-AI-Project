from sentence_transformers import SentenceTransformer
import chromadb

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load DB
chroma_client = chromadb.Client()
collection = chroma_client.get_collection("docs")

query = "How can I request design assets?"
query_emb = model.encode(query).tolist()

results = collection.query(query_embeddings=[query_emb], n_results=1)
print("🔍 Answer:", results["documents"][0][0])