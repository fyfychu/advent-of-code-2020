import sys

file_name = sys.argv[1]
with open(file_name, 'r') as file:
    lines = file.readlines()

rules_and_passwords = []
for line in lines:
    count_range, letter, password = line.split()
    rules_and_passwords.append({'count_range': count_range, 'letter': letter[:-1], 'password': password})

def is_password_match_range_rule(rule_and_password):
    min_count, max_count = rule_and_password['count_range'].split('-')
    letter_count = rule_and_password['password'].count(rule_and_password['letter'])
    return (letter_count >= int(min_count)) and (letter_count <= int(max_count))

def is_password_match_position_rule(rule_and_password):
    first_pos, second_pos= rule_and_password['count_range'].split('-')
    password = rule_and_password['password']
    letter = rule_and_password['letter']
    return ((password[int(first_pos) -1] == letter) ^ (password[int(second_pos) -1] == letter)) and \
            ((password[int(first_pos) -1] == letter) or (password[int(second_pos) -1] == letter))

def get_valid_count(rules_and_passwords):
    valid_count_range = 0
    valid_count_position = 0
    for rule_and_password in rules_and_passwords:
        if is_password_match_range_rule(rule_and_password):
            valid_count_range += 1
        if is_password_match_position_rule(rule_and_password):
            valid_count_position += 1
    return valid_count_range, valid_count_position

print(f'{get_valid_count(rules_and_passwords)} valid passwords')
