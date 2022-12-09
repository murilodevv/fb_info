
import requests
from bs4 import BeautifulSoup

class Foot:

    def __init__(self):
        pass

    def get_players(self):
        players = []

        page = requests.request('GET', 'https://fbref.com/en/country/players/BRA/Brazil-Football-Players')
        content = page.content

        soup = BeautifulSoup(content, 'html.parser')

        div1 = soup.find("div",attrs={"class":"section_content"})
        
        for i in div1:
            a = i.find('a')
            print(a.contents)

    def get_clubs(self):
        clubs = []

        page = requests.request('GET', 'https://fbref.com/en/country/clubs/BRA/Brazil-Football-Clubs')
        content = page.content

        soup = BeautifulSoup(content, 'html.parser')

        tbody = soup.find('tbody')
        tr = tbody.find_all('tr')

        for i in tr:
            a = i.find('a')
            clubs.append(a.contents)
        
        print(clubs)

if __name__=='__main__':
    clubs = Foot()
    clubs.get_players()
