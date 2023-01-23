''' CPS 312 - Spring, 2023
    TA 02: Python Hints & Functions
    
    Gabriela Calderon
    Jenna Ryan
    
    See README.md for project instructions.
    
'''

# define function iRev here - it must "return" the result
# using an iterative approach
def iRev(inputString: str) -> str:
  lst = []
  for i in inputString:
    lst.append(i)
  lst.reverse()
  out = ''.join(lst)
  return out
  

# define function rRev here - it must "return" the result
# using a recursive approach
def rRev(inputString: str, index: int) -> str:
  if index == 0:
    return inputString[index]
  else:
    return inputString[index] + rRev(inputString, index - 1)


def main():
  # body of your main program here
  
  validInput = False
  while not validInput == True :
    inputString = input('Enter a string: ')
    if len(inputString) <= 1:
      print('Please enter a string longer than 1 character.')
    else:
      validInput = True

  print(f'The reverse is "{iRev(inputString)}", computed iteratively.')
  print(f'The reverse is "{rRev(inputString, len(inputString) - 1)}", computed recursively.')


# do not touch the code below
if __name__ == "__main__":
  main()