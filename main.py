import datetime

import pyhik.hikvision

from players import HikVideoPlayer
from setting import HIK_HOST, HIK_USER, HIK_PASSWORD

message = {"cam_id": {"event_type": {"channel": None}}}


def motion_callback(msg):
    print(datetime.datetime.now())
    print(msg)


def main():
    camera = pyhik.hikvision.HikCamera(host=f"http://{HIK_HOST}", usr=HIK_USER, pwd=HIK_PASSWORD)
    camera.add_update_callback(motion_callback, message)
    camera.start_stream()

    reader = HikVideoPlayer()
    reader.play()

    print(camera.get_device_info())


if __name__ == '__main__':
    main()
