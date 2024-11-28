# FileNotFound

try:
    file = open('a_file.txt')
    dictionary = {'key': 'value'}
    print(dictionary['key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f'The key {error_message} was not found.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was close.')
