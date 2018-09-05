import turtle as t


def koch_rek(i, length):
    if i < 1:
        t.forward(length)
        return
    else:
        koch_rek(i - 1, length / 3)
        t.left(60)
        koch_rek(i - 1, length / 3)
        t.right(120)
        koch_rek(i - 1, length / 3)
        t.left(60)
        koch_rek(i - 1, length / 3)


def koch_line(i, delka):
    t.up()
    t.setx(-t.window_width()/2 + 20)
    t.down()
    koch_rek(i, delka)


def koch_flake(i, delka):
    koch_rek(i, delka)
    t.right(120)
    koch_rek(i, delka)
    t.right(120)
    koch_rek(i, delka)


if __name__ == '__main__':
    t.speed(0)
    koch_line(4, t.window_width() - 40)
    # koch_flake(4, 300)
    t.done()


