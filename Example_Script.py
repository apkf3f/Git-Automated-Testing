
#####################################################################
# Purpose: This is a test file for creating a useful script.		#
# Programmer(s): Adam Kraus											#
# Starting Date: 5.30.2019											#
#																	#
#####################################################################

#USEFUL INFO: 
	#Parse File: https://stackoverflow.com/questions/6497722/how-to-create-a-very-large-file-cheaply-using-python-in-windows-7/6497779#6497779
	#GitPython: https://gitpython.readthedocs.io/en/stable/tutorial.html#examining-references

#SUBPROCESS INIT
import subprocess
PIPE = subprocess.PIPE
branch = 'my_branch'

process = subprocess.Popen(['git', 'pull', branch], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = process.communicate()
subprocess.call(["git","status"])

#USER DISPLAY & VARIABLE INPUT
print("VCS Project\n")
num_files = input("number of files needed: ")	#Get number of files for repo 
file_size = input("Size of file needed(KB): ")	#Get file size in kilobytes - IMPORTANT NOTE: Github recommended maximum file size = 50MB

# MAKE <num_files> .txt FILES of <file_size> size in KB
for index in range(int(num_files)):
	with open("%u_ex_file.txt" %index,"w+") as file: #var new file opens <new_file>, w+ says to make the file if it doesn't exist
		file.truncate(1024*int(file_size))	#Creates a sparse file of <file_size> KB's
		subprocess.call(["git","add","%u_ex_file.txt" %index]) #Add the <num_files>[index] for commit stage

#SUBPROCESS -> GIT FUNCTIONS
subprocess.call(["git","status"])	#Check difference in what's added

