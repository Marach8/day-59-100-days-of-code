print('PALINDROME CHECKER')
print()
ask = input('Enter the word here: ').lower()
list = [] 
i = -1
while i >= -len(ask):
  list.append(ask[i])
  i -= 1

a = ''.join(list)
if a == ask:
  print()
  print('\033[32mYes, this word is a Palindrome')
else:
  print()
  print('\033[31mNo, this word is not a Palindrome')
