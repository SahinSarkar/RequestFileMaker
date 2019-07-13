import os
import tkinter.filedialog as fdlog
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def get_conffile_from_options(bound_var_to_selectbox):
	return 'configurations/' + config_options.get() + '.cfg'
	
def set_config_file(event):
	line = open(get_conffile_from_options(config_options)).readlines()
	dynamic_parameter_display = (line[line.index('--\n')+2:-1])
	lab_disp = "".join(dynamic_parameter_display)
	
	static_parameter_display = (line[1:line.index('--\n')-1])
	static_param = "".join(static_parameter_display)
	string_to_show = 'input file format(number is column number):\n' + lab_disp + '\n\nOther constant parameters are:\n' + static_param
	messagebox.showinfo('Ok', string_to_show)
	
def set_input_file():
	ftypes = [
	('CSV files', '*.csv')
	]
	global in_file
	in_file_path = fdlog.askopenfilename(filetypes=ftypes)
	Label(master, text=in_file_path).grid(row=1, column=1)
	in_file = in_file_path
		
def set_output_file():
	ftypes = [
	('Request files', '*.req')
	]
	out_file_path = fdlog.asksaveasfilename(defaultextension="req", filetypes=ftypes)
	Label(master, text=out_file_path).grid(row=2, column=1)
	global out_file
	out_file = out_file_path

#to print one line of request in the outputfile (basically converts python dict form di[inp. param] to .req key-value pair form)
def printdict(di):
	s=[]
	for k in di:
		st=k+' '+di[k]+','
		s.append(st)
	toreturn = ''.join(s)
	return toreturn[:-1]+'\n'

def make_req_file():
	config = open(get_conffile_from_options(config_options))
	output = open(out_file,'w')
	
	s=''													##format string static info form of output, for output file
	linesofdict = []
	for li in config:
		if li.rstrip() != '--':
			linesofdict.append(li.rstrip())
		else:
			break
	
	request = eval(''.join(linesofdict))
	
	###########################################################################################################################################
	#open inputfile where variable keys of dict are stored
	
	fi = in_file
	
	###########################################################################################################################################
	#evaluate the positional dictionary that comes after in config file AND read the values of the positional dict values from the inputfile. Append those values to the original request
	linesoforder = []
	for li in config:										# now config will read the positions of variable parameters
		linesoforder.append(li.rstrip())
	
	order = eval(''.join(linesoforder))						#order is a dict of variable parameters and their positions
	
	#start_time = time.time()
	for line in open(fi, encoding='utf8'):
		li = line.rstrip().split(',')						#li is an array of variable parameters from the input file
		for x in order:		#part of request dict was already made. now appending the variable parts to partially complete request dict and repeatedly printing them to file
			request[x] = li[int(order[x])-1]
		output.write(printdict(request))
	output.close()
	print("request file made")							
	
#main method analogue starts here
config_file_list = os.listdir('configurations')

in_file=""
out_file=""
	
master = Tk()

Label(master, text="Operation required: ").grid(row=0)
Label(master, text="Input File: ").grid(row=1)
Label(master, text="Output file: ").grid(row=2)

config_options = StringVar() #will come from combobox, hence binding this var to combobox later
act_codes = [el.split('.')[0] for el in config_file_list]
combo = ttk.Combobox(master, values=act_codes, textvariable=config_options, state='readonly')
combo.grid(row=0, column=1)
combo.bind('<<ComboboxSelected>>',set_config_file)#binding of user selection with a custom callback

Label(master, text="<Path to Input File>").grid(row=1, column=1)
Label(master, text="<Path to Output file>").grid(row=2, column=1)

Button(master, text='Browse input csv file...', command=set_input_file).grid(row=1, column=2, sticky=W, pady=4)
Button(master, text='Browse...', command=set_output_file).grid(row=2, column=2, sticky=W, pady=4)

Button(master, text='Make request file', command=make_req_file).grid(row=3, column=1, sticky=W, pady=4)

mainloop()