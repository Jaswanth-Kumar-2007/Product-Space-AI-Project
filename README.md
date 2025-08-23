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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
📂 Project Structure 
.
├── docs/                 # Folder containing your internal text files
├── chroma_db/            # Persistent Chroma vector database
├── index_docs.py         # Script to index documents into Chroma
├── app.py                # Streamlit Q&A app (Docs + Groq fallback)
├── requirements.txt
└── README.md
```


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚡ Quick Start
1.Clone Repository
```bash
git clone https://github.com/Jaswanth-Kumar-2007/Product-Space-AI-Project.git
cd Product-Space-AI-Project
```

2.Create a Virtual Environment
```python
python -m venv venv
source venv/bin/activate     #Mac/Linux
venv\script\activate         #Windows
```

3.Install Required Packages
```python
pip install chromadb sentence-transformer streamlit
```

4.Running Code
```python
python build_db.py
```

```python
python query_test.py
```

```python
streamlit run app.py
```

🫱 A Web UI opens at http://localhost:8501 where you can Ask Questions








