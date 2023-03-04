import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.utils.data import Dataset, DataLoader
from torchsummary import summary

import numpy as np
import pandas as pd
import random
from glob import glob
import os, shutil
import gc
from PIL import Image
from typing import Dict, List, Tuple, Any, Optional
from collections import namedtuple, defaultdict
import copy

import cv2
import matplotlib.pyplot as plt

from sklearn.model_selection import KFold, StratifiedKFold, StratifiedGroupKFold

import segmentation_models_pytorch as smp
import piqa
import albumentations as A
from albumentations.pytorch import ToTensorV2
import wandb
from tqdm import tqdm
tqdm.pandas()

from colorama import Fore, Back, Style
c_  = Fore.GREEN
sr_ = Style.RESET_ALL

import warnings
warnings.filterwarnings("ignore")

from config import config
from dataset import Pix2PixRNNDataset
from engine import run_training
from model import Pix2PixRNN


if __name__ == '__main__':
    df = pd.read_csv('../../images.csv')
    train_df = df.iloc[:500]
    valid_df = df.iloc[500:]
    
    train_dataset = Pix2PixRNNDataset(df=train_df, window_size=6)
    valid_dataset = Pix2PixRNNDataset(df=valid_df, window_size=6)

    train_loader = DataLoader(dataset=train_dataset, batch_size=config.train_bs)
    valid_loader = DataLoader(dataset=valid_dataset, batch_size=config.valid_bs)
    
    run_training(trainloader=train_loader, validloader=valid_loader)
