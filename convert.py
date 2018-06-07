def convert(from_filename, to_filename, convert_func):
  with open(from_filename) as from_file, open(to_filename, 'w') as to_file:
    converted = convert_func(from_file.readlines())
    to_file.write(converted)
    print(converted)