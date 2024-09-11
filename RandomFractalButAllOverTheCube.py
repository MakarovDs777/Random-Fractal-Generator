import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random 
import math

def draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, axis):
    if length > min_length:
        # Рассчитываем координаты следующей точки
        new_x = x + length * np.cos(angle_xy) * np.cos(angle_z)
        new_y = y + length * np.sin(angle_xy) * np.cos(angle_z)
        new_z = z + length * np.sin(angle_z)

        # Рисуем линию между текущей и следующими точками
        axis.plot([x, new_x], [y, new_y], [z, new_z], 'k-')

        # Рекурсивный вызов для левой и правой ветвей
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy - np.pi / 4, angle_z + np.pi / 8, axis)
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy + np.pi / random.randint(1, 4), angle_z - np.pi / 8, axis)

# Создаем фигуру и ось для 3D отображения
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Начальные параметры
x, y, z = 0, 0, 0
length = 100
min_length = 5
angle_xy = np.pi / 2  # Угол в плоскости XY
angle_z = 0           # Начальный угол по оси Z

# Вызываем функцию для рисования фрактала
draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, ax)

# Показываем график
plt.show()
