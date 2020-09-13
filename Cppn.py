"""
Cppn Module

Consillio
"""

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn.functional as F


class Cppn_model(torch.nn.Module):
    def __init__(self):
        super(Cppn_model, self).__init__()
        self.lay=[]
        self.input_linear = torch.nn.Linear(2,8)
        for i in range(1):
            self.lay.append(torch.nn.Linear(8,8))
        self.output = torch.nn.Linear(8,3)

    def forward(self, x):
        x = self.input_linear(x)
        for i in self.lay:
            x = F.relu(x)
            x = i(x)
        x = self.output(x)
        x = torch.tanh(x)
        return x

class Cppn:
    def __init__(self):
        self.M = Cppn_model()
    
    def getimg(self, h = 64, w = 64, zoom = 1):
        offset = 0 # add feature later
        xx,yy = np.meshgrid(
            np.linspace(-zoom + offset, zoom + offset, h),
            np.linspace(-zoom + offset, zoom + offset, w)
            )

        # 3rd parameter
        #roh = np.ones((w,h)) * (xx**2+yy**2)

        #combine inputs
        z = np.array([xx,yy])
        #rearange
        zT=np.transpose(z,(2,1,0))
        result = self.M(torch.Tensor(zT))

        return result

    def NormNP(self,img):
        """
        Img :: Tensor 
        """
        resultScaled = (img.detach().numpy() + 1.0)/2.0
        return resultScaled


    def __call__(self,h = 64, w = 64, zoom = 1):
        return self.NormNP(self.getimg(h,w,zoom))



if __name__=="__main__":
    print("Unit_Test")
    M = Cppn()
    r = M()
    plt.imshow(r)
    plt.show()

