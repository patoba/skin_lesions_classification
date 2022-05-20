import torch.nn as nn
from torch.nn import functional as F
import torch.optim as optim
import torch

import pytorch_lightning as pl
import torchmetrics

class RedNeuronal(pl.LightningModule):
    def __init__(self, class_weights):
        super(RedNeuronal, self).__init__()
        self.class_weights = torch.FloatTensor(class_weights)

        self.accuracy = torchmetrics.Accuracy()
        self.f1 = torchmetrics.F1Score()
        self.accuracy_val = torchmetrics.Accuracy()
        self.f1_val = torchmetrics.F1Score()
        self.conv1 = nn.Conv2d(3, 6, (5, 5), padding=2)
        self.conv2 = nn.Conv2d(6, 16, (5, 5))
        self.fc1   = nn.Linear(16 * 54 * 54, 120)
        self.fc2   = nn.Linear(120, 84)
        self.fc3   = nn.Linear(84, len(class_weights))

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        print(y_hat.device)
        loss = F.cross_entropy(y_hat, y, 
                               weight = self.class_weights.type_as(x))
        self.log("train_loss_step", loss, on_epoch=True)
        self.accuracy(y_hat, y)
        self.log("train_acc_step", self.accuracy, on_epoch=True)
        self.f1(y_hat, y)
        self.log("train_f1_step", self.f1, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y, 
                               weight = self.class_weights.type_as(x))
        self.log("val_loss", loss)
        self.accuracy_val(y_hat, y)
        self.log("val_acc_step", self.accuracy_val, on_epoch=True)
        self.f1_val(y_hat, y)
        self.log("val_f1_step", self.f1_val, on_epoch=True)
        return y_hat

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr = 0.02)

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
