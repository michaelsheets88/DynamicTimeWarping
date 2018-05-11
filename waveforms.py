import numpy as np
import wave


class WaveformConverter:

    def __init__(self):
        pass

    @classmethod
    def get_2d_array_from_waveform(cls, wavefile):
        raw_wave = wave.open(wavefile, 'r')

        # Extract Raw Audio from Wav File
        signal = raw_wave.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        fs = raw_wave.getframerate()

        # If Stereo
        if raw_wave.getnchannels() == 2:
            print('Just mono files')
            return [[]]

        time = np.linspace(0, len(signal)/fs, num=len(signal))
        our_2d = np.zeros(shape=(len(signal), 2))
        for index, value in enumerate(signal):
            our_2d[index] = [time[index], value]
        return our_2d

