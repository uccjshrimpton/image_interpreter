def get_file():
    image_file = open(input("Please enter the file location of a 24 bit colour depth bitmap image ") + ".bmp", "rb")
    all_bytes = list(image_file.read())

    for index, byte in enumerate(all_bytes):
        all_bytes[index] = str(hex(byte)[2:])

    # [x:x:-1] = start, end, steps
    offset = int(str("".join(all_bytes[13:9:-1])), 16)
    width = int(str("".join(all_bytes[21:17:-1])), 16)
    height = int(str("".join(all_bytes[25:21:-1])), 16)
    depth = int(str("".join(all_bytes[29:27:-1])), 16)

    print("Offset:", offset)
    print("Width:", width)
    print("Height:", height)
    print("Depth:", depth)

    # pixel data stored from bottom right to top left
    all_pixel_data = all_bytes[offset:]
    map_bits(all_pixel_data, offset, width, height, depth)


def get_symbol(RGB):
    total = 0
    for colour in RGB:
        total += int(colour, 16)

    if (total / 3) >= 254:
        char = " "
    elif (total / 3) >= 189:
        char = "~"
    elif (total / 3) >= 126:
        char = "`"
    elif (total / 3) >= 63:
        char = "£"
    elif (total / 3) >= 0:
        char = "#"

    return char


def map_bits(all_pixel_data, offset, width, height, depth):
    count = 0
    pixel_data = []
    horizontal_line = []
    ascii_image = []

    for byte in all_pixel_data:
        pixel_data.append(byte)
        count += 1

        if count == 3:
            count = 0

            horizontal_line.append(get_symbol(pixel_data))
            pixel_data = []

            if len(horizontal_line) == width:
                horizontal_line = horizontal_line[::-1]
                ascii_image.insert(0, horizontal_line)
                horizontal_line = []


def create_file(ascii_image):
    text_file = open("pixel_data.txt", "w")

    for line in ascii_image:
        count += 1
        text_file.write("".join(line) + "\n")
    text_file.close()


get_file()