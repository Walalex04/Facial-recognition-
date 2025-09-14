

#using the first model that is a model of CNN
from recognition import Yolo

import torch 

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"The model will be stored in {device} device")

model = Yolo()

print(model)
