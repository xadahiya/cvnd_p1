## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        
        ## Input 224
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.a1 = nn.ELU()
        self.mp1 = nn.MaxPool2d(2)
        self.drop1 = nn.Dropout(p=0.2)
        
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.a2 = nn.ELU()
        self.mp2 = nn.MaxPool2d(2)
        self.drop2 = nn.Dropout(p=0.2)
        
        self.conv3 = nn.Conv2d(64, 128, 5)
        self.a3 = nn.ELU()
        self.mp3 = nn.MaxPool2d(2)
        self.drop3 = nn.Dropout(p=0.3)
        
        self.conv4 = nn.Conv2d(128, 256, 5)
        self.a4 = nn.ELU()
        self.mp4 = nn.MaxPool2d(2)
        self.drop4 = nn.Dropout(p=0.4)

        self.flatten = nn.Flatten()

        self.dense1 = nn.Linear(25600, 1000)
        self.a5 = nn.ReLU()
        self.drop5 = nn.Dropout(p=0.5)
        self.dense2 = nn.Linear(1000, 136)
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        x = self.drop1(self.mp1(self.a1(self.conv1(x))))
        x = self.drop2(self.mp2(self.a2(self.conv2(x))))
        x = self.drop3(self.mp3(self.a3(self.conv3(x))))
        x = self.drop4(self.mp4(self.a4(self.conv4(x))))
        x = self.flatten(x)
        x = self.drop5(self.a5(self.dense1(x)))
        x = self.dense2(x)
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
