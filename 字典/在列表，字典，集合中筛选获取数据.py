import random

data = [random.randint(-10,10) for i in range(10)]

# 用函数式编程来过滤掉负数
filter1 = filter(lambda x : x>=0, data)
filter1 = list(filter1) #将filter转化为数组

# 用列表解析除去负数
for1 = [x for x in data if x >= 0]

print("生成的数据测试数据")
print(data)
print("用函数式编程来过滤掉负数")
print(filter1)
print("用列表解析除去负数")
print(for1)
