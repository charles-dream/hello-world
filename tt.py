#-*- coding=UTF-8-*-
height = 1.75
weight = 80.5
BMI = weight / height
if BMI <= 18.5:
    print('过轻')
elif BMI > 18.5 and BMI <25:
    print('正常')
elif BMI >= 25 and BMI <= 28:
    print('过重')
elif BMI > 28 and BMI <= 32:
    print('胖子')
else:
    BMI > 32
    print('你可能是一座山')