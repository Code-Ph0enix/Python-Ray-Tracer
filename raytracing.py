import os

import numpy as np
import matplotlib.pyplot as plt

from Spheres import get_objects, Sphere
from lights import get_lights
import functions as f

objects = get_objects()
max_depth = 1
width = 1500
height = 500
exposure = 1
gamma = 2.2
hdr = False

camera = np.array([0, 0, 1])
ratio = width / height
screen = (-1, 1/ratio, 1, -1/ratio)

image = np.zeros((height, width, 3))
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
        pixel = np.array([x, y, 0])
        origin = camera
        direction = f.normalise(pixel - origin)
        color = np.zeros(3)
        reflection = 1
        for k in range(max_depth):
            nearest_object: Sphere
            nearest_object, min_distance = f.nearest_intersected_object(objects, origin, direction)
            if nearest_object is None:
                break
            intersection = origin + min_distance * direction
            normal_to_surface = f.normalise(intersection - nearest_object.center)
            shifted_point = intersection + 1e-5 * normal_to_surface
            illumination = np.zeros(3)
            shadowed_illumination = np.zeros(3)
            for light in get_lights():
                intersection_to_light = f.normalise(light.position - shifted_point)
                _, min_distance = f.nearest_intersected_object(objects, shifted_point, intersection_to_light)
                intersection_to_light_distance = np.linalg.norm(light.position - intersection)
                is_shadowed = min_distance < intersection_to_light_distance
                if is_shadowed:
                    reflection *= 0.25 * (nearest_object.diffuse * nearest_object.reflection) * (light.diffuse * (1 - 0.63661977236759*np.arccos(np.dot(intersection_to_light, normal_to_surface))) / intersection_to_light_distance ** 2)
                    shadowed_illumination += reflection
                illumination += nearest_object.diffuse * light.diffuse * (1 - 0.63661977236759*np.arccos(np.dot(intersection_to_light, normal_to_surface))) / intersection_to_light_distance ** 2
                intersection_to_camera = f.normalise(camera - intersection)
                illumination += nearest_object.specular * light.specular * np.dot(normal_to_surface, f.normalise(intersection_to_light + intersection_to_camera)) ** (nearest_object.shininess / 4)
            color += (reflection * illumination) + shadowed_illumination
            reflection *= nearest_object.reflection * nearest_object.diffuse * illumination
            origin = shifted_point
            direction = f.reflected(direction, normal_to_surface)

        color = color * exposure + ((gamma*-1)+2.2)
        if hdr:
            color = color**0.6
        image[i, j] = np.clip(color, 0, 1)

    print(f"{i+1} / {height}, {(i+1)/height:.2%}")

render = os.path.join("imgs", "render.png")
plt.imsave(render, image)