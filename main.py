from scipy.spatial.distance import euclidean
from waveforms import WaveformConverter as wc
import os
from fastdtw import fastdtw
import matplotlib.pyplot as plt
import pandas as pd


def get_waveform(position='first'):
    looking_for_file = True
    while looking_for_file:
        filepath = input("Enter the name of the {0} wave file\n".format(position))
        looking_for_file = not os.path.isfile("{0}.wav".format(filepath))
    return filepath


def main():
    first_form = get_waveform()
    second_form = get_waveform('second')

    first_2d = wc.get_2d_array_from_waveform(first_form)
    second_2d = wc.get_2d_array_from_waveform(second_form)

    first_df = pd.DataFrame(first_2d)
    first_plot = first_df.plot(title=first_form)
    first_plot.set_xlabel("Time(Microseconds)")

    second_df = pd.DataFrame(second_2d)
    second_plot = second_df.plot(title=second_form)
    second_plot.set_xlabel("Time(Microseconds)")

    distance, path = fastdtw(first_2d, second_2d, dist=euclidean)

    path_x = [path[i][0] for i in range(0, len(path))]
    path_y = [path[i][1] for i in range(0, len(path))]
    path_df = pd.DataFrame(path_y, index=path_x)
    path_plot = path_df.plot(title="Path results for best distance: {0}".format(distance))
    path_plot.set_xlabel("Time(Microseconds)")

    plt.show()


main()
