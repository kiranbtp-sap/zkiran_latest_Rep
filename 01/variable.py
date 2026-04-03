#scaler variable this store only single value

# string varibale 

name = "kiran"

#intiger variable 

age = 30

#float variable 
height  = 5.9

# boollen variabl 
is_stuents  = False

print("name: ", name, "is of type ", type(name))
print("age : ", age, "is of type ", type(age))
print("height : ", height, "is of type ", type(height))
print("is student : ", is_stuents, "is of type ", type(is_stuents))


# newage = input("Enter your age : ")

# if int(newage) > 18 :
#     print(name,"is an adult")
# elif int(newage) == 18:
#      print(name,"is just an adult")
# else: 
#      print(name,"is not an adult")




age = int(input("Enter your age: "))

if age >= 18:
    print("He/She is an Adult")
else:
    print("He/She is Not an Adult")


