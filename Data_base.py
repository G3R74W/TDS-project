# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile
import wave
from numpy.fft import fft, fftfreq


#reading wav file
Fs, aud = wavfile.read('Sarkozy2008.wav')

#openning wav file
wav_obj = wave.open('Sarkozy2008.wav', 'rb')

#sampling file
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq

# select left channel only
aud = aud[:, 0]
# trim the first 30 seconds of the audio
first = aud[:int(Fs*30)]

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
plt.specgram(first, Fs=Fs)
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.title("Spectrogramme de fréquence")

#add colorbar
plt.colorbar()

#add padding between figures
plt.tight_layout(pad=2.0)
plt.show()

####################################################################
#filtrage haute fréquence

powerSpectrum2, frequenciesFound2, time2, im = plt.specgram(first, Fs=Fs, vmin=20.0, vmax=21)
plt.title('filtrage hautes fréquences')
plt.xlabel('temps (s)')
plt.ylabel('Fréquences (Hz)')
plt.colorbar()
plt.show()



###################################################################
#transfo de fourier
# Calcul FFT
X = fft(aud)  # Transformée de fourier
freq = fftfreq(aud.size, d=1/Fs)  # Fréquences de la transformée de Fourier

# Calcul du nombre d'échantillon
N = aud.size

# On prend la valeur absolue de l'amplitude uniquement pour les fréquences positives et normalisation
X_abs = np.abs(X[:N//2])*2.0/N
# On garde uniquement les fréquences positives
freq_pos = freq[:N//2]

plt.plot(freq_pos, X_abs, label="Amplitude absolue")
plt.xlim(0, 12000)  # On réduit la plage des fréquences à la zone utile

plt.grid()
plt.xlabel(r"Fréquence (Hz)")
plt.ylabel(r"Amplitude $|X(f)|$")
plt.title("Transformée de Fourier du signal")
plt.show()



#nuages de points de la TF
fig, ax2 = plt.subplots()

points = plt.scatter(freq_pos, X_abs, s=10)

plt.xlim(0, 100)  # On réduit la plage des fréquences à la zone utile

#on set une valeur minimale de y pour réduire le nombre de pts
plt.ylim(10, 1000)

plt.title("Graph nuage de points de la transformée de fourier")
plt.xlabel(r"Fréquence (Hz)")
plt.ylabel(r"Amplitude $|X(f)|$")
plt.show()

#récupération des coordonées de chaque point de la TF
coordinates = points.get_offsets()

#filtrage de la liste pour avoir uniquement les coordonées des points du graph

filtered_coordinates = [(x,y) for x,y in coordinates if x >= 0 and x <= 100 and y >= 10 and y <= 1000]
print(filtered_coordinates)

#On ouvre un fichier txt pour y stocker la liste de coordonées
#ce fichier texte servira de base de donnée
with open("coordinates.txt", "a") as file:
    for coord in filtered_coordinates:
        file.write(str(coord))
    file.write("\n")