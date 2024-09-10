import numpy as np
import matplotlib.pyplot as plt

# 设置参数
p = 0.55  # 螺距
theta = np.linspace(0, 32 * np.pi, 1000)  # 角度范围

# 计算极坐标
r = p * theta

# 转换为直角坐标
x = r * np.cos(theta)
y = r * np.sin(theta)

# 绘图
plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.title('等距螺线 (螺距 = 0.55)')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.axis('equal')
plt.grid()

# 保存图像到文件
plt.savefig('spiral_plot.png')  # 保存为PNG文件
plt.close()  # 关闭图形