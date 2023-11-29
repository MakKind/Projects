# FileNotFoundError
# IndexError
# TypeError
# KeyError

# try: Something that might cause an exception
# except: Do this is the exception occurs
# else: Do this if the exception does not occur
# finally: Do this regardless of anything

# try:
#     file = open("file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # print('There was an error')
#     file = open("file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist!")
# else:
#     content = file.read()
#     print(f"the try block block is sucessfull.\n {content}")
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is a madeup error!")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("The height is invalid. ")

bmi = weight/height ** 2
print(bmi)
