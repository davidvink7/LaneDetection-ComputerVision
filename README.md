## Advanced Lane Finding

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./test_images/chessboard_calibration.png "Undistorted"
[image2]: ./test_images/test1.jpg "Road Transformed"
[video1]: ./project_video.mp4 "Video"

[rgb]: ./output_images/test1.jpg "Original"
[undist]: ./output_images/undistorted.png "Undistorted"
[sx]: ./output_images/sx.png "Sobelx"
[sy]: ./output_images/sy.png "Sobely"
[sxy]: ./output_images/sxy.png "Sobelxy"
[masked]: ./output_images/masked_binary.png "Masked"
[warped]: ./output_images/warped.png "Warped"
[augmented]: ./output_images/test1_augmented.jpg "Augmented"
[smooth]: ./output_images/smooth_curve.jpg "Smooth"
[testResult]: ./output_images/testResult.jpg "Result"

## Camera Calibration

The code for this step is contained in the first code cell of the IPython notebook located in "./camera_calibration.py". 

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function. I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![alt text][image1]

### Pipeline (single images)

#### 1. Distortion-corrected image

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:

  Original Image           |  Undistorted Image        |
:-------------------------:|:-------------------------:|
  ![rgb][rgb]              |  ![undistorted][undist]   |

#### 2. Color transforms, gradients to create a thresholded binary image.

I used a combination of color and gradient thresholds to generate a binary image located in "./camera_calibration.py".  The output of the Sobel filter in X, Y and XY axis as well as a masked image for the effective area:

  Sobel X binary           |  Sobel Y binary (masked)  |  Sobel XY binary          |
:-------------------------:|:-------------------------:|:-------------------------:|
  ![sx_image][sx]          |  ![sy_image][sy]          |  ![sxy_image][sxy]        |
  

#### 3. Perspective Transform

The code for my perspective transform includes a function called `warp()`, which appears in lines 25 through 44 in the file `perspective_transform.py`. This results in the following source and destination points:

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

#### 4. Lane-line pixels identification and polynomial fit

To find the pixels of the lane lines in the warped binary image, we use a sliding window approach and apply a histogram starting from the bottom. Then we slide the windows from bottom to top of the image. We have found the lines we fit a polynomial and create a smoothe lane curve.

  Warped Binary            |  Lane Line Curve          |
:-------------------------:|:-------------------------:|
  ![warped_image][warped]  |  ![smooth_image][smooth]  |

![augmented_image][augmented] 

#### 5. Radius of curvature and position of the vehicle with respect to center.

The functions curvature and lanePosition in `lanes.py` define the radius and position from the lane center. The measurements are converted from pixel size to meter: ym_per_pix = 3.0/72.0 and xm_per_pix = 3.7/700.0. Mapping the lane and including data has been done with drawLane in lines 159-180.

Frame example with data:

![testResult_image][testResult]

### Pipeline (video)

#### 1. Link to Video Output

Lane Detection [video result](./project_video_output.mp4)

Lane and Vehicle Detection with [darknet](./vehicle_detection-20fpr.mp4)
