from .models import Job
class Scheduler:
    def __init__(self,gpus:int=1,cpus:int=16,memory_gb:int=64): self.capacity=(gpus,cpus,memory_gb)
    def fits(self,job:Job)->bool:
        g,c,m=self.capacity; r=job.resources
        return r.gpu<=g and r.cpu<=c and r.memory_gb<=m
