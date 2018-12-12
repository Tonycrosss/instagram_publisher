import os
from instabot import Bot
import glob
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_images


def publish_photos():
    pics = glob.glob(".\\images\\*")
    instagram_bot = Bot()
    instagram_bot.login()

    for pic in pics:
        instagram_bot.upload_photo(pic)


if __name__ == '__main__':
    if not os.path.exists('./images'):
        os.mkdir('./images')

    fetch_spacex_last_launch()
    fetch_hubble_images()
    publish_photos()




