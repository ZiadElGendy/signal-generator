from time import sleep

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy
from numpy import sin, pi
from scipy.signal import square, sawtooth

# Constants

# Time
bar = 5
fourBars = bar * 4
quarterNote = bar / 4
eighthNote = bar / 8
sixteenthNote = bar / 16
thirtySecondNote = bar / 32

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

t = np.linspace(0, 16 * bar, 16 * 12 * 1024)
x = np.zeros(16 * 12 * 1024)

# 16 bar song
for i in range(16):
    # melody
    # starting notes
    if i == 0 or i == 4 or i == 8 or i == 12:
        melody = 0.5 * square(D * t) * ((t >= 0 + (i * bar)) & (t <= thirtySecondNote + (i * bar)))
        x = x + melody

        melody = 0.5 * square(D * t) * ((t >= sixteenthNote + (i * bar)) & (t <= 3 * thirtySecondNote + (i * bar)))
        x = x + melody

    if i == 1 or i == 5 or i == 9 or i == 13:
        melody = 0.5 * square(C * t) * ((t >= 0 + (i * bar)) & (t <= thirtySecondNote + (i * bar)))
        x = x + melody

        melody = 0.5 * square(C * t) * ((t >= sixteenthNote + (i * bar)) & (t <= 3 * thirtySecondNote + (i * bar)))
        x = x + melody

    if i == 2 or i == 6 or i == 10 or i == 14:
        melody = 0.5 * square(B * t / 2) * ((t >= 0 + (i * bar)) & (t <= thirtySecondNote + (i * bar)))
        x = x + melody

        melody = 0.5 * square(B * t / 2) * ((t >= sixteenthNote + (i * bar)) & (t <= 3 * thirtySecondNote + (i * bar)))
        x = x + melody

    if i == 3 or i == 7 or i == 11 or i == 15:
        melody = 0.5 * square(Bb * t / 2) * ((t >= 0 + (i * bar)) & (t <= thirtySecondNote + (i * bar)))
        x = x + melody

        melody = 0.5 * square(Bb * t / 2) * ((t >= sixteenthNote + (i * bar)) & (t <= 3 * thirtySecondNote + (i * bar)))
        x = x + melody

    # repeating notes
    melody = 0.5 * square(2 * D * t) * ((t >= 2 * sixteenthNote + (i * bar)) & (t <= 3 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(A * t) * ((t >= 4 * sixteenthNote + (i * bar)) & (t <= 5 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(Ab * t) * ((t >= 7 * sixteenthNote + (i * bar)) & (t <= 8 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(G * t) * ((t >= 9 * sixteenthNote + (i * bar)) & (t <= 10 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(F * t) * ((t >= 11 * sixteenthNote + (i * bar)) & (t <= 12 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(D * t) * ((t >= 13 * sixteenthNote + (i * bar)) & (t <= 14 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(F * t) * ((t >= 14 * sixteenthNote + (i * bar)) & (t <= 15 * sixteenthNote + (i * bar)))
    x = x + melody

    melody = 0.5 * square(G * t) * ((t >= 15 * sixteenthNote + (i * bar)) & (t <= 16 * sixteenthNote + (i * bar)))
    x = x + melody

    # sub bass
    if i > 3:
        if i == 0 or i == 4 or i == 8 or i == 12:
            subBass = 0.5 * sin(D * t / 2) * ((t >= (i * bar)) & (t <= (i * bar) + bar))
            x = x + subBass

        if i == 1 or i == 5 or i == 9 or i == 13:
            subBass = 0.5 * sin(C * t / 2) * ((t >= (i * bar)) & (t <= (i * bar) + bar))
            x = x + subBass

        if i == 2 or i == 6 or i == 10 or i == 14:
            subBass = 0.5 * sin(B * t / 4) * ((t >= (i * bar)) & (t <= (i * bar) + bar))
            x = x + subBass

        if i == 3 or i == 7 or i == 11 or i == 15:
            subBass = 0.5 * sin(Bb * t / 4) * ((t >= (i * bar)) & (t <= (i * bar) + 1.75 * quarterNote))
            x = x + subBass

            subBass = 0.5 * sin(C * t / 2) * ((t >= (i * bar) + 1.75 * quarterNote) & (t <= (i * bar) + bar))
            x = x + subBass

    if i > 7:

        # drums

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * ((t >= (i * bar)) & (t <= (i * bar) + thirtySecondNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 2 * thirtySecondNote) & (t <= (i * bar) + 3 * thirtySecondNote))
        x = x + noise

        noise = 0.5 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 4 * thirtySecondNote) & (t <= (i * bar) + 5 * thirtySecondNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 6 * thirtySecondNote) & (t <= (i * bar) + 7 * thirtySecondNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + quarterNote) & (t <= (i * bar) + thirtySecondNote + quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 2 * thirtySecondNote + quarterNote) & (
                t <= (i * bar) + 3 * thirtySecondNote + quarterNote))
        x = x + noise

        noise = 0.5 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 4 * thirtySecondNote + quarterNote) & (
                t <= (i * bar) + 5 * thirtySecondNote + quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 6 * thirtySecondNote + quarterNote) & (
                t <= (i * bar) + 7 * thirtySecondNote + quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 2 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 2 * quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 2 * thirtySecondNote + 2 * quarterNote) & (
                t <= (i * bar) + 3 * thirtySecondNote + 2 * quarterNote))
        x = x + noise

        noise = 0.5 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 4 * thirtySecondNote + 2 * quarterNote) & (
                t <= (i * bar) + 5 * thirtySecondNote + 2 * quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 6 * thirtySecondNote + 2 * quarterNote) & (
                t <= (i * bar) + 7 * thirtySecondNote + 2 * quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 3 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 3 * quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 2 * thirtySecondNote + 3 * quarterNote) & (
                t <= (i * bar) + 3 * thirtySecondNote + 3 * quarterNote))
        x = x + noise

        noise = 0.5 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 4 * thirtySecondNote + 3 * quarterNote) & (
                t <= (i * bar) + 5 * thirtySecondNote + 3 * quarterNote))
        x = x + noise

        noise = 0.1 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 6 * thirtySecondNote + 3 * quarterNote) & (
                t <= (i * bar) + 7 * thirtySecondNote + 3 * quarterNote))
        x = x + noise

        # saw bass
        if i == 0 or i == 4 or i == 8 or i == 12:
            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar)) & (t <= (i * bar) + thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * (
                    (t >= (i * bar) + 2 * thirtySecondNote) & (t <= (i * bar) + 3 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t) * (
                    (t >= (i * bar) + 4 * thirtySecondNote) & (t <= (i * bar) + 5 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * (
                    (t >= (i * bar) + 6 * thirtySecondNote) & (t <= (i * bar) + 7 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * (
                    (t >= (i * bar) + quarterNote) & (t <= (i * bar) + thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t) * ((t >= (i * bar) + 4 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * (
                    (t >= (i * bar) + 2 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t) * ((t >= (i * bar) + 4 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * (
                    (t >= (i * bar) + 3 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t) * ((t >= (i * bar) + 4 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(D * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

        if i == 1 or i == 5 or i == 9 or i == 13:
            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar)) & (t <= (i * bar) + thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * (
                    (t >= (i * bar) + 2 * thirtySecondNote) & (t <= (i * bar) + 3 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * (
                    (t >= (i * bar) + 4 * thirtySecondNote) & (t <= (i * bar) + 5 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * (
                    (t >= (i * bar) + 6 * thirtySecondNote) & (t <= (i * bar) + 7 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * (
                    (t >= (i * bar) + quarterNote) & (t <= (i * bar) + thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * ((t >= (i * bar) + 4 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * (
                    (t >= (i * bar) + 2 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * ((t >= (i * bar) + 4 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * (
                    (t >= (i * bar) + 3 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * ((t >= (i * bar) + 4 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

        if i == 2 or i == 6 or i == 10 or i == 14:
            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar)) & (t <= (i * bar) + thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * (
                    (t >= (i * bar) + 2 * thirtySecondNote) & (t <= (i * bar) + 3 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 2) * (
                    (t >= (i * bar) + 4 * thirtySecondNote) & (t <= (i * bar) + 5 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * (
                    (t >= (i * bar) + 6 * thirtySecondNote) & (t <= (i * bar) + 7 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * (
                    (t >= (i * bar) + quarterNote) & (t <= (i * bar) + thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar) + 2 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 2) * ((t >= (i * bar) + 4 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar) + 6 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * (
                    (t >= (i * bar) + 2 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar) + 2 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 2) * ((t >= (i * bar) + 4 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar) + 6 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * (
                    (t >= (i * bar) + 3 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar) + 2 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 2) * ((t >= (i * bar) + 4 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(B * t / 4) * ((t >= (i * bar) + 6 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

        if i == 3 or i == 7 or i == 11 or i == 15:
            sawBass = 0.5 * sawtooth(Bb * t / 4) * ((t >= (i * bar)) & (t <= (i * bar) + thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(Bb * t / 4) * (
                    (t >= (i * bar) + 2 * thirtySecondNote) & (t <= (i * bar) + 3 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(Bb * t / 2) * (
                    (t >= (i * bar) + 4 * thirtySecondNote) & (t <= (i * bar) + 5 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(Bb * t / 4) * (
                    (t >= (i * bar) + 6 * thirtySecondNote) & (t <= (i * bar) + 7 * thirtySecondNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(Bb * t / 4) * (
                    (t >= (i * bar) + quarterNote) & (t <= (i * bar) + thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(Bb * t / 4) * ((t >= (i * bar) + 2 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * ((t >= (i * bar) + 4 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * (
                    (t >= (i * bar) + 2 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * ((t >= (i * bar) + 4 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 6 * thirtySecondNote + 2 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 2 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * (
                    (t >= (i * bar) + 3 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t / 2) * ((t >= (i * bar) + 2 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 3 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t * 2) * ((t >= (i * bar) + 4 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 5 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass

            sawBass = 0.5 * sawtooth(C * t) * ((t >= (i * bar) + 6 * thirtySecondNote + 3 * quarterNote) & (
                    t <= (i * bar) + 7 * thirtySecondNote + 3 * quarterNote))
            x = x + sawBass
    if i == 7 or i == 15:
        # drum fill
        noise = 0.3 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 3 * quarterNote) & (t <= (i * bar) + thirtySecondNote + 3 * quarterNote))
        x = x + noise

        noise = 0.4 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 2 * thirtySecondNote + 3 * quarterNote) & (
                t <= (i * bar) + 3 * thirtySecondNote + 3 * quarterNote))
        x = x + noise

        noise = 0.5 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 4 * thirtySecondNote + 3 * quarterNote) & (
                t <= (i * bar) + 5 * thirtySecondNote + 3 * quarterNote))
        x = x + noise

        noise = 0.6 * np.random.normal(0, 1, 16 * 12 * 1024) * (
                (t >= (i * bar) + 6 * thirtySecondNote + 3 * quarterNote) & (
                t <= (i * bar) + 7 * thirtySecondNote + 3 * quarterNote))
        x = x + noise
x = np.transpose(x)
plt.plot(t, x)
plt.show()

sd.play(x, bar * 1024)

sleep(60)
