from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np


def function(x, a , b, f, phi):
    """a function of x with four parameters"""
    result = a * np.exp(-b * np.sin(f * x + phi))
    return result


x = np.linspace(0, 2 * np.pi, 50)
actual_parameters = [3, 2, 1.25, np.pi / 4]
y = function(x, *actual_parameters)
p = plt.plot(x,y)
# plt.show()

from scipy.stats import norm
y_noisy = y #+ 0.8 * norm.rvs(size=len(x))
p = plt.plot(x, y, 'k-')
p = plt.plot(x, y_noisy, 'rx')

# plt.show()
p_est, err_est = curve_fit(function, x, y_noisy)


print(p_est)
p = plt.plot(x, y_noisy, "rx")
p = plt.plot(x, function(x, *p_est), "k--")