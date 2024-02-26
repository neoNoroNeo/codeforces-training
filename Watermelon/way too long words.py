repeat = int(input())

for angka in range(1,repeat +1):
    words = input()
    words_length = len(words)
    if words_length > 10:
        first_character = words[0]
        last_character = words[-1]
        len_minus_2 = str(words_length - 2)
        concat = first_character + len_minus_2 + last_character
        print(concat)
    else:
        print(words)