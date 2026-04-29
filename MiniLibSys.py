filename = "dagayt.txt"

try:
    file = open(filename, "x")
    print("File created successfully")
    file.close()
except FileExistsError:
    print("File already exists")

file = open(filename, "w")

data = input("Enter what u want to save: ")
file.write(data + "\n")

print("Saved")

file.close()
