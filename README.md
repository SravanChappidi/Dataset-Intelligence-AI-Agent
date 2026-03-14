**Dataset Intelligence AI Agent**
Automated Data Auditing, Privacy Scanning, and Strategic AI Insight Engine

**Overview**
The Dataset Intelligence AI Agent is a professional-grade bimodal system designed to automate the "First Hour" of the data science lifecycle. It transforms raw, unvetted datasets into audited, compliant, and strategically analyzed assets in seconds.

By integrating Llama 3.3 70B and a custom Privacy Guard engine, this agent ensures that data is not only technically sound but also legally compliant with the Indian Digital Personal Data Protection (DPDP) Act 2023.

**Key Features**
1. Privacy Guard (DPDP Act Compliance)
Automated PII Scanning: Identifies sensitive Indian identifiers including Aadhaar numbers, PAN cards, Voter IDs, and contact details.

Risk Mitigation: Flags compliance risks before data is ingested into Machine Learning pipelines.

2. Automated Data Profiling
Health Telemetry: Instant calculation of "Quality Scores" based on missingness, schema integrity, and distribution.

Reactive UI: No-click execution; the audit begins the moment a file is uploaded.

3. AI Strategic Inference
Contextual Roadmap: Generates a senior-level strategic report using Llama 3.3.

ML Readiness: Evaluates the dataset for potential supervised/unsupervised learning use cases.

**System Architecture**
The project follows a Microservices Architecture, ensuring scalability and clean separation of concerns:

Backend (The Brain): A FastAPI service that manages data processing, pattern matching, and LLM orchestration via the Groq inference engine.

Frontend (The Interface): A Streamlit dashboard providing an executive-level view of data health and privacy risks.

**Tech Stack**
Logic: Python 3.9+, Pandas, NumPy.

API Layer: FastAPI, Uvicorn (Asynchronous Server).

UI Layer: Streamlit, Plotly (Dynamic Visualization).

AI Engine: Groq Cloud API (Llama 3.3 70B).

**Installation & Setup**
1. Clone the Repository
Bash
git clone https://github.com/Sravan-Chappidi/Dataset_Intelligence_Agent.git
cd Dataset_Intelligence_Agent
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configuration
The system is pre-configured with environment secrets in .streamlit/secrets.toml for immediate internal verification.

**Execution Sequence**
To run the full system, you must initialize both the service layer and the interface:

Step 1: Start the FastAPI Backend
Bash
uvicorn main:app --reload
Access API Docs at: **http://127.0.0.1:8000/docs**

Step 2: Start the Streamlit Agent
Bash
streamlit run streamlit_app.py
Access Dashboard at: **http://localhost:8501**
