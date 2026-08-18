import hashlib,json
class ModelRegistry:
    def __init__(self):self.artifacts={};self.stages={}
    def register(self,job_id:str,metrics:list[dict])->str:
        digest=hashlib.sha256(json.dumps({"job":job_id,"metrics":metrics},sort_keys=True).encode()).hexdigest()[:16]
        self.artifacts[digest]={"job_id":job_id,"metrics":metrics}; self.stages[digest]="candidate"; return digest
    def promote(self,artifact_id:str,min_accuracy:float)->bool:
        item=self.artifacts.get(artifact_id)
        if not item:return False
        accuracy=item["metrics"][-1]["accuracy"] if item["metrics"] else 0
        if accuracy>=min_accuracy:self.stages[artifact_id]="production";return True
        return False
