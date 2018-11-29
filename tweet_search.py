from bottle import route, run, template, redirect, request


class TweetSearch:
    def __init__(self, word="", favorite="", rt="", media="", since=""):
        self.word = word
        self.favorite = favorite
        self.rt = rt
        self.media = media
        self.since = since

    def search(self):
        search_word = self.word + self.favorite + self.rt + self.media + self.since
        ptint(f"{search_word}で検索します")

        (Twitterの検索機能を利用して検索してくれる, 検索ワード)


@route("/")
def index():
    tweetsearch = TweetSearch()
    tweetsearch
