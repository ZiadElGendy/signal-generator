from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from numpy import sin, pi


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


n = 12 * 1024  # samples
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


plt.plot(t, x)
plt.xlabel ('Time')
plt.ylabel ('Amplitude')
plt.show()


sd.play(x, 3 * 1024)

sleep(6)
