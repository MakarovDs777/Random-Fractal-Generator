import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import os

def draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, points):
    """
    Рекурсивно рисует фрактальное дерево и собирает точки.
    Внутри функции все вычисления с вещественными числами.
    """
    if length > min_length:
        # Рассчитываем координаты следующей точки (вещественные)
        new_x = x + length * np.cos(angle_xy) * np.cos(angle_z)
        new_y = y + length * np.sin(angle_xy) * np.cos(angle_z)
        new_z = z + length * np.sin(angle_z)

        # Добавляем текущие точки (вещественные)
        points.extend([x, y, z])
        # Добавляем новые точки (вещественные)
        points.extend([new_x, new_y, new_z])

        # Рекурсивный вызов для ветвей
        new_length = length * 0.75
        if new_length < 1e-3:
            new_length = 1e-3  # чтобы не было очень маленьких значений
        draw_fractal_tree(new_x, new_y, new_z, new_length, min_length, angle_xy - np.pi / 4, angle_z + np.pi / 8, points)
        draw_fractal_tree(new_x, new_y, new_z, new_length, min_length, angle_xy + np.pi / random.randint(1, 4), angle_z - np.pi / 8, points)

def save_points_to_file(filename, points):
    """
    Сохраняет координаты точек в файл, преобразуя все числа в целые.
    """
    try:
        # Преобразуем все числа в целые
        int_points = [int(round(coord)) for coord in points]
        with open(filename, 'w') as f:
            f.write(str(int_points))
        print(f"Points saved to {filename}")
    except Exception as e:
        print(f"Error saving points to file: {e}")

# Начальные параметры
x, y, z = 0.0, 0.0, 0.0
length = 100.0
min_length = 5.0
angle_xy = np.pi / 2  # Угол в плоскости XY
angle_z = 0           # Начальный угол по оси Z

# Список для точек
points = []

# Вызов функции для генерации фрактала
draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, points)

# Сохраняем точки в файл
output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'fractal_tree_points.txt')
save_points_to_file(output_path, points)

# Визуализация (оставляем без изменений)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(0, len(points), 6):
    x1, y1, z1 = points[i], points[i+1], points[i+2]
    x2, y2, z2 = points[i+3], points[i+4], points[i+5]
    ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Fractal Tree')

plt.show()
