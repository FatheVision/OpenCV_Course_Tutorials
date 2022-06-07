import sys

import cv2


def resize_frame(img, shape):
    img_reshape = cv2.resize(img, shape)
    return img_reshape


def video_read(path):
    cap = cv2.VideoCapture(path)
    if cap.isOpened() is False:
        print("Error opening video  file")
        sys.exit(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    print("old shape of video {} x {}".format(height, width))
    new_width = width//2
    new_height = height//2
    print("new shape of video {} x {}".format(new_height, new_width))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is True:
            frame_resize = resize_frame(frame, (new_width, new_height))
            cv2.imshow('Resized Video Play', frame_resize)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()


def main():
    print("*******  Playing video *******")
    print("Press q: Quit")
    video_file_path = "../data/lion_video1.mp4"
    video_read(video_file_path)
    cv2.destroyAllWindows()
    print("****************************")


if __name__ == "__main__":
    main()
