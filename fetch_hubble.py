import requests


def download_image(url, name, extension="jpg"):
    response = requests.get(url)
    with open(f"./images/{name}.{extension}", "wb") as f:
        f.write(response.content)


def get_extension_from_link(url):
    extension = url.split(".")[-1]
    return extension


def fetch_hubble_images():
    for image_id in get_ids_from_hubble_collection("holiday_cards"):
        url = f"http://hubblesite.org/api/v3/image/{image_id}"
        response = requests.get(url)
        images_data_list = response.json()['image_files']
        images_urls = []
        for img_data in images_data_list:
            images_urls.append(img_data['file_url'])
        best_picture_link = images_urls[-1]
        picture_extension = get_extension_from_link(best_picture_link)
        print(f'Downloading image: {image_id}.{picture_extension}...')
        download_image(best_picture_link, name=image_id, extension=picture_extension)
        print('Done!')


def get_ids_from_hubble_collection(collection_name):
    url = f"http://hubblesite.org/api/v3/images/{collection_name}"
    response = requests.get(url)
    images_data_list = response.json()
    ids_list = []
    for img_data in images_data_list:
        ids_list.append(img_data['id'])
    return ids_list
