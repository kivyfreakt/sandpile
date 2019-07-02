
# 03-07-2019 by musicfreakt
# Functions and classes for sandpiles.

class Sandpile():
    def __init__(self):
        super(Sandpile, self).__init__()
        self.width = 3
        self.height = 3
        self.max_sand = 4
        self.sandpile = [[0 for y in range(self.height)] for x in range(self.width)]

    def check_topple(self):
        num = []
        for x in range(self.width):
            for y in range(self.height):
                if self.sandpile[x][y] >= self.max_sand:
                    num.append([x,y])
        if len(num) > 0:
            return num
        else:
            return None

    def topple_batch(self, num):
        newpile = self.sandpile
        for pos in num:
            x = pos[0]
            y = pos[1]
            newpile[x][y] = self.sandpile[x][y] - self.max_sand
            if x+1 < self.width:
                newpile[x+1][y]+=1
            if x-1 >= 0:
                newpile[x-1][y]+=1
            if y+1 < self.height:
                newpile[x][y+1]+=1
            if y-1 >= 0:
                newpile[x][y-1]+=1

        self.sandpile = newpile

    def topple(self):
        num = self.check_topple()
        while num != None:
            self.topple_batch(num)
            num = self.check_topple()

    def get_pile(self):
        return self.sandpile

    def set_sand(self, number, x, y):
        self.sandpile[x][y] = number

if __name__ == '__main__':
    pile = Sandpile()
    pile.set_sand(10, 1, 1)
    print(pile.get_pile())
    pile.topple()
    print(pile.get_pile())
