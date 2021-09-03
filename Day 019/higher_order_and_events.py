def add(n1, n2):
    print(n1 + n2)


def multiply(n1, n2):
    print(n1 * n2)


def perform(n1, n2, fun):
    fun(n1, n2)


perform(2, 3, add)
perform(2, 3, multiply)


