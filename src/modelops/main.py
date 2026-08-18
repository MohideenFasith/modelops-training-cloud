from fastapi import FastAPI,HTTPException
from .models import JobCreate,PromotionRequest
from .service import ModelOpsService
app=FastAPI(title="ModelOps Training Cloud",version="0.1.0");service=ModelOpsService()
@app.get("/health")
def health():return {"status":"ok"}
@app.post("/jobs",status_code=201)
def create(c:JobCreate):return service.create(c)
@app.get("/jobs/{jid}")
def get(jid:str):
    try:return service.get(jid)
    except KeyError:raise HTTPException(404,"job not found")
@app.post("/jobs/{jid}/run")
def run(jid:str):
    try:return service.run(jid)
    except KeyError:raise HTTPException(404,"job not found")
@app.post("/artifacts/{aid}/promote")
def promote(aid:str,p:PromotionRequest):
    if aid not in service.registry.artifacts:raise HTTPException(404,"artifact not found")
    ok=service.registry.promote(aid,p.min_accuracy);return {"promoted":ok,"stage":service.registry.stages[aid]}
