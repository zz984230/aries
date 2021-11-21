import requests


class Repo(object):
    def _make_request(self, url, data=None, typ=0, json_data=None):
        print(url)
        if typ:
            if json_data:
                r = requests.post(url, verify=False, json=json_data)
            else:
                r = requests.post(url, verify=False, data=data)
        else:
            r = requests.get(url, verify=False)
        return r.json()
