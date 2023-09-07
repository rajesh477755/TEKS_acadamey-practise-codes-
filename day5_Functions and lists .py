def min(l):
  mini = l[0]
  for x in l:
    if (x < mini):
      mini = x
  return mini


'''the above function will take the list as an arugumnt and it will take the least value from the list and stores it in mini'''


def sort(l):
  if (l == []) or (len(l) == 1):
    return l
  x = min(l)
  l.remove(x)
  return [x] + sort(l)


'''the above function will take the list as argument and it will check whether the list is empty or having only one element then it will take minimum value in the list using the min function and removes it from the list and returns that value in form of list this happens untill the length of the list is 1  '''

l = [10, 25, 1, 11, 9, 0]
print(sort(l))
