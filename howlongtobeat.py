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
        gamebreakdown = gamelist.find(
            ".//a[@title='Full Game Page']").get("href")
    except:
        return "No results."

    html = etree.HTML(
       session.get(
          base_url + gamebreakdown,
          headers=headers
       ).text
    )

    title = html.find(".//div[@class='headermain']").text

    params = {"url": base_url + gamebreakdown}

    link = session.get(
        "http://tinyurl.com/api-create.php?", params=params).text

    table = html.find(".//table")

    main_time = ""
    extra_time = ""
    complete_time = ""
    overall = ""

    for tbody in table.findall(".//tbody"):
        if tbody.find(".//td").text == "Main Story (Required) Completion":
            main_time = "Main time: %s" % tbody.findall(".//td")[3].text.strip()
        if tbody.find(".//td").text == "Main + Extras (Quests/Medals/Unlockables)":
            extra_time = "Main + Extras: %s" % tbody.findall(".//td")[3].text.strip()
        if tbody.find(".//td").text == "Completionists":
            complete_time = "100%%: %s" % tbody.findall(".//td")[3].text.strip()
        if tbody.find(".//a") is not None:
            overall = "Overall: %s" % tbody.findall(".//td")[3].text.strip()

    output = "How long to beat %s (%s) (Averages) -" % (title, link)

    if not main_time == "":
        output += " %s," % main_time

    if not extra_time == "":
        output += " %s," % extra_time

    if not complete_time == "":
        output += " %s," % complete_time

    output += " %s" % overall

    return output

@hook.command('hltb')
@hook.command('howlong')
@hook.command
def howlongtobeat(inp):
    ".howlongtobeat <game> -- gets the top result from howlongtobeat.com"

    return how_long(inp)

if __name__ == "__main__":
    print how_long("Bastion", "user")
