import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 设置参数
p = 0.55  # 螺距
theta = np.linspace(0, 32 * np.pi, 1000)  # 角度范围

# 计算极坐标
r = p * theta

# 转换为直角坐标
x = r * np.cos(theta)
y = r * np.sin(theta)

# 已知点的坐标（圆心）
point_x = 3.0  # 修改为你需要的坐标
point_y = 4.0  # 修改为你需要的坐标

# 绘图
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='等距螺线')

# 标记已知点（圆心）
plt.scatter(point_x, point_y, color='red', label='圆心 (焦点)')  # 绘制选定点

# 以已知点为圆心绘制直径为 2.86 的圆
diameter = 2.86
radius = diameter
circle = Circle((point_x, point_y), radius, color='blue', fill=False, label='直径 = 2.86 的圆')
plt.gca().add_patch(circle)

# 标记等距螺线的焦点（原点）
plt.scatter(0, 0, color='green', label='螺线焦点 (原点)')  # 原点

# 设置图形属性
plt.title("等距螺线与圆")
plt.xlabel("X 轴")
plt.ylabel('Y 轴')
plt.axis('equal')
plt.grid()
plt.legend()

# 保存图像到文件
plt.savefig('spiral_with_circle_and_foci.png')  # 保存为PNG文件
plt.close()  # 关闭图形