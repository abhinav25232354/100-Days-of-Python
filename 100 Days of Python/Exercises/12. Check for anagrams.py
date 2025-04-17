# anagrams are the word which can be formed with rearranging
# the position of the letters
# Like - "Listen", "silent"
user1 = input("Enter 1st word: ")
user2 = input("Enter 2nd word: ")

if len(user1)!=len(user2):
    print("Both words are different because there length are different")
else:
    if sorted(user1) == sorted(user2):
        print("This is anagramn")
    else:
        print("This is not anagram")
