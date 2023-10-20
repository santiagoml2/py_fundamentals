class Point:

    def __init__(self, point_one: int = 0, point_two: int = 0, point_three: int = 0,):
        self.point_one = point_one
        self.point_two = point_two
        self.point_three = point_three
    
    
    def __str__(self):
        return "Your current point is: {},{},{}".format(self.point_one,self.point_two,self.point_three)
    

    def set_coordinates(self):
        print('-' * 30)
        print("Now define your point")
        print('-' * 30)

        self.point_one = input("Insert the first value: ")
        print(f'-You said "{self.point_one}"')

        self.point_two = input("Insert the second value: ")
        print(f'-You said "{self.point_two}"')

        self.point_three = input("Insert the third value: ")
        print(f'-You said "{self.point_three}"')

        print('-' * 30)
        print(self.__str__())


point_test_two = Point(8,14,0)
print(point_test_two.__str__())
point_test_two.set_coordinates()
        
