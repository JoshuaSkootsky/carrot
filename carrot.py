#                  Project: Is it a carrot?
#              Copyright Joshua Skootsky 2015
#    Distributed under the Boost Software License, Version 1.0
# See LICENSE file or copy at http://www.boost.org/LICENSE_1_0.txt
#

import numpy as np
import cv2
import dm
from matplotlib import pyplot as plt

# MODIFY THESE TO COMPARE TWO PICTURES
img1path = 'pictures_carrots/carrot_train2.png'
img2path = 'pictures_carrots/carrot6.jpg'

img1 = cv2.imread(img1path, 0)
img2 = cv2.imread(img2path, 0)

# Initiate ORB detector
orb = cv2.ORB()

# keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# ORB uses cv2.NORM_HAMMING
# crossCheck gives better results

# make BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(des1, des2)

# Sort by distances
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches
# use the drawMatches program from the imported dm module
img3 = dm.drawMatches(img1,kp1,img2, kp2, matches[:10]) 

# Draw matches
plt.show(plt.imshow(img3))

