"""
Cppn Module

Consillio
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import torch
import torch.nn.functional as F


class Cppn_model(torch.nn.Module):
    def __init__(self):
        super(Cppn_model, self).__init__()
        self.input_linear = torch.nn.Linear(4,8)
        self.conv = torch.nn.Conv1d(8,8,1)
        self.conv2 = torch.nn.Conv1d(8,8,1)
        self.output = torch.nn.Linear(8,3)

    def forward(self, x):
        x = torch.tanh(self.input_linear(x))
        x = torch.transpose(x,1,2)
        res = x
        x = torch.tanh(self.conv(x) + res)
        x = torch.tanh(self.conv2(x)+ res)
        x = torch.transpose(x,1,2)
        x = torch.tanh(self.output(x))
        return x

def initweights(m):
    if isinstance(m,torch.nn.Linear):
        torch.nn.init.normal_(m.weight.data,0,math.sqrt(1/4))
        torch.nn.init.zeros_(m.bias.data)

    if isinstance(m,torch.nn.Conv1d):
        torch.nn.init.normal_(m.weight.data,0,math.sqrt(1/4))
        torch.nn.init.zeros_(m.bias.data)


class Cppn:
    def __init__(self):
        self.M = Cppn_model()
        self.M.apply(initweights)
    
    def getimg(self, h = 64, w = 64, zoom = 1):
        offset = 0 # add feature later
        xx,yy = np.meshgrid(
            np.linspace(-zoom + offset, zoom + offset, h),
            np.linspace(-zoom + offset, zoom + offset, w)
            )

        roh = np.ones((w,h)) *(np.tanh(xx)+np.sin(yy)**2)
        apl = np.ones((w,h)) * 1

        #combine inputs
        z = np.array([xx,yy,roh,apl])
        #rearange

        zT=np.transpose(z,(2,1,0))
        result = self.M(torch.Tensor(zT))

        return result

    def NormNP(self,img):
        """
        Img :: Tensor 
        """
        resultScaled = (img.detach().numpy() + 1.0)/2.0 * 255
        return np.uint8(resultScaled)


    def __call__(self,h = 64, w = 64, zoom = 10):
        return self.NormNP(self.getimg(h,w,zoom))



def output():
    M = Cppn()
    r = M(800,800,zoom=1.73205080)
    plt.imshow(r)
    plt.show()

if __name__=="__main__":
    output()

