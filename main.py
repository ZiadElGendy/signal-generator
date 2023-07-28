import math
from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from numpy import sin, pi
from scipy.fftpack import fft

# Constants
# Notes in 4th octave
C = 2 * pi * 130
Db = 2 * pi * 138
D = 2 * pi * 146
Eb = 2 * pi * 155
E = 2 * pi * 164
F = 2 * pi * 174
Gb = 2 * pi * 185
G = 2 * pi * 196
Ab = 2 * pi * 208
A = 2 * pi * 220
Bb = 2 * pi * 233
B = 2 * pi * 246

# Time
bar = 3
quarterNote = bar / 4
eighthNote = bar / 8
sixteenthNote = bar / 16
thirtySecondNote = bar / 32


n = 3 * 1024  # samples
f = np.linspace(0, 512, int(n / 2))  # frequency

t = np.linspace(0, 3, n)  # time
x = np.zeros(n)  # signal


melody = 0.5 * sin(D * t) * ((t >= 0) & (t <= thirtySecondNote))
x = x + melody

melody = 0.5 * sin(D * t) * ((t >= sixteenthNote) & (t <= 3 * thirtySecondNote))
x = x + melody

melody = 0.5 * sin(2 * D * t) * ((t >= 2 * sixteenthNote) & (t <= 3 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(A * t) * ((t >= 4 * sixteenthNote) & (t <= 5 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(Ab * t) * ((t >= 7 * sixteenthNote) & (t <= 8 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(G * t) * ((t >= 9 * sixteenthNote) & (t <= 10 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(F * t) * ((t >= 11 * sixteenthNote) & (t <= 12 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(D * t) * ((t >= 13 * sixteenthNote) & (t <= 14 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(F * t) * ((t >= 14 * sixteenthNote) & (t <= 15 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(G * t) * ((t >= 15 * sixteenthNote) & (t <= 16 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(D * t / 2) * ((t >= 13 * sixteenthNote) & (t <= 14 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(F * t / 2) * ((t >= 14 * sixteenthNote) & (t <= 15 * sixteenthNote))
x = x + melody

melody = 0.5 * sin(G * t / 2) * ((t >= 15 * sixteenthNote) & (t <= 16 * sixteenthNote))
x = x + melody


xFFT = fft(x)
xFFT = 2 / n * np.abs(xFFT[0:int(n / 2)])

plt.plot(t, x)
plt.title("Time domain without noise")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(f, xFFT)
plt.title("Frequency domain without noise")
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()


# adding noise
fn = np.random.randint(0, 512, 2)
fn1 = sin(fn[0] * t * 2 * pi)
fn2 = sin(fn[1] * t * 2 * pi)

x = x + fn1 + fn2

xFFT = fft(x)
xFFT = 2 / n * np.abs(xFFT[0:int(n / 2)])

plt.plot(t, x)
plt.title("Time domain with noise")
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(f, xFFT)
plt.title("Frequency domain with noise")
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()


# filtering noise
xFiltered = x
freq = 0
usedFreq = np.zeros(0)
for i in xFFT:
    if i >= 0.2:
        freq2 = round(freq / 3)

        # print()
        # print(freq / 3)

        if freq2 not in usedFreq:

            # print(freq2)
            # print(xFFT[freq])
            # print(xFFT[freq + 1])
            # print("not in list")

            if xFFT[freq] >= xFFT[freq + 1]:
                # print("selected")
                xFiltered = xFiltered - sin(freq2 * t * 2 * pi)

                usedFreq = np.append(usedFreq, freq2)
                usedFreq = np.append(usedFreq, freq2 + 1)

    freq += 1


xFFT = fft(xFiltered)
xFFT = 2 / n * np.abs(xFFT[0:int(n / 2)])

plt.plot(t, xFiltered)
plt.title("Time domain after filtration")
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()

plt.plot(f, xFFT)
plt.title("Frequency domain after filtration")
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()

sd.play(xFiltered, 4 * 1024)

sleep(6)
