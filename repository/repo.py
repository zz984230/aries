import requests


class Repo(object):
    def _make_request(self, url, data=None, typ=0, json_data=None):
        print(url)
        if typ == 1:
            if json_data:
                r = requests.post(url, verify=False, json=json_data)
            else:
                r = requests.post(url, verify=False, data=data)
        elif typ == 2:
            r = requests.put(url, verify=False)
        else:
            r = requests.get(url, verify=False)

        print(url, r)
        return r.json()
