import argparse
import ascii_image

def main():
    ap = argparse.ArgumentParser(
        description="Convert images to ascii")
    ap.add_argument("-i", "--input", required=True,
                    help="Input file name")
    ap.add_argument("-o", "--output", default=None,
                    help="Output file base name. Extension not needed")
    ap.add_argument("-s", "--size", default=None,
                    help="Size as number of rows and cols of characters. \
                    (Sample values [Cols]x[Rows]: '200x' '300x100')")
    ap.add_argument("-inv", "--invert", default=False, action='store_true',
                    help="Invert the dark and light shades")
    ap.add_argument("-html", "--html", default=False, action='store_true',
                    help="Generate HTML output")
    ap.add_argument("-img", "--image", default=False, action='store_true',
                    help="Generate image output")

    args = ap.parse_args()

    input_file = args.input

    output_file = "ascii_output"
    if args.output is not None:
        output_file = args.output

    cols, rows = args.size.split('x') if args.size else (0, 0)
    max_cols = int(cols) if cols else 0
    max_rows = int(rows) if rows else 0
    invert = args.invert

    ascii_text = ascii_image.image_to_ascii(input_file, size=(max_cols, max_rows), invert=invert)
    if args.html:
        ascii_image.ascii_to_html(output_file, ascii_text)
    elif args.image:
        ascii_image.ascii_to_image(output_file, ascii_text)
    else:
        ascii_image.ascii_to_text(output_file, ascii_text)

if __name__ == '__main__':
    main()
