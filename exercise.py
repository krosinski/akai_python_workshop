import csv
import pprint

class FruitMeta(type):
    def __new__(cls, name, bases, ns, **kw):
        name = kw.get("filename") or name
        ns = kw.get("fields") or ns
        return type.__new__(cls, name, bases, ns)

    def __init__(cls, name, bases, ns, **kw):
        type.__init__(cls, name, bases, ns)

def get_fruits(filename):
    returnval = []
    with open(filename, newline= '') as csvfile:
        reader = csv.reader(csvfile, delimiter = '\n')
        field_names = reader.__next__()[0].split(',')
        class Fruit(object, metaclass=FruitMeta, filename=filename[:-4], fields = {x : None for x in field_names}):
            pass


        for line in reader:
            split_line = line[0].split(',')
            new_fruit = Fruit()
            for i in range(len(field_names)):
                new_fruit.__setattr__(field_names[i], float(split_line[i]))
            returnval.append(new_fruit)
        return returnval


f1 = get_fruits("Orange.csv")
f2 = get_fruits("Pear.csv")



assert f1[0].id
assert f2[0].id
assert f1[0].weight
assert f2[0].weight
assert len(f1) == len(f2) == 2

# oranges have slices
assert f1[0].slices
assert f1[0].__class__.__name__ == "Orange"

# pears are oblong and have diameter
assert f2[0].oblongless
assert f2[0].diameter
assert f2[0].__class__.__name__ == "Pear"

total_weight = sum([f.weight for f in f1 + f2])
print("total weight", total_weight)
assert total_weight == 1.035
