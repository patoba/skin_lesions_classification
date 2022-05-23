import numpy as np

from sklearn.utils.class_weight import compute_class_weight

import torch
import torchvision
from torchvision import transforms
from torch.utils.data.sampler import SubsetRandomSampler

from sampleo import StratifiedSampler
from constantes import test_size, dest_dir, val_size, shape, norm_mean, \
                        norm_std, batch_size, validation_batch_size
from lectura_data import metadata

y = metadata["label"].unique()

class_weights = compute_class_weight(class_weight = "balanced",
                                    classes = np.unique(y),
                                    y = list(metadata["label"]))

transform_train = transforms.Compose([
                    transforms.Resize(shape),
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomRotation(degrees=60),
                    transforms.ToTensor(),
                    transforms.Normalize(norm_mean, norm_std),
                    ])

transform_test = transforms.Compose([
                    transforms.Resize(shape),
                    transforms.ToTensor(),
                    transforms.Normalize(norm_mean, norm_std),
                    ])

dataset = torchvision.datasets.ImageFolder(root = dest_dir)
data_label = [s[1] for s in dataset.samples]

ss = StratifiedSampler(torch.FloatTensor(data_label), test_size)
pre_train_indices, test_indices = ss.gen_sample_array()

train_label = np.delete(data_label, test_indices, None)
ss = StratifiedSampler(torch.FloatTensor(train_label), val_size)
train_indices, val_indices = ss.gen_sample_array()

indices = {'train': pre_train_indices[train_indices],  
           'val': pre_train_indices[val_indices],  
           'test': test_indices
           }

train_indices = indices['train']
val_indices = indices['val']
test_indices = indices['test']

dataset = torchvision.datasets.ImageFolder(root= dest_dir, 
                                            transform=transform_train)

train_samples = SubsetRandomSampler(train_indices)
val_samples = SubsetRandomSampler(val_indices)
test_samples = SubsetRandomSampler(test_indices)

train_data_loader = torch.utils.data.DataLoader(dataset, 
                            batch_size = batch_size, shuffle=False,
                            num_workers = 1, sampler = train_samples)
validation_data_loader = torch.utils.data.DataLoader(dataset, 
                            batch_size = validation_batch_size, 
                            shuffle = False, sampler = val_samples)

dataset = torchvision.datasets.ImageFolder(root = dest_dir, 
                                           transform = transform_test)
test_data_loader = torch.utils.data.DataLoader(dataset, 
                                            batch_size = validation_batch_size, 
                                            shuffle=False, sampler=test_samples)

