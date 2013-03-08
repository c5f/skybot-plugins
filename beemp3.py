from util import hook, http
from urllib import urlencode

def get_mp3(inp):
    """ search beemp3.com """

    search_url = "http://beemp3.com/index.php"
    base_url = "http://beemp3.com/download.php"

    post_dict = {
        q = inp,
        st = "all"
    }

    songs = []
    links = []

    results = http.get_html(search_url, post_data=urlencode(post_data))

    for i in range(0, 2):
        

    return results

@hook.command('mp3')
@hook.command
def beemp3(inp):
    return get_mp3(inp)

if __name__ == "__main__":
    print get_mp3("Some Day My Prince Will Come")
