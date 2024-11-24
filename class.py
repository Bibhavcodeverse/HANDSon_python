import math

def distance_between_points(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def cartesian_to_polar(x, y):
    """Convert Cartesian coordinates (x, y) to polar coordinates (r, θ)."""
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, math.degrees(theta)

def move_point(x, y, dx, dy):
    """Move a point (x, y) by a displacement (dx, dy)."""
    return x + dx, y + dy

# Test data
points = [(1, 2), (1, 3), (2, 4), (5, 7)]

# Distance between first two points
dist = distance_between_points(points[0][0], points[0][1], points[1][0], points[1][1])
print(f"Distance between {points[0]} and {points[1]}: {dist}")

# Polar coordinates of the first point
polar = cartesian_to_polar(points[0][0], points[0][1])
print(f"Polar coordinates of {points[0]}: r = {polar[0]}, θ = {polar[1]} degrees")

# Move the first point by a displacement of (2, 3)
new_position = move_point(points[0][0], points[0][1], 2, 3)
print(f"New position of {points[0]} after moving by (2, 3): {new_position}")
