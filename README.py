# # Literate Programming in Markdown
# ---------------------------------------------------------------------------

# Literate Programming in Markdown takes a markdown file and converts it into a programming language.  Traditional programming often begins with writing code, followed by adding comments.  The Literate Programming approach encourages the programmer to document one's program prior to writing executable code.


# # Literate Python
# ---------------------------------------------------------------------------

# The first language to experiment with is Python.  The Main Purpose of the Literate Python package is to convert a text or markdown file into an executable python file.  Literate Python looks like markdown.  The key difference is that the code blocks will become live code, and the rest of the document becomes the documentation.

# **NOTE**: This README file is, infact, the parser itself!  Using "README.py" to parse "README.md" will produce the identical python file "README.py"!


# # File Names
# ---------------------------------------------------------------------------

# Basic Input Starts by identifying the file that is to be parsed.  While we call this "the markdown file" it shouldn't actually matter what the filetype is, so long as it is text.

inputFile_name = str(input("Type the Input File:"))
outputFile_name = str(input("Output File Name (.py added automatically):"))



# # Reading the Input File
# ---------------------------------------------------------------------------

# Now that we have a File's name specified, we will read the file.  We only need the data inside the file, and don't need to keep it open any longer than is neccesary.  We open the file, then copy the data to an array, and then close the file agan.  The array is a list of strings (one string for each line), 

with open(inputFile_name) as inputFile:
    inputFile_data = list(inputFile)



# # Initialize some Variables
# ---------------------------------------------------------------------------

# Since we are generating a new file with new lines, let's initialize another list.  This will start empty, but we will add strings to it as we go. We will also need a boolean for detecting if we are inside a Code Block or not.

newFile_string = str()
insideCodeBlock = False



# # Line by Line
# ---------------------------------------------------------------------------

# We will iterate through each line of the text.  We either add comments, or add live code.

# 1. Checking to see if the first line contains 3x the symbol "~" will tell us we are at either the beginning, or the end, of a codeblock.  Flipping the boolean "insideCodeBlock" will help us keep track.

# 2. If we ARE inside of a codeblock, then we just print lines without any modification.  These lines become live code.

# 3. Blank lines are printed as blank lines.  No need to change anything.

# 4. Reaching this point in the for-loop means that we are outside of a codeblock.  Add a comment to the line.

for line in inputFile_data:

    if (line[:3] == '~~~'):
        insideCodeBlock = not insideCodeBlock
        continue

    if insideCodeBlock:
        newFile_string += line
        continue

    if (line[:2] == '\n'):
        newFile_string += '\n'
        continue

    newFile_string += '# ' + line


# Fun feature - add commented lines underneath the headers. 

    if (line[:1]) == '#': newFile_string += '# ' + '-' * 75 + '\n'



# # Write to the File.
# ---------------------------------------------------------------------------

# Finally, Write the newly created string of data into the a new file.

with open(outputFile_name + '.py', "w") as newFile:
    newFile.write(newFile_string)
