
import Dicominfo

# To extract the information of the file.
# As output is defined a dictionary with.
# All the structures selected.
# The selection of the structures is by.
# Typing all the IDs with blanckspace.
path = './Examples/structures/'
structures = Dicominfo.Dicominfo(path).read(path)
