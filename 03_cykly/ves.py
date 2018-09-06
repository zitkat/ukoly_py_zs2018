from math import sqrt
import turtle as t

strana = 20
populace = 5
for i in range(populace):
    # nakreslime domecek
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.left(45)
    t.forward(sqrt(2) * strana)
    t.left(90)
    t.forward(sqrt(2) * strana / 2)
    t.left(90)
    t.forward(sqrt(2) * strana / 2)
    t.left(90)
    t.forward(sqrt(2) * strana)

    # a posuneme se k sousedovi
    t.left(45)  # nejdriv se musime srovnat, aby byla ulice rovne
    t.forward(10)


t.done()
