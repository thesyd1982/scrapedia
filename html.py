import httplib2
import re

class HTTPConnection:
    """ Gére une instance de connection Http"""
    def __init__(self, langue):
        self.langue = langue



    def get(self, page):
        """ Retrouve une page"""
        h = httplib2.Http(".cache")

        self.url = "https://{0}.wikipedia.org/wiki/{1}".format(self.langue, page.replace(' ', '_'))

        response, content = h.request(self.url, "GET")
        codage = response['content-type'].split('=')[1]
        # print(s)

        # cles = ['content-location','age','status','last-modified']
        # res = {
        #     c: response[c]for c in cles
        # }
        # print(res)
        self.page = content.decode(codage)
        print(self.page)
