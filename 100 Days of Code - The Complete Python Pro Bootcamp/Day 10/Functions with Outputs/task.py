def format_name(f_name: str, l_name: str) -> str:
    return (f_name + ' ' + l_name).title()


name = input("Your name: ")
last_name = input("Your last name: ")

print(format_name(name, last_name))
