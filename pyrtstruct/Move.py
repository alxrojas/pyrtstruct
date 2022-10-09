
import numpy as np


class Move():
    def __init__(self, iso, point, key, angle):
        self.isocenter = iso
        self.point = point
        self.key = key
        self.angle = angle

    def rot(self, iso, point, key, angle):
        # Real movements are unique performed in roll, pitch and yaw.
        angle = np.radians(angle)
        point.append(1)
        m = {'roll': np.array([[1, 0, 0, 0],
                               [0, np.cos(angle), -np.sin(angle), 0],
                               [0, np.sin(angle), np.cos(angle), 0],
                               [0, 0, 0, 1]]),
             'pitch': np.array([[np.cos(angle), 0,
                                 np.sin(angle), 0],
                                [0, 1, 0, 0],
                                [-np.sin(angle), 0, np.cos(angle), 0],
                                [0, 0, 0, 1]]),
             'yaw': np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                              [np.sin(angle), np.cos(angle), 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]]),
             'p2iso': np.array([[1, 0, 0, -iso[0]],
                                [0, 1, 0, -iso[1]],
                                [0, 0, 1, -iso[2]],
                                [0, 0, 0, 1]]),
             'iso2p': np.array([[1, 0, 0, iso[0]],
                                [0, 1, 0, iso[1]],
                                [0, 0, 1, iso[2]],
                                [0, 0, 0, 1]])}
        rotation = m['iso2p']@m[key]@m['p2iso']@point
        return rotation

    def tra(self, iso, point, key, delta):
        point.append(1)
        m = {'x': np.array([[1, 0, 0, delta],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]),
             'y': np.array([[1, 0, 0, 0],
                            [0, 1, 0, delta],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]),
             'z': np.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, delta],
                            [0, 0, 0, 1]]),
             'p2iso': np.array([[1, 0, 0, -iso[0]],
                                [0, 1, 0, -iso[1]],
                                [0, 0, 1, -iso[2]],
                                [0, 0, 0, 1]]),
             'iso2p': np.array([[1, 0, 0, iso[0]],
                                [0, 1, 0, iso[1]],
                                [0, 0, 1, iso[2]],
                                [0, 0, 0, 1]])}
        translation = m['iso2p']@m[key]@m['p2iso']@point
        return translation
