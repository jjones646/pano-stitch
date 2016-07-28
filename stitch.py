#!/usr/bin/env python2

import argparse
import imutils
import cv2

import stitcher as st

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="The first image")
ap.add_argument("-s", "--second", required=True, help="The second image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageA = imutils.resize(imageA, width=600)
imageB = imutils.resize(imageB, width=600)

# stitch the images together to create a panorama
stitcher = st.Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
