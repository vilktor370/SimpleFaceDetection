import cv2
import cv2.aruco as aruco
import numpy as np
import matplotlib.pyplot as plt


def main():
    img = (plt.imread('aruco.png') * 255).astype(np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    arucoParams = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=arucoParams)
    for i in rejectedImgPoints:
        coord = i[0, :, :].astype(np.uint16)
        for i in range(4):
            cv2.circle(img, (coord[i, 0], coord[i, 1]), 2, (255, 255, 255), 2)

    plt.imsave("test.png", img)


if __name__ == '__main__':
    main()
