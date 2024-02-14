"""A program that encodes and decodes hidden messages in images through LSB steganography"""
# http://blog.justsophie.com/image-steganography-in-python/
from PIL import Image, ImageFont, ImageDraw
import textwrap
import sys


def write_text(text_to_write, image_size):
    """Writes text to an RGB image. Automatically line wraps

    text_to_write: the text to write to the image
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    # Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin, offset), line, font=font)
        offset += 10
    return image_text


def encode_image_red(text_to_encode, template_image):
    """Encodes a text message into an image

    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    # template_image = Image.open(template_image)
    red_template = template_image.split()[0]
    green_template = template_image.split()[1]
    blue_template = template_image.split()[2]

    x_size = template_image.size[0]
    y_size = template_image.size[1]

    # text draw
    image_text = write_text(text_to_encode, template_image.size)
    bw_encode = image_text.convert('1')

    # encode text into image
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            red_template_pix = bin(red_template.getpixel((i, j)))
            tencode_pix = bin(bw_encode.getpixel((i, j)))

            if tencode_pix[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 2),
                            green_template.getpixel((i, j)),
                            blue_template.getpixel((i, j)))

    return encoded_image
    # encoded_image.save("encoded_image.png")


def encode_image_green(text_to_encode, template_image):
    """Encodes a text message into an image

    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    # template_image = Image.open(template_image)
    red_template = template_image.split()[0]
    green_template = template_image.split()[1]
    blue_template = template_image.split()[2]

    x_size = template_image.size[0]
    y_size = template_image.size[1]

    # text draw
    image_text = write_text(text_to_encode, template_image.size)
    bw_encode = image_text.convert('1')

    # encode text into image
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            green_template_pix = bin(green_template.getpixel((i, j)))
            tencode_pix = bin(bw_encode.getpixel((i, j)))

            if tencode_pix[-1] == '1':
                green_template_pix = green_template_pix[:-1] + '1'
            else:
                green_template_pix = green_template_pix[:-1] + '0'
            pixels[i, j] = (red_template.getpixel((i, j)),
                            int(green_template_pix, 2),
                            blue_template.getpixel((i, j)))

    return (encoded_image)
    # encoded_image.save("encoded_image.png")


def encode_image_blue(text_to_encode, template_image):
    """Encodes a text message into an image

    text_to_encode: the text to encode into the template image
    template_image: the image to use for encoding. An image is provided by default.
    """
    # template_image = Image.open(template_image)
    red_template = template_image.split()[0]
    green_template = template_image.split()[1]
    blue_template = template_image.split()[2]

    x_size = template_image.size[0]
    y_size = template_image.size[1]

    # text draw
    image_text = write_text(text_to_encode, template_image.size)
    bw_encode = image_text.convert('1')

    # encode text into image
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            blue_template_pix = bin(blue_template.getpixel((i, j)))
            tencode_pix = bin(bw_encode.getpixel((i, j)))

            if tencode_pix[-1] == '1':
                blue_template_pix = blue_template_pix[:-1] + '1'
            else:
                blue_template_pix = blue_template_pix[:-1] + '0'
            pixels[i, j] = (red_template.getpixel((i, j)),
                            green_template.getpixel((i, j)),
                            int(blue_template_pix, 2))

    # encoded_image.save("encoded_image.png")
    return encoded_image


def main():
    if (len(sys.argv) != 4):
        print("Error: wrong number of argument")
        print("py multi_encoder.py [image_to_encode] \
[name_of_image_encoded] [flag_to_hide]")
        return

    s = int(len(sys.argv[3])/3)
    flag_p1 = sys.argv[3][:s]
    flag_p2 = s * " " + sys.argv[3][s:2*s]
    flag_p3 = 2 * s * " " + sys.argv[3][2*s:]

    template_image = Image.open(sys.argv[1])

    encode_image = encode_image_red(flag_p1, template_image)
    encode_image = encode_image_green(flag_p2, encode_image)
    encode_image = encode_image_blue(flag_p3, encode_image)

    encode_image.save(sys.argv[2])


if __name__ == '__main__':
    main()
