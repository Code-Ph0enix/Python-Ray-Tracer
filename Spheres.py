import numpy as np


class Sphere:
    def __init__(self, center, radius, diffuse, specular, shininess, reflection):
        self.center = np.array(center)
        self.radius = float(radius)
        self.diffuse = np.array(diffuse)
        self.specular = np.array(specular)
        self.shininess = float(shininess)
        self.reflection = float(reflection)


def get_objects():
    return [
        Sphere([-0.75, -0.25, -2], .75, [0.9, 0.05, 0.05], [0.2, 0.2, 0.2], 100, 1),
        Sphere([0, -9000, 0], 8999, [0.8, 0.8, 0.8], [0.2, 0.2, 0.2], 100, 0.7),
        Sphere([0, 9002, 0], 8999, [0.8, 0.8, 0.8], [0.2, 0.2, 0.2], 100, 0.7),
        Sphere([-9001, 0, 0], 8999, [0.8, 0.05, 0.05], [0.2, 0.2, 0.2], 100, 2),
        Sphere([9001, 0, 0], 8999, [0.05, 0.05, 0.8], [0.2, 0.2, 0.2], 100, 2),
        Sphere([0, 0, -9002], 8999, [0.05, 0.8, 0.05], [0.2, 0.2, 0.2], 100, 0.7),
        Sphere([0, 0, 9002], 8999, [0.8, 0.8, 0.05], [0.2, 0.2, 0.2], 100, 0.7),
        Sphere([0.5, -0.5, -1], .5, [0.05, 0.75, 0.9], [0.2, 0.2, 0.2], 100, 1)
    ]