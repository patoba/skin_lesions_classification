import torch.nn as nn
from torch.nn import functional as F
import torch.optim as optim

from preprocesamiento import class_weights

class RedNeuronal(nn.Module):
    def __init__(self, num_classes):
        super(RedNeuronal, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, (5, 5), padding=2)
        self.conv2 = nn.Conv2d(6, 16, (5, 5))
        self.fc1   = nn.Linear(16 * 54 * 54, 120)
        self.fc2   = nn.Linear(120, 84)
        self.fc3   = nn.Linear(84, num_classes)
        
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
        
    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

net = RedNeuronal(len(class_weights)).to("cuda")
criterion = nn.CrossEntropyLoss(weight = class_weights).cuda()
optimizer = optim.Adam(net.parameters(), lr=1e-5)