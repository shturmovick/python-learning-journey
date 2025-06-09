games = ['Rdr2', 'Tlou', 'Witcher 3', 'Uncharted 4', 'God of War', 'Elden Ring', 'Dark souls', 'death stranding', 'death stranding']

games.append ( 'Horizon')
games.pop ( 5)
games.sort ( )
games.insert ( 0, 'Battlefield')
games.remove ( 'Dark souls')
games.reverse ( )
duplicates = games.count ( 'death stranding')

print ( games)
print ( f"'death stranding' встречается {duplicates} раза" )