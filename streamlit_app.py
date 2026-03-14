import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json


st.set_page_config(page_title="AI Dataset Agent", layout="wide", page_icon="🤖")

st.title("🤖 Dataset Intelligence AI Agent")
st.markdown("### Automated Audit, Privacy Scanning, and AI Strategy")


with st.sidebar:
    st.header("⚙️ Configuration")
    try:
        health_check = requests.get("http://127.0.0.1:8000/", timeout=2)
        if health_check.status_code == 200:
            st.success("✅ AI Backend Online")
    except:
        st.error("❌ Backend Offline! Run 'uvicorn main:app'")
    
    st.divider()
    uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "xlsx", "json"])


if uploaded_file:
  
    file_ext = uploaded_file.name.split('.')[-1]
    if file_ext == 'csv':
        df_preview = pd.read_csv(uploaded_file)
    elif file_ext == 'xlsx':
        df_preview = pd.read_excel(uploaded_file)
    else:
        df_preview = pd.read_json(uploaded_file)
    
    uploaded_file.seek(0)

    
    if "api_result" not in st.session_state or st.session_state.get("last_file") != uploaded_file.name:
        with st.spinner(f"⚡ Auto-Auditing {uploaded_file.name}..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                response = requests.post("http://127.0.0.1:8000/analyze", files=files)
                
                if response.status_code == 200:
                    st.session_state["api_result"] = response.json()
                    st.session_state["last_file"] = uploaded_file.name
                else:
                    st.error("API Error: Backend logic failed.")
            except Exception as e:
                st.error(f"Connection Error: {e}")

    if "api_result" in st.session_state:
        data = st.session_state["api_result"]
        
        # --- TOP METRICS ---
        m1, m2, m3, m4 = st.columns(4)
        
        health_data = data.get('health', {})
        metadata = health_data.get('metadata', {})
        
        
        m1.metric("Total Rows", metadata.get('rows', 0))
        m2.metric("Total Columns", metadata.get('columns', 0))
        m3.metric("Quality Score", f"{data.get('quality_score', 0)}%")
        
        pii_risks = data.get('pii_found', {})
        pii_count = len(pii_risks)
        m4.metric("PII Detected", "YES" if pii_count > 0 else "NO", 
                  delta=f"{pii_count} risks", delta_color="inverse")

        # --- TABS ---
        tabs = st.tabs(["📄 Preview", "📊 Analysis", "🔒 Privacy", "🧠 AI Report"])

        with tabs[0]:
            st.dataframe(df_preview.head(20), use_container_width=True)

        with tabs[1]:
            st.subheader("Data Health Check")
            st.write("**ML Readiness Assessment:**")
            st.json(data.get('ml_readiness', {}))
            
            if 'schema' in health_data:
                missing_data = pd.DataFrame([
                    {"Column": col, "Missing %": info['missing_pct']} 
                    for col, info in health_data['schema'].items()
                ])
                fig = px.bar(missing_data, x="Column", y="Missing %", title="Missing Data Distribution")
                st.plotly_chart(fig, use_container_width=True)

        with tabs[2]:
            st.subheader("Privacy Scan (DPDP Act Compliance)")
            if data['pii_found']:
                for col, risk in data['pii_found'].items():
                    st.error(f"⚠️ **{col}**: {', '.join(risk)} detected")
            else:
                st.success("Verified: No sensitive Indian PII found.")

        with tabs[3]:
            st.subheader("📋 Dataset Analysis Report")
            st.markdown(data['ai_report'])
            
            st.download_button(
                label="📥 Download AI Strategy Report",
                data=data['ai_report'],
                file_name=f"AI_Strategy_{uploaded_file.name}.txt"
            )
else:
    st.info("Welcome! Please upload a dataset in the sidebar to begin the intelligence audit.")