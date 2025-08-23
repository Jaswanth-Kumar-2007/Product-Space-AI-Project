📑 Internal Docs Q&A Agent 

An AI-powered assistant that helps teams instantly find answers from internal documents (Notion, Google Docs, Confluence, etc.) with a smart fallback to Groq LLM when no relevant document is found.

🚀 Why we built this

Employees waste time searching across multiple tools for answers to company policies, workflows, or updates.
This bot makes it as easy as asking a question in plain English:

If the answer exists in internal docs → it shows the snippet directly.

If not → it falls back to Groq LLM for a general answer.

✨ Features

📂 Document indexing with ChromaDB (persistent storage).

🤖 Groq LLM fallback when no relevant doc is found.

🔎 Semantic search using sentence-transformers.

🖥️ Streamlit UI for quick interaction.

⚡ Real-time distance scoring (helps tune results).

🛠️ Tech Stack

Python 3.10+

Streamlit
 – frontend UI

ChromaDB
 – vector database

Sentence-Transformers
 – embeddings

Groq API
 – LLM fallback
