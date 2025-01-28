name_of_file = input("What is the name of the file?")

with open(name_of_file, "w") as file:
    write_text = input("What text would you like to write?")
    file.write(write_text)

print("end of code")