from PIL import Image

class OurImage(object):

    rawImage = None
    height = 0
    width = 0
    rgbList = []
    gsList = []

    def __init__(self, image):
        self.rawImage = image
        self.rgbList = self.convert_to_rgb(self.rawImage)
        self.gsList = self.convert_to_gs(self.rawImage)

    def rgb(self):
        return self.rgbList

    def gs(self):
        return self.gsList

    def convert_to_rgb(self, image):
        rawRgb = self.rawImage.convert("rgb")
        fullList = []
        for i in range(0, rawImage.size[1]):
            subList = []
            for j in range(0, rawImage.size[0]):
                sublist.append(rawRgb.getpixel(i,j))
            fullList.append(subList)
        self.rgbList = fullList

    def convert_to_gs(self, image):
        rawGs = self.rawImage.convert("L")
        fullList = []
        for i in range(0, rawImage.size[1]):
            subList = []
            for j in range(0, rawImage.size[0]):
                sublist.append(rawRgb.getpixel(i,j))
            fullList.append(subList)
        self.gsList = fullList



