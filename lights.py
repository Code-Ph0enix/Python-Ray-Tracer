import numpy as np
from Spheres import get_objects


class Light:
    def __init__(self, position, diffuse, specular, intensity):
        self.position = np.array(position)
        self.diffuse = np.array(diffuse) * intensity
        self.specular = np.array(specular)


def get_lights() -> list[Light]:
    return [
        Light([1, 2, 0], [1, 1, 1], [1, 1, 1], 10)
    ]


def check_lights():
    for light in get_lights():
        for sphere in get_objects():
            if np.any(light.position == sphere.center):
                raise ValueError("Light is inside a sphere")