import string
def checkFields(passport):
    credentials = passport.split()
    for x in credentials:
        field = x.split(":")
        valid = False

        if field[0] == 'byr' and 2002 >= int(field[1]) >= 1920:
            valid = True
            
        elif field[0] == 'iyr' and 2020 >= int(field[1]) >= 2010:  
            valid = True

        elif field[0] == 'eyr' and 2030 >= int(field[1]) >= 2020:
            valid = True
        
        elif field[0] == 'hgt':
            if field[1][-2:] == 'cm' and 193 >= int(field[1][:-2]) >= 150:
                valid = True
            if field[1][-2:] == 'in' and 76 >= int(field[1][:-2]) >= 59:
                valid = True            
        
        elif field[0] == 'hcl' and field[1][0] == "#" and all(y in string.hexdigits for y in field[1][1:]):
            valid = True
        
        elif field[0] == 'ecl' and any(y in field[1] for y in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            valid = True

        elif field[0] == 'pid' and field[1].isnumeric() and len(field[1]) == 9:
            valid = True

        elif field[0] == 'cid':
            valid = True

        if not valid:
            return False
    return True

def validPassport(passports):
    count = 0
    for passport in passports:
        if all(x in passport for x in ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']):
            if checkFields(passport):
                count += 1
    return count

def main():
    with open('input.txt') as f:
        passports = f.read().split('\n\n')
    print(validPassport(passports))

if __name__ == "__main__":
    main()