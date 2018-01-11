
# 先生成随机序列
from random import randint

data = [randint(0, 20) for _ in range(20)]

# 方法一
# 创建一个以data为键，0为值的字典
c = dict.fromkeys(data, 0)

for x in data:
    c[x] += 1


print(c)


# 方法二
# 使用 collection 的 Counter 对象
# 可以统计频率

from collections import Counter

c2 = Counter(data)
print(c2)

#统计出现次数最多的  n 个元素  传递的 n 是最多的次数
c3 = c2.most_common(3)
print(c3)

