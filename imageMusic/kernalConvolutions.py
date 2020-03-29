class KernalConvolutions(object):

    __height = 0
    __width = 0
    __weights = []

    def __init__(self, height, width, weights):
        self.__height = height
        self.__width = width
        self.__weights = weights

    def apply_filter(self, image):
        
        finalArray = [[0 for j in range(0, image[i])] for i in range(0, len(image))]
        for i in range(0, len(image)):
            for j in range(0, len(image[i])):
                weightedSum = 0
                for x in range(max(0, i - self.__width), min(len(image) - 1), i + self.__width):
                    for y in range(max(0, j - self.__height), min(len(image[i] - 1, j + self.__height))):
                        weightedSum += image[y][x]*weights[y - max(0, j - self.__height)][x - max(0, i - self.__width)]        
                finalArray[j][i] = weightedSum
        return finalArray

    def change_filter(self, weights):
        self.__weights = weights

    def check_filter_dimensions(self):
        if len(self.__weights) != self.__height*2 + 1:
            return False
        for line in self.__weights:
            if len(line) != self.__width*2 + 1:
                return False
        return True
