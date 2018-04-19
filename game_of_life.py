import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
Uses 2D list to visualize the universe.

[  x 0  1  2  3  4  5   y
    [0, 0, 0, 0, 0, 0], 0
    [0, 0, 0, 0, 0, 0], 1
    [0, 0, 0, 0, 0, 0], 2
    [0, 0, j, 0, 0, 0], 3
    [0, 0, 0, 0, 0, 0], 4
    [0, 0, 0, 0, 0, 0], 5
]

pos(j)      => (2,3)
closest(j)  => (current_row[x-1, x+1], top_row[x-1, x, x+1], bottom_row[x-1, x, x+1])

"""


def create_universe(width: int, height: int) -> list:
    """
    Create 2D list with given width and height.

    :param width: width of the universe
    :param height: height of the universe
    :return:
    """
    return [[0 for x in range(0, width)] for x in range(0, height)]


def print_universe(univ: list):
    """
    Print the universe with coordinates.

    :param univ: the list representing the universe
    """
    max_x = len(univ[0])
    y = 0

    print()
    for i in range(0, max_x):
        print("%d " % i, end="")
    print("\n")

    for row in univ:
        for col in row:
            print("%s " % str(col), end="")

        print(" " + str(y), end="")
        print()

        y += 1
    print()


def get_closest(x: int, y: int) -> list:
    """
    Get the closest 8 points for given point. It is irrelevent where the point
    exists in the universe.

    :param x:
    :param y:
    :return: a list of points
    """
    return [
        [x - 1, y - 1], [x, y - 1], [x + 1, y - 1],
        [x - 1, y], [x + 1, y],
        [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]
    ]


def map_closest(closest_list: list, univ: list):
    """
    This is a helper function, just to mark the closest points given by
    the function get_closest() in the universe.

    :param closest_list: a list of coordinates
    :param univ: the universe list
    :return: a new universe with closest points marked
    """
    max_x = len(univ[0])
    max_y = len(univ)

    for coord in closest_list:
        x = coord[0]
        y = coord[1]
        if (x >= 0 and y >= 0) and (x < max_x and y < max_y):
            univ[y][x] = 1

    return univ


def map_pos(pos, univ, key=1) -> list:
    """
    Mark the given position in the universe with given key(0=dead,1=alive)
    and return a new universe with marking.

    :param pos: the position to mark
    :param univ: the universe where position is to be marked
    :param key: the key 0/1
    :return: a new universe
    """
    x = pos[0]
    y = pos[1]
    univ[y][x] = key
    return univ


def count_closest(pos, univ) -> int:
    """
    For the given position in the given universe, it counts how many
    closest points are alive.

    :param pos: a given position in a universe
    :param univ: universe list
    :return: number of closest alive points
    """
    count = 0

    x = pos[0]
    y = pos[1]

    max_x = len(univ[0])
    max_y = len(univ)

    closest_points = get_closest(x, y)
    for coord in closest_points:
        x = coord[0]
        y = coord[1]

        if (x >= 0 and y >= 0) and (x < max_x and y < max_y):
            if univ[y][x] == 1:
                count += 1
    return count


def init_structure(start_pos: list, struct: list, univ: list) -> list:
    """
    This helps map predefined structure into the universe at the given point.

    :param start_pos: starting position to map the structure
    :param struct: the structure to be mapped
    :param univ: the universe
    :return: a new universe with structure mapped
    """
    y = start_pos[1]

    for row in struct:
        x = start_pos[0]
        for col in row:
            univ[y][x] = col
            x += 1
        y += 1
    return univ


def apply_rules(univ: list) -> list:
    """
    Apply the game of life rules to determine whether each point will become dead or alive
    in the next iteration. Once it is determined, a new universe with outcome will pe produced
    and returned.

    :param univ: the pre-universe
    :return: new universe with rules applied
    """
    alive = []
    dead = []

    y = 0
    for row in univ:
        x = 0
        for col in row:
            pos = [x, y]

            closest = count_closest(pos, univ)

            if col == 1 and (closest < 2 or closest > 3):
                dead.append(pos)
            if col == 0 and (closest == 3):
                alive.append(pos)

            x += 1
        y += 1

    # make cells alive
    for pos in alive:
        univ = map_pos(pos, univ, key=1)

    # make cells die
    for pos in dead:
        univ = map_pos(pos, univ, key=0)

    return univ


def animate_universe(univ, generations=100):
    """
    Create animation based on the game of life.
    Uses matplotlib's animation module for animating the evolution.
    It is simply applying apply_rules() to the same universe list and plotting it.

    :param univ: the universe to run the animation
    :param generations: number of iterations
    """
    fig = plt.figure()
    plt.axis("off")
    ims = []

    np_univ = np.array(univ)

    for i in range(generations):
        ims.append((plt.imshow(np_univ, cmap="Greens"),))
        np_univ = np.array(apply_rules(univ))

    gol_animation = animation.ArtistAnimation(fig, ims, interval=30, repeat_delay=3000, blit=True)

    # if you want to save the animation into a mp4 file.
    # gol_animation.save('gol.mp4')
    plt.show()


"""
=== SAMPLE STRUCTURES FOR UNIVERSE ==========================
"""

beacon = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
]

ploy = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 1, 0],
]

blinker = [
    [1, 1, 1]
]

toad = [
    [0, 1, 1, 1],
    [1, 1, 1, 0]
]

glider = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
]

engine = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0]
]
