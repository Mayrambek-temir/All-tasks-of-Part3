text = input().strip()

number_of_letters = len(text) - text.count(' ') - text.count(',') - text.count('.')
lower = 0
upper = 0

for i in range(0, len(text)):

    try:
        int(text[i])
        number_of_letters -= 1

    except:

        if text[i] == ' ' or text[i] == ',':
            continue
        else:
            if ord(text[i]) > 96:
                lower += 1
            else:
                upper += 1

upper_percent = round((upper / number_of_letters) * 100, 1)
lower_percent = round((lower / number_of_letters) * 100, 1)

print('Upper percentage: ' + str(upper_percent) + ' number of Upper letters: ' + str(upper))
print('Lower percentage: ' + str(lower_percent) + ' number of lower letters: ' + str(lower))