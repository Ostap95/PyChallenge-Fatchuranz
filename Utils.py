import math
def get_angle(origin, destination):
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return math.atan2(-y_dist, x_dist) / math.pi*180

def project(angle, speed):
    x_coordinate = math.cos(degrees_to_radians(angle)) * speed
    y_coordinate = math.sin(degrees_to_radians(-angle)) * speed
    return (x_coordinate, y_coordinate) 

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180.0)
