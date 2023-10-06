string_count = int(input())
for current_string in range(string_count):
    string_type = input()
    if '_' in string_type or '.' in string_type or \
            ',' in string_type:
        print(f'{string_type} is not pure!')
    else:
        print(f'{string_type} is pure')
