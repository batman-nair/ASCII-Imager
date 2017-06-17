import cv2
import numpy as np 
import argparse

# The source image should be saved as (name)_sketch.png
# Adjust the fx and fy to get required scale for images
# Text based file for the image will be generated as (name).txt
# Code to recreate the image will be in (name)_code.txt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, 
	help="Filename of input image")
ap.add_argument("-o", "--output", default=None,
	help="Filename for output files")
ap.add_argument("-s", "--scale", default=1.0,
	help="Scale(Scale <1 for smaller text output)")
ap.add_argument("-f", "--fill", default="#", 
	help="Fill text for dark part")
ap.add_argument("-fw", "--fillw", default=".", 
	help="Fill text for white part")


args = ap.parse_args()

input_file = args.input

if(args.output is None):
	output = input_file.split(".")[0]
else:
	output = args.output

scale = float(args.scale)

fill = args.fill
fillw = args.fillw


img = cv2.imread(input_file, 0)
if(img is None):
	print("Input file doesnt exist")
	exit(0)
target_file = open(output + ".txt", 'w')
special = open(output + "_code.txt", 'w')
target_file.truncate() 


#Auto scaling
h, w = img.shape[:2]
#Height and width limits to how big the ascii text should be
WIDTH_LIMIT = 400.0
HEIGHT_LIMIT = 400.0
min_yscale = HEIGHT_LIMIT/h
min_xscale = WIDTH_LIMIT/w
#Check to see if scaling based on height or width is more
if (min_xscale < min_yscale):
	min_scale = min_xscale
else:
	min_scale = min_yscale
#1 char is equivalent to box of 5px hight and 2.5px width
yscale = min_scale/5.0
xscale = min_scale/2.5

#Additional program scaling
fy = yscale*scale
fx = xscale*scale

resized_img = cv2.resize(img, (0,0), fx = xscale, fy = yscale)

h, w = resized_img.shape[:2]
#Create a white bar on left side
resized_img[0:h, 0:1] = 255;

# Last character was space
was_space = True
count = 0

for i in resized_img:
	for j in i:
		#100 threshold for black
		if(j>100):	
			target_file.write(fill)
			if(was_space):
				count+=1
				# print "Space found", count, "= ", chr(count)
			else:
				# print " changing to space"
				special.write(chr(count+40))
				was_space = True;
				count = 1
		else:
			target_file.write(fillw)
			if(was_space == False):
				count+=1
				# print "Not Space found", count, "= ", chr(count+40)

			else:
				# print " changing to non space"
				special.write(chr(count+40))
				was_space = False;
				count = 1
	target_file.write("\n")
	special.write(chr(count+40))
	special.write(chr(40))
	was_space = True
	count = 0

