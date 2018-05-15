from scipy.spatial.distance import euclidean
from waveforms import WaveformConverter as wc
import os
from fastdtw import fastdtw


def get_waveform(position='first'):
    looking_for_file = True
    while looking_for_file:
        filepath = input("Enter the name of the {0} wave file(include extension)".format(position))
        looking_for_file = not os.path.isfile("{0}.wav".format(filepath))
    return filepath


def main():
    first_form = get_waveform()
    second_form = get_waveform('second')

    first_2d = wc.get_2d_array_from_waveform(first_form)
    second_2d = wc.get_2d_array_from_waveform(second_form)

    distance, path = fastdtw(first_2d, second_2d, dist=euclidean)
    print(distance)


main()
