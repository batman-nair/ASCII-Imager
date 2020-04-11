import argparse
import ascii_image

def main():
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

    output_file = "ascii_output"
    if args.output is not None:
        output_file = args.output

    scale = float(args.scale)
    invert = args.invert

    ascii_text = ascii_image.image_to_ascii(input_file, scale=scale, invert=invert)
    ascii_image.ascii_to_text(output_file, ascii_text)

if __name__ == '__main__':
    main()
