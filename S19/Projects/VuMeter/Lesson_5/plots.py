import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 16,9
mpl.rcParams['font.size'] = 22
mpl.rcParams['axes.grid'] = True

noise_freq = 2*np.pi*10
signal_freq= 2*np.pi*1

ts = np.linspace(0,5,1000)
noise = 0.1*np.sin(noise_freq*ts)
signal = 0.1*np.sin(signal_freq*ts)
noisy = signal+noise

plt.subplot(311)
plt.plot(ts, noise, label='Noise')
plt.legend()
plt.subplot(312)
plt.plot(ts, signal, label='Signal')
plt.legend()
plt.subplot(313)
plt.plot(ts, noisy, label='Noisy Wave')
plt.legend()
plt.tight_layout()
plt.savefig('noisy_wave.png')
plt.clf()

num_samples = 50
low_signal = np.zeros_like(signal)
moving_average = np.mean(noisy[:num_samples])
for i in range(num_samples, 1000):
    low_signal[i] = moving_average
    moving_average = moving_average + (noisy[i] - noisy[i-num_samples])/num_samples

plt.plot(ts, low_signal, label='Cleaner Wave')
plt.legend()
plt.savefig('cleaner_wave.png')
