# Pytorch Tensor Practice

- To give brief introductions to Tensors - To understand the working of Pytorch and tensors operations in it

## Overview
Pytorch is one of the deep learning frameworks developed by Facebook(Meta). It is an open-source machine learning library based on Torch. Pytorch tensors are very similar to Numpy arrays with GPU support, making the coding fast and efficient. Tensors are generalizations of scalars, vectors, and matrices to an arbitrary number of indices and are understood as multi-dimensional arrays. Tensors are building blocks for any machine learning algorithm. This project introduces the Pytorch library and various tensors operations in it.

Why Pytorch?
- Easy to learn and simpler to code
- Support of computational graphs at run time
- Reach set of libraries
- It is flexible, faster, and provides better optimization
- Support of both CPU and GPU
- Easy to debug using Python IDEs

Applications
- Image Classification
- Handwriting recognition
- Text generation
- Forecast time sequence
- Style transfer

## Data
The dataset used in this project has information about the customer churn based on the various features. The dataset contains 2000 rows and 15 features to predict the churn.

_Data is not included in this repository._

## Approach
- Creating tensors
- Creating tensors from the dataset
- Arithmetic, Trigonometric operations
- Statistical operations
- Functions operations
- Gradient calculation

Modular Codes Overview:

Once you unzip the tesnors_part1.zip file, you can find the following folders within it.
1. Input
2. Notebook
3. src
4. Readme.md
5. requirements.txt
1. The input folder contains the data that we have for analysis. In our case, it contains churn_data.csv
2. The Notebook folder contains the jupyter notebook file of the project.
3. The src folder is the heart of the project. This folder contains all the modularized code for all the above steps in a modularized manner. It further includes the following. a. ML_pipeline b. Engine.py

The ML_pipeline is a folder that contains all the functions put into different python files, which are appropriately named. These python functions are then called inside the Engine.py file.

4. The requirements.txt file has all the required libraries with respective versions. Kindly install the file by using the command pip install -r requirements.txt
5. All the instructions for running the code are present in Readme.md file

## Tech stack
➔ Language: Python ➔ Libraries: Pandas, Pytorch

## How to run
```bash
pip install -r modular_code/requirements.txt
```
Notebooks: [`Tensors_Notebook.ipynb`](Tensors_Notebook.ipynb)

## Project structure
```
.gitignore
README.md
Solution Methodology.pdf
Tensors_Notebook.ipynb
data.zip
modular_code.zip
modular_code/
  Readme.md
  requirements.txt
  src/
    Engine.py
    MLPipeline/
```

## Credits
Based on a ProjectPro guided project.
