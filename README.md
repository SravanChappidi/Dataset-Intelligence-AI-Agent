**Project Objective**

The Dataset Intelligence AI Agent transforms raw datasets into structured intelligence reports.

**The system automatically performs:**

dataset profiling
sensitive data detection
data quality evaluation
statistical insight generation
machine learning readiness analysis
model recommendation

This helps data analysts, data scientists, and ML engineers quickly evaluate a dataset before building models.

**Key Features**
Automated Dataset Profiling
The system analyzes the uploaded dataset and extracts:
number of rows and columns
column names and data types
missing value percentages
unique values per column
duplicate row detection
inferred column roles (numerical, categorical, temporal, text)

This provides an instant overview of the dataset structure.

**Privacy Risk Detection**

The system scans datasets for sensitive information using regex pattern matching and column name hints.

**Detected identifiers include:**

Aadhaar numbers
PAN numbers
Voter IDs
phone numbers
email addresses
passport numbers
driving license numbers

**This feature helps identify privacy risks before the dataset is used in machine learning pipelines.**

The design aligns with the requirements of the Indian Digital Personal Data Protection (DPDP) Act 2023.

**Data Quality Assessment**

The agent calculates a Data Quality Score based on:

missing values
schema consistency
dataset completeness

This score provides a quick indication of whether the dataset is reliable for analysis.

**Machine Learning Readiness Evaluation**

The system evaluates whether the dataset can be used for machine learning.

The evaluation considers:

dataset size
feature availability
missing value ratios
presence of sensitive information
numeric feature distribution

The agent outputs an ML Readiness Score and an explanation.

**Machine Learning Use Case Identification**

Based on the dataset structure, the system identifies potential machine learning tasks such as:

classification
regression
clustering
anomaly detection

**It also suggests suitable algorithms including:**
Logistic Regression
Random Forest
XGBoost
Decision Trees
K-Means
Isolation Forest

**AI Generated Dataset Insights**

The system uses a large language model to generate explanations about the dataset.

These insights include:

dataset description
important patterns in the data
potential data quality issues
suggested machine learning applications
recommended preprocessing steps

This allows non-technical stakeholders to understand the dataset easily.

**System Architecture**

The project follows a modular architecture with separate components for data processing, API services, and visualization.

**Backend**

The backend is built using FastAPI and handles:

dataset ingestion
data profiling
PII detection
ML readiness evaluation
LLM orchestration

The backend runs with Uvicorn.

**Frontend**

The frontend is implemented using Streamlit.

It provides a dashboard where users can:

upload datasets
view dataset structure
inspect privacy risks
analyze data quality
review ML recommendations
visualize data patterns

**Technology Stack**

Programming Language
Python 3.9+

Data Processing
Pandas
NumPy

Backend API
FastAPI
Uvicorn

Frontend Dashboard
Streamlit
Plotly

AI Model
Llama 3.3 70B via Groq Cloud API

**Project Structure
Dataset_Intelligence_Agent**

backend
├── main.py
├── dataset_loader.py
├── data_profiler.py
├── pii_detector.py
├── insight_engine.py
├── ml_readiness.py
├── model_recommender.py
└── dataset_agent.py

frontend
└── streamlit_app.py

requirements.txt
README.md


**Installation**
Clone the repository
git clone https://github.com/Sravan-Chappidi/Dataset_Intelligence_Agent.git
cd Dataset_Intelligence_Agent
Install dependencies
pip install -r requirements.txt

**Configuration**

API keys and environment settings are stored in:

.streamlit/secrets.toml

Add your Groq API key before running the application.

**Running the System**
Both the backend and the Streamlit interface need to be started.

Start the backend service
uvicorn main:app --reload

**API documentation will be available at:**
http://127.0.0.1:8000/docs
Start the Streamlit interface
streamlit run streamlit_app.py

**Dashboard will be available at:**
http://localhost:8501
Example Workflow

Upload a dataset using the Streamlit dashboard

The backend processes the dataset automatically

The system generates:

dataset metadata
privacy risk report
data quality score
ML readiness evaluation
model recommendations
AI generated insights

Results are displayed through the dashboard.

**Example Output**

The system produces a structured intelligence report similar to:

{
  "dataset_metadata": {...},
  "quality_score": 82.5,
  "pii_detection": {...},
  "insights": {...},
  "ml_readiness": {...},
  "model_recommendations": {...},
  "ai_summary": "..."
}
**Potential Applications**

This system can be useful for:

data scientists evaluating new datasets
organizations auditing datasets for privacy risks
ML teams performing dataset readiness checks
research teams exploring public datasets
government or enterprise data compliance workflows

**Author- Sravan Chappidi**
