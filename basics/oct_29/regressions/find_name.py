import re

def find_name_in_txt_file(name, txt_file_path):
  name_regex = re.compile(rf"\b{name}\b", re.IGNORECASE)
  with open(txt_file_path, "r") as f:
    line_number = 1
    for line in f:
      column_number = 1
      for match in name_regex.finditer(line):
        yield line_number, column_number
        column_number += match.end() - match.start()
      line_number += 1

# Example usage:

name = "Aiden"
txt_file_path = "names.txt"
name_matches = find_name_in_txt_file(name, txt_file_path)

for line_number, column_number in name_matches:
    print(f"The name {name} is found on line {line_number} and column {column_number}.")
