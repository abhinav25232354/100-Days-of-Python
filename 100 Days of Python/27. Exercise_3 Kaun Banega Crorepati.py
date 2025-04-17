# Taking Questions in a list
# Taking Correct Answers in a list
# Displaying final amount the player wins

Questions = [
    "Who is the current prime minister of india?",
    "Who is known as missile man of India?",
    "Who is Ronaldo?",
    "Where is Taj Mahal Located"
]
correct_answer = [
    "Narendra Modi",
    "APJ Abdul Kalam",
    "FootBall Player",
    "Agra"
]
count = 0

for i in range(0, 4, 1):
    print(Questions[i])
    answer = input("Enter Answer: ")
    if correct_answer[i]==answer:
        print("Correct Answer")
        count += 1000
print(f"You have Won {count} Rupees.")