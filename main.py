# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile
import wave

Fs, aud = wavfile.read('riff.wav')

#openning wav file
wav_obj = wave.open('riff.wav', 'rb')

#sampling file
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq

# select left channel only
aud = aud[:, 0]
# trim the first 20 seconds
first = aud[:int(Fs*20)]

#amplitude en fct du temps
times = np.linspace(0, n_samples/sample_freq, num=n_samples)
plt.figure(figsize=(15, 5))
ax1 = plt.subplot(211)
plt.title("Visualisation du signal")
plt.ylabel('Amplitude')
plt.xlabel('Temps (s)')
plt.xlim(0, t_audio)
plt.plot(times, aud)
plt.subplot(212, sharex=ax1)

#spectrogramme de frequence
powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.title("Spectrogramme de fréquence")
plt.show()



