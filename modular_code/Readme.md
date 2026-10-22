# Pytorch

- PyTorch is an open source machine learning library for Python and is completely based on Torch. 
- It is primarily used for applications such as natural language processing
- PyTorch redesigns and implements Torch in Python while sharing the same core C libraries for the backend code.
- PyTorch developers tuned this back-end code to run Python efficiently. They also kept the GPU based hardware acceleration as well as the extensibility features that made Lua-based Torch.

## Tensors

Tensors are simply mathematical objects that can be used to describe physical properties, just like scalars and vectors. In fact tensors are merely a generalisation of scalars and vectors
- When we represent data for machine learning, this generally needs to be done numerically. 
- Especially when referring specifically of neural network data representation, this is accomplished via a data repository known as the tensor.
- A tensor is a container which can house data in N dimensions. Often and erroneously used interchangeably with the matrix (which is specifically a 2-dimensional tensor). 
- Tensors are generalizations of matrices to N-dimensional space

## PyTorch Tensors

- Tensors are the workhorse of PyTorch. We can think of tensors as multi-dimensional arrays. PyTorch has an extensive library of operations on them provided by the torch module
- PyTorch Tensors are very close to the very popular NumPy arrays . In fact, PyTorch features seamless interoperability with NumPy.
- Compared with NumPy arrays, PyTorch tensors have added advantage that both tensors and related operations can run on the CPU or GPU. 
- The second important thing that PyTorch provides allows tensors to keep track of the operations performed on them that helps to compute gradients or derivatives of an output with respect to any of its inputs.


## Code Description


    File Name : Engine.py
    File Description : Main class for starting different parts and processes of the lifecycle


    File Name : Arithmetic.py
    File Description : Code to do arithmetic operations in tensor
    
    File Name : Gradient.py
    File Description : Code to do Gradient operations in tensor


## Steps to Run

There are two ways to execute the end to end flow.

- Modular Code
- IPython

### Modular code

- Create virtualenv
- Install requirements `pip install -r requirements.txt`
- Run Code `python Engine.py`
- Check output for all the visualization

### IPython Google Colab

Follow the instructions in the notebook `Tensors_Notebook.ipynb`

