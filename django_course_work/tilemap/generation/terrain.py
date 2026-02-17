import math
import random


# -------------------------
# Utility functions
# -------------------------

def lerp(a, b, t):
    return a + t * (b - a)


def smoothstep(t):
    return t * t * (3 - 2 * t)


# -------------------------
# Seeded grid value
# -------------------------

def random_value(x, y, seed):
    n = x * 374761393 + y * 668265263 + int(seed * 1000000)
    n = (n ^ (n >> 13)) * 1274126177
    n = n ^ (n >> 16)
    return (n & 0xFFFFFFFF) / 0xFFFFFFFF


# -------------------------
# 2D value noise
# -------------------------

def value_noise(x, y, seed):
    x0 = int(math.floor(x))
    y0 = int(math.floor(y))
    x1 = x0 + 1
    y1 = y0 + 1

    sx = smoothstep(x - x0)
    sy = smoothstep(y - y0)

    n00 = random_value(x0, y0, seed)
    n10 = random_value(x1, y0, seed)
    n01 = random_value(x0, y1, seed)
    n11 = random_value(x1, y1, seed)

    ix0 = lerp(n00, n10, sx)
    ix1 = lerp(n01, n11, sx)

    return lerp(ix0, ix1, sy)


# -------------------------
# Fractal noise (octaves)
# -------------------------

def fractal_noise(x, y, seed, octaves=4, persistence=0.5, lacunarity=2.0):
    amplitude = 1.0
    frequency = 1.0
    max_value = 0.0
    total = 0.0

    for _ in range(octaves):
        total += value_noise(x * frequency, y * frequency, seed) * amplitude
        max_value += amplitude

        amplitude *= persistence
        frequency *= lacunarity

    return total / max_value


def generate_heightmap(width, height, seed, scale=10.0):
    heightmap = []

    for y in range(height):
        row = []
        for x in range(width):
            nx = x / scale
            ny = y / scale

            value = fractal_noise(nx, ny, seed, octaves=4, persistence=2.0, lacunarity=1.3)

            # # Increase contrast
            # value = value ** 1.6

            # Push terrain toward water near edges
            dx = x / width - 0.5
            dy = y / height - 0.5
            distance = math.sqrt(dx * dx + dy * dy)

            value *= (1 - distance * 1.2)

            row.append(value)

        heightmap.append(row)

    return heightmap


def classify_tile(elevation):
    if elevation < 0.3:
        return "water"
    elif elevation < 0.4:
        return "beach"
    elif elevation < 0.5:
        return "plains"
    elif elevation < 0.6:
        return "hills"
    else:
        return "mountain"


def generate_tilemap(width, height, seed):
    heightmap = generate_heightmap(width, height, seed)

    tiles = []

    for y in range(height):
        row = []
        for x in range(width):
            elevation = heightmap[y][x]
            terrain = classify_tile(elevation)

            row.append({
                "x": x,
                "y": y,
                "elevation": elevation,
                "terrain": terrain,
            })
        tiles.append(row)
    return tiles
