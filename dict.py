goty = {
  'God of War' : '2018',
  'Sekiro: Shadow die twice' : '2019',
  'The Last of Us 2' : '2020',
  'It takes two' : '2021',
  'Elden Ring' : '2022',
  "Baldur's gate 3" : '2023',
  'Astro bot' : '2024'
}
goty['GTA5'] = '2013'
goty['The Witcher 3'] = '2015'
goty.pop ('Elden Ring')
for game, year in goty.items (  ):
  if int(year) < 2018:
    print(f'{game} : {year} - Старая классика')
  else:
    print (f'{game} : {year}')