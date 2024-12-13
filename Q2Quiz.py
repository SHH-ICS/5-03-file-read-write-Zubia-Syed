# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
score = 0
questions = [
    {"q": "Where were french fries originally made?", "c": {"a": "Belgium", "b": "France", "c": "America", "d": "Italy"}, "a": "a"}
]


for question in questions:
    print(question["q"])
    
    print("a) " + question["c"]["a"])
    print("b) " + question["c"]["b"])
    print("c) " + question["c"]["c"])
    print("d) " + question["c"]["d"])
    answer = input("Answer (a/b/c/d): ")
    if answer == question["a"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")


print("Your final score is: " + str(score))
