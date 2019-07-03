
# 03-07-2019 by musicfreakt
# Functions and class for sandpiles.

import numpy as np

class Sandpile():
    def __init__(self, width, height, max_sand = 3):
        super(Sandpile, self).__init__()
        self.width = width
        self.height = height
        self.max_grains = max_sand + 1
        self.grid = np.zeros((width,height), int)

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

    def set_sand(self, number, x, y):
        self.grid[x][y] = number


if __name__ == '__main__':
    pile = Sandpile(11,11)
    pile.set_sand(4096, 5, 5)
    pile.run()
    grid = pile.get_pile()
    for x in range(11):
        for y in range(11):
            print(grid[x][y], end = ' ')
        print()
