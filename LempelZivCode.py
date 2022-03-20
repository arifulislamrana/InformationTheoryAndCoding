text = "WYS*WYGWYS*WYSWYSG"
table = {}
code = 256

for i in range(code):
    table[chr(i)] = i

output = []
i = 0

while i < len(text):
    currentChar = text[i]
    currentValue = 0;
    while currentChar in table:
        currentValue = table[currentChar]
        i += 1
        if i < len(text):
            currentChar += text[i]
        else:
            break
    else:
        table[currentChar] = code
        code += 1

    output.append(currentValue)


print(output)