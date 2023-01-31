# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile
import wave
from numpy.fft import fft, fftfreq

#ce programme permet d'analyser un enregistrement audio et de le comparer a la base de donnees


#il faut modifier a chaque execution le fichier audio a analyser
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

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

powerSpectrum2, frequenciesFound2, time2, im = plt.specgram(first, Fs=Fs, vmin=20.0, vmax=21)

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

points = plt.scatter(freq_pos, X_abs, s=10)

#récupération des coordonées de chaque point de la TF
coordinates = points.get_offsets()

#filtrage de la liste pour avoir uniquement les coordonées des points du graph

filtered_coordinates = [(x,y) for x,y in coordinates if x >= 0 and x <= 100 and y >= 10 and y <= 1000]

#ecriture du résultat de l'analyse dans un fichier texte
with open("analysis.txt", "w") as file:
    for coord in filtered_coordinates:
        file.write(str(coord))

with open("analysis.txt", "r") as file:
    to_compare = file.read().splitlines()

next_file = False

# Open the text file for reading
with open('Mitterrand', 'r') as file:
    # Read the contents of the file
    file_contents = file.read().splitlines()

    if to_compare != file_contents:
            next_file = True
    if (next_file == False):
        print("Il s'agit du président Mitterrand en 1994")


if(next_file):
    with open('Pompidou', 'r') as file:
        # Read the contents of the file
        file_contents = file.read().splitlines()
        next_file = False

        if to_compare != file_contents:
            next_file = True
        if(next_file == False):
            print("Il s'agit du président Pompidou en 1970")

if(next_file):
    with open('Sarkozy', 'r') as file:
        # Read the contents of the file
        file_contents = file.read().splitlines()
        next_file = False

        if to_compare != file_contents:
            next_file = True
        if(next_file == False):
            print("Il s'agit du président Sarkozy en 2008")
