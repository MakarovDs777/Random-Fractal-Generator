import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import os

def draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, points):
    """
    Рекурсивно рисует фрактальное дерево и собирает точки.

    Args:
        x, y, z: Координаты начала текущей ветви.
        length: Длина текущей ветви.
        min_length: Минимальная длина ветви для продолжения рекурсии.
        angle_xy: Угол в плоскости XY.
        angle_z: Угол наклона по оси Z.
        points: Список для хранения координат всех точек.

    Returns:
        None (изменяет список points по ссылке)
    """
    if length > min_length:
        # Рассчитываем координаты следующей точки
        new_x = x + length * np.cos(angle_xy) * np.cos(angle_z)
        new_y = y + length * np.sin(angle_xy) * np.cos(angle_z)
        new_z = z + length * np.sin(angle_z)

        # Добавляем точки
        points.extend([x, y, z]) # Используем extend для добавления нескольких элементов
        points.extend([new_x, new_y, new_z])


        # Рекурсивный вызов для левой и правой ветвей
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy - np.pi / 4, angle_z + np.pi / 8, points)
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy + np.pi / random.randint(1, 4), angle_z - np.pi / 8, points)

def save_points_to_file(filename, points):
    """
    Сохраняет координаты точек в текстовый файл в виде единого массива.

    Args:
        filename: Имя файла для сохранения.
        points: Список координат точек (x, y, z).
    """
    try:
        with open(filename, 'w') as f:
            f.write(str(points))  # Записываем весь список как строку
        print(f"Points saved to {filename}")
    except Exception as e:
        print(f"Error saving points to file: {e}")


# Начальные параметры
x, y, z = 0, 0, 0
length = 100
min_length = 5
angle_xy = np.pi / 2  # Угол в плоскости XY
angle_z = 0           # Начальный угол по оси Z

# Список для точек
points = []

# Вызываем функцию для рисования фрактала и сбора точек
draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, points)

# Сохраняем точки в файл
output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'fractal_tree_points.txt')
save_points_to_file(output_path, points)


# Создаем фигуру и ось для 3D отображения (опционально, если хотите видеть визуализацию)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#  Рисуем линии (опционально, только для визуализации)
for i in range(0, len(points), 6):
    x1, y1, z1 = points[i], points[i+1], points[i+2]
    x2, y2, z2 = points[i+3], points[i+4], points[i+5]
    ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')

# Настройки отображения (опционально)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Fractal Tree')

# Показываем график (опционально)
plt.show()
