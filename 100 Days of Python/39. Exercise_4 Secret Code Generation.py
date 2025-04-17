# Generating secret code using some rules
# If word contains at least 3 characters then remove first character and append it to end
# Else reverse the string (if two charcters only)

a = "Abhinav is a good boy"
string_list = []

if len(a)<=2:
    print(a[::-1])

else:
    for i in a:
        # print(i)
        string_list.append(i)
    secret_code_1 = string_list[0]
    string_list.remove(string_list[0])
    string_list.append(secret_code_1)
    result = ''.join(string_list)
    print(result)
    # print(string_list)