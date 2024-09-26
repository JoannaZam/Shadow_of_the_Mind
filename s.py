import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class Juego:
    def __init__(self, root):
        self.root = root
        self.root.title("Shadows of the Mind")
        self.root.geometry("800x600")

        self.username = ""

        self.cargar_fondo()
        self.setup_main_menu()

    def cargar_fondo(self):
        global fondo_imagen  # Asegúrate de que la imagen no sea recolectada como basura
        fondo = Image.open("imagen.PNG")
        fondo = fondo.resize((800, 600))  # Ajustar el tamaño de la imagen
        fondo_imagen = ImageTk.PhotoImage(fondo)

        etiqueta_fondo = tk.Label(self.root, image=fondo_imagen)
        etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar el fondo correctamente

    def setup_main_menu(self):
        # Crear el menú principal
        self.menu_frame = tk.Frame(self.root, bg="lightgrey")  # Color de fondo visible para el menú
        self.menu_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el menú

        title = tk.Label(self.menu_frame, text="¡Desata el misterio!", font=("Imprint MT Shadow", 18), bg="lightgrey")
        title.pack(pady=10)

        # Botón para ingresar nombre de usuario
        username_button = tk.Button(self.menu_frame, text="Iniciar juego", command=self.get_username)
        username_button.pack(pady=5)

        # Salir
        exit_button = tk.Button(self.menu_frame, text="Salir", command=self.root.quit)
        exit_button.pack(pady=5)

        # Crear el frame para ingresar el nombre de usuario sin fondo
        self.username_frame = tk.Frame(self.root, bg="lightgrey", bd=0)  # Sin borde y color de fondo
        self.username_label = tk.Label(self.username_frame, text="Ingresa tu nombre de usuario:", font=("Arial", 12),
                                       bg="lightgrey")
        self.username_entry = tk.Entry(self.username_frame, bg="white")  # Fondo blanco solo para la entrada
        self.continue_button = tk.Button(self.username_frame, text="Continuar", command=self.set_username)

    # Función para mostrar el cuadro de entrada de nombre de usuario
    def get_username(self):
        self.menu_frame.place_forget()  # Ocultar el menú principal
        self.username_frame.place(relx=0.5, rely=0.5, anchor="center")  # Mostrar el cuadro de entrada

        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=5)
        self.continue_button.pack(pady=10)

    # Función para establecer el nombre de usuario
    def set_username(self):
        self.username = self.username_entry.get()
        if not self.username:
            messagebox.showwarning("Advertencia", "¡Debes ingresar un nombre de usuario!")
            return
        self.username_frame.place_forget()  # Cerrar el cuadro de entrada
        self.iniciar_juego()

    def iniciar_juego(self):
        print(f"Iniciando juego para {self.username}...")
        # Aquí puedes agregar la lógica para iniciar el juego


# Crear la ventana principal
ventana = tk.Tk()
juego = Juego(ventana)
ventana.mainloop()

("¡Desata el misterio!", front=("Imprint MT Shadow", 18)
