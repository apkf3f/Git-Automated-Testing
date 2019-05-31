
#####################################################################
# Purpose: Deletes any extra files created during testing			#
# Programmer(s): Adam Kraus											#
# Starting Date: 5.30.2019											#
#																	#
#####################################################################


#VARIABLES
commit_msg = "automated commit message"
commit_msg2 = "Automated remove of scripted files"
#SUBPROCESS -> INIT
import subprocess
PIPE = subprocess.PIPE
branch = 'my_branch'
process = subprocess.Popen(['git', 'pull', branch], stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = process.communicate()
subprocess.call(["git","status"])

#USER DISPLAY & VARIABLE INPUT
print("VCS Project\n")
base_num = input("Base number: ")
base_num = int(base_num)
num_files = input("number of files needed: ")	#Get number of files for repo 
num_files = int(num_files)


rm_files = input("Delete Scripted files (Y/N)? ")	#Get number of files for repo
if rm_files == 'Y':
	for rm_index in range(num_files):
		subprocess.call(["git","rm","%u_ex_file.txt" %(rm_index+base_num)]) #remove the <num_files>[index] for commit stage
	subprocess.call(["git","commit","-m",commit_msg2]) #Commit the new files to repo
	subprocess.call(["git","push","origin","master"]) #Push new files to repo
