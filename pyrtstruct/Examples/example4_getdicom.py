
import Conversor

# At the same directory is placed the new DICOM file
path = './Examples/structures/'
Conversor.Conversor(path, 'data').excel2dicom(path, 'data')
