# Take a string
# 1. If length is < 3 then reverse the string
# 2. If Length > 3 then remove first character and add it to the last of the string
# 3. Then add three random characters at starting and 3 random characters at ending
# 4. Also make a decoder for it

# string = ""
result_string = []
encoded_string = ""
decoded_string = []

def encode():
    string = input("Message: ")
    words = string.split()
    global result_string
    print(words)
    if len(string)<3:
        print(f"Coded: {string[::-1]}")
    else:
        for word in words:
            r1 = "5568hgh2376"
            r2 = "2354rfs2246"
            new = r1 + word[1:] + word[0] + r2
            # print(new)
            result_string.append(new)
        # global encoded_string = "".join(result_string)
        global encoded_string
        # print("Coded: ", "".join(result_string))
        print("Coded:", "".join(result_string))

def decode(encoded_string):
    # message = input("Message: ")
    global decoded_string
    for word in encoded_string:
        new = word[11:-11]
        another_new = new[-1] + new[:-1]
        decoded_string.append(another_new)
        print(decoded_string)
        print(" ".join(decoded_string))

if __name__ == "__main__":
    print("Welcome to Abhinav's Secret Code Generation System")
    print("1. Encode Message")
    print("2. Decode Message")
    user = input("--> ")
    match(user):
        case "1":
            encode()
        case "2":
            decode(result_string)
# print("".join(result_string))