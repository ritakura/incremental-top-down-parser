# Convert transcript to accepted format by roark parser
# @Input (Command Line):
#       Input filename - the name of the file to re-format
#       Output filename - the name of the file to write output to
# @Returns (to output file):
#       The re-formatted text.
# Note: You can change what creates a new line (endmark), 
#       punctuation that doesn't create a new line (punctuation), 
#       and characters that denote quotes (quotes) in the sets below.

# Symbol rules:
endmark = {'.', '?', '!'}
punctuation = {';', ':', ','}
quotes = {'"'}

# Input transcript filename and output filename
fname = input("Input Filename: ")
output = input("Output Filename: ")

# read file in as string
with open(fname, 'r') as transcript:
    text = transcript.read()

# open output to write to
ofile = open(output, "w")

# length of story text
n = len(text)

i = -1

while (i+1 < n):
    i += 1
    # punctuation that should not start newline
    if (text[i] in punctuation):
        ofile.write(' ')
        ofile.write(text[i])
        continue

    if (text[i] in quotes):
        if (i - 1 >= 0 and text[i-1] != ' '):
            ofile.write(' ')
        ofile.write(text[i])
        if (i + 1 < n and text[i+1] != ' '):
            ofile.write(' ')
        continue

    # punctuation that starts newline
    if (text[i] in endmark) :
        ofile.write(' ')
        ofile.write(text[i])

        if (i + 1 < n and text[i+1] in quotes): # include quote in current line
            ofile.write(" \"")
            i += 1
        ofile.write('\n')
        i += 1
        continue
    ofile.write(text[i])

# close both files
transcript.close()
ofile.close()