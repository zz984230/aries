import requests


class Repo(object):
    def _make_request(self, url, data=None, typ=0):
        print(url)
        if typ:
            r = requests.post(url, verify=False, data=data)
        else:
            r = requests.get(url, verify=False)
        return r.json()
