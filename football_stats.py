### TO RUN TYPE python football_stats.py 

from bs4 import BeautifulSoup
from urllib.request import urlopen
import copy

class CollectStats:

    def __init__(self):
        self.player_stats = {
            "Player's Name": '',
            "Player's Position": '',
            "Player's Team": '',
            "G": '',
            "PTS": '',
            "PTS/G": '',
            "Player's Touch Down": ''
            }
        self.response = urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns')
        self.links = None
        self.counter = 0

    def reset_player_status(self, player_status):
        for key, value in player_status.items():
            player_status[key] = ''
        return player_status

    def create_player_data(self,link):
        for key, value in self.player_stats.items():
            if value == '':
                data = link.contents[0]
                try:
                    if 'players' in link.contents[0].get('href') or 'teams' in link.contents[0].get('href'):
                        data = link.contents[0].contents[0]
                finally:
                    self.player_stats[key] = data
                    return self.player_stats[key]
            elif self.player_stats["Player's Touch Down"] != '':
                return self.player_stats



    def start_process(self):
        soup = BeautifulSoup(self.response, "lxml")
        self.links = soup.find_all('td')
        self.links.pop(0)
        players = []
        for link in self.links:
            self.create_player_data(link)
            if self.player_stats["Player's Touch Down"] != '' and len(players) < 20:
                # print(self.player_stats, 'line player_stats')
                player = copy.copy(self.player_stats)
                keys = ["G", "PTS", "PTS/G"]
                player = {key: player[key] for key in player if key not in keys}
                players.insert(self.counter, player)
                self.counter = 1 + self.counter
                del self.links[0:12]
                self.reset_player_status(self.player_stats)


        return players


if __name__ == '__main__':
    start = CollectStats()
    results = start.start_process()
    counter = 1
    for player in results:
        playername = str(list(player.values())[0])
        print(str(counter) + ' ' + playername + ' = ' + str(player))
        counter = counter + 1
