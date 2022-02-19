import numpy as np
import matplotlib.pyplot as plt
import librosa.display as lplt




#calculate the AE
def amplitude_mask(signal, frame_size):
    amplitude_mask = []

    #calculate AE for each frame
    for i in range(0, len(signal), frame_size):
        current_frame_AE = max(signal[i:i+frame_size])
        amplitude_mask.append(current_frame_AE)

    return np.array(amplitude_mask)


#Plot Magnitude Spectrum
def plt_mag_spec(signal, title, sr, f_ratio=1):
    ft                 = np.fft.fft(signal)
    magnitude_spectrum = np.abs(ft)

    plt.figure(figsize = (15, 5))

    frequency          = np.linspace(0, sr, len(magnitude_spectrum))
    num_frequency_bins = int(len(frequency) * f_ratio)

    plt.plot(frequency[:num_frequency_bins], 
             magnitude_spectrum[:num_frequency_bins])
    plt.xlabel("Frequency Hz")
    plt.ylabel("Magnitude")
    plt.title(title)

    plt.show()


#Plot Spectogram
def plt_spectogram(Y, sr, hop_length, y_axis="log"):
    plt.figure(figsize=(30,15))
    lplt.specshow(Y,
                  sr=sr,
                  hop_length=hop_length,
                  x_axis='time',
                  y_axis=y_axis)
    
    plt.colorbar(format="%+2.f")




 