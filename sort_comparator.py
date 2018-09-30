from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
 
    def __repr__(self):
        return ' '.join([self.name, str(self.score)])

    @staticmethod
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            return 1 if a.name > b.name else -1
        return -1
      

players = ['amy 100', 'david 100', 'heraldo 50', 'aakansha 75', 'aleksa 150']
ordered_players = ['aleksa 150', 'amy 100', 'david 100', 'aakansha 75', 'heraldo 50']
data = []
for player in players:
    name, score = player.split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
data = sorted(data, key=cmp_to_key(Player.comparator))
assert [str(player) for player in data] == ordered_players
