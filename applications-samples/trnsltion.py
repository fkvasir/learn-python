def trnsltr(phrase):
  translation = ""
  for letter in phrase:
    if letter in "aeiouAEIOU":
      translation = translation + "eow"
    else:
      translation = translation + letter
  return translation
print(trnsltr(input("Enter a word =>")))

