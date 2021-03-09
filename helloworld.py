#!/usr/bin/python3
# -*- coding:utf-8 -*-

# *************************
# ** Before running this **
# ** code ensure you've  **
# ** turned on SPI on    **
# ** your Raspberry Pi   **
# ** & installed the     **
# ** Inky library        **
# *************************

import os, time, sys, random
from PIL import Image
import ffmpeg

def generate_frame(in_filename, out_filename, time, width, height):
    (
        ffmpeg
        .input(in_filename, ss=time)
        .filter('scale', width, height, force_original_aspect_ratio=1)
        .filter('pad', width, height, -1, -1)
        .output(out_filename, vframes=1)
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )


def inky_clear(inky):
    for _ in range(2):
        for y in range(inky.height - 1):
            for x in range(inky.width - 1):
                inky.set_pixel(x, y, CLEAN)

        inky.show()
        time.sleep(1.0)


# Ensure this is the correct import for your particular screen
from inky.inky_uc8159 import Inky, CLEAN

# Ensure this is the correct path to your video folder
viddir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Videos/')

# Ensure this is the correct driver for your particular screen
inky = Inky()

# Initialise and clear the screen
print("Clearing the screen")
inky_clear(inky)

while 1:

    # Pick a random .mp4 video in your video directory
    currentVideo = ""
    while not (currentVideo.endswith('.mp4')):
        videoCount = len(os.listdir(viddir))
        randomVideo = random.randint(0,videoCount-1)
        currentVideo = os.listdir(viddir)[randomVideo]
    inputVid = viddir + currentVideo

    print(inputVid)

    # Set the width and height of the screen from the Inky library
    width = inky.width
    height = inky.height

    # Check how many frames are in the movie
    frameCount = int(ffmpeg.probe(inputVid)['streams'][0]['nb_frames'])

    # Pick a random frame
    frame = random.randint(0,frameCount)

    # Convert that frame to Timecode
    msTimecode = "%dms"%(frame*41.666666)

    # Use ffmpeg to extract a frame from the movie, crop it, letterbox
    # it and save it as grab.jpg
    generate_frame(inputVid, 'grab.jpg', msTimecode, width, height)

    # Open grab.jpg in PIL
    pil_im = Image.open("grab.jpg")

    # display the image
    inky.set_image(pil_im, saturation=0.25)
    inky.show()
    print('Diplaying frame %d of %s' %(frame,currentVideo))

    # Wait for 30 seconds to allow the screen to update
    time.sleep(30)

exit()
