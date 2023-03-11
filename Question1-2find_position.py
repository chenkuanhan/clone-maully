def find_position(numbers,target):
  for i in range(len(numbers)):
    if numbers[i] == target:
      return i
  return -1

print(find_position([5,2,7,1,6],5))
print(find_position([5,2,7,1,6],7))
print(find_position([5,2,7,7,7,1,6],7))
print(find_position([5,2,7,1,6],8))
