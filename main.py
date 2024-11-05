# Griffin King
# Unit 3 Lab 3
# Sorting a list with recursion



from os import system
def merge_sort(list):
  if len(list) == 1:
    #print(f"\nBase case reached:{list}\n")
    return list

  #print(list)
  
  right = merge_sort(list[:int(len(list)/2)])
  left = merge_sort(list[int(len(list)/2):])
  
  
  sorted = []
  numR = 0
  numL = 0
  

  while numR < len(right) and numL < len(left):
    if left[numL] > right[numR]:
      sorted.append(right[numR])
      numR += 1
    elif left[numL] < right[numR]:
      sorted.append(left[numL])
      numL += 1
    else:
      sorted.append(left[numL])
      sorted.append(right[numR])
      numL += 1
      numR += 1
  if numR != len(right):
    while numR != len(right):
      sorted.append(right[numR])
      numR += 1
  elif numL != len(left):
    while numL != len(left):
      sorted.append(left[numL])
      numL += 1 
  
  print(f"\nRIGHT: {right}")
  print(f"LEFT: {left}")
  print(f"RETURNING: {sorted}\n")
  return sorted
'''
  print("\nRight:")
  print(right)
  print(len(right), numR)
  print("\nleft:")
  print(left)
  print(len(left), numL)
  print("\n\n<>----------")
'''
  


def main():
  nums1 = [6,2,5,8,3,4,8]
  nums2 = [1,2,3,4,5,6,7,8]
  nums3 = [8,2,6,0,1,3]
  countyThing = 0

  for num_list in [nums1, nums2, nums3]:
    countyThing += 1
    print("\n<>---------------------\n")
    print(f"\nTest {countyThing}:\n\nOriginal: {num_list}")
    new = merge_sort(num_list)
    print(f"Sorted: {new}\n")

if __name__ == "__main__":
  system("clear")
  main()