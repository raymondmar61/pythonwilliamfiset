#williamfiset 45 pip third partys

#pip pronounced "pipe"
#must be downloaded and installed.  https://pip.pypa.io/
#pip for python3.5 add the number 3 after pip; for example pip3 list

#import pillow #not going to work.  Unique because its successor to photo imaging library or PIL (Photo Imaging Library)
from PIL import Image #going to work to use pillow, an image manipulation library
from PIL import ImageFilter #going to work to use pillow, an image manipulation library

img = Image.open("IMG_5521.JPG")
img = img.rotate(180)
img.show()
img = img.resize((400,400))
img.show()
blurred = img.filter(ImageFilter.BLUR) #blur the image
blurred.show()

#math modules below instructor recommended using.
#type print(dir(numpy)) or print(dir(gmpy2)) to see their functions
#numpy
#gmpy/gmpy2
#skipped

#http://matplotlib.org/index.html
#matplotlib
#download two examples plothistogram.py and rain.py
#skipped

#pyx or "pie x" a post script imaging generator