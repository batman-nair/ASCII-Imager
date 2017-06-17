# Image-to-ASCII
Convert image to ascii art using OpenCV 3.1 and Python 2.7

## Method
There are 2 ways in which this can be done  
 1.Direct fine conversion  
 2.Convert to compressed code and remake


### 1. Direct Method  
Easy and Quality method to generate ASCII art of an image.  
Image is given as input, ASCII art is output as html file.  
HTML file is used better quality viewing experience  
Example: 
`python img_to_ascii.py -i samples/sample1.jpg`


### 2. Compress and Remake
The image is converted to a special code and ASCII art with only 2 shades.  
The special code is compressed form of the ASCII art  
It can reproduce the ASCII art with just basic python and no OpenCV  
To create special code : 
`python image_to_code.py -i samples/sample1.jpg`  
To generate ASCII art from the code: `python special_code_to_ascii.py -i samples/sample1_code.txt`


## Usage

Create ASCII from image :
```
usage: img_to_ascii.py [-h] -i INPUT [-o OUTPUT] [-s SCALE] [-inv]

Convert images to ascii

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of input image
  -o OUTPUT, --output OUTPUT
                        Filename for output files
  -s SCALE, --scale SCALE
                        Scale(Scale <1 for smaller text output)
  -inv, --invert        Invert the dark and light shades


```
Generate special code :
```
usage: image_to_code.py [-h] -i INPUT [-o OUTPUT] [-s SCALE] [-f FILL]
                        [-fw FILLW]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of input image
  -o OUTPUT, --output OUTPUT
                        Filename for output files
  -s SCALE, --scale SCALE
                        Scale(Scale <1 for smaller text output)
  -f FILL, --fill FILL  Fill text for dark part
  -fw FILLW, --fillw FILLW
                        Fill text for white part
```
Convert code to ASCII :
```
usage: special_code_to_ascii.py [-h] -i INPUT [-o OUTPUT] [-f FILL]
                                [-fw FILLW]

Generate ASCII image from special code

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Filename of special code
  -o OUTPUT, --output OUTPUT
                        Output filename for ascii image
  -f FILL, --fill FILL  Fill text for dark part
  -fw FILLW, --fillw FILLW
                        Fill text for white part

```
