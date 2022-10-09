
import Dicominfo
import isocenter
import move2

path = './Examples/structures/'
path_plan = './Examples/dose/'
structures = Dicominfo.Dicominfo(path_plan).read(path_plan)
iso = isocenter.isocenter(structures)
key = 'roll'
ang = 1
# Or iso = [0, 0, 0] or another arbitrary point
# key-> if rotate: 'roll', 'pitch' or 'yaw'.
# key-> if translate: 'x', 'y', 'z'
# ang: If rotate, is in degress.
# and: If translate, is in mm.
# report -> True, if report is created in excel
move2.move2(path, iso, key, ang, report=True)
