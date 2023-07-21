from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import random
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from sorts import *

root = Tk()
root.title("Algoritmo de Ordenamientos PROYECTO 1")
root.state('zoomed')
frame1 = Frame(root, highlightbackground="blue", highlightthickness=2, padx=20, pady=20)
frame2 = Frame(root)

fig = Figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=frame2)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def ordenar():
    tamano = int(entry1.get())
    rango = int(entry2.get())
    ax.cla()
    ax.set_ylabel("Tiempo (segundos)")
    ax.set_xlabel("Tamaño de la lista")

    canvas.draw()
    tmpx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tmpy = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #cambios = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #comparaciones = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lista = []
    for i in range(0, tamano, rango):
        if var1.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'g', label="Bubble Sort")
            order_bubble_sort(ax, lista, tmpx, tmpy)
        if var2.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'r', label="Quicksort")
            order_quicksort(ax, lista, tmpx, tmpy)
        
        if var3.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'b', label="Selection Sort")
            order_selection_sort(ax, lista, tmpx, tmpy)

        if var4.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, 'y', label="Insertion Sort")
            order_insertion_sort(ax, lista, tmpx, tmpy)
        
        if var5.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#FF00FF', label="Shell Sort")
            order_shell_sort(ax, lista, tmpx, tmpy)
        
        if var6.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#FFA500', label="Merge Sort")
            order_merge_sort(ax, lista, tmpx, tmpy)
        
        if var7.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#800080', label="Heap Sort")
            order_heap_sort(ax, lista, tmpx, tmpy)
        
        if var8.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#444444', label="Comb Sort")
            order_comb_sort(ax, lista, tmpx, tmpy)

        if var9.get() == True:
            lista = [random.randint(0, tamano - 1) for _ in range(i)]
            if(i == 0):
                ax.plot(0, 0, '#CCCCCC', label="Cocktail Sort")
            order_cocktail_sort(ax, lista, tmpx, tmpy)
        canvas.draw()
        root.update()
        time.sleep(0.0001)
        ax.legend()

    #if var1.get() == True:
        #lst.append(("Bubble Sort", comparaciones[0], cambios[0]))
    #t.mostrar(len(lst), len(lst[0])) 

var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()
var6 = BooleanVar()
var7 = BooleanVar()
var8 = BooleanVar()
var9 = BooleanVar()

label1 = Label(frame1, text="ALGORITMO DE ORDENAMIENTOS", fg="black", font=("Agencia", 16))
label1.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="n")

label2 = Label(frame1, text="Cantidad de Elementos: ", fg="black", font=("Agencia", 14))
label3 = Label(frame1, text="Recorrido Maximo: ", fg="black", font=("Agencia", 14))

entry1 = Entry(frame1, fg="black", font=("Agencia", 14))
entry2 = Entry(frame1, fg="black", font=("Agencia", 14))

checkbox1 = Checkbutton(frame1, text="Bubble Sort", variable=var1, width=20, font=("Agencia", 14))
checkbox2 = Checkbutton(frame1, text="Quicksort", variable=var2, width=20, font=("Agencia", 14))
checkbox3 = Checkbutton(frame1, text="Selection Sort", variable=var3, width=20, font=("Agencia", 14))
checkbox4 = Checkbutton(frame1, text="Insertion Sort", variable=var4, width=20, font=("Agencia", 14))
checkbox5 = Checkbutton(frame1, text="Shell Sort", variable=var5, width=20, font=("Agencia", 14))
checkbox6 = Checkbutton(frame1, text="Merge Sort", variable=var6, width=20, font=("Agencia", 14))
checkbox7 = Checkbutton(frame1, text="Heap Sort", variable=var7, width=20, font=("Agencia", 14))
checkbox8 = Checkbutton(frame1, text="Comb Sort", variable=var8, width=20, font=("Agencia", 14))
checkbox9 = Checkbutton(frame1, text="Cocktail Sort", variable=var9, width=20, font=("Agencia", 14))

simular = Button(frame1, text="Simular", command=ordenar, bg="skyblue", font=("Agencia", 12))

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

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

root.mainloop()



