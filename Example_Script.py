
#####################################################################
# Purpose: This is a test file for creating a useful script.		#
# Programmer(s): Adam Kraus											#
# Starting Date: 5.30.2019											#
#																	#
#####################################################################

################################ IMPORTANT NOTE: Github recommended maximum file size = 50MB ############################################################
#VARIABLES


#MAIN
print("Adam Kraus: VCS Project\n")
num_files = input("number of files needed: ")	#Get number of files for repo 
file_size = input("Size of file needed(KB): ")	#Get file size in kilobytes

#FUNCTION 1: MAKE X .txt FILES
for index in range(int(num_files)):
	with open("%u_ex_file.txt" %index,"w+") as file: #var new file opens <new_file>, w+ says to make the file if it doesn't exist
		file.truncate(1024*int(file_size))	#Creates a sparse file of <file_size> KB's

