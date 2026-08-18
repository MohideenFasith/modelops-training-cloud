import math

def train(epochs:int,learning_rate:float)->list[dict]:
    rows=[]
    for epoch in range(1,epochs+1):
        # Smooth deterministic curve approximating a converging classifier.
        loss=max(0.02,math.exp(-learning_rate*8*epoch))
        accuracy=min(0.995,0.5+(1-loss)*0.5)
        rows.append({"epoch":epoch,"loss":round(loss,6),"accuracy":round(accuracy,6)})
    return rows
