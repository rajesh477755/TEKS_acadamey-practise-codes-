with open("hi.txt", "r") as f:
  contents = f.read()
  print(contents)
with open("hi.txt", "w") as f:
  f.write("hi")
