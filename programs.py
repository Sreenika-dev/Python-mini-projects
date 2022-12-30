# def count_substring(string, sub_string):
#     counter = 0
#     for i in range(len(string)-len(sub_string)+1):
#         if (string[i:i+len(sub_string)] == sub_string):
#          counter += 1     
#     return counter

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner   #returning inner in outer function and changing its functionality

# add_five = outer(5)
# print(add_five)
# result = add_five(6)
# print(result) 


# def star(func):
#     def star_inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*"*15)
#     return star_inner


# def percent(func):
#     def percent_inner(*args, **kwargs):
#         print("%"*15)
#         func(*args, **kwargs)
#         print("%"*15)
        
#     return percent_inner

# @star
# @percent
# def printer(msg):
#     print(msg)
    
# printer("Hello")


# class Celsius:
#     def __init__(self, temperature):
#        self.temperature = temperature

#     def fahrenheit(self):
#         return (self.temperature * 1.8) + 32
    
#     def get_temperature(self):
#         print("Getting Value")
#         return self._temperature
    
#     def set_temperature(self, value):
#         print("Setting Value")
#         if value < -273.15:
#              raise ValueError("Temperature below -273.15 is not possible.")
#         self._temperature = value
        
#     temperature =  property(get_temperature, set_temperature)


# man1 = Celsius(23)
# print(man1.temperature)
# print(man1.fahrenheit())
