class KernalConvolutions(object):

    __height = 0 #how many pixels above and below the center the filter references
    __width = 0 #how many pixels left and right of the center the filter references
    __weights = [] #the list of weights for the relative positions of the pixels to the center

    def __init__(self, height, width, weights):
        self.__height = height
        self.__width = width
        self.__weights = weights

    def apply_filter(self, image):
        """Applies the filter defined by the object to the image. Assumes the image is a 2D list of integers"""

        finalArray = [[0 for j in range(0, len(image[i]))] for i in range(0, len(image))] #initializes the array to be the same dimension as image but full of zeroes
        for i in range(0, len(image)): #loops over every horizontal line of pixels
            for j in range(0, len(image[i])): #loops over ever pixel in that line
                weightedSum = 0
                sumCount = 0
                for y in range(max(0, j - self.__height), min(len(image[i]) - 1, j + self.__height) + 1):
                    #loops over each horizontal line referenced by the filter
                    for x in range(max(0, i - self.__width), min(len(image) - 1, i + self.__width) + 1):
                        #loops over each pixel referenced by the filter in the line and adds it's value times the corrosponding weight to the weighted sum
                        weightedSum += image[y][x]*self.__weights[y - max(0, j - self.__height)][x - max(0, i - self.__width)]
                        sumCount += self.__weights[y - max(0, j - self.__height)][x - max(0, i - self.__width)]
                #writes the average weighted value of the pixels to the final array
                finalArray[j][i] = (int)(weightedSum/sumCount)
        return finalArray

    def check_filter_dimensions(self):
        """Checks to see if the weights array is the correct dimensions. Returns True if it is, and False otherwise"""

        if len(self.__weights) != self.__height*2 + 1:
            return False
        for line in self.__weights:
            if len(line) != self.__width*2 + 1:
                return False
        return True

