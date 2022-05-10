import re


def add(numbers_string):
    if numbers_string == '':
        return 0

    delimiters = [',', '\n']
    custom_delimiter_match = re.match('//(.+)\n(.*)', numbers_string)
    if custom_delimiter_match:
        group0 = custom_delimiter_match.groups(0)
        delimiters.append(group0[0])
        numbers_string = group0[1]

    delimiters_pattern = '|'.join(map(re.escape, delimiters))
    numbers_strings = re.split(delimiters_pattern, numbers_string)

    numbers = list(map(int, numbers_strings))

    neg_numbers = list(filter(lambda x: x < 0, numbers))
    if any(neg_numbers):
        raise Exception('negatives not allowed %s' %
                        (', '.join(map(str, neg_numbers))))

    result = sum(numbers)

    return result
