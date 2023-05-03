import pandas as pd
import os
from os import listdir
import numpy as np
import mne
import matplotlib.pyplot as plt


mypath = "Testovaya_baza2/Тестовая_База_РОХМИНЕ_12_стандарт/EDF"
newpath = "Testovaya_baza2"
for f_name in listdir(mypath):
    if f_name[9:] == 'edf':
        f = mne.io.read_raw_edf(os.path.join(mypath, f_name))
        header = ','.join(f.ch_names)
        f_new_name = f_name[0: -3] + 'txt'
        np.savetxt(os.path.join(newpath, f_new_name), f.get_data().T, delimiter=',', header=header)
        pd_file = pd.read_csv(os.path.join(newpath, f_new_name), sep=',')
        pd_file['time'] = np.arange(0.0, 10.0, 0.002)
        for name in list(pd_file.columns)[0:12]:
             plot = pd_file.plot(x='time', y=name)
             plot_name = f_name[0: -3] + '_plot_' + '{}'.format(name) + '.png'
             plt.savefig(plot_name)



