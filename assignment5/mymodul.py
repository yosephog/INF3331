import re
import sys


def read_syntax(syntax_file):

	""" This method takes a syntax file and add it to a
	 dictonary. where the regx becomes the key and the
	 names become the value
	"""
	syntax_dictonary={}
	with open(syntax_file,'r') as temp_file:
		for fil in temp_file:
			txt=fil.split(':')
			key=txt[0]
			key=key[1:len(key)-1]
			value=txt[1].strip()
			syntax_dictonary[key]=value

	return syntax_dictonary

def read_theme(theme_file):
	"""
	this method read a theme file and create a dictonary makeing
	the names as key and the color codes as value
	"""
	theme_dictonary={}
	with open(theme_file,'r') as temp_file:
		for text in temp_file:
			text=text.split(':')
			key=text[0]
			value=text[1].strip()
			theme_dictonary[key]=value

	return theme_dictonary

def merge_dictornaries(syntax_dictonary,theme_dictonary):
	"""
	this method merge the syntax and theme dictornary in to a
	single dictonary.the dictonary will have the syntax_dictonary key
	as it's key and the theme_dictonary value as it't value
	"""
	merged_dictornary={}

	"""
	 This for loop do nothing more than read both the dictonaries
	 simatinously and merge them in to a single dictonary as explaind
	 above

	"""
	for (key_syntax,value_syntax),(key_them,value_theme) in zip(syntax_dictonary.items(),theme_dictonary.items()):
		merged_dictornary[key_syntax]=value_theme

	return merged_dictornary

def read_file(file_name):
	"""
	this method just read a file and return it
	"""
	sourcefile=open(file_name,'r')
	file=sourcefile.read()
	sourcefile.close()
	return file

def apply_coloring(merge_dictornaries,file):
	"""
	This method takes the merged dictornary and used its key
	that is the syntax to find the strings to be colored and
	applie the color that is the value to the matched string.
	"""
	for syntax in merge_dictornaries:
		start_code = "\033[{}m".format(merge_dictornaries[syntax])
		end_code = "\033[0m"

		pattern= "("+syntax+")"
		apply_color = start_code + r"\1" + end_code
		file = re.sub(pattern,apply_color,file)

	print(file)
