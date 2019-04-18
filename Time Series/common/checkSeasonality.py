import matplotlib.pyplot as plt
import math
from scipy import signal
import numpy as np

def checkSeasonality(ts):
    f, Pxx_den = signal.periodogram(ts, fs=60.0)
    plt.semilogy(f[:60], Pxx_den[:60])
    plt.ylim([1e10, 1e15])
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()