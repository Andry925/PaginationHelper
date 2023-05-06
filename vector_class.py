class Operations:
    def basic_operation(self,new_vector_coordinate,operation):
        self.operation = operation
        self.result_vector = []
        self.new_vector_coordinate = new_vector_coordinate
        if len(self.list_coordinate) == len(self.new_vector_coordinate):
            for number in range(len(self.list_coordinate)):
                 if operation == "+":
                     self.result_vector.append(self.list_coordinate[number] + self.new_vector_coordinate[number])
                 if operation == "*":
                     self.result_vector.append(self.list_coordinate[number] * self.new_vector_coordinate[number])
                 if operation == "norm":
                     self.result_vector.append(self.list_coordinate[number] ** self.new_vector_coordinate[number])
                 if operation == "-":
                     self.result_vector.append(self.list_coordinate[number] - self.new_vector_coordinate[number])
                     
        return self.result_vector
        
        
class Vector(Operations):
    def __init__(self,list_coordinate):
        self.list_coordinate = list_coordinate
        

    


vector1 = Vector([1,2,3])
vector2 = Vector([3,4,5])
print(vector1.basic_operation(vector2.list_coordinate,"*"))

