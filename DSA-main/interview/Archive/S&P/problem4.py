import re
input_string = "asdf 45gGH 96 gKd 02sa"
# input_string1 = list(input_string.split(''))
# input_string1.remove(['0-9'])
# print(input_string1)
result = re.sub(r'\d+', '', input_string)
print(result)
output_string = ""
for i in range(0, len(input_string)):
    if input_string[i].isdigit():
        pass 
    else:
        output_string=output_string+input_string[i]
print(output_string)

