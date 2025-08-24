<!-- Header Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,100:0072ff&height=200&section=header&text=Jaswanth%20Kumar&fontSize=40&fontColor=ffffff&animation=twinkling&fontAlignY=35"/>
</p>

<!-- Typing Animation -->
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=00F700&center=true&vCenter=true&width=500&lines=Hi+👋+I'm+Jaswanth+Kumar;Full+Stack+Developer;Open+Source+Enthusiast;Always+Learning+New+Things" alt="Typing SVG" />
  </a>
</p>

![YourName's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jaswanth-Kumar-2007&show_icons=true&theme=radical)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jaswanth-Kumar-2007&layout=compact&theme=tokyonight)

![Profile Views](https://komarev.com/ghpvc/?username=Jaswanth-Kumar-2007&label=Profile%20views&color=0e75b6&style=flat)
![Followers](https://img.shields.io/github/followers/Jaswanth-Kumar-2007?label=Followers&style=social)
![Stars](https://img.shields.io/github/stars/Jaswanth-Kumar-2007?label=Stars&style=social)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


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
├── build_db.py           # Script to index documents into Chroma
├── app.py                # Streamlit Q&A app (Docs + Groq fallback)
├── query_test.py         #To Build the query Format
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
venv\Scripts\activate         #Windows
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








