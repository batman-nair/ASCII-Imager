import cv2
import argparse

ap = argparse.ArgumentParser(
	description="Convert images to ascii")
ap.add_argument("-i", "--input", required=True, 
	help="Filename of input image")
ap.add_argument("-o", "--output", default=None,
	help="Filename for output files")
ap.add_argument("-s", "--scale", default=1.0,
	help="Scale(Scale <1 for smaller text output)")
ap.add_argument("-inv", "--invert", default=False, action='store_true',
	help="Invert the dark and light shades")

args = ap.parse_args()

input_file = args.input

if(args.output is None):
	output = input_file.split(".")[0]
else:
	output = args.output

scale = float(args.scale)
invert = args.invert

img = cv2.imread(input_file, 0)
if(img is None):
	print("Input file doesnt exist")
	exit(0)

#Auto scaling
h, w = img.shape[:2]
#Height and width limits to how big the ascii text should be
WIDTH_LIMIT = 800.0
HEIGHT_LIMIT = 600.0
min_yscale = HEIGHT_LIMIT/h
min_xscale = WIDTH_LIMIT/w
#Check to see if scaling based on height or width is more
if (min_xscale < min_yscale):
	min_scale = min_xscale
else:
	min_scale = min_yscale
#1 char is 5px high and about 2.5px wide
yscale = min_scale/5.0
xscale = min_scale/2.5

#Additional program scaling
fy = yscale*scale
fx = xscale*scale

resized_img = cv2.resize(img, (0,0), fx = fx, fy = fy)


#Change the shades for your own liking
ascii_shades = ['M', '#', '+', ';', ':', ',', '.']
if invert:
	#Reverse list
	ascii_shades = ascii_shades[::-1]
depth = len(ascii_shades)
shade = 0

with open(output + ".html", 'w') as target_file:
	target_file.truncate() 
	#HTML initial body
	target_file.write("<html> \n <body> \n")
	target_file.write('<div class="ascii-art" style="font: 5px monospace ; text-align: center;"> \n')

	for row in resized_img:
		for val in row:
			#Loop to select appropriate shade
			for i in range(depth):
				if (val > 255*i/depth):
					shade = i

			target_file.write(ascii_shades[shade])
		target_file.write('\n')

	#HTML ending body
	target_file.write("</body> \n </html> \n")
