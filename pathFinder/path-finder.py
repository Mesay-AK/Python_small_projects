import curses
import time
import queue
from curses import wrapper

maze = [
    ["#", "#", "#", "#", "O", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "X", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(stdscr, maze, path = []):
    Blue = curses.color_pair(1)
    Red = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", Red)
            else:
                stdscr.addstr(i, j*2, value, Blue)

def find_start(start, maze):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
            
    return None
            

        
def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_position = find_start(start, maze)


    q = queue.Queue()
    q.put((start_position, [start_position]))
    visited = set()

    while not q.empty():
        curr, path = q.get()
        row, col = curr

        stdscr.clear()
        print_maze(stdscr, maze, path)
        time.sleep(0.2)
        stdscr.refresh()
        
        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(curr, maze)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                r, c = neighbor
                if maze[r][c] != "#":
                    q.put((neighbor, path + [neighbor]))
                    visited.add(neighbor)


def find_neighbors(curr, maze):
    row, col = curr
    neighbours = []

    if row > 0: # checking Up
        neighbours.append((row - 1, col))
    if row < len(maze) - 1: # checking down
        neighbours.append((row + 1, col))
    if col > 0: # checking left
        neighbours.append((row, col - 1))
    if col < len(maze[0]) - 1: # checking right
        neighbours.append((row, col + 1))
    
    return neighbours

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


    path = find_path(maze, stdscr)
    stdscr.getch()



wrapper(main)