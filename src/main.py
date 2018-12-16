import os
from PIL import Image
from array import *
from model import Model
#
#
# img = Image.open('scaledinput.png').convert('LA')
# img.save('grayscaledinput.png')

file = 'grayscaledinput.png'

data_image = array('B')

Im = Image.open(file)
pixel = Im.load()
width, height = Im.size

untupled_pixels = [[0 for x in range(28)] for y in range(28)]

for x in range (28):
    for y in range (28):
        untupled_pixels[x][y] = pixel[x,y][0]

for x in range (0, width):
    for y in range(0,height):
        # if (untupled_pixels[x][y] < 150):
        #     untupled_pixels[x][y] = 0
        data_image.append(int(127.5 - (float(untupled_pixels[y][x]) - 127.5)))
        print(str(int(127.5 - ((float(untupled_pixels[y][x])) - 127.5))) + "\t", end="")
    print("")

hexval = "{0:#0{1}x}".format(1,6)

header = array('B')
header.extend([0,0,8,1,0,0])
header.append(int('0x'+hexval[2:][:2],16))
header.append(int('0x'+hexval[2:][2:],16))

header.extend([0,0,0,width,0,0,0,height])
header[3] = 3  #New MSB (image data) 0x00000803

data_image = header + data_image

output_file = open('inputdata-images-idx3-ubyte', 'wb')
data_image.tofile(output_file)
output_file.close()

os.system('gzip inputdata-images-idx3-ubyte')







mydigits = Model()
mydigits.build
mydigits.train(1)  # EPOCH NUM is param variable
mydigits.save



