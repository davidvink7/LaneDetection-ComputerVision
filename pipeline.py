import cv2
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip

from camera_calibration import calibrate
from camera_calibration import undistort
from perspective_transform import convertBinary
from perspective_transform import mask
from perspective_transform import warp
from lanes import visualizeLanes
from lanes import curvature
from lanes import lanePosition
from lanes import addData
from lanes import drawLane

def processFrame(img):
    objpoints, imgpoints = calibrate(9, 6)
    undist = undistort(objpoints, imgpoints, img)
    sxybinary = convertBinary(undist)
    masked_sxybinary = mask(sxybinary)
    binary_warped, Minv = warp(masked_sxybinary)
    left_fit, right_fit, left_fitx, right_fitx, ploty, leftx, lefty, rightx, righty = visualizeLanes(binary_warped)

    left_radius, right_radius = curvature(leftx, lefty, rightx, righty)
    distance = lanePosition(left_fitx, right_fitx, undist)
    img = addData(undist, left_radius, right_radius, distance)

    return drawLane(img, left_fit, right_fit, left_fitx, right_fitx, ploty, binary_warped, Minv)



fileClip = VideoFileClip('project_video.mp4')
clip = fileClip.fl_image(processFrame)
clip.write_videofile('output_videos/project_video_output.mp4', audio=False)

'''
testImage = cv2.imread('./test_images/test1.jpg')
testResult = processFrame(testImage)
cv2.imwrite('./output_images/testResult.jpg', testResult)
'''