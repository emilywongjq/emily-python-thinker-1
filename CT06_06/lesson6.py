# print("Hello from lesson 6")
# print("レッスン6からこんにちは")

students = int(input("How many students are there?"))
score = 0

for i in range(students):
    score = score + int(input("What is the score of this pupil?╰(*°▽°*)╯(☆▽☆)"))

print(score/students)