# https://www.tocode.co.il/bundles/python/lessons/21-class-syntax-lab (4)

# Lines management: get in line, call next, choose clerk
# commands: wait clerk_name person, next clerk_name

class Lineup:
    def __init__(self):
        from collections import defaultdict
        self.lineup = defaultdict(list)
        self.loop = True

    def wait(self, *args):
        clerk = args[0]
        person = args[1]
        self.lineup[clerk].append(person)

    def next(self, *args):
        try:
            l = {key: len(value) for key, value in self.lineup.items() if len(value) > 0}
            clerks = [k for k, v in l.items() if v == min(l.values())]
            if args[0] in clerks:
                clerk = args[0]
            else:
                clerk = clerks[0]
            print(self.lineup[clerk])
            print(self.lineup[clerk].pop(0))
        except IndexError as e:
            print(f"No lineup for clerk {args[0]}. {e}")
            self.loop = False


lineup = Lineup()
while lineup.loop:
    cmd_input = (input(": ")).strip()
    atts = [att for att in cmd_input.split(' ')[1:]]
    func = getattr(lineup, cmd_input.split(' ')[0])
    func(*atts)
