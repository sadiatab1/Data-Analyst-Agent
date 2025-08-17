# Data Analyst Agent — Modular, Resilient, AI-Powered  
> Built for clarity, speed, and bulletproof automation using **FastAPI + LangChain + Gemini AI.**  
> Repository: *Insert your GitHub repo link here*

---

## 📌 What Is This?

Meet your **TDS Data Analyst Agent** — a production-ready assistant that transforms raw data and natural language queries into actionable insights.  
Designed for reproducibility, modularity, and edge-case resilience.

✅ Visual reports  
✅ AI-generated summaries  
✅ Robust fallback logic for Gemini API keys  
✅ Modular handlers for parsing, scraping, dispatching, and plotting  

Perfect for:  
- Analysts 🧾  
- Engineers 🛠️  
- Researchers 🔬  
- Anyone building reliable data agents  

---

## ✨ Key Highlights  

| Feature                      | Why It’s Awesome 🚀 |
|-----------------------------|----------------------|
| 🔁 Gemini Key Fallback       | Rotates across 10 keys with quota-aware retries |
| 🧠 LangChain Integration     | Structured LLM orchestration with tool binding |
| 📊 Visualizations            | Seaborn + Matplotlib for clean plots |
| 🧼 Modular Architecture      | Handlers for parsing, scraping, dispatching, plotting |
| 📂 Multi-Format Support      | CSV, Excel, JSON, Parquet, TXT |
| 🧪 Parametric Testing Ready  | Designed for CI pipelines and rubric validation |
| ⚡ FastAPI Backend           | High-performance, reloadable server |

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repo  
```bash
git clone https://github.com/your-username/tds-data-analyst-agent.git
cd tds-data-analyst-agent
```

### 2️⃣ Install Requirements  - pip install -r requirements.txt

### 3️⃣ Configure API Keys  
Create a `.env` file inside the root folder:  
GEMINI_API_KEY=your_google_api_key
LLM_TIMEOUT_SECONDS=240


### 4️⃣ Start the Application  - python -m uvicorn app:app --reload

Now open [**http://localhost:8000/**](http://localhost:8000/) in your browser 🌐  

## 🧑‍💻 How It Works  

1. **Write Your Questions**  
   Create a `.txt` file with queries like:  What’s the revenue growth month-over-month?, Find correlation between Age and Income, Show most profitable products...etc

2. **Upload Dataset + Questions File**  
- Dataset (optional) → CSV, Excel, JSON, Parquet, or TXT  
- Questions file (required) → Plain text  

3. **Voilà!**  
- AI processes the queries  
- Generates insights + summaries  
- Builds neat visualizations  

---

## 🛠 Tech Behind the Scenes  

### Backend  
- FastAPI ⚡ → High-performance web server  
- LangChain 🧠 → Orchestrates LLM interactions  
- Google Generative AI ✨ → Core AI engine  
- Pandas + NumPy 📊 → Data wrangling made smooth  
- Seaborn + Matplotlib 🎨 → Clean, insightful charts  

### Frontend  
- HTML5 + CSS + JavaScript  
- Bootstrap-inspired modern UI  

---

## 🔧 API Blueprint  

| Method | Endpoint  | Purpose |
|--------|-----------|----------|
| `GET`  | `/`       | Access web app |
| `POST` | `/api`    | Submit dataset + questions |
| `GET`  | `/summary`| App diagnostics & summaries |

---

## 📂 File Support  

| Format | Extensions |
|--------|------------|
| CSV    | `.csv`     |
| Excel  | `.xlsx`, `.xls` |
| JSON   | `.json`    |
| Parquet| `.parquet` |
| Text   | `.txt`     |

---

## 🎯 Where Can You Use This?  

- 📈 Business Strategy – Sales, KPIs, forecasts  
- 🔬 Research – Data exploration, hypothesis validation  
- 🤖 Data Science – Quick EDA, anomaly detection  
- 📊 Reporting – Automated dashboards  

---

## 🔒 Security First  
- ✅ No cloud storage → All data stays local  
- ✅ API keys kept safe via `.env`  
- ✅ Configurable CORS policy for production use  

---

## 📜 License  

Licensed under **MIT** – free for personal & commercial use. 





  
