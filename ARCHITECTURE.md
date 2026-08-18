# Architecture

ModelOps models a training control plane: jobs are scheduled against resource requests, trainers emit deterministic metric histories, artifacts are registered by content digest, and promotion is gated by validation metrics. The local runner is deliberately deterministic for tests; production adapters can map jobs to Kubernetes, Slurm or managed GPU services.
