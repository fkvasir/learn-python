from multiplechoice import question
question_prompt =[
  "What color are the apples?\n(a)Red\n(b)Pink\n(c)Yellow\n(d)Blue\n\n"
  "What is your hobby?\n(a)Reading\n(b)Gaming\n(c)Sleeping\n\n"
  
]

questions = [
  question(question_prompt[0], "a")

]

def run_test(questions):
  score = 0
  for question in questions:
    answer1 = input(question.prompt)
    if answer1 == input(question.answer):
      score += 1
  print("You got" + str(score) + str(len(question)) + "right" +"Congratulations!!")
run_test(questions)