import cv2

#Height and width limits to how big the ascii text should be
WIDTH_LIMIT = 100.0
HEIGHT_LIMIT = 100.0

def _scale_image(img, scale=1):
    height, width = img.shape[:2]
    print("Height, width: ", height, width)
    min_yscale = HEIGHT_LIMIT/height
    min_xscale = WIDTH_LIMIT/width
    #Check to see if scaling based on height or width is more
    min_scale = min_yscale
    if min_xscale < min_yscale:
        min_scale = min_xscale

    # Text size scaling
    yscale = min_scale*0.7
    xscale = min_scale*1

    #Additional program scaling
    final_xscale = xscale*scale
    final_yscale = yscale*scale

    print("Height, width: ", height*final_yscale, width*final_xscale)
    resized_img = cv2.resize(img, (0, 0), fx=final_xscale, fy=final_yscale)
    return resized_img

def image_to_ascii(input_file, scale=None, invert=False):
    img = cv2.imread(input_file, 0)
    if img is None:
        raise ValueError("File doesn't exist")
    if scale is not None:
        img = _scale_image(img, scale)

    #Change the shades for your own liking
    ascii_shades = list('M@GOCc+;:,. ')
    if invert:
        ascii_shades = ascii_shades[::-1]
    depth = len(ascii_shades)
    shade = 0

    output_text = ""
    for row in img:
        for val in row:
            #Loop to select appropriate shade
            for index in range(depth):
                if val > 255*index/depth:
                    shade = index

            output_text += ascii_shades[shade]
        output_text += '\n'

    return output_text

def ascii_to_text(output_file, output_text):
    with open(output_file + ".txt", 'w') as target_file:
        target_file.truncate()
        target_file.write(output_text)
