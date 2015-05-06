import json, random

def strats(map):
    maps = ['general', 'nuke', 'train', 'season', 'd2', 'inferno', 'mirage', 'cache', 'cbble', 'overpass']
    with open('res/strats.json') as data:
        data = json.load(data);
        if map not in maps:
            return "Map must be from " + ", ".join(maps)
        else:
            rand = random.randint(1, len(data[map]) - 1)
            return "[Map] " + map + "\n[Strat Name] " + data[map][rand]['title'] + "\n[Strat] " + data[map][rand]['text'] + "\n[Side] " + data[map][rand]['side']
