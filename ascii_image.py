import cv2

# Height and width limits to how big the ascii text should be
WIDTH_LIMIT = 200.0
HEIGHT_LIMIT = 150.0

def _scale_image(img, size=None):
    img = cv2.resize(img, (0, 0), fx=1, fy=0.6) # Letter width usually 0.6-1 times less that height
    height, width = img.shape[:2]
    max_cols, max_rows = 0, 0
    if size is not None:
        max_cols, max_rows = size
    if max_cols and max_rows:
        return cv2.resize(img, (max_cols, max_rows))

    min_scale = 1
    if max_cols or max_rows:
        yscale = max_rows/height
        xscale = max_cols/width
        min_scale = yscale + xscale # Atleast one will be zero
    else:           # No size specified
        min_xscale = WIDTH_LIMIT/width
        min_yscale = HEIGHT_LIMIT/height
        min_scale = min_xscale if min_xscale < min_yscale else min_yscale

    resized_img = cv2.resize(img, (0, 0), fx=min_scale, fy=min_scale, interpolation=cv2.INTER_AREA)
    return resized_img

def image_to_ascii(input_file, size=None, invert=False):
    img = cv2.imread(input_file, 0)
    if img is None:
        raise ValueError("File doesn't exist")
    if size is not None:
        img = _scale_image(img, size)

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

def ascii_to_html(output_file, output_text):
    with open(output_file + ".html", 'w') as target_file:
        target_file.truncate()
        target_file.write("<!DOCTYPE html>\n"
                          "<html>\n"
                          "<body style='text-align: center;'>\n"
                          "<pre style='font-size:0.6em; line-height:1.1em;'>\n")
        target_file.write(output_text)
        target_file.write("</pre>\n"
                          "</body>\n"
                          "</html>\n")
