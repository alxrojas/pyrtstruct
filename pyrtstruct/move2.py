
import numpy as np
import xlsxwriter

import Dicominfo
import Move


def move2(path, iso, key, ang, report=True):
    agenda = Dicominfo.Dicominfo(path).read(path)
    structures, geometry, distance, data_info = {}, {}, {}, {}
    for lesions in agenda:
        contour = {}
        xyz_data, dist, data, radius = [], [], [], []
        for slices in range(len(agenda[lesions])):
            rtn, xyz_all = [], []
            length = int(len(agenda[lesions][slices])/3)
            param = agenda[lesions][slices]
            for delta in range(length):
                x_coor = round(param[3*delta], 3)
                y_coor = round(param[3*delta + 1], 3)
                z_coor = round(param[3*delta + 2], 3)
                xyz = [x_coor, y_coor, z_coor]
                if key in ['roll', 'pitch', 'yaw']:
                    rtn = Move.Move(iso, xyz, key, ang).rot(iso, xyz, key, ang)
                elif key in ['x', 'y', 'z']:
                    rtn = Move.Move(iso, xyz, key, ang).tra(iso, xyz, key, ang)
                else:
                    print('Wrong key')
                xyz_all.append(rtn[0])
                xyz_all.append(rtn[1])
                xyz_all.append(rtn[2])
                xyz_data.append(rtn)
                data.append(xyz)
                dist.append(np.sqrt(sum(np.square(xyz - rtn))))
            contour[slices] = xyz_all
        mean_xyz = np.mean(xyz_data, axis=0)
        mean_dist = np.mean(dist)
        min_dist = np.min(dist)
        max_dist = np.max(dist)
        std_dist = np.std(dist)
        structures[lesions] = contour
        geometry[lesions] = mean_xyz
        distance[lesions] = [mean_dist, std_dist, min_dist, max_dist]
        for count in range(len(data)):
            rad = np.sqrt(sum(np.square(data[count]-geometry[lesions])))
            radius.append(rad)
        data_info[lesions] = radius
    if report:
        workbook = xlsxwriter.Workbook('Report.xlsx')
        worksheet = workbook.add_worksheet('Main')
        counter = 1
        for lesions in structures:
            cm_aux = geometry[lesions][:-1]
            ctr = list(cm_aux)
            if key in ['roll', 'pitch', 'yaw']:
                cm_tra = Move.Move(iso, ctr, key, ang).rot(iso, ctr, key, ang)
            elif key in ['x', 'y', 'z']:
                cm_tra = Move.Move(iso, ctr, key, ang).tra(iso, ctr, key, ang)
            else:
                print('Wrong key')
            dist_cm = np.sqrt(sum(np.square(geometry[lesions] - cm_tra)))
            dist2iso = int(np.sqrt(sum(np.square(cm_aux - iso))))
            radius_max = max(data_info[lesions])
            radius_min = min(data_info[lesions])
            excentricity = radius_max/radius_min
            radius_all = [radius_max, radius_min, excentricity]
            worksheet.write_row(0, 1, ['Name', 'CM x [mm]',
                                       'CM y [mm]', 'CM z [mm]',
                                       'Dist2iso [mm]',
                                       'Displ. CM [mm]',
                                       'Mean displ. [mm]',
                                       'STD [mm]',
                                       'Min displ. [mm]',
                                       'Max displ. [mm]',
                                       'Max radius [mm]',
                                       'Min radius [mm]',
                                       'Excentricity'])
            worksheet.write_row(counter, 1, [lesions])
            worksheet.write_row(counter, 2, geometry[lesions])
            worksheet.write_row(counter, 5, [dist2iso])
            worksheet.write_row(counter, 6, [dist_cm])
            worksheet.write_row(counter, 7, distance[lesions])
            worksheet.write_row(counter, 11, radius_all)
            counter += 1
        workbook.close()
    else:
        pass
    return structures
