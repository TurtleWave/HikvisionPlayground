import cv2

from setting import HIK_HOST, HIK_USER, HIK_PASSWORD


class HikVideoPlayer:
    def __init__(self):
        pass

    def play(self):
        url = f"rtsp://{HIK_USER}:{HIK_PASSWORD}@{HIK_HOST}:554/Streaming/Channels/101"
        video = cv2.VideoCapture(url)

        while (video.isOpened()):
            ret, frame = video.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()
