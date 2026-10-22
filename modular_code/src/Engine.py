#!/usr/bin/env python
# coding: utf-8

# # Pytorch: Tensors
# 
# ---
# 
# 
# 
# ### Contents:
# 1. Create tensor
# 2. Tensor attributes
# 3. Arithmetic operations
# 4. Trigonometric operations
# 5. Functions using tensors
# 6. Gradients
# 
# 
# ---
# 
# 

# ### 0. Import required libraries and prepare data


import torch
import pandas as pd
from MLPipeline.Arithmetic import Arithmetic
from MLPipeline.Gradient import Gradient


# ### 1. create tensors

# #### 1-D tensor

# one dimensional tensor
x_list = [1,2,3]
x = torch.tensor(x_list)
print(x)


# #### attributes of a tensor

# shape
print('tensor shape: ',x.shape)


# data type
print('tensor data type: ',x.dtype)

# device for operation
print('tensor operations on device: ',x.device)


# #### 2-D tensor (also called matrix)

x_list = [[1,2,3],[4,5,6]]
x = torch.tensor(x_list)

# tensor attributes
# shape
print('tensor shape: ',x.shape)
# data type
print('tensor data type: ',x.dtype)
# device for operation
print('tensor operations on device: ',x.device)


# #### 3-D Tensor

# three dimensional array: tensor (>=3 dimensions)
x_list = [[[1],[2]],[[3], [4]],[[5],[6]]]
x = torch.tensor(x_list)

# shape
print('tensor shape: ',x.shape)
# data type
print('tensor data type: ',x.dtype)
# device for operation
print('tensor operations on device: ',x.device)


# #### empty tensor

# create empty tensor
x = torch.ones((6))
print('empty tensor \n', x)

# modify tensor through indexing and assignment
for i in range(6):
    x[i] = x[i]+3
    
print('modified tensor \n', x)


# ## Creating tensors from Dataset

#%% convert features of a dataset into tensor
data_path = "../Input"
# read dataset stored as csv using pandas
file_path = data_path + '/churn_data.csv'
# read csv file
df = pd.read_csv(file_path)
# features of the dataset
columns_names = df.columns.values
print('The dataset has {} attributes : \n {}'.format(len(columns_names), columns_names))


# create tensor using the weekly_mins_watched feature in the dataset
x = torch.tensor(df[['weekly_mins_watched', 'minimum_daily_mins',"maximum_daily_mins"]].values)


# tensor shape
print(x.shape)


print(x.dtype)



# ## Arithmetic operations
Arithmetic().operations(x)

# Gradient
# Gradient
Gradient().compute(df)

