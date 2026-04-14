# 🔬 ResearchMind — Multi-Agent AI Research System

> **Four specialized AI agents collaborate in a pipeline** — searching the web, scraping content, writing reports, and critiquing quality — to deliver a polished research report on any topic in seconds.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agent%20Framework-green?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📌 Overview

ResearchMind is a **multi-agent AI pipeline** built with LangChain and Streamlit. You enter any research topic and four agents automatically work together in sequence to generate a comprehensive, reviewed research report.

**What makes it interesting:** Instead of a single LLM call, this uses a real agentic pipeline where each agent has a distinct role, tool access, and responsibility — mimicking how a real research team operates.

---

## 🧠 Agent Pipeline

```
User Input → [Search Agent] → [Reader Agent] → [Writer Chain] → [Critic Chain] → Final Report
```

| # | Agent | Role | Tools Used |
|---|-------|------|------------|
| 01 | **Search Agent** | Finds recent, reliable web information on the topic | Web Search Tool |
| 02 | **Reader Agent** | Picks the most relevant URL and scrapes deep content | Web Scraper / Reader Tool |
| 03 | **Writer Chain** | Synthesizes all research into a structured markdown report | LLM Chain |
| 04 | **Critic Chain** | Reviews the report, scores quality, suggests improvements | LLM Chain |

---

## 🗂️ Project Structure

```
MULTI AGENT SYSTEM/
│
├── app.py              # Streamlit UI — main entry point
├── agents.py           # Agent definitions (Search Agent, Reader Agent)
├── pipeline.py         # Pipeline orchestration logic
├── tools.py            # Custom tool definitions (search, scrape, etc.)
├── requirement.txt     # Python dependencies
└── .env                # API keys (not committed)
```

---

## ⚙️ Tech Stack

- **[LangChain](https://python.langchain.com/)** — Agent framework, chains, and tool use
- **[Streamlit](https://streamlit.io/)** — Interactive web UI with real-time pipeline status
- **LLM Backend** — Configurable (OpenAI / Gemini / other via LangChain)
- **Web Tools** — Search + scraping tools for live data retrieval
- **Python 3.10+**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/researchmind.git
cd researchmind
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
# Add your API keys here
OPENAI_API_KEY=your_openai_key        # or use Gemini/other LLM
TAVILY_API_KEY=your_tavily_key        # for web search tool
```

### 5. Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🖥️ How to Use

1. Enter any research topic in the input field (e.g., *"LLM agents 2025"*, *"CRISPR gene editing"*)
2. Click **⚡ Run Research Pipeline**
3. Watch the four agents execute in real-time via the pipeline status panel
4. View the final report and critic feedback in the results section
5. Download the report as a `.md` file

---

## 📸 Screenshots

> *(Add a screenshot or demo GIF of the Streamlit UI here)*

---

## 🔑 Key Concepts Demonstrated

- **Multi-agent orchestration** with LangChain's agent framework
- **Tool use** — agents equipped with search and scraping tools
- **Chain of responsibility** — each step builds on the previous agent's output
- **Streamlit state management** — `st.session_state` for pipeline tracking across reruns
- **Custom CSS theming** in Streamlit for production-quality UI

---

## 🛣️ Future Improvements

- [ ] Add memory/caching to avoid redundant searches
- [ ] Support multiple scraping URLs (not just top result)
- [ ] Add a feedback loop where the critic can trigger a re-write
- [ ] Export report as PDF in addition to Markdown
- [ ] Deploy to Streamlit Cloud / HuggingFace Spaces

---

## 👨‍💻 Author

**Hardik** — B.Tech CSE (AI/ML), VIT Bhopal  
Building practical AI agent systems as part of my learning journey in LLMs and agentic pipelines.

- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

> *Built with LangChain multi-agent pipeline · Streamlit UI · ResearchMind*
