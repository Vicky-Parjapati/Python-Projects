# steganography_tool.py

from PIL import Image
import binascii

# Convert text to binary
def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Convert binary to text
def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(b, 2)) for b in chars if b != '00000000'])

# Hide text inside image
def hide_data(img_path, output_path, secret_msg):
    img = Image.open(img_path)
    binary_msg = text_to_bin(secret_msg) + '00000000'  # delimiter to mark end
    data_index = 0

    pixels = list(img.getdata())
    new_pixels = []

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # R, G, B
            if data_index < len(binary_msg):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_msg[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path)
    print(f"[+] Secret message hidden successfully in {output_path}")

# Extract hidden text from image
def extract_data(img_path):
    img = Image.open(img_path)
    binary_data = ""
    for pixel in img.getdata():
        for value in pixel[:3]:  # R, G, B
            binary_data += str(value & 1)

    message = bin_to_text(binary_data)
    print("[+] Extracted message:")
    print(message)

# Main menu
if __name__ == "__main__":
    print("Image Steganography Tool")
    print("1. Hide Data")
    print("2. Extract Data")

    choice = input("Choose an option (1/2): ")

    if choice == "1":
        image_path = input("Enter input image path (PNG recommended): ")
        output_image = input("Enter output image path: ")
        secret_message = input("Enter secret message to hide: ")
        hide_data(image_path, output_image, secret_message)
    elif choice == "2":
        image_path = input("Enter image path to extract from: ")
        extract_data(image_path)
    else:
        print("Invalid option.")
