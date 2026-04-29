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
    
print("Initial data written.\n")

while True:
    file = open(filename, "a")

    entry = input("Add Book: ")
    if entry.lower() == "stop":
        file.close()
        print("Library log saved. thankyou!")
        break

    file.write(entry + "\n")
    file.close()
    print("Entry added!\n")