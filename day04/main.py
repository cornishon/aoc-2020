from dataclasses import dataclass


@dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def check_byr(self) -> bool:
        return 1920 <= int(self.byr) <= 2002
    
    def check_iyr(self) -> bool:
        return 2010 <= int(self.iyr) <= 2020

    def check_eyr(self) -> bool:
        return 2020 <= int(self.eyr) <= 2030

    def check_hgt(self) -> bool:
        unit = self.hgt[-2:]
        if unit == 'cm':
            return 150 <= int(self.hgt[:-2]) <= 193
        elif unit == 'in':
            return 59 <= int(self.hgt[:-2]) <= 76
        else:
            return False
    
    def check_hcl(self) -> bool:
        if not self.hcl.startswith('#') or len(self.hcl) != 7:
            return False
        return all(map(lambda c: c in '0123456789abcdef', self.hcl[1:]))
    
    def check_ecl(self) -> bool:
        allowed_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return self.ecl in allowed_values

    def check_pid(self) -> bool:
        return len(self.pid) == 9

    def check_empty(self) -> bool:
        mandatory = self.__dict__.copy()
        mandatory.pop('cid')
        return None not in mandatory.values()

    def is_valid(self) -> bool:
        mandatory = self.__dict__.copy()
        mandatory.pop('cid')
        if None in mandatory.values():
            return False
        else:
            return all([
                self.check_byr(),
                self.check_iyr(),
                self.check_eyr(),
                self.check_hgt(),
                self.check_hcl(),
                self.check_ecl(),
                self.check_pid()
            ])

def parse(data: str) -> Passport:
    pass_dict = {}
    for field in data.split():
        key, value = field.split(':')
        pass_dict[key] = value
    return Passport(**pass_dict)


with open('input.txt') as f:
    passport_data = f.read().split('\n\n')
    passports = []
    for data in passport_data:
        passports.append(parse(data))


def count_valid(passport_list: list, validate_function: callable) -> int:
    return sum(map(validate_function, passport_list))


def part1():
    return count_valid(passports, lambda p: p.check_empty())

def part2():
    return count_valid(passports, lambda p: p.is_valid())


print("Part1:", part1())
print("Part2:", part2())