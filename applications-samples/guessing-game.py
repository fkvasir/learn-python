print("The strongest feeling in the world\nwhich drives people crazy enough\nto become a hero or a monster.")
print("You only have 3 guess chances\n")
scrt_word = "love"
guess = ""
guess_count = 0
guess_limit = 3
out_ofGuesses = False
while guess != scrt_word and not out_ofGuesses:
  if guess_count < guess_limit:
    guess = input("Enter your guess\n=>")
    guess_count += 1
  else:
    out_ofGuesses = True
  
if out_ofGuesses:
  print("\nOUT OF CHANCES! You Lose!")
else:

  print("\nCongratulation! You won $30!")
