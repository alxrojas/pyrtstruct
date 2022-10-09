
import numpy as np


def build(vector, dicom):
    lendicom = len(dicom.ROIContourSequence)
    if len(vector) == 0:
        vector = np.arange(1, lendicom, 1)
    else:
        pass
    contour = {}
    names, volumes = [], []
    for item in vector:
        if item <= lendicom:
            base = dicom.StructureSetROISequence[item]
            basseq = dicom.ROIContourSequence[item]
            name = base.ROIName
            volume = base.ROIVolume
            names.append(name)
            volumes.append(volume)
            sequence = basseq.ContourSequence
            contour[name] = [s.ContourData for s in sequence]
        else:
            print(f'Item {item} exceed maximum length {lendicom}')
    contours = {x: contour[x] for x in names}
    return contours
