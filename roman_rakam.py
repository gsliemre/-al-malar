def roman_to_integer(roman):
    roman_numerals = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    integer_value = 0
    i = 0

    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_numerals:
            integer_value += roman_numerals[roman[i:i + 2]]
            i += 2
        else:
            integer_value += roman_numerals[roman[i]]
            i += 1

    return integer_value

# Kullanıcıdan Roma rakamını alın
roman_input = input("Lütfen Roma rakamını girin: ")

try:
    arabic_integer = roman_to_integer(roman_input.upper())
    print(f"{roman_input} = {arabic_integer}")
except KeyError:
    print("Geçersiz Roma rakamı girdiniz. Lütfen doğru bir değer girin.")
