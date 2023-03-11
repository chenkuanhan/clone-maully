def find_max(numbers):
  mmax = numbers[0]
  for i in numbers:
    if mmax < i:
      mmax = i
  return mmax



print(find_max([1,2,4,5]))
print(find_max([5,2,7,1,6]))
