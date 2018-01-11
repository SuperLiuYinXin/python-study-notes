# 用Python生成1000条评教内容

> 随着大家使用评教的人越来越多，评教的内容一尘不变，有点不太好，所以昨天花了一个晚上的时间，用Python撸了一个随机生成评教内容的程序。

原理很简单，每段话都是由几小句话组成的，所以只要准备好几小句话，然后将这几小句话随机组合就好。  
废话不多说，直接看代码  

## 1. 读取文件
首先我们需要准备好小段话的文件，并且用python来读取他们
这里我们用codecs库（自然语言编码转化）来读取文件，好处是可以指定读取和保存时候的编码.  
但是我们需要注意一下读取一行的时候在文件尾会有 `\r\n` 这个换行符。  
由于每行都有所以我偷懒直接去掉了读取文件的最后两个字符(即去掉`\r\n`)。  
然后使用python的生成器将读取文件写成一个函数。  
通过生成器我们可以将读取到的内容编变成一个列表。  
这里我们只要指定读取文件的路径即可。下面是代码
```python
import random  # 导入随机数库
import codecs # 导入文件读取和输出库

def read_line(path):
    with codecs.open(path, 'r', 'utf-8') as file:
        line = file.readline()[0:-2]  # 去回车 \n\r
        while line:
            yield line
            line = file.readline()[0:-2]  # 去回车 \n\r

# 使用列表生成式将从文件中读取到的内容变成一个列表集合
line_list = [line for line in read_line('./text.txt')] 
line_length = len(line_list) #计算读取到的句子的条数
```
## 2. 生成随机数数组
我们读取到了每个小句子的集合，接下来要做的只是要将它们随机组合就好了。  
这时候我们需要一个不重复的,每个元素都小于准备好的句子条数的随机数组。用随机数选择第几小句，把选择出来的句子拼接到一起，就是一个评教句子了。所以我们需要生成随机数组。这里用到了set集合，他的特性是相同的元素只能存在一个，添加两个时只会保留一个。利用set的这个特性，并且为了保证每个句子不至于过长，让产生3-5位的一个值，当set之中元素个数小于这个值时，就一直产生随机数添加到set集合中，直到set集合中元素大于这个值时，返回生成的set集合。
```
# 产生3-5位长的不相同的数字的set集合
def gen_random_list(limit):
    limit = limit-1 if limit > 2 else 1
    d = set([])
    temp_length = random.randint(3,5)
    while len(d) < temp_length:
        d.add(random.randint(0, limit))
    return d
```
## 3. 生成评教句子
下面就是生成评教的内容的语句了。  
主要是下面这条语句，用函数式编程，将生成的随机数对应的句子取出来，保存到一个表中
`str_list = list(map(lambda x: line_list[x], gen_random_list(line_length)))
`
  
  全部代码：
```
length = 50 # 指定生成多少条句子
# 将生成的内容保存到 `./out_file.txt` 这个目录下 `./`是当前目录
with codecs.open('./out_file.txt', 'w','utf-8') as out:
    for i in range(length):
        str_list = list(map(lambda x: line_list[x], gen_random_list(line_length)))
        out.writelines(','.join(str_list))
        out.writelines('\n')
```