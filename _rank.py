import ScraperTools.tools as ST
import hltv_main as HM

import csv

def get_todays_ranks():
    try:
        main_url = HM.MAIN_URL
        todays_rank = "/ranking/teams/"
        soup = ST.get_soup(main_url + todays_rank)
        today_rank_box = ST.get_elem(soup, "div", "class", "ranking")
        todays_teams = ST.get_elems(today_rank_box, "div", "class", "ranked-team")
        todays_rank_dict = {}
        count = 0
        for team in todays_teams:
            header =  ST.get_elem(team, "div", "class", "ranking-header")
            players = ST.get_elems(team, "div", "class", "rankingNicknames")
            print(header.find_all())
            count += 1
            links = ST.get_elems(team, "a", "class", "moreLink")
            profile_link = links[0].attrs['href']
            rank_stats_link = links[1].attrs['href']
            todays_rank_dict[count] = {
                "position": ST.get_elem(header, "span", "class", "position").get_text().replace("#", ""),
                "name": ST.get_elem(header, "span", "class", "name").get_text(),
                "points": ST.get_elem(header, "span", "class", "points").get_text().replace("(", "").replace("points)", ""),
                "profile_link": f"{main_url}{links[0].attrs['href']}",
                "rank_stats_link": f"{main_url}{links[1].attrs['href']}",
                "team_players": [x.get_text() for x in players]
            }

        with open(f"{HM.TODAY}_rank.csv", mode='w') as rank_file:
            ST.write_csv(rank_file, todays_rank_dict)
        return True
    except Exception as ex:
        print(ex)
        return False
