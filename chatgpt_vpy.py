from vpython import *
import numpy as np

pitch_length = 22  # Length of the pitch in meters
pitch_width = 3.05  # Width of the pitch in meters
release_speed = 140  # Release speed in km/h
cor = 0.7  # Coefficient of restitution (how bouncy the ball is)
bounce_height = 0.8  # Bounce height in meters

def cricket_ball_trajectory(pitch_length, pitch_width, release_speed, cor, bounce_height):
    # Time intervals (you may have this data available)
    time_intervals = np.linspace(0, 10, 100)  # Adjust the range and number of intervals as needed

    # Initial conditions
    x = 0
    y = 0
    z = bounce_height
    vx = release_speed * 1000 / 3600  # Convert release speed from km/h to m/s
    vy = 0
    vz = 0

    # Constants
    g = 9.81  # Acceleration due to gravity in m/s^2

    # Lists to store ball positions for animation
    x_list, y_list, z_list = [], [], []

    for t in time_intervals:
        x += vx * t
        y += vy * t
        z += vz * t - 0.5 * g * t ** 2

        # Bounce conditions
        if z < 0:
            z = 0
            vz = -vz * cor

        x_list.append(x)
        y_list.append(y)
        z_list.append(z)

    return x_list, y_list, z_list


x_coords, y_coords, z_coords = cricket_ball_trajectory(pitch_length, pitch_width, release_speed, cor, bounce_height)



scene = canvas(width=800, height=600, center=vector(pitch_length / 2, pitch_width / 2, 0), background=color.white)
pitch = box(pos=vector(pitch_length / 2, pitch_width / 2, 0), size=vector(pitch_length, pitch_width, 0.1), color=color.green)
ball = sphere(radius=0.1, color=color.red)

# Set the animation rate (adjust the value as needed)
animation_rate = 2

for i in range(len(x_coords)):
    # if not run: continue
    rate(animation_rate)

    # Update ball position at the current frame
    ball.pos = vector(x_coords[i], y_coords[i], z_coords[i])

