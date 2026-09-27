def convert_to_roman(num):
    roman_num = [
        (1000, "M"), (900, "CM"),
        (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"),
        (1, "I")
    ]

    sonuc = ""

    for numbers,sembol in roman_num:
        adet , num = divmod(num, numbers)
        sonuc += sembol * adet
    return sonuc

def main():

    roman_dict={
        convert_to_roman(num) : num for num in range(1,5000)
    }

    while True:

        roman_input = input("Enter a roman numeral: ").strip().upper()

        if roman_input == "Q":
            break

        number = roman_dict.get(roman_input)

        if number is None:
            print("Invalid input")
            continue
        else:
            print("Roman numeral="+ roman_input + " --> " + "numerals="+ str(number))

if __name__ == "__main__":
    main()






