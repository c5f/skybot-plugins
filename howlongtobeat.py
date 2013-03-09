import requests
from lxml import etree
from util import hook

def how_long(inp):
    """ 
    returns a breakdown of the top result from a howlongtobeat.com search
    """

    session = requests.Session()

    base_url = "http://howlongtobeat.com/"

    gamelist = "gamelist_main.php"

    data = {
        "queryString": inp
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
    gamelist = session.post(
        base_url + gamelist, 
        data=data, 
        headers=headers
    ).text

    gamebreakdown = gamelist.xpath(
        "//div[@id='gamelist_list']/div[1]/a[@title='Full Game Page']/@href/text()")[0]

#    html = etree.HTML(
#        session.get(
#            base_url + gamebreakdown,
#            headers=headers
#        ).text
#    )

    return gamelist

@hook.command('hltb')
@hook.command('howlong')
@hook.command
def howlongtobeat(inp):
    return how_long(inp)

if __name__ == "__main__":
    print how_long("Bastion")
