# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
q = "Where were french fries originally made?"
options = "A) Belgium B) France C) America D) Italy"
print(q, "\n" + options)
answer = input("Enter your answer (A/B/C/D): ").strip().upper()
print("Correct!" if answer == "A" else "Incorrect. The correct answer is A) Belgium.")


score = 0
questions = [
    {"q": "Where were french fries originally made?", "c": {"a": "Belgium", "b": "France", "c": "America", "d": "Italy"}, "a": "a"},]


for q in questions:
    print(q["q"])
    for k, v in q["c"].items():
        print(f"{k}) {v}")
    if input("Answer (a/b/c/d): ").lower() == q["a"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print(score)
