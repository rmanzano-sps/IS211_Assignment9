from bs4 import BeautifulSoup
from urllib.request import urlopen



def reset_player_status(player_status):
    for key, value in player_status.items():
        player_status[key] = None
    return player_status

response = urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns')
# html = response.read()
# print(html)

soup = BeautifulSoup(response)
links = soup.find_all('td')
links.pop(0)

player_stats = {
    'Name': None,
    'POS': None,
    'Team': None,
    'G': None,
    'PTS': None,
    'PTS/G': None,
    'TD': None
    }

players = []

for link in links:

    for key, value in player_stats.items():
        # print(player_stats['TD'], '34')
        if value == None:
            data = link.contents[0]
            try:
                if 'players' in link.contents[0].get('href') or 'teams' in link.contents[0].get('href'):
                    data = link.contents[0].contents[0]
            finally:
                player_stats[key] = data
                break
        elif player_stats['TD'] != None:
            if len(players) < 21:
                player_data = player_stats
                players.append(player_data)
                del links[0:19]
                # print(links, '47')
                reset_player_status(player_stats)



print(players, '49')
    # print(link.contents)
    # a_tag = link.findAll('a')
    # if a_tag:
    #     search_href = a_tag[0].get('href')
    #
    #     if 'players' in search_href:
    #         player_list.append(a_tag[0].contents[0])
    #
    #     if 'teams' in search_href:
    #         player_team.append(a_tag[0].contents[0])
    #
    # if link.contents ==

# print(player_team)
