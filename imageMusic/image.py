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
        if self.rawImage.mode == "RGB":
            rawRgb = self.rawImage
        else:
            rawRgb = self.rawImage.convert("RGB")
        fullList = []
        for i in range(0, rawRgb.size[1]):
            subList = []
            for j in range(0, rawRgb.size[0]):
                subList.append(rawRgb.getpixel((j,i)))
            fullList.append(subList)
        self.rgbList = fullList

    def convert_to_gs(self, image):
        rawGs = self.rawImage.convert("L")
        fullList = []
        for i in range(0, rawGs.size[1]):
            subList = []
            for j in range(0, rawGs.size[0]):
                subList.append(rawGs.getpixel((j,i)))
            fullList.append(subList)
        self.gsList = fullList


my_image = OurImage(Image.open("dog.jpg"))
