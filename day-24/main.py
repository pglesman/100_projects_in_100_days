with open(r"my_file.txt", mode="a") as file:  # You may want to use a raw (r-prefixed) string though, to make sure your
    # path does not contain any escape characters like \n that will be translated to special characters.
    file.write("\nnew text")


with open("new_file.txt", mode="w") as new_file:
    new_file.write("new file")
