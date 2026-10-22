
import torch



class Arithmetic:

    def operations(self, x):
        # ### Add and Subtract

        # add
        x2 = torch.add(x, x)
        print(x2)
        print('x2 shape: {} \n'.format(x2.shape))

        # In[21]:

        x2 = x + x
        print(x2)
        print('x2 shape: {}'.format(x2.shape))

        # subtract
        x_2 = torch.subtract(x, x)
        print(x_2)
        print('x_2 shape: {} \n'.format(x_2.shape))

        x_2 = x - 2 * x
        print(x_2)
        print('x_2 shape: {}'.format(x_2.shape))

        # ### Multiply

        # element wise multiplication
        x_mult = x[0:5, :] * x[0:5, :]
        print(x_mult.shape)

        print(x_mult)

        # matrix multiplication of sliced tensor with transpose of it
        x_matmult = x[0:5, :] @ x[0:5, :].T
        print(x_matmult.shape)
        # 5 X 3 | 3 X 5

        print(x_matmult)

        # ### Trigonometric Operations

        # %% All trignonometric functions can be performed on tensors
        # the values are considered in radians

        x_cos = torch.cos(x[:5, :])
        print(x_cos)

        x_sin = torch.sin(x[:5, :])
        print(x_sin)

        # ### Statistics

        # %% math operations for statistics

        # calculate mean value of the number of weekly_mins_watched, minimum daily mins
        x_mean = x.mean(dim=0)
        print(x_mean)

        # calculate mean value of the number of weekly_mins_watched, minimum daily mins
        x_median = x.median(dim=0)
        print(x_median)
