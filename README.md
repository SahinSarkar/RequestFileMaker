# RequestFileMaker
Creates a csv file, whose each line has key value pairs, some of whose values don't change and rest of the keys have values from an input csv file

"Requestmaker" is a software which generates request files having .req extensions given the following inputs:
1) a configuration from a prespecified list of configurations, 
2) an input file having the values of the variable parameters
3) name of the output .req file which is to be generated.

# Windows:
## Steps to build one-click executable from the source code
1)	Firstly, install python 3.5 or above in your system.
2)	Run the batch file named 'buildExe.bat'.
3)	The actual required folder is named as ‘dist’ which gets generated upon completion of the previous step.
4)	Go to the path such that ‘dist’ folder is visible and archive/zip the only folder called ‘Requestmaker_final’ inside the ‘dist’ folder and send it to end users.

## To use the software
1)	Extract the given ‘Requestmaker_final’ zip file. If you built the software to use it, then directly go to the 'dist' folder.
2)	Inside the folder, double click the executable called ‘Requestmaker_final.exe’.

## To insert more configuration files for a new type of request
Just make a configuration file following the rules for making it and put it in the ‘configurations’ folder in the ‘Requestmaker_final’ folder and restart the software to reflect the changes.