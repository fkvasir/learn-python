import random

feet_in_mile = 5280
meters_in_km = 1000
hello_venus = ["Alice","Nara","Jessica"]

def get_file_extension(filename):
  return filename[filename.index(".") + 1:]

def rolldice(num):
  return random.randint(1,num)