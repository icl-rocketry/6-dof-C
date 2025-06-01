import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class param_approx_boattail_NN(nn.module): # NN to approximate each part parameter (this one for the boat tail)
    def __init__(self,state_dim,out_dim):
        super(param_approx_boattail_NN,self).__init__
        self.layer1 = nn.Linear(state_dim,128)
        self.layer2 = nn.Linear(128,128)
        self.layer3 = nn.Linear(128,64)
        self.layer4 = nn.Linear(64,out_dim)
        def forward(self,x):
            x = torch.relu(self.layer1(x))
            x = torch.relu(self.layer2(x))
            x = torch.relu(self.layer3(x))
            return self.layer4(x)
    

    

    



