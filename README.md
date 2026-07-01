# 🔬 Deep Scholar

### AI-Powered Multi-Agent Research System

Deep Scholar is an autonomous research platform built using LangChain, Groq, Tavily, and Streamlit. It employs a team of specialized AI agents that collaborate to search, analyze, synthesize, and critique information, generating comprehensive research reports on any topic.  
App link: https://deep-scholar-a-research-app.streamlit.app/

---

## 🚀 Features

### 🔍 Search Agent
- Searches the web for relevant and recent information.
- Uses Tavily Search API for reliable search results.
- Collects titles, URLs, and summaries.

### 📖 Reader Agent
- Scrapes and extracts content from relevant web pages.
- Removes unnecessary page elements.
- Provides clean textual data for analysis.

### ✍️ Writer Agent
- Synthesizes gathered information.
- Produces structured research reports.
- Generates:
  - Introduction
  - Key Findings
  - Conclusion
  - Sources

### 🧐 Critic Agent
- Reviews the generated report.
- Evaluates quality and completeness.
- Provides:
  - Score
  - Strengths
  - Areas for Improvement
  - Final Verdict

### 📄 PDF Export
- Download generated research reports as PDF files.

### 🎨 Modern UI
- Built with Streamlit.
- Interactive multi-agent workflow visualization.
- Real-time research generation.

---

## 🏗️ Architecture

```text
User Query
     │
     ▼
┌──────────────┐
│ Search Agent │
└──────┬───────┘
       ▼
┌──────────────┐
│ Reader Agent │
└──────┬───────┘
       ▼
┌──────────────┐
│ Writer Agent │
└──────┬───────┘
       ▼
┌──────────────┐
│ Critic Agent │
└──────┬───────┘
       ▼
 Final Research Report
       +
 Critic Feedback
```

---

## 🛠️ Tech Stack

### AI & Agents
- LangChain
- Groq LLM
- Multi-Agent Architecture

### Search & Scraping
- Tavily Search API
- BeautifulSoup
- Requests

### Frontend
- Streamlit

### Report Generation
- ReportLab

---

## 📂 Project Structure

```text
Multi_Agent_Research_System/

├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/HarshSaxena479/Multi_Agent_Research_System.git

cd Multi_Agent_Research_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

MODEL_NAME=llama-3.3-70b-versatile
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## ☁️ Deployment

This project is deployed using Streamlit Community Cloud.

### Required Secrets

```toml
GROQ_API_KEY="your_groq_api_key"

TAVILY_API_KEY="your_tavily_api_key"

MODEL_NAME="llama-3.3-70b-versatile"
```

---

## 🎯 Example Use Cases

- AI Research
- Technology Trend Analysis
- Academic Research Assistance
- Market Research
- Product Research
- Industry Reports
- Competitive Analysis

---

## 📈 Future Improvements

- Multi-source scraping
- Citation generation
- Research memory
- Report comparison
- Vector database integration
- Research report templates
- Multi-language support

---

## 👨‍💻 Author

**Harsh Saxena**

AI & Machine Learning Enthusiast

GitHub: https://github.com/HarshSaxena479

---

## ⭐ If you found this project useful

Please consider giving it a star on GitHub.
