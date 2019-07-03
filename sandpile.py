
# 03-07-2019 by musicfreakt
# Functions and class for sandpiles.

class Sandpile():
    def __init__(self, width, height, max_sand = 3):
        super(Sandpile, self).__init__()
        self.width = width
        self.height = height
        self.max_grains = max_sand + 1
        self.sandpile = [[0 for y in range(self.height)] for x in range(self.width)]

    def check_topple(self):
        num = []
        for x in range(self.width):
            for y in range(self.height):
                if self.sandpile[x][y] >= self.max_grains:
                    num.append([x,y])
        if len(num) > 0:
            return num
        else:
            return None

    def topple(self, num):
        newpile = self.sandpile
        for pos in num:
            x = pos[0]
            y = pos[1]
            newpile[x][y] = self.sandpile[x][y] - self.max_grains
            if x+1 < self.width:
                newpile[x+1][y]+=1
            if x-1 >= 0:
                newpile[x-1][y]+=1
            if y+1 < self.height:
                newpile[x][y+1]+=1
            if y-1 >= 0:
                newpile[x][y-1]+=1

        self.sandpile = newpile

    def run(self):
        num = self.check_topple()
        while num != None:
            self.topple(num)
            num = self.check_topple()

    def get_pile(self):
        return self.sandpile

    def set_sand(self, number, x, y):
        self.sandpile[x][y] = number

if __name__ == '__main__':
    pile = Sandpile(9,9)
    pile.set_sand(1000, 4, 4)
    pile.run()
    grid = pile.get_pile()
    for x in range(9):
        for y in range(9):
            print(grid[x][y], end = ' ')
        print()
