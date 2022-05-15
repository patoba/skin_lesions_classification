import torch as nn

class RedNeuronal(nn.model):
    def __init__(self, num_classes):
        self.model = nn.Sequential(
          nn.Conv2d(3, 6, (5, 5), padding=2),
          nn.ReLU(),
          nn.Conv2d(6, 16, (5, 5)),
          nn.ReLU(), 
          nn.Linear(16 * 54 * 54, 120), 
          nn.ReLU(), 
          nn.Linear(120, 84), 
          nn.ReLU(), 
          nn.Linear(84, num_classes)
        )

    def forward(self, x):
        logits = self.model(x)
        return logits

