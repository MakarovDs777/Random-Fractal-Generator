import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_fractal_tree(x, y, z, length, min_length, angle, axis):
    if length > min_length:
        # Рассчитываем координаты следующей точки
        new_x = x + length * np.cos(angle)
        new_y = y + length * np.sin(angle)
        new_z = z + length * np.sin(angle)

        # Рисуем линию между текущей и следующей точками
        axis.plot([x, new_x], [y, new_y], [z, new_z], 'k-')

        # Рекурсивный вызов для левой и правой ветвей
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle - np.pi / 4, axis)
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle + np.pi / 4, axis)

# Создаем фигуру и ось для 3D отображения
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Начальные параметры
x, y, z = 0, 0, 0
length = 100
min_length = 5
angle = np.pi / 2

# Вызываем функцию для рисования фрактала
draw_fractal_tree(x, y, z, length, min_length, angle, ax)

# Показываем график
plt.show()
