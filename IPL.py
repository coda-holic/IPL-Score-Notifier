from pycricbuzz import Cricbuzz
from plyer import notification
import time

c = Cricbuzz()


teams = {'Chennai Super Kings':'CSK', 'Delhi Capitals':'DC','Kings XI Punjab':'KXIP', 'Kolkata Knight Riders':'KKR', 'Mumbai Indians': 'MI', 'Rajasthan Royals':'RR', 'Royal Challengers Bangalore':'RCB','Sunrisers Hyderabad':'SRH'}

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'E:\\Codaholic\\Videos\\Other videos\\IPL Score\\IPL Logo.ico',
        timeout = 300
    )

if __name__ == "__main__":
    while True:
        match = c.matches()
        IPL = []
        for tournament in match:
            if tournament['srs'] == 'Indian Premier League 2020':
                IPL.append(tournament)
        for data in IPL:
            match_id = data['id']
            score = c.livescore(match_id)
            team_1 = data['team1']['name']
            team_2 = data['team2']['name']
            team_1_sf = teams[data['team1']['name']]
            team_2_sf = teams[data['team2']['name']]
            stadium = data['venue_name']
            if data['mchstate'] == 'toss':
                mch_toss = data['toss']
                notify(f'{team_1_sf} VS {team_2_sf}', f'{mch_toss}')
            elif data['mchstate'] == 'inprogress':
                try:
                    if score['batting']['score'][0]['inning_num'] == '1':
                            batting_team = score['batting']['team']
                            batting_team_sf = teams[batting_team]
                            runs = score['batting']['score'][0]['runs']
                            wickets = score['batting']['score'][0]['wickets']
                            overs = score['batting']['score'][0]['overs']
                            batsman_1 = score['batting']['batsman'][0]['name']
                            batsman_1_runs = score['batting']['batsman'][0]['runs']
                            batsman_1_balls = score['batting']['batsman'][0]['balls']
                            batsman_2 = score['batting']['batsman'][1]['name']
                            batsman_2_runs = score['batting']['batsman'][1]['runs']
                            batsman_2_balls = score['batting']['batsman'][1]['balls']
                            bowler = score['bowling']['bowler'][0]['name']
                            bowler_runs = score['bowling']['bowler'][0]['runs']
                            bowler_wickets = score['bowling']['bowler'][0]['wickets']
                            bowler_overs = score['bowling']['bowler'][0]['overs']
                            notify(f'{team_1_sf} VS {team_2_sf}', f'{batting_team_sf} : {runs}/{wickets} ({overs})\n{batsman_1} : {batsman_1_runs}({batsman_1_balls})\n{batsman_2} : {batsman_2_runs}({batsman_2_balls})\n{bowler} : {bowler_wickets}-{bowler_runs} ({bowler_overs})')
                            break
                    elif score['batting']['score'][0]['inning_num'] == '2' and float(score['batting']['score'][0]['overs'])<16:
                            batting_team = score['batting']['team']
                            batting_team_sf = teams[batting_team]
                            runs = score['batting']['score'][0]['runs']
                            wickets = score['batting']['score'][0]['wickets']
                            overs = score['batting']['score'][0]['overs']
                            batsman_1 = score['batting']['batsman'][0]['name']
                            batsman_1_runs = score['batting']['batsman'][0]['runs']
                            batsman_1_balls = score['batting']['batsman'][0]['balls']
                            batsman_2 = score['batting']['batsman'][1]['name']
                            batsman_2_runs = score['batting']['batsman'][1]['runs']
                            batsman_2_balls = score['batting']['batsman'][1]['balls']
                            bowler = score['bowling']['bowler'][0]['name']
                            bowler_runs = score['bowling']['bowler'][0]['runs']
                            bowler_wickets = score['bowling']['bowler'][0]['wickets']
                            bowler_overs = score['bowling']['bowler'][0]['overs']
                            notify(f'{team_1_sf} VS {team_2_sf}', f'{batting_team_sf} : {runs}/{wickets} ({overs})\n{batsman_1} : {batsman_1_runs}({batsman_1_balls})\n{batsman_2} : {batsman_2_runs}({batsman_2_balls})\n{bowler} : {bowler_wickets}-{bowler_runs} ({bowler_overs})')
                            break
                    elif score['batting']['score'][0]['inning_num'] == '2' and float(score['batting']['score'][0]['overs'])>16:
                            batting_team = score['batting']['team']
                            batting_team_sf = teams[batting_team]
                            runs = score['batting']['score'][0]['runs']
                            wickets = score['batting']['score'][0]['wickets']
                            overs = score['batting']['score'][0]['overs']
                            batsman_1 = score['batting']['batsman'][0]['name']
                            batsman_1_runs = score['batting']['batsman'][0]['runs']
                            batsman_1_balls = score['batting']['batsman'][0]['balls']
                            batsman_2 = score['batting']['batsman'][1]['name']
                            batsman_2_runs = score['batting']['batsman'][1]['runs']
                            batsman_2_balls = score['batting']['batsman'][1]['balls']
                            mch_status = data['status']
                            notify(f'{team_1_sf} VS {team_2_sf}', f'{batting_team_sf} : {runs}/{wickets} ({overs})\n{batsman_1} : {batsman_1_runs}({batsman_1_balls})\n{batsman_2} : {batsman_2_runs}({batsman_2_balls})\n{mch_status}')
                            break
                except:
                    batting_team = score['batting']['team']
                    batting_team_sf = teams[batting_team]
                    runs = score['batting']['score'][0]['runs']
                    wickets = score['batting']['score'][0]['wickets']
                    overs = score['batting']['score'][0]['overs']
                    batsman_1 = score['batting']['batsman'][0]['name']
                    batsman_1_runs = score['batting']['batsman'][0]['runs']
                    batsman_1_balls = score['batting']['batsman'][0]['balls']
                    bowler = score['bowling']['bowler'][0]['name']
                    bowler_runs = score['bowling']['bowler'][0]['runs']
                    bowler_wickets = score['bowling']['bowler'][0]['wickets']
                    bowler_overs = score['bowling']['bowler'][0]['overs']
                    notify(f'{team_1_sf} VS {team_2_sf}', f'{batting_team_sf} : {runs}/{wickets} ({overs})\n{batsman_1} : {batsman_1_runs}({batsman_1_balls})\n{bowler} : {bowler_wickets}-{bowler_runs} ({bowler_overs})')
                    break
            elif data['mchstate'] == 'innings break':
                batting_team = score['batting']['team']
                batting_team_sf = teams[batting_team]
                runs = score['batting']['score'][0]['runs']
                wickets = score['batting']['score'][0]['wickets']
                overs = score['batting']['score'][0]['overs']
                mch_status = data['status']
                notify(f'{team_1_sf} VS {team_2_sf}', f'{batting_team_sf} : {runs}/{wickets} ({overs})\n{mch_status}')
                break
            else:
                notify('Indian Premier League 2020', 'There are no live matches going on now')
                break
        IPL.clear()
        time.sleep(300)