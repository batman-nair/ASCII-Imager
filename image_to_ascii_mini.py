import cv2
img = cv2.imread('samples/dog.jpg', 0)
resized_img = cv2.resize(img, (0,0), fx=1/2.5, fy=1/5)
ascii_shades = list('M@GOCc+;:,. ')
shade = 0
with open("ascii_output.txt", 'w') as target_file:
    for row in resized_img:
        for val in row:
            for index in range(len(ascii_shades)):
                if val > 255*index/len(ascii_shades):
                    shade = index
            target_file.write(ascii_shades[shade])
        target_file.write('\n')
