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

	for syntaxies in syntax_dictonary:
		for themes in theme_dictonary:
			if syntax_dictonary[syntaxies] == themes:
				merged_dictornary[syntaxies]=theme_dictonary[themes]
				break

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


if __name__ == '__main__':
	"""
	if no argument is provided it uses the default files that are
	provided.
	"""
	if len(sys.argv) < 3:
		syntax=read_syntax("python.syntax")
		theme=read_theme("python.theme")
		file=read_file("demo.py")
	else:
		syntax=read_syntax(sys.argv[1])
		theme=read_theme(sys.argv[2])
		file=read_file(sys.argv[3])

	merged_dictornary=merge_dictornaries(syntax,theme)
	apply_coloring(merged_dictornary,file)
