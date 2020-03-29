class KernalConvolutions(object):

    __height = 0
    __width = 0
    __weights = []

    def __init__(self, height, width, weights):
        self.__height = height
        self.__width = width
        self.__weights = weights

    def apply_filter():
        

        return []

    def change_filter(self, weights):
        self.__weights = weights

    def check_filter_dimensions(self):
        if len(self.__weights) != self.__height:
            return False
        for line in self.__weights:
            if len(line) != self.__width:
                return False
        return True
