import tkinter as tk
from queue import Queue

maze = [
    ["O", "#", " ", " ", " ", "#", " ", " ", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", " ", " ", "#", " ", " ", " ", "#", " "],
    ["#", "#", "#", "#", "#", "#", " ", "#", " "],
    [" ", " ", " ", " ", " ", " ", " ", "#", " "],
    [" ", "#", "#", "#", "#", "#", "#", "#", " "],
    [" ", "#", " ", " ", " ", " ", " ", " ", " "],
    [" ", "#", " ", "#", "#", "#", "#", "#", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", "X"]
]

CELL_SIZE = 40

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.rows = len(maze)
        self.cols = len(maze[0])

        self.canvas = tk.Canvas(root, width=self.cols*CELL_SIZE, height=self.rows*CELL_SIZE)
        self.canvas.pack()

        self.draw_maze()
        self.start_pos = self.find_start()

        self.queue = Queue()
        self.queue.put((self.start_pos, [self.start_pos]))
        self.visited = set()

        self.animate()

    def draw_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = "white"
                if maze[i][j] == "#":
                    color = "black"
                elif maze[i][j] == "O":
                    color = "green"
                elif maze[i][j] == "X":
                    color = "red"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def find_start(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if maze[i][j] == "O":
                    return (i, j)

    def get_neighbors(self, row, col):
        neighbors = []
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for dr, dc in directions:
            r, c = row+dr, col+dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbors.append((r, c))
        return neighbors

    def color_cell(self, row, col, color):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def animate(self):
        if self.queue.empty():
            return

        current_pos, path = self.queue.get()
        row, col = current_pos

        if maze[row][col] == "X":
            for r, c in path:
                self.color_cell(r, c, "blue")
            return

        for r, c in path:
            if maze[r][c] not in ("O", "X"):
                self.color_cell(r, c, "yellow")

        for neighbor in self.get_neighbors(row, col):
            if neighbor in self.visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            self.queue.put((neighbor, path + [neighbor]))
            self.visited.add(neighbor)

        self.root.after(100, self.animate)


root = tk.Tk()
root.title("Maze Solver BFS - Tkinter")
app = MazeApp(root)
root.mainloop()
