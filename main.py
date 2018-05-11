import numpy as np
from scipy.spatial.distance import euclidean
from waveforms import WaveformConverter as wc
import os
from fastdtw import fastdtw


def get_waveform(position='first'):
    looking_for_file = True
    while looking_for_file:
        filepath = input("Enter the name of the {0} wave file(include extension)".format(position))
        looking_for_file = not os.path.isfile(filepath)
    return filepath


def main():

    first_form = get_waveform()
    second_form = get_waveform('second')

    first_2d = wc.get_2d_array_from_waveform(first_form)
    second_2d = wc.get_2d_array_from_waveform(second_form)

    distance, path = fastdtw(first_2d, second_2d, dist=euclidean)
    print(distance)

    # x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
    # y = np.array([[2,2], [3,3], [4,4]])
    # distance, path = fastdtw(x, y, dist=euclidean)
    # print(distance)


main()
