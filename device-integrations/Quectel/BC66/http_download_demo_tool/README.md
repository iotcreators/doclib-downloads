# Public
This software is meant to be used by IoT creators customers. You are not supposed to have a deep knowledge about programming, but it can definitely help.
# Purpose
This software is meant to help and test the download of a file through the BC66 modem vie HTTP over Nb-IoT.
# Instructions
This software is not meant to substitute or emulate a real world application (for example but not limited to, running on a microcontroller), but to help, demonstrate and show the capabilities of IoT creators HTTP download.
## Prepare your Machine to run the software
1) Install the latest version of Python (Python 3.6+ is required to launch this application)
2) It is also recommended that you also install a Python IDE, it will make things much easier. One of the (if not, THE) best is Webstorm by Jetbrains https://www.jetbrains.com/pycharm/
3) Rename your settings file (config_example.json) into config.json and modify the values according to your needs. You can find more informations in the "settings file" section.
4) Make sure that modem is already configured on the Nb-IoT network of your choice (e.g., that you have completed this step https://docs.iotcreators.com/docs/_-quectel-bc66-t-be-dvk#attach-to-nb-iot-network )
5) Clone this repo
6) Install dependencies listed in requirements.txt, see https://pip.pypa.io/en/stable/cli/pip_install/#usage for the syntax in your favourite OS.
7) Go to the root folder of the project and run python main.py [-h] [-o [OUTPUT_FILE] -m [MODE] -p PORT. More informations about the parameters can be found in the "CLI parameters" section.
## Settings File
The default settings file is config.json file. It is used to configure essential parameters necessary to run the download.
Here's the description of such parameters:
* "remote_host": the address of the remote host (ipv4 format). Variable type: string.
* "remote_path": the path of the file to be downloaded via HTTP GET (it has to be in the form of /path). Variable type: string.
* "remote_port": the remote port of the http server to connect to. Usually the standard port is 80, you can however insert any value between 1 and 65535. Variable type: integer.
* "local_port": the local port of the connection. Any value between 1 and 65535 is admitted. Just for reference, the value reported on BC66 manual is 9000. Variable type: integer.
## CLI parameters
* -h: optional parameter, displays the help for the application
* -p (or --Port) <SERIAL_PORT>: mandatory parameter, used to input your serial port which your will communicate to your modem with. Example (on windows) -p COM4.
* -o (or --output_file): optional parameter, used to specify the output file path (absolute path) with extension. If not specified, file will be saved into folder "/download" with name "output.bin"
* -m (or --mode): optional parameter, used to specify the access mode of the modem, either direct or buffer. If not specified, mode will be set as direct.
