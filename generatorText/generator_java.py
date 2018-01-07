import codecs
import random


def read_line(path):
    with codecs.open(path, 'r', 'utf-8') as file:
        line = file.readline()[0:-2]  # 去回车 \n\r
        while line:
            yield line
            line = file.readline()[0:-2]  # 去回车 \n\r

# 产生3-5位长的不相同的数字
def gen_random_list(limit):
    limit = limit-1 if limit > 2 else 1
    d = set([])
    temp_length = random.randint(3,5)
    while len(d) < temp_length:
        d.add(random.randint(0, limit))
    return d


line_list = [line for line in read_line('./text.txt')]
line_length = len(line_list)
length = 1000

with codecs.open('./out.txt', 'w','utf-8') as out:
    out.writelines("lines = new HashMap({});".format(length))
    out.write('\n')
    for i in range(length):
        str_list = list(map(lambda x: line_list[x], gen_random_list(line_length)))
        out.write('lines.put({},"'.format(i))
        out.writelines(','.join(str_list))
        out.writelines('。");\n')

