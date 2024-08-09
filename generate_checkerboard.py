from PIL import Image

def generate_checkerboard_image(size=32, block_size=4):
    # Create a new image with grayscale mode ('L') and the given size
    img = Image.new('L', (size, size))

    # Fill the image with a checkerboard pattern
    pixels = img.load()
    for y in range(size):
        for x in range(size):
            # Determine the color of the pixel (0 for black, 255 for white)
            color = 255 if (x // block_size + y // block_size) % 2 == 0 else 0
            pixels[x, y] = color

    # Save the image
    img.save("checkerboard_32x32.png")
    img.show()  # This will open the image in the default image viewer

    return img

if __name__ == "__main__":
    generate_checkerboard_image()