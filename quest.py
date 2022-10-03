from multiplechoice import Question
question_prompt =[
  "What color are the apples?\n(a)Blue\n(b)Pink\n(c)Yellow\n(d)Red\n\n",
  "What is my hobby?\n(a)Sleeping\n(b)Gaming\n(c)Writing\n(d)Reading\n\n",
  
]

questions = [
  Question(question_prompt[0], "d"),
  Question(question_prompt[1], "d"),
  
]

def run_test(questions):
  score = 0
  for questions in questions:
    answer = input(question.prompt)
    if answer == input(question.answer):
      score += 1
  print("You got (" + str(score) + "/"+ str(len(questions)) + ") right>.<" +" Congratulations!!")
  run_test(questions)