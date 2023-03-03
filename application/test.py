import os
import cv2 as cv

test_img =cv.imread("C:\\Users\\Lenovo\\Desktop\\127.bmp")

filename = None
image = None
kp1, kp2, mp = None, None, None
best_score  = 0

for file in [file for file in os.listdir("C:\\Users\\Lenovo\Downloads\\db")]:
    file1 = "C:\\Users\\Lenovo\\Downloads\\db\\" + str(file)
    fingerprint_img = cv.imread(file1)

    sift = cv.SIFT_create()
    keypoints_1, descriptor_1 = sift.detectAndCompute(test_img, None)

    keypoints_2, descriptor_2 = sift.detectAndCompute(fingerprint_img, None)

    matches = cv.FlannBasedMatcher({'algorithm':1, 'trees': 10},{}).knnMatch(descriptor_1, descriptor_2, k = 2)

    match_points = []

    for p,q in matches:
        if p.distance < q.distance * 0.1:
            match_points.append(p)

   
    keypoints = 0

    if len(keypoints_1) < len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    if len(match_points) / keypoints * 100 > best_score:
        best_score = len(match_points) / keypoints * 100
        filename = file1
        image = fingerprint_img
        kp1, kp2, mp = keypoints_1, keypoints_2, matches

        print("Best match:" + filename)
        print("Best score:", best_score) 


