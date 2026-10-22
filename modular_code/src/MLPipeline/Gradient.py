import torch


class Gradient:

    def compute(self, df):
        # ## Functions
        # tensors can be used to create functions

        # ### Example 1:
        # $F(x)$ is a function of $x$
        # $F(x) = x^2 + 2x + 1$

        ### 1-D tensor
        x = torch.ones((6))
        print(x)

        f = x ** 2 + 2 * x + 1
        print(f)

        ### 2-D tensor
        x = torch.ones((3, 2))
        f = x ** 2 + 2 * x + 1
        print(f)

        # ### Example 2:
        # $H(x)$ is a function of $F(x)$
        # $H(x) = 3F(x) + 1$
        h = 3 * f + 1
        print(h)

        # ## Gradients
        # gradients are first order derivates of a function
        #

        # ### Example 1:
        # $F(x)$ is a function of $x$
        # $F(x) = x^2 + 2x + 1$
        #
        # $G(x)$ is the gradient of $F(x)$ with respect to $x$
        # $G(x) = \frac{dF(x)}{dx} = 2(x + 1)$

        # %% gradients are first order derivates of a function

        # create a tensor with gradient tracing enabled
        # tensors should be of floating point type to calculate gradients
        x = torch.tensor(5.0, requires_grad=True)

        # define function
        f = x ** 2 + 2 * x + 1

        # compute gradients
        f.backward()

        # print the gradient value
        print(x.grad)

        # %% computing gradients with respect to a tensor

        # create tensor using  'weekly_mins_watched', 'minimum_daily_mins' features in dataset
        x = torch.tensor(df[['weekly_mins_watched', 'minimum_daily_mins']].values, requires_grad=True)

        # calculate function of x
        y = x ** 2 + 3

        # calculate derivative of y with respect to x
        y.backward(torch.ones_like(x))

        # print x derviative values
        print(x.grad)

        # ### Example 2:

        # $F(x)$ is a function of $x$
        # $F(x) = x^2 + 2x + 1$
        #
        # $H(x)$ is a function of $F(x)$
        # $H(x) = F^2(x) + 1$
        #
        # $G(x)$ is the gradient of $H(x)$ with respect to $x$
        # $G(x) = \frac{dH(x)}{dx} = 4(x + 1)^3$

        x = torch.tensor(1.0, requires_grad=True)

        # define functions
        f = x ** 2 + 2 * x + 1
        h = f ** 2 + 1

        # compute gradients
        h.backward()

        # print the gradient value
        print(x.grad)


