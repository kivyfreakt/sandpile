
# 03-07-2019 by musicfreakt
# Functions and class for sandpiles.

import numpy as np
import matplotlib.pyplot as plt

class Sandpile():
    def __init__(self, arr = None ,rows = 3, cols = 3, max_sand = 4):
        """
        arr - 2d array of values
        rows - height of sandpile
        cols - width of sandpile
        max_sand - max count of sandpile grains (> 3)
        """
        if arr == None:
            self.rows = rows
            self.cols = cols
            self.max_grains = max_sand
            self.grid = np.zeros((cols,rows), int)
        else:
            self.rows = len(arr)
            self.cols = len(arr[0])
            self.max_grains = max_sand
            self.grid = np.array(arr)

    def topple(self, max_sand):
        self.grid[max_sand] -= self.max_grains
        self.grid[1:,:][max_sand[:-1,:]] += 1
        self.grid[:-1,:][max_sand[1:,:]] += 1
        self.grid[:,1:][max_sand[:,:-1]] += 1
        self.grid[:,:-1][max_sand[:,1:]] += 1

    def run(self):
        while np.max(self.grid) >= self.max_grains:
            max_sand = self.grid >= self.max_grains
            self.topple(max_sand)

    def get_pile(self):
        return self.grid

    def set_sand(self, x, y, number):
        self.grid[x][y] = number

    def show(self):
        plt.matshow(self.grid, cmap=plt.get_cmap('gist_rainbow'))
        plt.axis('off')
        filename = "sandpile.png"
        plt.savefig(filename, bbox_inches='tight')

if __name__ == '__main__':
    pile = Sandpile(rows = 101, cols = 101)
    pile.set_sand(50, 50, 65536)
    pile.run()
    pile.show()
