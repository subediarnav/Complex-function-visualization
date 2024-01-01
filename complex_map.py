import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import sympy as sy

def return_reals(n):
    x = np.linspace(-1, 1, n)
    y = np.linspace(-1, 1, n)
    return x, y

def create_complex(x, y):
    c_input = []
    for i in x:
        for k in y:
            c_input.append(complex(i,k))
    input_real = [a.real for a in c_input]
    input_imag = [a.imag for a in c_input]
    return c_input, input_real, input_imag

def f(c_input):
    c_output = [np.arctan(np.log(z)) for z in c_input]
    output_real = [a.real for a in c_output]
    output_imag = [a.imag for a in c_output]
    return c_output, output_real, output_imag

def create_plots(input_real, input_imag, output_real, output_imag):
    plt.rc('axes', axisbelow=True)
    fig, ax = plt.subplots(1, 2, figsize = (8,4), squeeze=False)
    ax[0][0].scatter(input_real, input_imag, s = 7, color = "black")
    ax[0][0].set_xticks(input_real)
    ax[0][0].set_yticks(input_imag)
    ax[0][0].set_title("Input space")
    ax[0][0].grid()
    ax[0][0].set_xticklabels([])
    ax[0][0].set_yticklabels([])
    ax[0][0].set_xlim([-1.125,1.125])
    ax[0][0].set_ylim([-1.125,1.125])

    ax[0][1].scatter(output_real, output_imag, s = 7, color = "black")
    ax[0][1].set_xticks(input_real)
    ax[0][1].set_yticks(input_imag)
    ax[0][1].set_title("Output space")
    ax[0][1].grid()
    ax[0][1].set_xticklabels([])
    ax[0][1].set_yticklabels([])
    # ax[0][1].set_xlim([-1.125,1.125])
    # ax[0][1].set_ylim([-1.125,1.125])

    plt.show()


def main(n):
    x, y = return_reals(n)
    c_input, input_real, input_imag = create_complex(x,y)
    c_output, output_real, output_imag = f(c_input)
    create_plots(input_real, input_imag, output_real, output_imag)

main(30)