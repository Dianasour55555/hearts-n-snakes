import pandas as pd
import os
from os import listdir
import numpy as np
import numpy.fft
import shutil
from os import path


for f_name in listdir():
    if f_name[9:] == 'txt':
        pd_file = pd.read_csv(os.path.join(path, f_name), sep=',')
        F = np.fft.rfft(pd_file['ECG II-Ref'], n=None, axis=-1)
        A = [((F[i].real) ** 2 + (F[i].imag) ** 2) ** 0.5 for i in np.arange(100, 1500, 1)]  # модуль амплитуды
        freq = (A.index(max(A)) + 100) / 500
        if freq < 0.99:
            name =
            new_location = shutil.move(source_path, 'brad')
        elif freq > 1.7:
            pass
        else:
            pass




