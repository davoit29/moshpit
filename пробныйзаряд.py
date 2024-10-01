import customtkinter as ctk
from tkinter import StringVar, IntVar

# Создаем главное окно
ctk.set_appearance_mode("dark")  # Темная тема
ctk.set_default_color_theme("green")  # Цветовая тема

# Функция для включения двигателя
def start_motor():
    print("Двигатель включен")

# Функция для остановки двигателя
def stop_motor():
    print("Двигатель остановлен")

# Функция для изменения скорости
def set_speed(value):
    print(f"Скорость установлена на {value}")

# Создаем главное окно
window = ctk.CTk()
window.title("Контроль вязальной машины")
window.geometry("500x500")

# Переменные для отслеживания количества петель и кругов
stitches_var = StringVar(value="0 петель")
rounds_var = StringVar(value="0 кругов")

# Создаем кнопку "Включить"
start_button = ctk.CTkButton(window, text="Включить", command=start_motor, width=200)
start_button.pack(pady=20)

# Создаем кнопку "Остановить"
stop_button = ctk.CTkButton(window, text="Остановить", command=stop_motor, width=200)
stop_button.pack(pady=20)

# Создаем ползунок для регулировки скорости
speed_slider = ctk.CTkSlider(window, from_=0, to=100, command=set_speed)
speed_slider.set(50)  # Устанавливаем начальную скорость
speed_slider.pack(pady=20)

# Метка для текущей скорости
speed_label = ctk.CTkLabel(window, text="Скорость")
speed_label.pack(pady=10)

# Графа для отображения количества петель
stitches_label = ctk.CTkLabel(window, textvariable=stitches_var, font=("Arial", 18))
stitches_label.pack(pady=10)

# Графа для отображения количества кругов
rounds_label = ctk.CTkLabel(window, textvariable=rounds_var, font=("Arial", 18))
rounds_label.pack(pady=10)

# Запуск основного цикла Tkinter
window.mainloop()
