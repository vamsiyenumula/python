import re

def find_and_remove_extra_spaces_in_text_file(txt_file_path, new_file_name):
  with open(txt_file_path, "r") as f, open(new_file_name, "w") as f_out:
    for line in f:
      line = re.sub(r"\s+", " ", line)
      f_out.write(line)

# Example usage:

txt_file_path = "text_extra_spaces.txt"
new_file_name = "text_file_without_extra_spaces.txt"
find_and_remove_extra_spaces_in_text_file(txt_file_path, new_file_name)
