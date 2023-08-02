import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

Nombre: Matias
Apellido: Machuca
Div: "I"

A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser
ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en
la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe
    4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):
        peso = self.txt_peso_articulo.get()
        tipo_peso = self.combobox_tipo_de_peso.get()

        if float(peso) > 0:
            peso = float(peso)
            if tipo_peso == "Onzas":
                peso = peso * 28.3495
            self.lista_pesos.append(peso)
            alert("Carga", "Carga exitosa")
        else:
            alert("Carga", "Error de carga")

        self.txt_peso_articulo.delete(0, 100)

        
    def btn_mostrar_on_click(self):
        # B - Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)
        contador = 0
        for peso in self.lista_pesos:
            print("Posicion " + str(contador) + ": " + str(peso) + " gramos" + " ó " + str(peso * 0.035274) + " onzas")
            contador += 1
            
        
    def btn_informar_on_click(self):
       # 0 - Valor (en onzas) y posicion del articulo mas pesado:
        peso_maximo = None
        posicion_maximo = None
        for i in range(0, len(self.lista_pesos), 1):
            if i == 0 or self.lista_pesos[i] > peso_maximo:
                peso_maximo = self.lista_pesos[i]
                posicion_maximo = i
        if peso_maximo is not None:
            print("El valor en onzas del articulo mas pesado es: " + str(peso_maximo * 0.035274) + " y su posicion en lista es: " + str(posicion_maximo))
        else:
            print("La lista esta vacia")


        # 1 - Valor (en gramos) y posicion del articulo mas liviano:
        peso_minimo = None
        posicion_minimo = None
        for i in range(0, len(self.lista_pesos), 1):
            if i == 0 or self.lista_pesos[i] < peso_minimo:
                peso_minimo = self.lista_pesos[i]
                posicion_minimo = i
        if peso_minimo is not None:
            print("1 - El valor en gramos del articulo mas liviano es: " + str(peso_minimo) + " y su posicion en lista es: " + str(posicion_minimo))
        else:
            print("1 - La lista esta vacia")


        # 2 - Peso promedio (en onzas)
        acumulador_pesos = 0
        for i in range(0, len(self.lista_pesos), 1):
            acumulador_pesos += self.lista_pesos[i]
        if len(self.lista_pesos) != 0:
            promedio_onzas = (acumulador_pesos * 0.035274) / len(self.lista_pesos)
            print("2 - El promedio en onzas es: " + str(promedio_onzas))
        else:
            print("2 - La lista esta vacia")


        # 3 - Peso promedio (en gramos)
        acumulador_pesos = 0
        for i in range(0, len(self.lista_pesos), 1):
            acumulador_pesos += self.lista_pesos[i]
        if len(self.lista_pesos) != 0:
            promedio_gramos = acumulador_pesos / len(self.lista_pesos)
            print("3 - El promedio en gramos es: " + str(promedio_gramos))
        else:
            print("3 - La lista esta vacia")


        # 4 - Informar los pesos que superan el promedio (en gramos)
        for i in range(0, len(self.lista_pesos), 1):
            if self.lista_pesos[i] > promedio_gramos:
                print("4 - Pesos que superan el promedio (en gramos): \n" + str(self.lista_pesos[i]))


        # 5 - Informar los pesos que NO superan el promedio (en onzas)
        for i in range(0, len(self.lista_pesos), 1):
            if self.lista_pesos[i] < promedio_gramos:
                print("5 - Pesos que no superan el promedio (en onzas): \n" + str(self.lista_pesos[i]))


        # 6 - Informar la cantidad de articulos que superan el peso promedio
        contador_articulos_sobre_promedio = 0
        for i in range(0, len(self.lista_pesos), 1):
            if self.lista_pesos[i] > promedio_gramos:
                contador_articulos_sobre_promedio += 1
        print("6 - Cantidad de productos que superan el peso promedio: " + str(contador_articulos_sobre_promedio))


        # 7 - Informar la cantidad de articulos que NO superan el peso promedio
        contador_articulos_bajo_promedio = 0
        for i in range(0, len(self.lista_pesos), 1):
            if self.lista_pesos[i] < promedio_gramos:
                contador_articulos_bajo_promedio += 1
        print("7 - Cantidad de productos que no superan el peso promedio: " + str(contador_articulos_bajo_promedio))


        # 8 - Indicar los pesos repetidos (gramos)
        lista_repetidos_gramos = []
        for peso in self.lista_pesos:
            if self.lista_pesos.count(peso) > 1 and lista_repetidos_gramos.count(peso) == 0:
                lista_repetidos_gramos.append(peso)
        print("8 - Pesos repetidos en gramos: " + str(lista_repetidos_gramos))


        # 9 - Indicar los pesos NO repetidos (gramos)
        lista_no_repetidos_gramos = []
        for peso in self.lista_pesos:
            if self.lista_pesos.count(peso) == 1:
                lista_no_repetidos_gramos.append(peso)
        print("9 - Pesos no repetidos en gramos: " + str(lista_no_repetidos_gramos))

       
if __name__ == "__main__":
    app = App()

    app.mainloop()