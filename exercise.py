def get_fruits(filename):
    # your code here
    pass


f1 = get_fruits("Orange.csv")
f2 = get_fruits("Pear.csv")

# both oranges and pears have id's and weight, there are 2 of each
assert f1[0].id
assert f2[0].id
assert f1[0].weight
assert f2[0].weight
assert len(f1) == len(f2) == 2

# oranges have slices
assert f1[0].slices
assert f1[0].__class__.__name__ == "Orange"

# pears are oblong and have diameter
assert f2[0].onlongness
assert f2[0].diameter
assert f2[0].__class__.__name__ == "Pear"

total_weight = sum([f.weight for f in f1 + f2])
print("total weight", total_weight)
assert total_weight == 1.035


# and now for some unicode
f3 = get_fruits("Ångström.csv")
assert sum([f.ilość for f in f3]) == 24.33


class Foobar(Ångström):
    def foo(self):
        return "fun in %s" % self.구역
