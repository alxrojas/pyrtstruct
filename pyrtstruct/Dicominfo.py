
import numpy as np
import pandas as pd

import build
import get_vector
import validate


class Dicominfo:
    def __init__(self, path):
        self.path = path

    def anonymize(self, path: str, name: str = 'anon.dcm'):
        # The function allows to anonymize the DICOM file. Change identifiers:
        # 1.PatientName
        # 2.Patient Birth Date
        # 3.Operators Name
        # 4.InstanceCreationDate
        # It receives as INPUT the file to anonymize and the name of new file.
        # It is necessary to include the extension .dcm).
        # The OUTPUT is the anonymized file with the new name.
        # INPUT:
        # File -> The DICOM file's path.
        # Name -> The name of the new DICOM file.
        # OUTPUT
        # It is created the new file at the same path.
        dicom = validate.validate(path)
        extension = '.dcm'
        if name.endswith(extension):
            pass
        else:
            name = ''.join([name, extension])
        dicom.PatientName = 'PatientName'
        dicom.PatientBirthDate = '1900101'
        dicom.OperatorsName = 'OperatorName'
        dicom.InstanceCreationDate = '19000101'
        dicom.save_as(name)
        return dicom

    def read(self, path: str) -> list:
        # The function allows to extract the information of:
        # Some structure (organs) or plan.
        # Data is stored in a dictionary.
        # IMPORTANT: Names have to match between the RT file and RS file.
        # INPUT:
        # Path -> The DICOM file's path.
        # OUTPUT:
        # Contours -> Dictionary with the information of names ([0]),
        # Coordinates ([1]) and the isocenter (RT file only).
        values = {}
        coordinates, names, dist2iso, dose = [], [], [], []
        dicom = validate.validate(path)
        if dicom[1] == 'RTPLAN':
            iso = np.ones(4)
            iso_all = dicom[0].BeamSequence[0].ControlPointSequence[0]
            iso[0] = iso_all.IsocenterPosition[0]
            iso[1] = iso_all.IsocenterPosition[1]
            iso[2] = iso_all.IsocenterPosition[2]
            for item in dicom[0].DoseReferenceSequence:
                if item.DoseReferenceStructureType == 'COORDINATES':
                    axis = np.ones(4)
                    axis[0] = item.DoseReferencePointCoordinates[0]
                    axis[1] = item.DoseReferencePointCoordinates[1]
                    axis[2] = item.DoseReferencePointCoordinates[2]
                    coordinates.append(axis)
                    names.append(item.DoseReferenceDescription)
                    dist2iso.append(round(np.sqrt(sum(np.square(axis-iso)))))
            values['Names'] = names
            values['Center-mass'] = np.array(coordinates)
            values['Dist2iso'] = np.array(dist2iso)
            values['Prescribed Dose'] = np.array(dose)
            values['Isocenter'] = np.array(iso)
            values['ID'] = dicom[0].PatientID
            values['BrithDate'] = dicom[0].PatientBirthDate
            values['Sex'] = dicom[0].PatientSex
            values['Intent'] = dicom[0].PlanIntent
        elif dicom[1] == 'RTSTRUCT':
            values = {}
            names = []
            for item in range(len(dicom[0].ROIContourSequence)):
                base = dicom[0].StructureSetROISequence[item]
                name = base.ROIName
                names.append(name)
            values['Names'] = names
            print('Select structures separated by single space, e.g.: 1 2 3')
            print('If you need all structures type Enter')
            print('Type any character: \n')
            print(pd.DataFrame(values))
            vect = input()
            vector = get_vector.get_vector(vect)
            values = build.build(vector, dicom[0])
        else:
            print('The modality is not RTPLAN nor RTSTRUCT')

        return values
