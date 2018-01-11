from collections import namedtuple

# 使用collections 内置的 namedtuple 类
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

# 直接传递所有参数
s1 = Student('Jim', 16, 'male', 'heo@qq.com')

# 关键字传参
s2 = Student(name='Jim', age=16, sex='male', email='heo@qq.com')

# 传递参数必须都有
# s3 = Student(name='Jim', age=16, sex='male')
print("传递所有参数"+ str(s1))
print("关键字传参数"+ str(s2))

print("使用s1.age取值：" + str(s1.age))
# print("传部分参数, 会报错"+ s3)
