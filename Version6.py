import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure
import os

def draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, points, scale):
    if length > min_length:
        # Рассчитываем координаты следующей точки
        new_x = x + length * np.cos(angle_xy) * np.cos(angle_z)
        new_y = y + length * np.sin(angle_xy) * np.cos(angle_z)
        new_z = z + length * np.sin(angle_z)

        # Добавляем точки вдоль текущей линии
        num_points = int(length * scale)
        for i in range(num_points):
            t = i / num_points
            point = np.array([x, y, z]) + t * (np.array([new_x, new_y, new_z]) - np.array([x, y, z]))
            points.append(point)

        # Рекурсивный вызов для левой и правой ветвей
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy - np.pi / 4, angle_z + np.pi / 8, points, scale)
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle_xy + np.pi / 4, angle_z - np.pi / 8, points, scale)

def create_surface_from_points(points, grid_size):
    # Создаем пустой 3D массив
    array = np.zeros(grid_size, dtype=bool)
    
    # Заполняем массив на основе точек
    for point in points:
        idx = np.floor(point).astype(int)
        if np.all(idx >= 0) and np.all(idx < np.array(grid_size)):
            array[tuple(idx)] = 1

    return array

def save_fractal(verts, faces, filename):
    try:
        with open(filename, 'w') as f:
            for v in verts:
                f.write('v {:.6f} {:.6f} {:.6f}\n'.format(v[0], v[1], v[2]))
            for face in faces:
                f.write('f {} {} {}\n'.format(face[0]+1, face[1]+1, face[2]+1))
        print(f"Model saved as {filename}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Начальные параметры
x, y, z = 0, 0, 0
length = 100
min_length = 5
angle_xy = np.pi / 4  # Угол в плоскости XY
angle_z = 0           # Начальный угол по оси Z
scale = 2             # Масштабирование координат для массива
grid_size = (128, 128, 128)  # Размер массива для ограничения фрактала

# Создаем список точек и вызываем функцию для рисования фрактала
points = []
draw_fractal_tree(x, y, z, length, min_length, angle_xy, angle_z, points, scale)

# Масштабируем точки так, чтобы они вмещались в массив
points = np.array(points)
min_vals = np.min(points, axis=0)
max_vals = np.max(points, axis=0)
scale_factors = np.array(grid_size) / (max_vals - min_vals)
scaled_points = (points - min_vals) * scale_factors
scaled_points = np.clip(scaled_points, 0, np.array(grid_size) - 1)

# Создаем 3D массив на основе масштабированных точек
array = create_surface_from_points(scaled_points, grid_size)

# Создание изосурфейса для всех линий фрактала
verts, faces, _, _ = measure.marching_cubes(array, level=0.5)

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Визуализация модели
verts = verts * np.array(grid_size) / np.max(grid_size)  # Масштабируем обратно для визуализации
verts -= np.min(verts, axis=0)  # Центрируем модель

# Создаем коллекцию полигонов для визуализации
poly3d = Poly3DCollection(verts[faces], alpha=0.5, edgecolor='k')
ax.add_collection3d(poly3d)

# Настройки отображения
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.auto_scale_xyz([0, 1], [0, 1], [0, 1])  # Устанавливаем диапазоны для осей

# Показываем окно с моделью
plt.show()

# Сохранение фрактала в формате OBJ
output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'fractal.obj')
save_fractal(verts, faces, output_path)
