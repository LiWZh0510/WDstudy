#!/usr/bin/python3
# author liwzh


import numpy as np
import matplotlib.pyplot as plt

us_file_path = "D:/lwzh/王道-python/week6/day34/day34/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "D:/lwzh/王道-python/week6/day34/day34/youtube_video_data/GB_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int")


print(np.count_nonzero(t2 != t2))

# 取评论的数据
t_us_comments = t2[:, -1]

# 选择比5000小的数据,因为数据主要集中在5000以下
t_us_comments = t_us_comments[t_us_comments <= 5000]

# 怎么知道分多少，打印最大和最小值
print(t_us_comments.max(), t_us_comments.min())

d = 100

bin_nums = (t_us_comments.max() - t_us_comments.min()) // d

# 绘图
plt.figure(figsize=(20, 8), dpi=80)

plt.hist(t_us_comments, bin_nums)

plt.show()
