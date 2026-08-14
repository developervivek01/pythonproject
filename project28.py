"""
Waving Indian Flag Animation - Happy Independence Day (15 August)
--------------------------------------------------------------
Draws the Indian tricolour (Saffron, White, Green) with the
24-spoke Ashoka Chakra, and animates a waving cloth effect.

Requirements:
    pip install matplotlib numpy

Run:
    python indian_flag_animation.py

This will open a matplotlib window with the animation playing.
Uncomment the `ani.save(...)` line near the bottom to export a GIF
(requires 'pillow': pip install pillow).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# ----------------------------
# Flag & wave parameters
# ----------------------------
FLAG_WIDTH = 9.0
FLAG_HEIGHT = 6.0
POLE_X = 0.0
N_COLS = 120          # horizontal resolution of the waving mesh
N_ROWS = 60            # vertical resolution
WAVE_AMPLITUDE = 0.35
WAVE_LENGTH = 6.0
WAVE_SPEED = 4.0

SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
GREEN = "#138808"
CHAKRA_BLUE = "#000080"

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlim(-1, FLAG_WIDTH + 1)
ax.set_ylim(-1, FLAG_HEIGHT + 2)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#eef2f5')
ax.set_title("Happy Independence Day - 15 August", fontsize=16,
             fontweight='bold', color='#333333', pad=15)

# Flagpole
ax.plot([POLE_X, POLE_X], [-0.5, FLAG_HEIGHT + 1.5],
         color='#5a3d1a', linewidth=6, solid_capstyle='round', zorder=1)
ax.add_patch(Circle((POLE_X, FLAG_HEIGHT + 1.5), 0.15, color='#c9a227', zorder=2))

# ----------------------------
# Build the base flag mesh (X, Y grid before waving)
# ----------------------------
xs = np.linspace(0, FLAG_WIDTH, N_COLS)
ys = np.linspace(0, FLAG_HEIGHT, N_ROWS)
X, Y = np.meshgrid(xs, ys)

# Colour each row of the mesh based on which stripe it falls in
band_height = FLAG_HEIGHT / 3.0
colors = np.empty(Y.shape, dtype=object)
colors[Y >= 2 * band_height] = SAFFRON
colors[(Y >= band_height) & (Y < 2 * band_height)] = WHITE
colors[Y < band_height] = GREEN

# We use a custom color array per face (constant across frames, only the
# mesh's X/Y coordinates change each frame to create the waving motion)
face_colors = np.empty((N_ROWS - 1, N_COLS - 1), dtype=object)
for i in range(N_ROWS - 1):
    for j in range(N_COLS - 1):
        mid_y = (Y[i, j] + Y[i + 1, j]) / 2
        if mid_y >= 2 * band_height:
            face_colors[i, j] = SAFFRON
        elif mid_y >= band_height:
            face_colors[i, j] = WHITE
        else:
            face_colors[i, j] = GREEN
face_colors_flat = list(face_colors.flatten())


def make_mesh(X_coords, Y_coords):
    """(Re)create the pcolormesh for the given (already-waved) coordinates."""
    mesh = ax.pcolormesh(X_coords, Y_coords, np.zeros((N_ROWS - 1, N_COLS - 1)),
                          shading='auto', zorder=3)
    mesh.set_array(None)
    mesh.set_facecolor(face_colors_flat)
    return mesh


flag_mesh = make_mesh(X, Y)

# ----------------------------
# Ashoka Chakra (24 spokes), drawn as a separate artist group
# ----------------------------
chakra_center_x = FLAG_WIDTH / 2
chakra_center_y = FLAG_HEIGHT / 2
chakra_radius = band_height * 0.35

chakra_circle_outer = Circle((chakra_center_x, chakra_center_y), chakra_radius,
                              fill=False, edgecolor=CHAKRA_BLUE, linewidth=2, zorder=5)
chakra_circle_inner = Circle((chakra_center_x, chakra_center_y), chakra_radius * 0.08,
                              color=CHAKRA_BLUE, zorder=5)
ax.add_patch(chakra_circle_outer)
ax.add_patch(chakra_circle_inner)

spokes = []
for k in range(24):
    angle = 2 * np.pi * k / 24
    line, = ax.plot([], [], color=CHAKRA_BLUE, linewidth=1.3, zorder=5)
    spokes.append((line, angle))


def wave_offset(x, t):
    """Vertical displacement for the waving cloth effect at position x, time t."""
    return WAVE_AMPLITUDE * np.sin((x / WAVE_LENGTH) * 2 * np.pi - WAVE_SPEED * t) \
           * (x / FLAG_WIDTH)  # damp near the pole so it stays attached


def x_shear(x, t):
    """Slight horizontal compression to enhance the cloth-waving illusion."""
    return 0.05 * np.sin((x / WAVE_LENGTH) * 2 * np.pi - WAVE_SPEED * t) * (x / FLAG_WIDTH)


def update(frame):
    global flag_mesh
    t = frame * 0.05

    # Wave the flag mesh: remove the old mesh and draw a new one at the
    # displaced coordinates (QuadMesh coordinates aren't updatable in place)
    Y_waved = Y + wave_offset(X, t)
    X_waved = X + x_shear(X, t)
    flag_mesh.remove()
    flag_mesh = make_mesh(X_waved, Y_waved)

    # Wave the chakra: move its center and squash slightly with the local wave
    cx = chakra_center_x + x_shear(np.array([chakra_center_x]), t)[0]
    cy = chakra_center_y + wave_offset(np.array([chakra_center_x]), t)[0]
    local_amp = 1 - 0.15 * abs(np.sin((chakra_center_x / WAVE_LENGTH) * 2 * np.pi - WAVE_SPEED * t))

    chakra_circle_outer.center = (cx, cy)
    chakra_circle_outer.set_radius(chakra_radius * local_amp)
    chakra_circle_inner.center = (cx, cy)

    artists = [flag_mesh, chakra_circle_outer, chakra_circle_inner]
    for line, angle in spokes:
        r = chakra_radius * local_amp
        x0, y0 = cx, cy
        x1 = cx + r * np.cos(angle)
        y1 = cy + r * np.sin(angle)
        line.set_data([x0, x1], [y0, y1])
        artists.append(line)

    return artists


ani = animation.FuncAnimation(fig, update, frames=200, interval=40, blit=False)

# To save as a GIF instead of showing a live window, comment out plt.show()
# below and uncomment this line (requires: pip install pillow):
# ani.save("indian_flag_wave.gif", writer="pillow", fps=25)

plt.tight_layout()
plt.show()