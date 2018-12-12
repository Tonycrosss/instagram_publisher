import requests


def download_image(url, name, extension="jpg"):
    response = requests.get(url)
    with open(f"./images/{name}.{extension}", "wb") as f:
        f.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload,
                            allow_redirects=False)
    json_resp = response.json()
    links_list = json_resp['links']['flickr_images']

    for number, link in enumerate(links_list):
        download_image(link, f"spacex{number}")
