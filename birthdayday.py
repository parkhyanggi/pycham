'''
생년월일로 태어난 요일 알려주는 프로그램
programmer. Park hyang-gi
date. 2021. 09. 13 ~
'''

import datetime

y = int(input('당신이 태어난 년도를 입력하세요\n'))
m = int(input('당신이 태어난 달을 입력하세요\n'))
d = int(input('당신이 태어난 일을 입력하세요\n'))

x = datetime.datetime(y,m,d)
print('\n당신이 태어난 요일은 '+ x.strftime("%A") +' 입니다.\n')

print(x.strftime("%A"))