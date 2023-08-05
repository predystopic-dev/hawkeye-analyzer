import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    y = pitch_width / 2
    z = 0.2
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



def update(frame):
    ax.clear()
    ax.set_xlim(0, pitch_length)
    ax.set_ylim(0, pitch_width)

    # Plot pitch dimensions
    ax.plot([0, 0, pitch_length, pitch_length, 0], [0, pitch_width, pitch_width, 0, 0], 'k')

    # Plot ball position at the current frame
    ax.plot(x_coords[frame], y_coords[frame], 'ro')

    # Add any additional visual elements based on your data (e.g., batsman, stumps, etc.)

    return ax


fig, ax = plt.subplots()

# Set the number of frames to match the number of time intervals
num_frames = len(x_coords)

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100, blit=False)
plt.show()
