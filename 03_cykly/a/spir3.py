import turtle as t

t.left(90)
for i in range(1, 300):
    t.forward(i/10)  # pomalu zvetsujeme stranu
    t.right(15)  # a kreslime "hodně"-uhelník

t.done()
