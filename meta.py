class Datum:
    """ imaginary base class for a CSV row """
    pass


class Apple(Datum):  # global Apple, class name Apple, bases Datum
    seeds = 10  # member


# Above is syntactic sugar, it is equivalent to
Apple = type("Apple", (Datum, ), dict(seeds=10))
# ^           ^        ^              ^- members
# |           |        \- list of bases
# |           \- class name
# \- global Apple


