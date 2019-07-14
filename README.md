# RequestFileMaker
Creates a csv file, whose each line has key value pairs, some of whose values don't change and rest of the keys have values from an input csv file

"Requestmaker" is a software which generates request files having .req extensions given the following inputs:
1) a configuration from a prespecified list of configurations, 
2) an input file having the values of the variable parameters
3) name of the output .req file which is to be generated.

# Windows:
## Steps to build one-click executable from the source code
1)	Firstly, install python 3.5 or above in your system.
2)	Then install a module called ‘pyinstaller’ by typing ‘pip install pyinstaller’ on the windows command line.
3)  Open a command line and navigate to the location where the file Requestmaker_final.py is present.
3)	Type ‘pyinstaller Requestmaker_final.py’ in the command line to generate the executable. It creates a bunch of files and folders of which the most important one is the 'dist' folder.
4)	The actual required folder is named as ‘dist’ which gets generated upon completion of the previous step.
5)	Open the folder ‘dist/Requestmaker_final’ and make a new folder in this location named ‘configurations’.
6)	In the ‘configurations’ folder created in the last step, put all configuration files. A sample 'configurations' directory is provided on the repo having a single sample config file. This folder can be used to test working of the software.
7)	Go to the path such that ‘dist’ folder is visible and archive/zip the only folder called ‘Requestmaker_final’ inside the ‘dist’ folder and send it to end users.

## To use the software
1)	Extract the given ‘Requestmaker_final’ zip file.
2)	Inside the folder, double click the executable called ‘Requestmaker_final.exe’.

## To insert more configuration files for a new type of request
Just make a configuration file following the rules for making it and put it in the ‘configurations’ folder in the ‘Requestmaker_final’ folder and restart the software to reflect the changes.

# Linux and MacOS
## Steps to build one-click executable from the source code
1)	Python should already be present on your system. But in case it is not, then, install python 3.5 or above in your system.
2)	Then install a module called ‘pyinstaller’ by typing ‘pip install pyinstaller’ on the terminal command line.
3)  Open a command line and navigate to the location where the file Requestmaker_final.py is present.
3)	Type ‘pyinstaller Requestmaker_final.py’ in the command line to generate the executable. It creates a bunch of files and folders of which the most important one is the 'dist' folder.
4)	The actual required folder is named as ‘dist’ which gets generated upon completion of the previous step.
5)	Open the folder ‘dist/Requestmaker_final’ and make a new folder in this location named ‘configurations’.
6)	In the ‘configurations’ folder created in the last step, put all configuration files. A sample 'configurations' directory is provided on the repo having a single sample config file. This folder can be used to test working of the software.
7)	Go to the path such that ‘dist’ folder is visible and archive/zip the only folder called ‘Requestmaker_final’ inside the ‘dist’ folder and send it to end users.

## To use the software
same as for Windows

## To insert more configuration files for a new type of request
same as for Windows
