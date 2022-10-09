
import glob
import os

import pydicom


def validate(path):
    os.chdir(path)
    file = glob.glob('*.dcm')
    new_file = pydicom.dcmread(file[0])
    modality = new_file.Modality
    return new_file, modality
