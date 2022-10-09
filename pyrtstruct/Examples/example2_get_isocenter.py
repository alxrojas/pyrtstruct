
import Dicominfo
import isocenter

# To extract the information of the (RT) plan file.
# As output is defined the isocenter coordinates.
path = './Examples/dose/'
structures = Dicominfo.Dicominfo(path).read(path)
iso = isocenter.isocenter(structures)
