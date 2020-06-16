import ScraperTools.tools as ST
import hltv_main as HM

import csv

def get_todays_events():
    try:
        main_url = HM.MAIN_URL
        todays_events = "/events#tab-TODAY"
        soup = ST.get_soup(main_url + todays_events)
        today_tab = ST.get_elem(soup, "div", "id", "TODAY")
        todays_events = ST.get_elems(today_tab, "a", "class", "ongoing-event")
        todays_events_dict = {}
        count = 0
        sorted_day = HM.TODAY.strftime("%d/%m/%Y")
        for event in todays_events:
            count += 1
            dates = ST.get_elems(event, "span", "data-time-format", "MMM do")
            if len(dates) > 1:
                start_date = dates[0].get_text()
                end_date = dates[1].get_text()
            else:
                start_date = dates[0].get_text()
                end_date = start_date
            todays_events_dict[count] = {
                "event_name": event.get_text().replace("\n", ""),
                "event_url": f"{main_url}{event.attrs['href']}",
                "start_date": ST.convert_date_ws_ns(start_date),
                "end_date": ST.convert_date_ws_ns(end_date)
            }

        with open(f"{HM.TODAY}_events.csv", mode='w') as events_file:
            ST.write_csv(events_file, todays_events_dict)
        return True
    except Exception as ex:
        print(ex)
        return False
