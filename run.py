from imageMusic.image import OurImage
from imageMusic.kernelConvolutions import KernelConvolution
from imageMusic.baseUi import gui

from PIL import Image

imageThing = OurImage(Image.open("imageMusic/dog.jpg"))

gui("GUI.py", "Import an image file")
