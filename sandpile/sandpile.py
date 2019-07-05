
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

    # def topple_S(self, max_sand):
    #     b = max_sand//4
    #     ost = max_sand - 4*b
    #     # self.grid[max_sand] = ost
    #     # self.grid[1:,:][max_sand[:-1,:]] += b
    #     # self.grid[:-1,:][max_sand[1:,:]] += b
    #     # self.grid[:,1:][max_sand[:,:-1]] += b
    #     # self.grid[:,:-1][max_sand[:,1:]] += b


    def run(self):
        while np.max(self.grid) >= self.max_grains:
            max_sand = self.grid >= self.max_grains
            # self.topple(max_sand)
            self.topple_S(max_sand)

    def get_pile(self):
        return self.grid

    def set_sand(self, x, y, number):
        self.grid[x][y] = number

    def show(self, filename = "sandpile.png"):
        """
        plot sandpile and save it in the file

        filename - name of the file, where would be picture of sandpile
        """
        plt.matshow(self.grid, cmap=plt.get_cmap('gist_rainbow'))
        plt.axis('off')
        plt.savefig(filename, bbox_inches='tight')

if __name__ == '__main__':
    pile = Sandpile(rows = 41, cols = 41)
    pile.set_sand(20, 20, 2**10)
    pile.run()
    pile.show()
