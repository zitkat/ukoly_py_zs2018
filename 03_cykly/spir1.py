import turtle as t

strana = 100

t.left(90)
for i in range(20):  # hranata spirala ma 5 zavitu, kazdy 4 strany
    t.forward(strana - 5*i)  # zmensujeme stranu, cisla odhadneme aby byl obrazek hezky
    t.right(90)  # kreslime "ctverce" takze pravy uhel
t.done()
