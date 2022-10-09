
import Dicominfo
import margin

# To expand the structure 1 mm.
# Radius is in mm.
path = path = './Examples/structures/'
structures = Dicominfo.Dicominfo(path).read(path)
radius = 1
margin.margin(structures, radius, True)
