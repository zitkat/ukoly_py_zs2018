from toolz import map, partial, cons, reduce, accumulate, sliding_window, iterate, first, second
from operator import mul, and_, add
from math import sqrt, ceil

#
# print("".join(map(lambda x: "a\n", range(5))))
#
# print("".join(map(lambda x: "Radek {0}\n".format(x), range(5))))
#
# print("".join(map(lambda x: "{0} na druhou je {1}\n".format(x, x**2), range(5))))
#
# print("".join(map(lambda y: "".join(map(lambda x: "x", range(5))) + "\n", range(5))))
#
# print("".join(map(lambda y: "".join(map(lambda x: " {0}".format(y*x), range(5))) + "\n", range(5))))
#
# print(list(map(lambda y: list(map(lambda x: " {0}".format(y*x), range(5))), range(5))))
#
# print(list(map(list, map(lambda y: map(lambda x: " {0}".format(y*x), range(5)), range(5)))))
#
# print("\n".join(map("".join, map(lambda y: map(lambda x: " {0}".format(y*x), range(5)), range(5)))))
#
# print("".join(map(lambda y: "".join(map(lambda x: "x", range(y))) + "\n", range(1, 5))))
#
# print(reduce(mul, range(1, int(input("Zadejte cislo: "))+1)))


def is_prime(N):
    return reduce(and_, map(lambda x: N % x != 0,
                                  cons(2, range(3, int(ceil(sqrt(N))+1), 2))))


# print(is_prime(int(input("Zadejte N: "))))

# print((lambda N: True if N == 2 else reduce(and_,
#                                             map(lambda x: N % x != 0,
#                                                 cons(2, range(3, int(ceil(sqrt(N))+1), 2)))))
#       (int(input("Zadejte N: "))))


def fibf(N):
    f = iterate(
        lambda x: list(cons(first(x) + second(x), x)),
        [1, 1])
    return list(map(lambda x: next(f), range(N)))[-1][::-1]

    # return [next(f) for i in range(N)][-1][::-1]
# print(fibf(5))


fibff = partial((lambda f, N: list(map(lambda _: next(f), range(N-1)))[-1][::-1]),
                iterate(lambda x: list(cons(first(x) + second(x), x)), [1, 1]))

print(fibff(22))

# list(map(print, iterate(lambda x: list(cons(first(x) + second(x), x)), [1, 1])))

