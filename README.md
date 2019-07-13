# RequestFileMaker
Creates a csv file, whose each line has key value pairs, some of whose values don't change and rest of the keys have values from an input csv file

"Requestmaker" is a software which generates request files having .req extensions given the following inputs:
1) a configuration from a prespecified list of configurations, 
2) an input file having the values of the variable parameters
3) name of the output .req file which is to be generated.

# Steps to build one-click executable from the source code
## Windows:
1)	Firstly, install python 3.5 or above in your system.
2)	Then install a module called ‘pyinstaller’ by typing ‘pip install pyinstaller’ on the windows command line.
3)	Type ‘pyinstaller Requestmaker_final.py’ in windows command line to generate the executable.
4)	The actual required folder is named as ‘dist’ which gets generated upon completion of the previous step.
5)	Open the folder ‘dist/Requestmaker_final’ and make a new folder in this place named ‘configurations’.
6)	In the ‘configurations’ folder created in the last step, put all configuration files.
7)	Go to the path such that ‘dist’ folder is visible and archive/zip the only folder called ‘Requestmaker_final’ inside the ‘dist’ folder and send it to end users.
