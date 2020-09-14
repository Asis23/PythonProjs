
def new_string(str):
  if len(str) >= 2 and str[0:2] == "Is":
    return str
  return "Is" + str

abc = str(input("input a word:"))
print(new_string(abc))

