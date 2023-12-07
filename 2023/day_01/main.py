
NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

EXAMPLE_1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

EXAMPLE_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

EXAMPLE_3 = [
    # "one2",
    # "3four",
    # "55",
    # "6",
    # "seven",
    "seven1seven",
]

def read_file():
    ret_val = []
    with open('data.txt') as f:
        ret_val = f.readlines()
    return [line.replace('\n', '') for line in ret_val]

def extract_numeric_values(line):
    number_as_string = ""
    index_one = 0
    index_two = 0

    for index, char in enumerate(line):
        try:
            number_as_string += str(int(char))
            index_one = index
            break
        except Exception as e:
            continue
    
    for index, char in enumerate(reversed(line)):
        try:
            number_as_string += str(int(char))
            index_two = len(line) - index
        except Exception as e:
            continue
    
    return [(index_one, index_two), int(number_as_string)]

def extract_numbers(line: str):
    data = []
    ret_val = 0

    for i in range(len(line)):
        for key, number in NUMBERS.items():
            index = line.find(key, i)
            if index > -1:
                data.append((index, number))
    
    for index, char in enumerate(line):
        try:
            data.append((index, int(char)))
        except Exception as e:
            continue
    
    if data:
        max_tuple = max(data, key=lambda x: x[0])
        min_tuple = min(data, key=lambda x: x[0])
        ret_val = int(f"{min_tuple[1]}{max_tuple[1]}")

    return ret_val



def main():
    lines = read_file()
    # lines = EXAMPLE_1
    # lines = EXAMPLE_2
    # lines = EXAMPLE_3
    data = []
    for index, line in enumerate(lines):
        x = extract_numbers(line)
        print(index + 1, x)
        data.append(x)
    
    print(sum(data))

    

if __name__ == '__main__':
    main()