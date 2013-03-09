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
    gamebreakdown = "http://howlongtobeat.com/gamebreakdown_main.php"

    params = {
        "s": inp
    }

    html = session.get(gamelist, params=params).text

    return html

@hook.command('hltb')
@hook.command('howlong')
@hook.command
def howlongtobeat(inp):
    return how_long(inp)

if __name__ == "__main__":
    print how_long("Bastion")
