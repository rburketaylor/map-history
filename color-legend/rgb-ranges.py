from PIL import Image
from glob import glob

r, g, b = [0, 1, 2]
minimum, maximum = [0, 1]

for filename in glob("color-legend/*.png"):
    image = Image.open(__file__ + "/../" + filename)
    width, height = image.size
    rgb_range = [[None, None], [None, None], [None, None]]

    for i in range(width):
        for j in range(height):
            red, green, blue = image.getpixel((i, j))

            if (rgb_range[r][minimum] is None) or (rgb_range[r][minimum] > red):
                rgb_range[r][minimum] = red
            if (rgb_range[r][maximum] is None) or (rgb_range[r][maximum] < red):
                rgb_range[r][maximum] = red

            if (rgb_range[g][minimum] is None) or (rgb_range[g][minimum] > green):
                rgb_range[g][minimum] = green
            if (rgb_range[g][maximum] is None) or (rgb_range[g][maximum] < green):
                rgb_range[g][maximum] = green

            if (rgb_range[b][minimum] is None) or (rgb_range[b][minimum] > blue):
                rgb_range[b][minimum] = blue
            if (rgb_range[b][maximum] is None) or (rgb_range[b][maximum] < blue):
                rgb_range[b][maximum] = blue

    print(filename[13:-4] + " = (" +
          "[" + str(rgb_range[r][minimum]) + "<R<" + str(rgb_range[r][maximum]) + "], " +
          "[" + str(rgb_range[g][minimum]) + "<G<" + str(rgb_range[g][maximum]) + "], " +
          "[" + str(rgb_range[b][minimum]) + "<B<" + str(rgb_range[b][maximum]) + "]" + ")")
