def Add_Digits(second_digit, extract_inputss):
    second_digit = str(second_digit)
    extract_inputss = str(extract_inputss)
    extract_inputss = extract_inputss + second_digit
    extract_inputss = int(extract_inputss)
    return extract_inputss

inputs = input()

contestants = int(inputs[0])
position = int(inputs[2])

inputss = str(input())
len_inputss = len(inputss)

result = 0

inputss_list = []

while result < len_inputss:
    extract_inputss = str(inputss[result])
    if extract_inputss == " ":
        pass
    else:
        result = result + 1
        if result < len_inputss and inputss[result] != " ":
            second_digit = inputss[result]
            extract_inputss = Add_Digits(second_digit, extract_inputss)
            extract_inputss = int(extract_inputss)
            inputss_list.append(extract_inputss)
        #elif int(extract_inputss) < position:
        elif len(inputss_list) == contestants:
            break
        else:
            extract_inputss = int(extract_inputss)
            inputss_list.append(extract_inputss)
    result = result + 1

if len(inputss_list) == 0:
    print("0")
else:
    position = inputss_list[position-1]
    inputss_list = [x for x in inputss_list if x >= position and x != 0]

    answer = len(inputss_list)
    print(answer)