from tkinter import *
from tkinter.filedialog import askopenfile

def get_file():
    image_file = askopenfile(parent=main_window, title='Select a Bitmap File').read("rb")
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

def create_canvas():
    print()

def plot_image():
    print()


main_window = Tk()
main_window.title("Bitmap Interpreter")

button_open = Button(main_window, text="Open Bitmap", command=create_canvas)

button_open.pack()

main_window.mainloop()