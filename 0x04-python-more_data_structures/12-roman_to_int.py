def roman_to_int(roman_string):
    roman_string = roman_string.upper()
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    result = 0
    prev_val = 0

    for num in roman_string:
        curr_val = roman_dict.get(num, 0)

        if curr_val == 0:
            return 0

        if curr_val > prev_val:
            result += curr_val - 2 * prev_val
        else:
            result += curr_val

        prev_val = curr_val

    return result
