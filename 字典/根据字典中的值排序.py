
# 使用 python中的 sorted 进行排序
# 推荐使用 sorted 这个内置函数 进行 排序

# 例： 创建一个字典

from random import randint

#使用列表生成式 生成成绩
grade = {x: randint(60, 100) for x in 'xyzabc'}

print(grade)

# 根据列表的值进行排序
# 先获取所有的元素
# 再根据指定的key 值进行排序
print(sorted(grade.items(), key=lambda x: x[1]))
