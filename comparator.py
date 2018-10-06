from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self): # know how to use this.
        return "".join([self.name, self.score])
        
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            return 1 if a.name > b.name else -1
        else:
            return -1


result =[]
data = [['amy', 100], ['david', 100], ['heraldo', 50], ['aakansha', 75], ['aleksa', 150]]
for name, score in data:
    player = Player(name, score)
    result.append(player)

print(sorted(data, key=cmp_to_key(Player.comparator)))