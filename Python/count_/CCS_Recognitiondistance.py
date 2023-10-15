import numpy as np
from fractions import Fraction
from tqdm import tqdm

# 定义m的取值范围和步长
start = -100
end = 100
step = 0.000001

# 生成m的所有可能值
m_values = np.arange(start, end, step)

# 初始化最小“识别距离”和对应的m值
min_distance = float('inf')
min_m = None

# 对每个m值，计算“识别距离”
for m in tqdm(m_values):  # 使用tqdm函数来添加进度条
    x1, y1 = m, 3/4*m+3  # 点C的坐标
    x2, y2 = 0, 1  # 点D的坐标

    # 计算“识别距离”
    if abs(x1-x2) >= abs(y1-y2):
        distance = abs(x1-x2)
    else:
        distance = abs(y1-y2)

    # 如果当前“识别距离”小于已知的最小“识别距离”，则更新最小“识别距离”和对应的m值
    if distance < min_distance:
        min_distance = distance
        min_m = m

# 输出最小“识别距离”和对应的m值，以分数形式表示
print('最小“识别距离”为：', Fraction(min_distance).limit_denominator())
print('对应的m值为：', Fraction(min_m).limit_denominator())
