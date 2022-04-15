with open("Config.txt", "w") as file:

    file.write("1")

with open("Config.txt", "r") as file:

    print(file.read())
 