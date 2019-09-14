from sandpile import Sandpile

pile = Sandpile(rows = 101, cols = 101)
pile.set_sand(50, 50, 2**17)
pile.run()
pile.save(filename = "2^17 grains(2).png")
