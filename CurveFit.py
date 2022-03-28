from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def cur_exp(x, k1, k2, k3):
    if 0.0<=x<=50.0:
        y = k1 * x
    elif 50.0<x<=70.0:
        y = k2 * (x-50.0)
    elif 70.0<x<=100.0:
        y = k3 * (x-100.0)
    else:
        y=x
    return y

def function1(xs, k1 , k2, k3):
    result = [cur_exp(x, k1 , k2, k3) for x in xs]
    return result

if __name__ == "__main__":
    # xs = np.linspace(0, 100, 101)
    # actual_parameters = [1, 2, -1]
    # print(function1(xs, *actual_parameters))

    x = np.linspace(0, 100, 101)
    actual_parameters = [1, 2, -1]
    y = function1(x, *actual_parameters)
    p = plt.plot(x,y)
    # plt.show()

    from scipy.stats import norm
    y_noisy = y            + 0.8 * norm.rvs(size=len(x))
    p = plt.plot(x, y, 'k-')
    p = plt.plot(x, y_noisy, 'rx')

    # plt.show()
    p_est, err_est = curve_fit(function1, x, y_noisy)


    print(p_est)
    p = plt.plot(x, y_noisy, "rx")
    p = plt.plot(x, function1(x, *p_est), "k--")