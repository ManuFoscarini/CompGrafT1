import numpy as np
import statistics
import math

from object.object3D import Object3D


flatten = lambda l: [item for sublist in l for item in sublist]

def transform_shape(shape, matrix):
    shape.points = transform_points(shape.points, matrix)


def transform_shape_3D(shape, matrix):
    if isinstance(shape, Point3D):
        shape.points = transform_points_3D(shape.points, matrix)

    if isinstance(shape, Object3D):
        shape.lines = [transform_points_3D(line, matrix) for line in shape.lines]


def transform_points(points, matrix):
    points = [np.array([x, y, 1]).dot(matrix).tolist() for [x, y] in points]
    return [[x, y] for [x, y, _] in points]


def transform_points_3D(points, matrix):
    points = [np.array([x, y, z, 1]).dot(matrix).tolist() for [x, y, z] in points]
    return [[x, y, z] for [x, y, z, _] in points]


def center(shape):
    cx = statistics.mean([x for [x, y] in shape.points])
    cy = statistics.mean([y for [x, y] in shape.points])

    return [cx, cy]


def center_3D(shape):
    if isinstance(shape, Point3D):
        return shape.point

    points = None
    if isinstance(shape, Object3D):
        points = flatten(shape.lines)

    cx = statistics.mean([x for [x, y, z] in points])
    cy = statistics.mean([y for [x, y, z] in points])
    cz = statistics.mean([z for [x, y, z] in points])

    return (cx, cy, cz)


def get_composite_rotation_matrix(angle, cx, cy):
    translate_to_origin = get_translation_matrix(-cx, -cy)
    rotate = get_rotation_matrix(angle)
    translate_back = get_translation_matrix(cx, cy)

    return translate_to_origin.dot(rotate).dot(translate_back)


def get_rotation_matrix(angle):
    radians = angle * (math.pi/180)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    return np.array([
        [cosine, -sine, 0],
        [sine, cosine, 0],
        [0, 0, 1]
    ])


def get_translation_matrix(dx, dy):
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [dx, dy, 1]
    ])

def get_translation_matrix_3D(dx, dy, dz):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [dx, dy, dz, 1]
    ])

def get_x_rotation_matrix(angle):
  cos_angle = np.cos(angle)
  sin_angle = np.sin(angle)
  return np.array((
    [1, 0, 0, 0],
    [0, cos_angle, sin_angle, 0],
    [0, -sin_angle, cos_angle, 0],
    [0, 0, 0, 1]
  ))

def get_y_rotation_matrix(angle):
  cos_angle = np.cos(angle)
  sin_angle = np.sin(angle)
  return np.array((
    [cos_angle, 0, -sin_angle, 0],
    [0, 1, 0, 0],
    [sin_angle, 0, cos_angle, 0],
    [0, 0, 0, 1]
  ))

def get_z_rotation_matrix(angle):
  cos_angle = np.cos(angle)
  sin_angle = np.sin(angle)
  return np.array((
    [cos_angle, sin_angle, 0, 0],
    [-sin_angle, cos_angle, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ))

def get_scale_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def get_scale_matrix_3d(sx, sy, sz):
  return np.array([
    [sx, 0, 0, 0],
    [0, sy, 0, 0],
    [0, 0, sz, 0],
    [0, 0, 0, 1]
  ])


def normalize_shape(shape, center, angle):
    cx, cy = center

    translate = get_translation_matrix(-cx, -cy)
    rotate_metrix = get_rotation_matrix(angle)
    translate_back = get_translation_matrix(cx, cy) 

    normalize_matrix = translate.dot(rotate_metrix).dot(translate_back)
    transform_shape(shape, normalize_matrix)


def rotate_shape(shape, angle, anchorPoint):
    [cx, cy] = anchorPoint
    rotate_matrix = get_composite_rotation_matrix(angle, cx, cy)

    transform_shape(shape, rotate_matrix)

def rotate_shape_3D(shape, anchorpoint, a, angle):
    [x0, y0, z0] = anchorpoint

    _a = transform_points_3D([a], get_translation_matrix_3D(-x0, -y0, -z0))[0]

    if _a[0] != 0:
        angle_of_a_with_x = math.atan(_a[2] / _a[0])
    else:
        angle_of_a_with_x = math.atan(_a[2] / _a[1])

    obj_to_xy_matrix = get_x_rotation_matrix(-angle_of_a_with_x)
    a_in_xy = transform_points_3D([_a], obj_to_xy_matrix)[0]

    angle_of_a_in_xy_with_y = (math.atan(a_in_xy[0] / a_in_xy[1]))

    transformation = (
            get_translation_matrix_3D(-x0, -y0, -z0)
            @ get_x_rotation_matrix(-angle_of_a_with_x)
            @ get_z_rotation_matrix(angle_of_a_in_xy_with_y)
            @ get_y_rotation_matrix(angle)
            @ get_z_rotation_matrix(-angle_of_a_in_xy_with_y)
            @ get_x_rotation_matrix(angle_of_a_with_x)
            @ get_translation_matrix_3D(x0, y0, z0)
    )

    return translate_shape_3D(shape, transformation)

def scale_shape(shape, sx, sy):
    [cx, cy] = center(shape)

    translate_to_origin = get_translation_matrix(-cx, -cy)
    translate_back = get_translation_matrix(cx, cy)
    scale_matrix = get_scale_matrix(sx, sy)

    scale_relative_origin_matrix = translate_to_origin.dot(scale_matrix).dot(translate_back)

    transform_shape(shape, scale_relative_origin_matrix)



def scale_shape_3d(shape, sx, sy, sz):
    [cx, cy, cz] = center_3D(shape)

    translate_to_origin = get_translation_matrix_3D(-cx, -cy, -cz)
    translate_back = get_translation_matrix_3D(cx, cy, cz)
    scale_matrix = get_scale_matrix_3d(sx, sy, sz)

    scale_relative_origin_matrix = translate_to_origin.dot(scale_matrix).dot(translate_back)

    transform_shape_3D(shape, scale_relative_origin_matrix)


def translate_shape(shape, dx, dy):
    transform_shape(shape, get_translation_matrix(dx, dy))

def translate_shape_3D(shape, dx, dy, dz):
    transform_shape_3D(shape, get_translation_matrix_3D(dx, dy, dz))
