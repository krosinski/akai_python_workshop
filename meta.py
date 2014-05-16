class Datum(object):
    """ imaginary base class for a CSV row """
    pass


#     /- global and class name
#     |      /- bases
class Apple(Datum):
    seeds = 10
    # member


# Above is syntactic sugar, it is equivalent to
Apple = type("Apple", (Datum, ), dict(seeds=10))
# ^           ^        ^              ^- members
# |           |        \- list of bases
# |           \- class name
# \- global Apple


# define a class at run time
def define_me_a_class(something):
    class Apple(Datum):
        seeds = something

    return Apple


# test
A1 = define_me_a_class(5)
A2 = define_me_a_class(7)

assert A1 is not A2
assert A1.seeds != A2.seeds


# alternatively define same using type
A1 = type("Apple", (Datum, ), dict(seeds=5))
A2 = type("Apple", (Datum, ), dict(seeds=7))


# What about dynamic member names?
# * syntacic definition -- kinda hard
# * type() works, but it's ugly

# Python got you covered, extend `type`
class FruityMeta(type):
    # magic prepare modifies target class namespace
    @classmethod
    def __prepare__(metacls, name, bases, **kw):
        kw["seeds"] = 42  # all fruits have seeds
        return kw


class Apple(Datum, metaclass=FruityMeta):
    pass


assert Apple().seeds == 42


# For more hack, override `type.__new__` and pass other keywords
class FruityMeta(type):
    def __new__(cls, name, bases, ns, **kw):
        xx = kw.pop("xx")
        rv = type.__new__(cls, name, bases, ns)
        rv.seeds = 13
        rv.xx = xx
        return rv


class Apple(Datum, metaclass=FruityMeta, xx=123):
    pass


assert Apple().seeds == 13
assert not Apple().xx
