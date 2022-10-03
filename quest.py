from multiplechoice import question
question_prompt =[
  "What color are the apples?\n(a)Red\n(b)Pink\n(c)Yellow\n(d)Blue\n\n",
  "What is my hobby?\n(a)Sleeping\n(b)Gaming\n(c)Writing\n(d)Reading\n\n",
  
]

questions = [
  question(question_prompt[0], "a"),
  question(question_prompt[1], "b"),
  
]

def run_test(questions):
  score = 0
  for questions in question_prompt:
    answer = input(question.prompt)
    if answer == input(question.answer):
      score += 1
  print("You got (" + str(score) + "/"+ str(len(questions)) + ") right>.<" +" Congratulations!!")
run_test(questions)