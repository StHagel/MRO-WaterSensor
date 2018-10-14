# MRO-WaterSensor

This software controlls the Water Flow Sensor installed at the MRO. It consists of the driver written for the sensor, written to run on an Arduino uno and a python script, which reads the data from the arduino and calculates and stores the total waterflow.

# Setup

## Configuring the Makefile

As of now there is no way to automatically configure the makefile, so it might need to be configured manually.
The example Makefile given in this repository consists of:

```
BOARD_TAG = uno
ARDUINO_PORT = /dev/ttyACM0
ARDUINO_DIR = /usr/share/arduino
ARDMK_DIR = /usr/share/arduino
include /usr/share/arduino/Arduino.mk
```

These lines have to be set to:

* `BOARD_TAG`: The type of Arduino used. The example is written for an Arduino uno.
* `ARDUINO_PORT`: The port of the Arduino. A simple way to find it is to `watch ls /dev/tty*` while plugging in the Arduino.
* `ARDUINO_DIR`: The directory in which the `arduino` package is installed. If it has been installed using `aptitude` or `apt-get`, the given directory should be the default one.
* `ARDMK_DIR`: The directory in which the `arduino-mk` package is installed. By default this is equal to `ARDUINO_DIR`.
* `include`: This points to the place, where the file `Arduino.mk` is stored. By default this is `ARDMK_DIR/Arduino.mk`.

## Building and uploading the driver

The project uses `arduino-mk` to create a Makefile for the driver.
Therefore compiling the driver requires the `arduino` and `arduino-mk` packages.
If the makefile is configured correctly, the driver can be build by simply running `make` and uploaded to the Arduino by running `make upload` when it is plugged in via USB.

# Running the python script

After the Arduino is set up properly, the file `waterflow.py` has to be run in python.
As of now, the recommended version of python to use is 2.7, but other versions could work as well.
To read the serial output of the Arduino, the package `serial` is required.

The script reads the serial output of the Arduino, which mainly consists of the current flow of water in liters/hour each second. And adds them up to get the total amount of water that has flown into the tank in one hour. The result is stored in a separate file.

# TODO

* Automatic configuration of the Makefile
* Dynamic/Elegant way to change the output of the python script from hourly water flow to daily/weekly water flow
* Alert system that warns when the system is collecting to much water
