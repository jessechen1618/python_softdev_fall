#Jesse "McCree" Chen
#SoftDev1 pd1
#K10 -- Jinja Tuning
#2019-09-21

from flask import Flask, render_template
import random

# CSV Script ----------------------------------------------------------
filehandle = open('occupations.csv', 'r')
csv_list = filehandle.readlines()
list_of_percents = list()
list_of_jobs = list()

#Make list of jobs and list of percents
for pair in csv_list:
	rev_pair = pair[::-1]
	rev_percentage = ''
	rev_job = ''
	index_of_comma = 0
	for char in rev_pair:
		if char != ',':
			rev_percentage += char
			index_of_comma += 1
		elif char == ',':
			break
	for char in rev_pair[(index_of_comma + 1):]:
		rev_job += char
	list_of_percents.append(rev_percentage[:0:-1])
	list_of_jobs.append(rev_job[::-1])

# End of CSV Script ---------------------------------------------------

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go? the console aka the terminal
    return "Hello World"

@app.route("/occupyflaskst") #assign following fxn to run when run route requested
def occ_table():
    return render_template('/occ_template.html', 
    	tab_title = "Occupation Table and Generator", 
    	pair_list = zip(list_of_jobs, list_of_percents))

if __name__ == "__main__":
    app.debug = True #When this is false, the website no longer able to update authomatically when you make a change in the code
    app.run() #If this is commented out, the webstie is just not hosted