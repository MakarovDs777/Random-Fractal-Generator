import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import os

def draw_fractal_tree(x, y, z, length, min_length, angle, axis, vertices, edges):
    if length > min_length:
        # Рассчитываем координаты следующей точки
        new_x = x + length * np.cos(angle)
        new_y = y + length * np.sin(angle)
        new_z = z + length * np.sin(angle)
        
        # Добавляем вершины
        vertices.append((x, y, z))
        vertices.append((new_x, new_y, new_z))
        edges.append((len(vertices)-2, len(vertices)-1))

        # Рисуем линию между текущей и следующей точками
        axis.plot([x, new_x], [y, new_y], [z, new_z], 'k-')

        # Рекурсивный вызов для левой и правой ветвей
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle - np.pi / 4, axis, vertices, edges)
        draw_fractal_tree(new_x, new_y, new_z, length * 0.75, min_length, angle + np.pi / random.randint(1,4), axis, vertices, edges)

def save_obj(vertices, edges, filename):
    with open(filename, 'w') as f:
        for vertex in vertices:
            f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        for edge in edges:
            f.write(f"l {edge[0]+1} {edge[1]+1}\n")  # OBJ индексы начинаются с 1

def on_key(event):
    if event.key == 'r':
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "fractal.obj")
        save_obj(vertices, edges, desktop_path)
        print(f"OBJ файл сохранен на рабочем столе как 'fractal.obj'")

# Создаем фигуру и ось для 3D отображения
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Начальные параметры
x, y, z = 0, 0, 0
length = 100
min_length = 5
angle = np.pi / 2

# Списки для хранения вершин и рёбер
vertices = []
edges = []

# Вызываем функцию для рисования фрактала
draw_fractal_tree(x, y, z, length, min_length, angle, ax, vertices, edges)

# Подключаем обработчик событий
fig.canvas.mpl_connect('key_press_event', on_key)

# Показываем график
plt.show()
