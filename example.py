import tbapy

tba = tbapy.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')

team = tba.team(254)
districts = tba.team_districts(1418)
match = tba.match(year=2017,
                  event='chcmp',
                  type='qm',
                  match=2)

print('Team 254 is from %s in %s, %s.' % (team['city'], team['state_prov'], team['country']))
print('Team 1418 is/was in the %s district in the most recent year of competition.' % districts[-1]['display_name'])
print('The second qual match at the 2017 CHS District Championship was predicted to start at Unix Time %s.' % match['predicted_time'])
