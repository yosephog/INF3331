import sys
import re
import itertools

def read_file(file_name):
	"""
	this method just read a file and return it
	as a list spliting at new line
	"""
	sourcefile=open(file_name,'r')
	file=sourcefile.read()
	sourcefile.close()
	return file.split('\n')


def diff(original_listinal,modified):
	""" This method find the difference between two file that is
	the original_listinal and the modifed of the original_listinal_lineinal version
	"""

	file=open("diff.txt",'w')

    # this for loop just reads the two file at the same time
	for (original_listinal_line,modified_line) in itertools.zip_longest(original_listinal,modified):
		"""
		 spliting the original and modifed line in to list of word in order to
		 compare word by word if the two lines have the same lenght
		 and amount of word
		 for example end and our. two words different but same length
		"""
		original_list=original_listinal_line.split(' ')
		modified_list=modified_line.split(' ')

		"""
		 if the two line have the same amount of words then
		 compare if there are word difference
		"""
		if len(original_list) == len(modified_list):
			if len(original_listinal_line) > len(modified_line):
				tx='- ' + original_listinal_line
				print(tx)
				file.write(tx+'\n')
				tx2='+ ' + modified_line
				print(tx2)
				file.write(tx2+'\n')
			elif len(original_listinal_line) == len(modified_line):
				tx='0 ' + original_listinal_line
				print(tx)
				file.write(tx+'\n')
			else:
				tx='+ ' + modified_line
				print(tx)
				file.write(tx+'\n')

				"""
				if the orginal list is greater then some word must
				have been deleted
				"""
		elif len(original_list) > len(modified_list):
			tx='0 ' + original_listinal_line
			file.write(tx+'\n')
			tx2='- ' + modified_line
			file.write(tx2)

			"""
			 if the orginal_list is smaller then words are added to the
			 modified version
			"""
		elif len(original_list) < len(modified_list):
			tx='- ' + original_listinal_line
			file.write(tx + '\n')
			tx2='+ ' + modified_line
			file.write(tx2 + '\n')

if __name__ == '__main__':
	original_listinal=read_file(sys.argv[1])
	modified=read_file(sys.argv[2])
	diff(original_listinal,modified)
