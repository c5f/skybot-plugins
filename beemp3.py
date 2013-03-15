import requests
from lxml import etree
from util import hook

def get_mp3(inp):
    """ search beemp3.com """

    session = requests.Session()

    search_url = "http://beemp3.com/index.php"
    base_url = "http://beemp3.com/"

    params = {
        "q": inp, 
        "st": "all"
    }

    html = etree.HTML(session.get(search_url, params=params).text)

    try:

        title = ""

        for part in html.xpath(
            "//ol/li[1]/div/div[@class='song-name']/a/font/strong/text()"):
                title = title + part + " "

        url =  base_url + html.xpath(
            "//ol/li[1]/div/div[@class='song-name']/a/@href")[0]

        url = session.get(
            "http://tinyurl.com/api-create.php?", params={"url": url}).text

        return "%s: %s" % (title, url)

    except IndexError:
        return "No results"

@hook.command('mp3')
@hook.command
def beemp3(inp):
    ".beemp3 <song title> -- gets the top result from beemp3.com. However, "\
    "the HTML rendering on that site is bananas, so the titles may display "\
    "funky."

    return get_mp3(inp)

if __name__ == "__main__":
    print get_mp3("Greyhound")
