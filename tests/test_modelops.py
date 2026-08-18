from modelops.models import JobCreate,ResourceRequest
from modelops.service import ModelOpsService

def test_training_and_promotion():
    s=ModelOpsService();j=s.create(JobCreate(name="baseline",epochs=20,learning_rate=.05))
    done=s.run(j.id);assert done.state.value=="succeeded" and done.artifact_id
    assert s.registry.promote(done.artifact_id,.8) is True

def test_resource_gate():
    s=ModelOpsService();j=s.create(JobCreate(name="too-big",resources=ResourceRequest(gpu=8)))
    assert s.run(j.id).state.value=="failed"
