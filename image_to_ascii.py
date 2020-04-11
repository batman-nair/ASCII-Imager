import cv2

#Height and width limits to how big the ascii text should be
WIDTH_LIMIT = 800.0
HEIGHT_LIMIT = 600.0

def _scale_image(img, scale=1):
    #Auto scaling
    height, width = img.shape[:2]
    min_yscale = HEIGHT_LIMIT/height
    min_xscale = WIDTH_LIMIT/width
    #Check to see if scaling based on height or width is more
    min_scale = min_yscale
    if min_xscale < min_yscale:
        min_scale = min_xscale

    yscale = min_scale/5.0
    xscale = min_scale/2.5

    #Additional program scaling
    final_xscale = yscale*scale
    final_yscale = xscale*scale

    resized_img = cv2.resize(img, (0, 0), fx=final_xscale, fy=final_yscale)
    return resized_img

def image_to_ascii(input_file, scale=None, invert=False):
    img = cv2.imread(input_file, 0)
    if img is None:
        raise ValueError("File doesn't exist")
    if scale:
        img = scale_image(img, scale)

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

    with open(output_file_name + ".txt", 'w') as target_file:
        target_file.truncate()
