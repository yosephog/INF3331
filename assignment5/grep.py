import sys
import re
import argparse
from mymodul import *

"""
 i didn't include any theme file. i just choose the color 94 to
 color when the flag is true. since it wa was not mention in the
 assignment to include a theme file i didn't do anything about it.
 syntax file should be in the format of 5.1 and 5.2
"""

def grep(syntax_dictonary,file,flag):
    """
     this method takes a syntax dictornary,a file and a flag
     when the flag is set true it colores the matches that are
     aquired from reading the file. when the flag is not set
     it just prints the line that is found
    """

    with open(file,'r') as inFile:
        for line in inFile:
            for syntax in syntax_dictonary:
                matches=re.finditer(syntax,line)
                if matches:
                        for to_color in matches:
                            if flag:
                                start_code = "\033[{}m".format(94)
                                end_code="\033[0m"
                                change=start_code + to_color.group() + end_code
                                line=re.sub(syntax,change,line)
                                print(line)
                            else:
                                print(line)


if __name__ == '__main__':

    parser=argparse.ArgumentParser()
    parser.add_argument('regx')
    parser.add_argument('file')
    parser.add_argument('--highlight',help='set true',action='store_true')
    args=parser.parse_args()

    # read_syntax is a method found in mymodule.
    syntax=read_syntax(args.regx)
    grep(syntax,args.file,args.highlight)
