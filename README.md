# SlowMovieInColor

![](Extras/img.jpg)

## An Adaptation of Tom Whitwell's SlowMovie Player to work with the Inky Impression

Original writeup of Tom's project:<br />
https://medium.com/@tomwhitwell/how-to-build-a-very-slow-movie-player-in-2020-c5745052e4e4

The Inky Impression:<br />
https://shop.pimoroni.com/products/inky-impression

This is an adapted version of the SlowMovie player to work with the Inky Impression, a 7 color e-ink display made by Pimoroni. The project uses a Raspberry Pi Zero W as the brains of the operation which works well, so far, in testing but this should work with any version of the Pi with a 40 pin header.

## Things You Need
* A Raspberry Pi
* The Inky Impression
* A 5V power supply
* A frame to mount it in
    - If you have a 3D printer I would recommend Scripsi's Inky Impression Case which can be found [here](https://github.com/scripsi/inky-impression-case). Otherwise a standard box frame like the Ribba from Ikea would work well with some modifications.

## Setup Instructions
* Set up your Raspberry Pi as you would normally, either graphically or in headless mode and connect it to the internet. (A guide to setting up in headless mode can be found [here](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html))
* SSH into the Pi.
* Run the command ```curl https://get.pimoroni.com/inky | bash``` found [here](https://shop.pimoroni.com/products/inky-impression) to install the required libraries for Inky and enable I2C and SPI (this might take a while).
* Clone this repo to your home directory.
* Run the command ```pip3 install ffmpeg-python```, all other python libraries should already be installed.
* Reboot the Pi and you should be ready to go!
* Navigate to SlowMovieInColor directory and run the helloworld.py script, should everything be set up right you should now see the test movie as seen in the image above.

## How To Run A Movie
* Place the mp4s which you want to play into the Videos directory in the SlowMovieInColor directory either directly onto the SD card of the Pi or using something like scp (copy over ssh).
* To start a movie you can run the slowmovie.py script and it will start to play a random mp4 with the default settings.
* To start a specific movie or to change any of the default settings run the script with the -h flag to see all the options available.

## Extra Setup
* To play a movie every time the Raspberry Pi boots, rather than needing to run the script from SSH, I would recommend you use cron. A guide on how to run a script at reboot can be found [here](https://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/).

## Future Work
* The Inky Impression comes with 4 buttons on the side that can be used for various functions. The plan in the future is to use the buttons to jump forward and back several frames and to pause the movie. The final button could then be used to shutdown the Pi gracefully.

<!-- ## Note
Currently this is a work in progress so no guarantees can be made about its functionality. -->


