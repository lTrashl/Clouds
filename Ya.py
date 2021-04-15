import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''




def upload_file(file, destination):
    pld = {'path': destination, 'overwrite': 'true'}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    resp = requests.get(URL + '/upload', params=pld, headers=headers)
    resp.raise_for_status()
    link = resp.json()['href']
    try:
        with open(file, 'rb') as f:
            data = f.read()
            resp = requests.put(link, data)
            if resp is None:
                return
        return resp
    except OSError as ex:
        print(f'Failed "{file}" - {ex.strerror}')


def mkDir(path):
    pld = {'path': path}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    resp = requests.put(URL, params=pld, headers=headers)
    return resp


def remove(path):
    pld = {'path': path}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    resp = requests.delete(URL, params=pld, headers=headers)
    return resp


def listed():
    pld = {'fields': 'items.path', 'limit': 10000}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    resp = requests.get(URL + '/files', params=pld, headers=headers)

    return [i['path'] for i in resp.json()['items']]


def download(path):
    pld = {'path': path}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    resp = requests.get(URL + '/download', params=pld, headers=headers)
    download_link = resp.json()['href']
    resp = requests.get(download_link)
    with open(path + '.tar', 'wb', encoding=resp.encoding) as f:
        f.write(resp.content)
    return resp
