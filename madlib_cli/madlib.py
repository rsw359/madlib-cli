import re

print('**************************************')
print('**    Welcome to the Madlib!        **')
print('**         Enjoy the game           **')
print('**                                  **')
print('** To quit at any time, type "quit" **')
print('**************************************')


def read_template(file):
    with open(file, 'r') as f:
        try:
            return f.read().strip()
        except FileNotFoundError:
            return "File does not exist"


def parse_template(my_str):
    stripped = ''
    parts = []
    capture = False
    current = ''

    for char in my_str:
        if char == '{':
            stripped += char
            capture = True
            current = ''
        elif char == '}':
            stripped += char
            capture = False
            parts.append(current)
        elif capture:
            current += char
        else:
            stripped += char

    return stripped, tuple(parts)

    # inner_regex = r'{\w*}'
    # outer_regex = r'\w{2,}'
    # parts = str(re.findall(inner_regex, my_str))
    # return_parts = tuple(re.findall(outer_regex, parts))
    # stripped = re.sub(inner_regex, '{}', my_str)
    # print(return_parts)
    # print(stripped)
    # return stripped, return_parts


def merge(string, user_input):
    merge_output = string.format(*user_input)
    return merge_output




