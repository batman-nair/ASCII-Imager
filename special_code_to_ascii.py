import argparse

ap = argparse.ArgumentParser(
	description="Generate ASCII image from special code")
ap.add_argument("-i", "--input", required=True,
	help="Filename of special code")
ap.add_argument("-o", "--output", default=None, 
	help="Output filename for ascii image")
ap.add_argument("-f", "--fill", default="#", 
	help="Fill text for dark part")
ap.add_argument("-fw", "--fillw", default=".", 
	help="Fill text for white part")

args = ap.parse_args()

code_filename = args.input
output_filename = args.output
fill = args.fill
fillw = args.fillw

code_file = open(code_filename, 'r')
if code_file is None:
	exit(1)
special_code = code_file.readline()

if output_filename is None:
	output_filename = code_filename.split('.')[0] + "_ascii.txt"

output = open(output_filename, 'w')
isSpace = True;
for i in special_code:
	if(ord(i) == 40): 
		output.write("\n")
		# print "\n"
		isSpace = True
	for j in range(ord(i) - 40):
		if(isSpace): 
			output.write(fillw)
			# print " ",
		else:
			output.write(fill)
			# print "8",
	isSpace = not isSpace

