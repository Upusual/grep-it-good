# grep-it-good
A Python GUI grep that can handle more than just simple text files.

To start, the goal is just to have it be able to handle single files of any common format and perform search and optional writing results.



Future Ideal features: cross-platform compatibility (or at least ports: for work purposes, Windows compatibility is a necessity); being able to write the results to .txt, .doc, or other formats (possibly smart output for XML or JSON way down the line); being able to use regex as specifically as possible without making it overly complex for the user since I want this to be usable by the average person; being able to tweak verbosity in output (e.g. line numbers or page numbers if it is in Word or another program that has page breaks); being able to change how a document is delimited in the write output, like the option to writing out whole pages rather than just lines; possible inclusion of other media (e.g. pictures in a PDF if it is whole page output; find and replace/erase capability. After most of this works, finding and handling multiple files in directories in a more grep-like scope.

My intuition is that it shouldn't do much more than this, so it can focus on staying true to task and avoid bloat. As mentioned earlier, my goal is to have something accessible to the average user, so I think two GUI's, a default with most broadly applicable features and options, and a more advanced one would be a good solution to that. But that's far in the future.



modules used
------------

from platform import system : to check for macOS 'Darwin' because it tried to be "helpful" with adding escape slashes to filepaths with spaces
from os import getcwd : for dealing with the macOS possible added \'s
re : 'nuff said
python-docx : allows interaction with MS Word 2007 and later doc files
PDF parser tbd
excel parser tbd
xml (xhtml?) needed 
json needed
html BSoup needed for prettying up
one for power point, perhaps
etc
