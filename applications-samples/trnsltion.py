# /sample-translation//cat-language/
def trnsltr(phrase):
  translation = ""
  for letter in phrase:
    if letter in "aeiouAEIOU":
      translation = translation + "eow"
    else:
      translation = translation + letter
  return translation
print(trnsltr(input("Enter a word =>")))
def trnslte(phrse):
  translation = ""
  for letter in phrse:
    if letter.upper() in "AEIOU":
      if letter.isupper():
        translation = translation + "Eow"
      else:
        translation = translation + "eow"
    else:
      translation = translation + letter
  return translation
print(trnslte(input("Enter a word =>")))
def add_lang(sentence):
  lngge = ""
  for lett in sentence:
    if lett.upper() in "AEIOU":
      if lett.islower():
        lngge = lngge + "ba"
      else:
        lngge = lngge + "Ba"
    else:
      lngge = lngge + lett
  return lngge
print(add_lang(input("To-be-translated~~ ")))