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

    gamelist = etree.HTML(
        session.post(
            base_url + gamelist, 
            data=data, 
            headers=headers
        ).text
    )

    try:
        gamebreakdown = gamelist.xpath(
            "//div[@id='gamelist_list']/div[1]/a[@title='Full Game Page']/@href")[0]
    except:
        return "No results."

    html = etree.HTML(
       session.get(
          base_url + gamebreakdown,
          headers=headers
       ).text
    )

    title = html.xpath(
        "//div[@class='headermain']/text()")[0]

    params = {"url": base_url + gamebreakdown}

    link = session.get(
        "http://tinyurl.com/api-create.php?", params=params).text

    table = html.xpath("//div[@class='gamepage_flow']/table")[0]

    main_time = table.xpath("//tbody[2]/tr/td[4]/text()")[0].strip()
    extra_time = table.xpath("//tbody[3]/tr/td[4]/text()")[0].strip()
    complete_time = table.xpath("//tbody[4]/tr/td[4]/text()")[0].strip()
    overall = table.xpath("//tbody[5]/tr/td[4]/text()")[0].strip()

    return "How long to beat %s (%s) (averages): Main Story: %s, Main + Extras: %s, Completionist: %s, Overall: %s" % (
        title, link, main_time, extra_time, complete_time, overall)

@hook.command('hltb')
@hook.command('howlong')
@hook.command
def howlongtobeat(inp, say=None):
    return how_long(inp)

if __name__ == "__main__":
    print how_long("Bastion")
