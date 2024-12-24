def custom_write(file_name, strings: list):
    file = open(file_name, 'w', encoding= 'utf-8')
    i = 1 # index current str in list -> 1... n
    strings_positions = dict()
    for new_str in strings:
        j = file.tell() # index current file position
        file.write(new_str + '\n')
        strings_positions [i, j] = new_str
        i += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


