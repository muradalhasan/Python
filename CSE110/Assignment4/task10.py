def mix_strings(input_string):
    str1, str2 = input_string.split(", ")
    result = ""
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        result += str1[i] + str2[i] 
    result += str1[min_len:] + str2[min_len:]
    
    return result

user_input = input("Enter two strings separated by a comma and a space: ")

output = mix_strings(user_input)
print("Mixed String:", output)
