import csv

import hltv_scrape as HM
import ScraperTools.tools as ST


def get_todays_results():
    try:
        main_url = HM.MAIN_URL
        todays_rank = "/results"
        soup = ST.get_soup(main_url + todays_rank)
        result_tags = []
        todays_results = soup.find_all("div", class_="result-con")
        for result in todays_results:
            result_tags += result
        todays_results_dict = {}
        count = 0
        for result in result_tags:
            act_result = result.find("tr")
            team_one, team_two = act_result.find_all("td", class_="team-cell")
            team_result = act_result.find("td", class_="result-score")
            score_one, score_two = team_result.find_all("span")
            event = act_result.find("td", class_="event")
            count += 1
            todays_results_dict[count] = {
                "team_one": team_one.get_text(),
                "score_one": score_one.get_text(),
                "score_two": score_two.get_text(),
                "team_two": team_two.get_text(),
                "result_url": f"{main_url}{result['href']}",
                "event": event.get_text()
            }

        with open(f"{HM.TODAY}_result.csv", mode='w') as file:
            ST.write_csv(file, todays_results_dict)

        return True
    except Exception as ex:
        print(ex)
        return False

if __name__ == "__main__":
    results = get_todays_results()
    print(f" Results: {HM.check_done(results)}")
