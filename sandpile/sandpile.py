
# 03-07-2019 by musicfreakt
# Functions and class for sandpiles.

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Sandpile():
    def __init__(self, arr = None ,rows = 3, cols = 3, max_sand = 4):
        """
        arr - 2d array of values
        rows - height of sandpile
        cols - width of sandpile
        max_sand - max count of sandpile grains (must be div by 4)
        """
        self.max_grains = max_sand
        if arr == None:
            self.rows = rows
            self.cols = cols
            self.grid = np.zeros((cols,rows), int)
        else:
            self.rows = len(arr)
            self.cols = len(arr[0])
            self.grid = np.array(arr)


    def topple(self, elem_x, elem_y):
        p = self.grid[elem_x, elem_y]
        b = p // self.max_grains
        o = p % self.max_grains
        self.grid[elem_x, elem_y] = o

        # increase height of neighbor piles
        try:
            self.grid[elem_x-1, elem_y] += b
            self.grid[elem_x+1, elem_y] += b
            self.grid[elem_x, elem_y-1] += b
            self.grid[elem_x, elem_y+1] += b
        except IndexError:
            print("IndexError: try to increase width or/and height of grid")


    def run(self):
        from time import time

        start_time = time()
        iterations = 0
        topple = self.topple
        where = np.where

        while np.max(self.grid) >= self.max_grains:
            elem_x, elem_y = where(self.grid >= self.max_grains)
            topple(elem_x, elem_y)
            iterations += 1

        print("--- %d iterations %s seconds ---" % (iterations, time() - start_time))

    def get_pile(self):
        return self.grid

    def set_sand(self, x, y, number):
        self.grid[x,y] = number

    def show(self, save = False, filename = "sandpile.png"):
        """
        plot sandpile and save it in the file

        filename - name of the file, where would be picture of sandpile
        """

        heatmap = plt.pcolor(self.grid)
        plt.axis('off')
        plt.imshow(self.grid)
        plt.colorbar(heatmap, ticks=range(self.max_grains))
        if save:
            plt.savefig(filename, bbox_inches='tight')
        plt.show()

    def save(self, filename = "sandpile.png"):
        colours = [(41, 128, 185), (22, 160, 133), (142, 68, 173), (52, 73, 94)]
        img = Image.fromarray(color_grid(self.grid, colours), "RGB")
        img.save(filename)

def color_grid(grid, colors):
    new_grid = np.zeros((len(grid), len(grid[0]), 3), dtype=np.uint8)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            new_grid[i, j] = colors[grid[i, j]]
    return new_grid

if __name__ == '__main__':
    pile = Sandpile(rows = 401, cols = 401)
    pile.set_sand(200, 200, 2**18)
    pile.run()
    pile.show(save = True)
    pile.save(filename = "sandpile2.png")
