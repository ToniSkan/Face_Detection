# RoboticaUVic-PR-week7
UVic Robotics Master. Pattern Recognition Homework 4

## Instructions

Fork this repository and write code to complete the assignments.
First upload the completed assignment to the course Moodle for
grading; then, correct all the issues marked by the teacher and push
it to GitHub for the final evaluation.

This is a personal assignment, please complete it **individually**. 

## OpenCV

- **Q1**) The file opencv-facedetect.ipynb has code to open a video
    file and detect faces using a pre-trained cascade of classifiers
    from OpenCV. Your task will be to read and understand the code,
    and re-write it using C++ to detect faces in a video stream coming
    from a webcam. You can use the code you developed in earlier
    homework assignments as a template.

## Extra

- **Q2**) Now that you can locate the faces in the video, let's try to
    decorate them! Load the Charlie Chaplin hat and mustache, and
    paint them in the image at the appropriate locations based on the
    detected faces.

- **Q3**) Haar features are not the only type available in
    OpenCV. There are also cascade detectors trained using Local
    Binary Patterns (LBP). Use the LBP based cascade detector and
    compare the performance of both. You can find this (and other
    cascades) in /usr/share/opencv/, or online at the [OpenCV
    github](https://github.com/Itseez/opencv/tree/master/data).

- **Q4**) The example provided in the notebook is a "bare bones"
    one. For a more complete example see
    [facedetect.py](https://github.com/Itseez/opencv/blob/master/samples/python2/facedetect.py). Read it and understand how it works.