from sandpile import Sandpile

pile = Sandpile(rows = 201, cols = 201)

pile.set_sand(100, 100, 2**16)

pile.run()

pile.show(save = True, filename = "2^16 grains(1).png")

pile.save(filename = "2^16 grains(2).png")
