# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile

Fs, aud = wavfile.read('riff.wav')

# select left channel only
aud = aud[:, 0]
# trim the first 20 seconds
first = aud[:int(Fs*20)]

powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
plt.xlabel("temps (s)")
plt.ylabel("test")
plt.title("premier spectrogramme")
plt.show()