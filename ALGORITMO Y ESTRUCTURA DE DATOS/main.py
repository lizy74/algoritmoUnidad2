from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import random
import numpy as np
from matplotlib.figure import Figure
from sorts import *

root = Tk()
root.title("Algoritmo de Ordenamientos - UNIDAD 2")
root.state('zoomed')

frame1 = Frame(root, highlightbackground="blue", highlightthickness=2, padx=15, pady=15)
frame2 = Frame(root)

fig = Figure(figsize=(6, 5), dpi=98)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=frame2)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def ordenar():
    tamano = int(entry1.get())
    rango = int(entry2.get())
    ax.cla()
    ax.set_ylabel("Tiempo (segundos)")
    ax.set_xlabel("Tamaño de la lista")

    tmpx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tmpy = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lista = []

    # Crear líneas para cada algoritmo de ordenamiento seleccionado
    for i in range(0, tamano, rango):
        if var1.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, 'g', label="Bubble Sort")
            order_bubble_sort(ax, lista, tmpx, tmpy)
        if var2.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, 'r', label="Quicksort")
            order_quicksort(ax, lista, tmpx, tmpy)
        if var3.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, 'b', label="Selection Sort")
            order_selection_sort(ax, lista, tmpx, tmpy)
        if var4.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, 'y', label="Insertion Sort")
            order_insertion_sort(ax, lista, tmpx, tmpy)
        if var5.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, '#FF00FF', label="Shell Sort")
            order_shell_sort(ax, lista, tmpx, tmpy)
        if var6.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, '#FFA500', label="Merge Sort")
            order_merge_sort(ax, lista, tmpx, tmpy)
        if var7.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, '#800080', label="Heap Sort")
            order_heap_sort(ax, lista, tmpx, tmpy)
        if var8.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, '#444444', label="Comb Sort")
            order_comb_sort(ax, lista, tmpx, tmpy)
        if var9.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if i == 0:
                ax.plot(0, 0, '#CCCCCC', label="Cocktail Sort")
            order_cocktail_sort(ax, lista, tmpx, tmpy)
        
    # Análisis Big O
    x = np.arange(0, tamano + 1, rango)
    if var_bubble_sort_big_o.get() == True:
        y = (x ** 2) / 1000000  # n^2 (Convertir microsegundos a segundos)
        ax.plot(x, y, label="Bubble Sort: O(n^2)", color='orange', linestyle='--')
    if var_selection_sort_big_o.get() == True:
        y = (x ** 2) / 1000000
        ax.plot(x, y, label="Selection Sort: O(n^2)", color='purple', linestyle='--')
    if var_quicksort_big_o.get() == True:
        y = (x * np.log(x + 1) / np.log(10))
        ax.plot(x, y, label="Quicksort: O(n*log(n))", color='blue', linestyle='--')
    if var_insertion_sort_big_o.get() == True:
        y = (x ** 2) / 1000000
        ax.plot(x, y, label="Insertion Sort: O(n^2)", color='green', linestyle='--')
    if var_merge_sort_big_o.get() == True:
        y = x * np.log(x + 1) / np.log(10)
        ax.plot(x, y, label="Merge Sort: O(n*log(n))", color='red', linestyle='--')
    if var_heap_sort_big_o.get() == True:
        y = x * np.log(x + 1) / np.log(10)
        ax.plot(x, y, label="Heap Sort: O(n*log(n))", color='cyan', linestyle='--')
    if var_shell_sort_big_o.get() == True:
        y = (x ** (3/2)) / 1000000  # Convertir microsegundos a segundos
        ax.plot(x, y, label="Shell Sort: O(n^(3/2))", color='#FF00FF', linestyle='--')
    if var_cocktail_sort_big_o.get() == True:
        y = (x ** 2) / 1000000
        ax.plot(x, y, label="Cocktail Sort: O(n^2)", color='#CCCCCC', linestyle='--')
    if var_comb_sort_big_o.get() == True:
        y = (x ** 2) / 1000000
        ax.plot(x, y, label="Comb Sort: O(n^2)", color='#444444', linestyle='--')

    ax.legend()
    ax.set_title("Gráfico de Ordenamientos y Big O")
    ax.grid(True)
    fig.tight_layout()
    canvas.draw()


var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()
var6 = BooleanVar()
var7 = BooleanVar()
var8 = BooleanVar()
var9 = BooleanVar()

var_bubble_sort_big_o = BooleanVar()
var_selection_sort_big_o = BooleanVar()
var_quicksort_big_o = BooleanVar()
var_insertion_sort_big_o = BooleanVar()
var_merge_sort_big_o = BooleanVar()
var_heap_sort_big_o = BooleanVar()
var_shell_sort_big_o = BooleanVar()
var_cocktail_sort_big_o = BooleanVar()
var_comb_sort_big_o = BooleanVar()

# Cuadro para el análisis Big O y algoritmos de ordenamiento
frame3 = Frame(root, highlightbackground="green", highlightthickness=2, padx=10, pady=15)
frame3.grid(row=0, column=0, padx=50, pady=20, rowspan=2)  # Aquí establecemos rowspan=2 para abarcar dos filas

label1 = Label(frame3, text="ALGORITMO DE ORDENAMIENTOS", fg="black", font=("Agencia", 16))
label1.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="n")

label2 = Label(frame3, text="Cantidad de Elementos: ", fg="black", font=("Agencia", 14))
label3 = Label(frame3, text="Recorrido Maximo: ", fg="black", font=("Agencia", 14))

entry1 = Entry(frame3, fg="black", font=("Agencia", 14))
entry2 = Entry(frame3, fg="black", font=("Agencia", 14))

checkbox1 = Checkbutton(frame3, text="Bubble Sort", variable=var1, width=20, font=("Agencia", 14))
checkbox2 = Checkbutton(frame3, text="Quicksort", variable=var2, width=20, font=("Agencia", 14))
checkbox3 = Checkbutton(frame3, text="Selection Sort", variable=var3, width=20, font=("Agencia", 14))
checkbox4 = Checkbutton(frame3, text="Insertion Sort", variable=var4, width=20, font=("Agencia", 14))
checkbox5 = Checkbutton(frame3, text="Shell Sort", variable=var5, width=20, font=("Agencia", 14))
checkbox6 = Checkbutton(frame3, text="Merge Sort", variable=var6, width=20, font=("Agencia", 14))
checkbox7 = Checkbutton(frame3, text="Heap Sort", variable=var7, width=20, font=("Agencia", 14))
checkbox8 = Checkbutton(frame3, text="Comb Sort", variable=var8, width=20, font=("Agencia", 14))
checkbox9 = Checkbutton(frame3, text="Cocktail Sort", variable=var9, width=20, font=("Agencia", 14))

simular = Button(frame3, text="Simular", command=ordenar, bg="skyblue", font=("Agencia", 12))

label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
label3.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

checkbox1.grid(row=3, column=0, padx=5, pady=5, sticky="w")
checkbox2.grid(row=4, column=0, padx=5, pady=5, sticky="w")
checkbox3.grid(row=5, column=0, padx=5, pady=5, sticky="w")
checkbox4.grid(row=3, column=1, padx=5, pady=5, sticky="w")
checkbox5.grid(row=4, column=1, padx=5, pady=5, sticky="w")
checkbox6.grid(row=5, column=1, padx=5, pady=5, sticky="w")
checkbox7.grid(row=3, column=2, padx=5, pady=5, sticky="w")
checkbox8.grid(row=4, column=2, padx=5, pady=5, sticky="w")
checkbox9.grid(row=5, column=2, padx=5, pady=5, sticky="w")

simular.grid(row=6, column=0, columnspan=3, pady=10)

label4 = Label(frame3, text="AANALISIS DE BIG O", fg="black", font=("Agencia", 16))
label4.grid(row=7, column=0, columnspan=3, pady=(20, 0), sticky="n")

# Checkboxes para seleccionar Big O
check_bubble_sort_big_o = Checkbutton(frame3, text="Bubble Sort: O(n^2)", variable=var_bubble_sort_big_o, font=("Agencia", 12))
check_selection_sort_big_o = Checkbutton(frame3, text="Selection Sort: O(n^2)", variable=var_selection_sort_big_o, font=("Agencia", 12))
check_quicksort_big_o = Checkbutton(frame3, text="Quicksort: O(n*log(n))", variable=var_quicksort_big_o, font=("Agencia", 12))
check_insertion_sort_big_o = Checkbutton(frame3, text="Insertion Sort: O(n^2)", variable=var_insertion_sort_big_o, font=("Agencia", 12))
check_merge_sort_big_o = Checkbutton(frame3, text="Merge Sort: O(n*log(n))", variable=var_merge_sort_big_o, font=("Agencia", 12))
check_heap_sort_big_o = Checkbutton(frame3, text="Heap Sort: O(n*log(n))", variable=var_heap_sort_big_o, font=("Agencia", 12))
check_shell_sort_big_o = Checkbutton(frame3, text="Shell Sort: O(n^(3/2))", variable=var_shell_sort_big_o, font=("Agencia", 12))
check_cocktail_sort_big_o = Checkbutton(frame3, text="Cocktail Sort: O(n^2)", variable=var_cocktail_sort_big_o, font=("Agencia", 12))
check_comb_sort_big_o = Checkbutton(frame3, text="Comb Sort: O(n^2)", variable=var_comb_sort_big_o, font=("Agencia", 12))

check_bubble_sort_big_o.grid(row=8, column=0, padx=5, pady=5, sticky="w")
check_selection_sort_big_o.grid(row=8, column=1, padx=5, pady=5, sticky="w")
check_quicksort_big_o.grid(row=8, column=2, padx=5, pady=5, sticky="w")
check_insertion_sort_big_o.grid(row=9, column=0, padx=5, pady=5, sticky="w")
check_merge_sort_big_o.grid(row=9, column=1, padx=5, pady=5, sticky="w")
check_heap_sort_big_o.grid(row=9, column=2, padx=5, pady=5, sticky="w")
check_shell_sort_big_o.grid(row=10, column=0, padx=5, pady=5, sticky="w")
check_cocktail_sort_big_o.grid(row=10, column=1, padx=5, pady=5, sticky="w")
check_comb_sort_big_o.grid(row=10, column=2, padx=5, pady=5, sticky="w")

frame2.grid(row=0, column=1, padx=20, pady=20, rowspan=2)  # Aquí establecemos rowspan=2 para abarcar dos filas

root.mainloop()