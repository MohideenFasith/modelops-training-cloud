from enum import Enum
from pydantic import BaseModel,Field
class JobState(str,Enum): queued="queued"; running="running"; succeeded="succeeded"; failed="failed"
class ResourceRequest(BaseModel): gpu:int=Field(0,ge=0,le=8); cpu:int=Field(2,ge=1,le=128); memory_gb:int=Field(4,ge=1,le=1024)
class JobCreate(BaseModel): name:str=Field(min_length=1,max_length=100); epochs:int=Field(5,ge=1,le=1000); learning_rate:float=Field(0.01,gt=0,le=1); resources:ResourceRequest=Field(default_factory=ResourceRequest)
class Job(BaseModel): id:str; name:str; epochs:int; learning_rate:float; resources:ResourceRequest; state:JobState=JobState.queued; metrics:list[dict]=Field(default_factory=list); artifact_id:str|None=None
class PromotionRequest(BaseModel): min_accuracy:float=Field(0.8,ge=0,le=1)
