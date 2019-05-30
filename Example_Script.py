
#####################################################################
# Purpose: This is a test file for creating a useful script.		#
# Programmer(s): Adam Kraus											#
# Starting Date: 5.30.2019											#
#																	#
#####################################################################
print("Adam Kraus: VCS Project")

#VARIABLES
files = ["one","two","three"]

#FUNCTION 1: MAKE X .txt FILES
for file in files;
	with open("%s_ex_file.txt","w+") as f: #var new file opens <new_file>, w+ says to make the file if it doesn't exist
	f.write("Line 1")
	f.write("Line 2")