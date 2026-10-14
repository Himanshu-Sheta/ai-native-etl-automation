from fastapi import FastAPI
from backend.pipeline import AIEtlEngine, ETLJobPayload

app = FastAPI(
    title="AI-Native ETL Automation Platform",
    description="Automated enterprise ETL processing, data validation, and LLM-assisted anomaly explanation.",
    version="1.0.0"
)

engine = AIEtlEngine()

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ai-native-etl-engine"}

@app.post("/api/v1/etl/run")
def run_etl_pipeline(payload: ETLJobPayload):
    result = engine.execute_etl(payload)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.server:app", host="0.0.0.0", port=8000, reload=True)
