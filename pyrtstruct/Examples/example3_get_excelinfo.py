
import Conversor

path = './Examples/structures/'
# Or is able to set path as dictionary. For example
# path = {'Eye Right': [[0, 1, 0], [1.5 , 3,2, 1.5],
# [0, 0.9, 0]], [[2, 4, 6], [-7, 4, 7], [5, 2.2, 0], so on]}
# At the same directory, excel file is created
Conversor.Conversor(path, 'name').dicom2excel(path, 'name')
