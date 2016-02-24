
import numpy as np

# BioSPPy  has the following dependencies
#import bidict, h5py, matplotlib, numpy, scikit-learn, scipy, shortuuid

from biosppy.signals import ecg

""" >>>>>>>> LOAD DATA <<<<<<<<< """
# load raw ECG signal
# ----------------------
# EXAMPLE:
#signal = np.loadtxt('./examples/ecg.txt')

# ----------------------
# Teresa ECG 2016/12/28
signal = np.loadtxt('C:\Users\Hugo\Dropbox\Projects\Neotilt\Code\Data\opensignals_98D3318047D6_2015-12-28_21-47-05.txt', usecols=[7])


""" >>>>>>>> PROCESS AND PLOT <<<<<<<<< """
# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1000, show=True)
