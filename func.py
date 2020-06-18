from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
def gui_fname(dir=None):
    """Select a file via a dialog and return the file name."""
    if dir is None: dir ='./'
    fname = QFileDialog.getOpenFileName(None, "Select data file...",
                dir, filter="All files (*);; SM Files (*.sm)")
    return fname[0]
