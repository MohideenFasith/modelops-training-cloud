from uuid import uuid4
from .models import Job,JobCreate,JobState
from .scheduler import Scheduler
from .trainer import train
from .registry import ModelRegistry
class ModelOpsService:
    def __init__(self):self.jobs={};self.scheduler=Scheduler();self.registry=ModelRegistry()
    def create(self,cfg:JobCreate)->Job:
        j=Job(id=str(uuid4()),**cfg.model_dump());self.jobs[j.id]=j;return j
    def get(self,jid):
        if jid not in self.jobs:raise KeyError(jid)
        return self.jobs[jid]
    def run(self,jid)->Job:
        j=self.get(jid)
        if not self.scheduler.fits(j):j.state=JobState.failed;return j
        j.state=JobState.running;j.metrics=train(j.epochs,j.learning_rate);j.artifact_id=self.registry.register(j.id,j.metrics);j.state=JobState.succeeded;return j
