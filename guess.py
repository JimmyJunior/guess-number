s = input('最小數:')
b = input('最大數:')
s = int(s)
b = int(b)
count = 0
count = int(count)
import random
a = random.randint(s, b)
a = int(a)
while True:
	count += 1
	B = '請猜' + str(s) + '到' + str(b) + '的數字:' 
	aa = input(B)
	aa = int(aa)
	if aa == a:
		print('你猜中了')
		break
	elif aa > a:
		print('比答案大')
		b = str(aa)
	elif aa < a:
		print('比答案小')
		s = str(aa)
	else:
		print("你已超出範圍")
	print('這是你猜的第', count ,'次')
print("恭喜答對")