import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import os

def draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, axis, points, lines):
    if length > min_length:
        # Рассчитываем координаты следующей точки
        new_x = x + length * np.cos(angle_xy) * np.cos(angle_z)
        new_y = y + length * np.sin(angle_xy) * np.cos(angle_z)
        new_z = z + length * np.sin(angle_z)

        # Добавляем точки и линии
        points.append([x, y, z])
        points.append([new_x, new_y, new_z])
        lines.append([len(points) - 2, len(points) - 1])

        # Рисуем линию между текущей и следующими точками
        axis.plot([x, new_x], [y, new_y], [z, new_z], 'k-')

        # Рекурсивный вызов для левой и правой ветвей
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy - np.pi / 4, angle_z + np.pi / 8, axis, points, lines)
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy + np.pi / random.randint(1, 4), angle_z - np.pi / 8, axis, points, lines)

def save_obj(filename, points, lines):
    try:
        with open(filename, 'w') as f:
            # Записываем точки
            for p in points:
                f.write('v {:.6f} {:.6f} {:.6f}\n'.format(p[0], p[1], p[2]))
            
            # Записываем линии как линии из двух точек
            for l in lines:
                f.write('l {} {}\n'.format(l[0] + 1, l[1] + 1))
        
        print(f"Model saved as {filename}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Создаем фигуру и ось для 3D отображения
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Начальные параметры
x, y, z = 0, 0, 0
length = 100
min_length = 5
angle_xy = np.pi / 2  # Угол в плоскости XY
angle_z = 0           # Начальный угол по оси Z

# Списки для точек и линий
points = []
lines = []

# Вызываем функцию для рисования фрактала
draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, ax, points, lines)

# Настройки отображения
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Fractal Tree')

# Сохранение изображения на рабочий стол
output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'fractal_tree.obj')
save_obj(output_path, points, lines)

# Показываем график
plt.show()
