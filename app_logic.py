import pandas as pd
import io
import re
import json
from groq import Groq
import streamlit as st

# DATA PROCESSING

class DatasetLoader:
    @staticmethod
    def load(file_bytes, filename) -> pd.DataFrame:
        stream = io.BytesIO(file_bytes)
        if filename.endswith('.csv'): return pd.read_csv(stream)
        elif filename.endswith('.json'): return pd.read_json(stream)
        elif filename.endswith('.xlsx'): return pd.read_excel(stream, engine='openpyxl')
        else: raise ValueError("Unsupported format. Use CSV, JSON, or XLSX.")

class DataProfiler:
    def profile(self, df: pd.DataFrame) -> dict:
        num_rows, num_cols = int(df.shape[0]), int(df.shape[1])
        missing_cells = int(df.isnull().sum().sum())
        quality_score = float(max(0, 100 - (missing_cells / (df.size) * 100))) if df.size else 0
        
        schema = {}
        for col in df.columns:
            dtype = str(df[col].dtype)
            unique = int(df[col].nunique())
            missing = int(df[col].isnull().sum())
            
            if 'datetime' in dtype: role = "Temporal"
            elif unique < 15 and num_rows > 30: role = "Categorical"
            elif 'int' in dtype or 'float' in dtype: role = "Numerical"
            else: role = "Text / ID"

            schema[str(col)] = {
                "dtype": dtype, "role": role,
                "missing_pct": float(round((missing / num_rows) * 100, 2)) if num_rows else 0,
                "unique_values": unique
            }
        return {"metadata": {"rows": num_rows, "columns": num_cols}, "schema": schema, "quality_score": round(quality_score, 2)}

class PIIDetector:
    def __init__(self):
        self.patterns = {
            "Aadhaar": r'\b[2-9]{1}[0-9]{3}\s?[0-9]{4}\s?[0-9]{4}\b',
            "PAN": r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b',
            "Indian_Phone": r'(?:\+91|0)?[6789]\d{9}',
            "Email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        }

    def detect(self, df: pd.DataFrame) -> dict:
        pii_results = {}
        sample = df.head(50).astype(str)
        for col in df.columns:
            matches = set()
            if any(hint in col.lower() for hint in ['aadhaar', 'pan', 'phone', 'email']): matches.add("Header Match")
            for val in sample[col]:
                for pii_type, pat in self.patterns.items():
                    if re.search(pat, val): matches.add(pii_type)
            if matches: pii_results[str(col)] = list(matches)
        return pii_results

# ANALYTICS & AI WORKERS

class MLReadinessAssessor:
    def assess(self, profile, pii) -> dict:
        score = 80
        reasons = []
        if profile['quality_score'] < 70:
            score -= 30
            reasons.append("Low data quality.")
        if pii:
            score -= 10
            reasons.append("Contains PII (needs masking per DPDP Act).")
        level = "High" if score > 70 else "Moderate" if score > 40 else "Low"
        return {"score": int(score), "level": level, "reasons": reasons}

class LLMInsightGenerator:
    def __init__(self):
        self.client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        self.model_name = "llama-3.3-70b-versatile"

    def generate(self, summary_json) -> str:
        prompt = f"""
        You are a Senior Indian Data Scientist. Analyze this dataset metadata:
        {json.dumps(summary_json, indent=2)}

        Provide a professional report with:
        1. Dataset Overview
        2. Strategic Insights (Indian business context)
        3. Data Quality & PII Risks (Mention DPDP Act if PII exists)
        4. ML Model Strategy (Why these specific algorithms?)
        """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model_name,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Llama AI Error: {str(e)}"



class DatasetIntelligenceAgent:
    def __init__(self):
        self.loader = DatasetLoader()
        self.profiler = DataProfiler()
        self.pii_detector = PIIDetector()
        self.ml_assessor = MLReadinessAssessor()
        self.llm = LLMInsightGenerator()
        print("✅ Engine Ready")

    def run_master_logic(self, file_bytes, filename):
        # Load & Profile
        df = self.loader.load(file_bytes, filename)
        profile = self.profiler.profile(df)
        pii = self.pii_detector.detect(df)
        
        # Assess ML Readiness score of the dataset
        ml_report = self.ml_assessor.assess(profile, pii)

        # Generate AI Report
        summary = {
            "metadata": profile['metadata'],
            "quality": profile['quality_score'],
            "pii_detected": pii,
            "ml_readiness": ml_report
        }
        ai_insight = self.llm.generate(summary)

        return {
            "status": "success",
            "filename": filename,
            "quality_score": profile['quality_score'],
            "health": profile, 
            "pii_found": pii,
            "ml_readiness": ml_report,
            "ai_report": ai_insight
        }