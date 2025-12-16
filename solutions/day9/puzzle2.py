# Find the largest rectangle, brute force it
import sys
from heapq import heappop, heappush

INPUT_FILE = sys.argv[1]

MAX_X = 0
MAX_Y = 0

tiles = []
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        x, y = list(map(int, line.split(",")))
        MAX_X = max(MAX_X, x)
        MAX_Y = max(MAX_Y, y)
        tiles.append((x, y))


# So make a map of horizontal lines, so that we have a list per x of what
# horizontal lines exist. This way, when we are doing our
def get_lines(points: list[tuple[int, int]]):
    n = len(points)
    lines = {"vertical": [], "horizontal": []}
    for i in range(n):
        x1, y1 = points[i % n]
        x2, y2 = points[(i + 1) % n]

        # Deal with negative range, or always use the smaller number as
        if x1 == x2:
            lines["horizontal"].append([(x1, y1), (x2, y2)])
        else:
            lines["vertical"].append([(x1, y1), (x2, y2)])

    return lines


def get_rect_lines(r1, r2):
    x1, y1 = r1
    x2, y2 = r2

    points = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
    lines = get_lines(points)
    return lines


def check_rect_inside(
    rectangle: list[tuple[int, int]], polygon: dict[str, list[list[tuple[int, int]]]]
):
    x1, y1 = rectangle[0]
    x2, y2 = rectangle[1]

    corners = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
    for corner in corners:
        # print("Corner being checked:", corner)
        if check_point_inside(corner, polygon) % 2 == 0:
            # print("Corner outside")
            return False

    # print("Rectangle inside")
    return True


def on_segement(point, line):
    xp, yp = point
    x1, y1 = line[0]
    x2, y2 = line[1]
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    if x1 == x2:
        if xp == x1 and min_y <= yp and yp <= max_y:
            return True

    if y1 == y2:
        if yp == y1 and min_x <= xp and xp <= max_x:
            return True

    return False


def check_point_inside(
    point: tuple[int, int], polygon: dict[str, list[list[tuple[int, int]]]]
) -> int:
    intercepts = 0
    xp, yp = point
    for line in polygon["vertical"] + polygon["horizontal"]:
        if on_segement(point, line):
            # print("Point on segement")
            return 1

        x1, y1 = line[0]
        x2, _ = line[1]
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        if x1 == x2:
            # Horizontal line, continue
            continue

        if xp <= min_x or xp > max_x:
            # Outside bounds of line
            continue

        # point is on the polygon edge
        if yp == y1:
            # print("point on edge")
            return 1

        if yp < y1:
            # There will be an intercept
            intercepts += 1

    return intercepts


def check_lines_intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    min_x1 = min(x1, x2)
    max_x1 = max(x1, x2)
    min_y1 = min(y1, y2)
    max_y1 = max(y1, y2)
    min_x2 = min(x3, x4)
    max_x2 = max(x3, x4)
    min_y2 = min(y3, y4)
    max_y2 = max(y3, y4)
    # Check lines paralellel
    if x1 == x2 and x3 == x4:
        return False

    if y1 == y2 and y3 == y4:
        return False

    # line1 horizontal
    if x1 == x2:
        # line1 x1 == x2 check if its x values are between line2 xs
        if min_x2 < x1 and x1 < max_x2:
            # Check if line1 y are on either side of line2 y (y3 == y4)
            if min_y1 < y3 and y3 < max_y1:
                return True

    # line1 vertical
    else:
        # line1 y1 == y2 check if its y values are between line2 ys
        if min_y2 < y1 and y1 < max_y2:
            # Check if line1 x are on either side of line2 x (x3 == x4)
            if min_x1 < x3 and x3 < max_x1:
                return True

    return False


def check_line_vertex_inside(line1, line2, rectangle):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    min_x1 = min(x1, x2)
    max_x1 = max(x1, x2)
    min_y1 = min(y1, y2)
    max_y1 = max(y1, y2)
    min_x2 = min(x3, x4)
    max_x2 = max(x3, x4)
    min_y2 = min(y3, y4)
    max_y2 = max(y3, y4)

    if x1 == x2:
        # If only vertices touch, we are ok
        if (min_x2, y3) in line1:
            return False
        if (max_x2, y3) in line1:
            return False

        if min_x2 == x1:
            if check_point_inside((max_x2, y3), rectangle):
                return True
        elif max_x2 == x1:
            if check_point_inside((min_x2, y3), rectangle):
                return True
    else:
        # If only vertices touch, we are ok
        if (x3, min_y2) in line1:
            return False
        if (x3, max_y2) in line1:
            return False

        if min_y2 == y1:
            # print(f"Checking {(x3, max_y2)} inside {rectangle}")
            if check_point_inside((x3, max_y2), rectangle) % 2 != 0:
                # print("is inside")
                return True
        elif max_y2 == y1:
            # print(f"Checking {(x3, min_y2)} inside {rectangle}")
            if check_point_inside((x3, min_y2), rectangle) % 2 != 0:
                # print("is inside")
                return True
    return False


def check_edge_intersections(rectangle, polygon):
    # Check if there are edge interesections
    rect_lines = get_rect_lines(*rectangle)
    # print(rect_lines)
    for line in rect_lines["vertical"] + rect_lines["horizontal"]:
        x1, _ = line[0]
        x2, _ = line[1]

        # if rect line is horizontal, only check vertical intersections and vice
        # versa
        if x1 == x2:
            orient = "vertical"
        else:
            orient = "horizontal"

        for l2 in polygon[orient]:
            # line interesects and other vertex inside
            if check_line_vertex_inside(line, l2, rect_lines):
                # print(f"Lines {line} - {l2} intersect")
                return True
            # check if any lines interset our rectangle
            if check_lines_intersect(line, l2):
                # print(f"Lines {line} - {l2} intersect")
                return True
    return False


def check_rect_valid(rectangle: list[tuple[int, int]], polygon):
    # print()
    # print("Checking:", rectangle)
    # print("---------------------")

    # 1. Check if the corners of the rect is inside the polygon
    if not check_rect_inside(rectangle, polygon):
        # print(f"Rectangle {rectangle} is invalid")
        return False

    # for each line, check if it intersects
    if check_edge_intersections(rectangle, polygon):
        # print("There are edges that intersect")
        return False

    return True


# Brute force to discover create


areas = []
n = len(tiles)
for i in range(n - 1):
    for j in range(1, n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        heappush(areas, (-area, tiles[i], tiles[j]))

# print(MAX_X, MAX_Y)
POLYGON = get_lines(tiles)
# print(POLYGON)
# 1. Capture the initial total to calculate percentage
total_items = len(areas)
bar_length = 30  # Length of the visual bar in characters

while len(areas):
    a, r1, r2 = heappop(areas)
    # --- Progress Bar Logic ---
    # Calculate how many we have processed
    processed = total_items - len(areas)

    # Calculate percentage and bar fill
    percent = (processed / total_items) * 100
    filled_length = int(bar_length * processed // total_items)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    # Print with \r to overwrite line, end='' to stay on line, flush=True to update immediately
    if len(areas) % 1 == 0:
        print(
            f"\x1b[2K\rProgress: |{bar}| {percent:.1f}% ({processed}/{total_items})",
            end="",
            flush=True,
        )
    # --------------------------
    if check_rect_valid([r1, r2], POLYGON):
        print()
        print(f"The largest valid rectangle {(r1, r2)} has area: {-a}")
        break
