from tkinter import *
from tkinter.filedialog import askopenfile

def get_file():
    image_file = askopenfile(parent=main_window, title='Select a Bitmap File')
    image_file = open(image_file.name, "rb")
    print(image_file.name)
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
    map_bits(width, height, depth, all_pixel_data)

def map_bits(width, height, depth, all_pixel_data):
    count = 0
    pixel_data = "#"
    horizontal_line = []
    bit_map = []

    for byte in all_pixel_data:
        if len(byte) < 2:
            byte = "0" + byte
        pixel_data += byte
        count += 1

        if count == 3:
            count = 0

            horizontal_line.append(pixel_data)
            pixel_data = "#"

            if len(horizontal_line) == width:
                horizontal_line = horizontal_line[::-1]
                bit_map.insert(0, horizontal_line)
                horizontal_line = []
    for line in bit_map:
        print(line)
    plot_image(width, height, depth, bit_map)

def plot_image(width, height, depth, bit_map):
    canvas_image = Canvas(main_window, width=width, height=height)
    canvas_image.pack()

    for v_pixel in range(height):
        for h_pixel in range(width):
            print(v_pixel, h_pixel)
            canvas_image.create_rectangle(h_pixel, v_pixel, h_pixel, v_pixel, outline=bit_map[v_pixel][h_pixel])
        canvas_image.update()

main_window = Tk()
main_window.title("Bitmap Interpreter")

button_open = Button(main_window, text="Open Bitmap", command=get_file)

button_open.pack()

main_window.mainloop()