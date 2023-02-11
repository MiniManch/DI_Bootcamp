# Perfect Number
user_num = input('give me a number i will check if its perfect \n')

while not user_num.isnumeric():
  user_num = input('thats not a number try again')

int_num = int(user_num)
sum = 0
divisors_list = []
for i in range(1, int_num - 1):
  if int_num % i == 0:
    divisors_list.append(i)
    sum += i
print(sum)
if sum == int_num:
  print('Thats a perfect Number!')
else:
  print('Thats not a perfet Number')
