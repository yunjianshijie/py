import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 设置参数
b = 0.55
theta1 = 0
theta2 = 32 * np.pi  # 计算从0到32π的长度

# 计算螺线的极坐标
def r(theta):
    return b * theta

def dr_dtheta(theta):
    return b

# 螺线长度的积分函数
def integrand(theta):
    return np.sqrt(dr_dtheta(theta)**2 + r(theta)**2)

# 计算长度
length, error = quad(integrand, theta1, theta2)

# 输出螺线长度
print(f'螺线长度: {length}')

# 生成螺线数据并绘图
theta = np.linspace(theta1, theta2, 1000)
r_values = r(theta)
x = r_values * np.cos(theta)
y = r_values * np.sin(theta)

# 选择一个点（例如，theta = 22π）
theta_point = 22 * np.pi
r_point = r(theta_point)
x_point = r_point * np.cos(theta_point)
y_point = r_point * np.sin(theta_point)

# 绘图
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='螺线 (螺距 = 0.55)')
plt.scatter(x_point, y_point, color='red')  # 标记点
plt.text(x_point, y_point, '  (x, y)', fontsize=12, color='red')  # 添加文本标签
plt.title('螺线 (螺距 = 0.55)')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.axis('equal')
plt.grid()
plt.legend()

# 保存图形到文件
plt.savefig('螺线_with_point.png')  # 保存为 PNG 文件
plt.close()  # 关闭当前图形