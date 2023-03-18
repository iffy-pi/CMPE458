import sys
import os


def strip_lines_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [ '{}\n'.format(l.strip()) for l in lines]

    with open(filename, 'w') as file:
        file.writelines(lines)

    print('Stripped lines for {}'.format(filename))

args = sys.argv[1:]

# each file is an argument
# just strips all the whitespace for each line
for a in args:
    strip_lines_file(a)
