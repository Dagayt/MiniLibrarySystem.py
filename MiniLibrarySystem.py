filename = "dagayt.txt"

try:
    file = open(filename, "x")
    print("File created successfully")
    file.close()
except FileExistsError:
    print("File already exists")

file = open(filename, "w")

data = input("Enter initial data to save: ")
file.write(data + "\n")

print("Initial data written to file")

file.close()
