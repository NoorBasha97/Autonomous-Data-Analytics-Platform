 # 📊 Autonomous Data Analytics Platform (GenAI)

An end-to-end AI-powered data analytics platform that automatically analyzes datasets and generates insights using a multi-agent architecture.

---

## 🚀 Features

- 📥 Data Ingestion (CSV/Excel support)
- 📊 Automated EDA (Exploratory Data Analysis)
- 📈 Statistical Analysis (correlation, metrics)
- 📉 Smart Visualizations (auto chart selection)
- 🧠 AI Insights Generation (LLM-powered)
- 🔄 Multi-Agent Workflow (LangGraph)
- 🛡️ Fault-Tolerant Execution (fallback handling)
- 🌐 Interactive Web UI (Streamlit)

---

## 🧠 Architecture

The system is built using a **multi-agent architecture**:
        Supervisor
            ↓
   ┌────────┼────────┐
   ↓        ↓        ↓
 ingestion  eda     stats
            ↓
     visualization
            ↓
        insights



### 🔹 Key Components

- **Supervisor Agent** → Controls workflow dynamically  
- **Specialized Agents** → Perform specific tasks  
- **Shared State** → Stores intermediate outputs  
- **Tools Layer** → Reusable functions for data processing  

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit
- LangChain
- LangGraph
- Groq API (LLM)

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

pip install -r requirements.txt

🔑 Setup Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key

▶️ Run the Application
streamlit run app.py

📸 UI Preview
Upload dataset
Ask queries
View:
Dataset preview
EDA summary
Visualizations
AI insights
🧪 Example Use Cases
Business data analysis
Salary trend analysis
Customer segmentation insights
Exploratory data analysis automation
🛡️ Fault Tolerance
Handles missing/invalid data
Skips failed visualizations
Provides fallback insights if LLM fails
Prevents pipeline crashes
🔮 Future Improvements
Add RAG-based insights
Deploy on cloud (AWS / GCP)
Add authentication
Real-time streaming data support
👨‍💻 Author

Noor Basha Shaik
