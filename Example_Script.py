
#####################################################################
# Purpose: This is a test file for creating a useful script.		#
# Programmer(s): Adam Kraus											#
# Starting Date: 5.30.2019											#
#																	#
#####################################################################

#USEFUL INFO: 
	#Parse File: https://stackoverflow.com/questions/6497722/how-to-create-a-very-large-file-cheaply-using-python-in-windows-7/6497779#6497779
	#GitPython: https://gitpython.readthedocs.io/en/stable/tutorial.html#examining-references
	#Subprocess: https://stackoverflow.com/questions/11113896/use-git-commands-within-python-code
import subprocess
import time
import os

#VARIABLES
commit_msg = "automated commit message"
commit_msg2 = "Automated remove of scripted files"
#SUBPROCESS -> INIT

start_time = time.time()	#initial EPOCH
PIPE = subprocess.PIPE
branch = 'my_branch'
process = subprocess.Popen(['git', 'pull', branch], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = process.communicate()

#USER DISPLAY & VARIABLE INPUT
print("VCS Project\n")
'''Direc_list = []
Dir_count = input("Enter number of directories: ")
while Dir_count != 'done':
	Direc_list.append(int(Dir_count))
	Dir_count = input("Enter number of directories: ")
print(Direc_list)
'''
num_files = input("number of files needed: ")	#Get number of files for repo 
num_files = int(num_files)
file_size = input("Size of file needed(KB): ")	#Get file size in kilobytes - IMPORTANT NOTE: Github recommended maximum file size = 50MB
file_size = int(file_size)

# MAKE <num_files> .txt FILES of <file_size> size in KB
for index in range(num_files):
	with open("%u_ex_file.txt" %index,"w+") as file: #var new file opens <new_file>, w+ says to make the file if it doesn't exist
		file.truncate(1024*file_size)	#Creates a sparse file of <file_size> KB's
		#subprocess.call(["git","add","%u_ex_file.txt" %index]) #Add the <num_files>[index] for commit stage

#SUBPROCESS -> GIT COMMANDS
start_add_cmd_time = time.time()
subprocess.call(["git","add","."]) #Add all files for commit stage
end_add_cmd_time = time.time()
subprocess.call(["git","commit","-m","commit_msg"]) #Commit the new files to repo
subprocess.call(["git","push","origin","master"]) #Push new files to repo
subprocess.call(["git","status"])	#Check difference in what's pushed

#SUBPROCESS -> REMOVE DELETED FILES FROM REPO
rm_files = input("Delete Scripted files (Y/N)? ")	#Get number of files for repo
if rm_files == 'Y':
	start_rm_cmd_time = time.time()
	#for rm_index in range(num_files):
	subprocess.call(["git","commit","-a", "-m",commit_msg2]) #remove the <num_files>[index] for commit stage
	end_rm_cmd_time = time.time()
	subprocess.call(["git","commit","-m",commit_msg2]) #Commit the new files to repo
	subprocess.call(["git","push","origin","master"]) #Push new files to repo
	
	print("Remove time: %.5f" %(end_rm_cmd_time - start_rm_cmd_time))
#DATA (Will move to text file creation)	
print("Add time: %.5f" %(end_add_cmd_time - start_add_cmd_time))
