import sys
import re

file_name = sys.argv[1]

passports = []
with open(file_name, 'r') as file:
    passport = {}
    for line in file:
        if line != '\n':
            items = line.rstrip().split()
            for item in items:
                key, val = item.split(':', 1)
                passport[key] = val
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    passport = {}

def valid_year_range(field, smallest, greatest):
    return field.isdigit() and smallest <= int(field) and int(field) <= greatest

def valid_height(height):
    cm_pattern = re.compile("^1[5-9][0-9]cm$")
    in_pattern = re.compile("^59|6[0-9]|7[0-6]in$")
    return cm_pattern.match(height) or in_pattern.match(height)

def valid_hair_color(color):
    pattern = re.compile("^#[a-f0-9]{6}$")
    return pattern.match(color)

def valid_eye_color(color):
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(pid):
    return len(pid) == 9 and pid.isdigit()

def is_fields_valid(passport):
    return valid_year_range(passport['byr'], 1920, 2002) and \
       valid_year_range(passport['iyr'], 2010, 2020) and \
       valid_year_range(passport['eyr'], 2020, 2030) and \
       valid_height(passport['hgt']) and \
       valid_hair_color(passport['hcl']) and \
       valid_eye_color(passport['ecl']) and \
       valid_pid(passport['pid'])

def count_valid_passports(passports):
    total = 0
    for passport in passports:
        if all(key in passport for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')) and \
           is_fields_valid(passport):
            total += 1
        elif all(key in passport for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')) and \
             is_fields_valid(passport):
            total += 1
    return total

result = count_valid_passports(passports)
print(f'{result} valid passports')
