#works as of Python 3.6.9
#searches text documents and separates them into pieces if string and not list (default is by line breaks)
#then finds the or phrases and writes all pieces containing them
#to the indicated file (creates one if doesn't already exist)
import re
from platform import system
#to check for macOS
from os import getcwd

print('\nSearches a file and writes all lines that include your \
word/expression\n(hit ctrl+C to escape at any time)')

f_path = input("\nType or paste the file path: ")

#dealing with annoying drag and drop backslashes created in macOS terminal
#and the whitespace it sometimes appends to be "helpful"
while system() == "Darwin" :
    os_answer = input("\nDid any \ start in the filepath? Don't count any that macOS \
added if you dragged and dropped a file path with any spaces in the names\n(y/n): ")
    if os_answer == 'y':
        r_slash = input('\n Please re-enter the file path and remove any \ added by macOS if \
file was dragged and dropped (just hit return if none): ')
        if r_slash != '' : f_path = r_slash
        f_path = f_path.rstrip()
        #hopefully no one puts in a file with whitespace at the END...
        break
    elif os_answer == 'n':
        f_path = f_path.replace('\\','')
        f_path = f_path.rstrip()
        break
    else:
        print("\nPlease answer 'y' or 'n'\n")


try :
    file = open(f_path)
except :
    if system() == "Darwin" :
        print("Invalid or no input [were any \ left in?]\nExiting...")
        quit()
    else :
        print("Invalid or no input. Exiting...")
        quit()
try :
    contents = file.read()
except :
    print("Failed to read file [Invalid file type?] Exiting...")
    quit()

"""
#this didn't seem to work, I guess it's worth looking into another time
if isinstance(contents, str) == True :
    delimiter = input('What character should I use to separate the lines/sections? \
\n(just hit return to use line breaks): ')
    #to make blank input default to line breaks
    if delimiter == '' : delimiter = '\n'
    pieces = contents.split(delimiter)
elif type(contents) != 'list' :
    pieces = contents
else : pieces = contents
"""
pieces = contents

while True:
    case = input('\nIs our search going to be case-sensitive?\n(y/n): ')
    if case == 'y' :
        filter_pieces = re.findall('.*' + input('\nEnter your search term \n (part or whole): ') + '.*', pieces)
        break
    elif case == 'n' :
        filter_pieces = re.findall('(?i).*' + input('\nEnter your search term \n (part or whole): ') + '.*', pieces)
        break
    else :
        print("\nPlease answer 'y' or 'n'\n")
        continue

if filter_pieces == [] :
    print('No results found.')
    quit()

created_file = input('\nChoose an output name \
(just hit return to use "results"): ') + '.txt'

if created_file == '.txt' : created_file = 'results.txt'

n_lines = 0

with open(created_file, 'w') as output:
    for item in filter_pieces:
        output.write(item + '\n')
        n_lines += 1

if n_lines >= 2 :
    print('\nWrote', n_lines, 'lines to', created_file, 'in', getcwd())
elif n_lines == 1 :
    print('\nWrote', n_lines, 'line to', created_file, 'in', getcwd())
#elif n_lines == 0 :
#    print('\n Wrote ', created_file, 'in', os.getcwd(), 'but no results were found!')
else :
    print('Hmmm, something went wrong.')
