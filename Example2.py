from Parser import *
#Complete processing of *.cha files

ChaHomePath=""# Input a folder containing *.cha files that you wish to process here.

ThisClamshell=Clamshell(ChaHomePath)
ThisClamshell.Parse()

# This is for display, you can skip this if you don't wish to print result right away
for ThisSketch in ThisClamshell.Sketches:
    print(ThisSketch.ToDictionary())

#Feel free to explore other variables in clamshell.