import requests
from lxml import etree
from util import hook

def how_long(inp):
    """ 
    returns a breakdown of the top result from a howlongtobeat.com search
    """

    session = requests.Session()

    session.get("http://howlongtobeat.com/")

    gamelist = "http://howlongtobeat.com/gamelist_main.php"
    gamebreakdown = "http://howlongtobeat.com/gamebreakdown.php"

    data = {
        "query": inp
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
    html = etree.HTML(session.post(gamelist, data=data, headers=headers).text)

    gameid = 0

    data = {
        "gameid": gameid
    }

    return html

@hook.command('hltb')
@hook.command('howlong')
@hook.command
def howlongtobeat(inp):
    return how_long(inp)

if __name__ == "__main__":
    print how_long("Bastion")
