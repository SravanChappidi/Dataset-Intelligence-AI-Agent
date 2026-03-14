from fastapi import FastAPI, UploadFile, File, HTTPException
from app_logic import DatasetIntelligenceAgent
import io

app = FastAPI(title="Dataset Intelligence API")

agent = DatasetIntelligenceAgent()

@app.get("/")
def home():
    return {"message": "AI Intelligence API is Online"}

@app.post("/analyze")
async def analyze_data(file: UploadFile = File(...)):
    if not (file.filename.endswith('.csv') or file.filename.endswith('.xlsx') or file.filename.endswith('.json')):
        raise HTTPException(status_code=400, detail="Please upload a CSV, XLSX, or JSON file.")

    try:
        content = await file.read()
        
        result = agent.run_master_logic(content, file.filename)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")