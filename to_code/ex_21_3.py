# https://www.tocode.co.il/bundles/python/lessons/21-class-syntax-lab (3)

# Question: I couldn't figure out how to add dependencies if they don't exist and how to not build twice....
# בניית רכיב שתלוי ברכיבים אחרים תבנה אוטומטית גם את כל הרכיבים בהם הוא תלוי. אין צורך לבנות רכיב פעמיים

# Why not use an instance variable (is_built) ?

class Widget:
    def __init__(self, name):
        self.is_built = False
        self.name = name
        self._dependencies = []

    def add_dependency(self, *args):
        self._dependencies.extend(args)

    def build(self):
        self.is_build = True
        print(f"{','.join([d.name for d in self._dependencies])}")


luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("")

luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
# print(_all)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)
