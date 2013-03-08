import requests
from lxml import etree
from util import hook

def get_mp3(inp):
    """ search beemp3.com """

    session = requests.Session()

    search_url = "http://beemp3.com/index.php"
    params = {
        "q": inp, 
        "st": "all"
    }

    html = etree.HTML(session.get(search_url, params=params).text)

    songs = []
    links = []

    for i in range(0, 2):
        songs[i] = "test %d" % i
        links[i] = "test %d" % i

    return html

@hook.command('mp3')
@hook.command
def beemp3(inp):
    return get_mp3(inp)

if __name__ == "__main__":
    print get_mp3("Some Day My Prince Will Come")
