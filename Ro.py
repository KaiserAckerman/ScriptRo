import tkinter as tk
from PIL import Image, ImageTk

class TimerApp:
    def __init__(self, master, title, initial_time, bg_image, row, column):
        self.master = master
        self.title = title  # Guardar el título para referencia

        # Configurar el ícono de la ventana
        self.master.iconbitmap('Imagenes Secciones/mvp.ico')  # Reemplaza 'icono.ico' con la ruta de tu archivo de ícono

        # Configurar el título de la ventana
        self.master.title("MVP TEMPORIZADOR")  # Cambia "Mi Aplicación" por el título deseado y agrega el título de la interfaz

        # Crear un Frame para agrupar los elementos con un borde y un margen
        self.frame = tk.Frame(master, bd=2, relief="groove", padx=10, pady=10)
        self.frame.grid(row=row, column=column)

        # Cargar la imagen de fondo
        self.bg_image = Image.open(bg_image)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Establecer la imagen de fondo del Frame
        self.background_label = tk.Label(self.frame, image=self.bg_photo)
        self.background_label.place(relwidth=1, relheight=1)  # Establecer el tamaño de la imagen de fondo para que llene todo el Frame

        # Crear un Label para el título con contorno ligero y fondo transparente
        self.title_label = tk.Label(self.frame, text=title, font=("Arial", 16, "bold"), bd=1, relief="solid", bg=self.master["bg"], padx=5, pady=5)
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="we")  # Agregar sticky="we" para hacer que el Label se expanda horizontalmente

        # Crear un Label para el temporizador con contorno ligero y fondo transparente
        self.timer_label = tk.Label(self.frame, text="00:00:00", font=("Arial", 24), bd=1, relief="solid", bg=self.master["bg"], padx=5, pady=5)
        self.timer_label.grid(row=1, column=0, columnspan=2, sticky="we")  # Agregar sticky="we" para hacer que el Label se expanda horizontalmente

        # Crear un botón de inicio y conectarlo a la función start_timer
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_timer, bg="green")
        self.start_button.grid(row=2, column=0, pady=10)

        # Crear un botón de reset y conectarlo a la función reset_timer
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_timer, bg="orange")
        self.reset_button.grid(row=2, column=1, pady=10)

        # Variables para el temporizador
        self.running = False
        self.initial_time = initial_time  # Guardar el tiempo inicial del temporizador
        self.seconds = initial_time  # Establecer el tiempo actual del temporizador

    def update_timer(self):
        # Actualizar el temporizador cada segundo
        if self.running:
            minutes, seconds = divmod(self.seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_label.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            if self.seconds <= 0:
                self.running = False
            else:
                self.seconds -= 1
                self.master.after(1000, self.update_timer)

    def start_timer(self):
        # Comenzar el temporizador
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        # Reiniciar el temporizador
        self.running = False
        self.seconds = self.initial_time  # Reiniciar el temporizador al tiempo inicial
        self.timer_label.config(text="00:00:00")  # Restablecer la etiqueta del temporizador

def main():
    root = tk.Tk()

    # Establecer un color de fondo para la ventana principal
    root.configure(bg="white")

    # Configuración de temporizadores
    timer_configs = [
        {"title": "Ifrit", "initial_time": 2400, "bg_image": "Imagenes Secciones\Ifrit.gif"},
        {"title": "Fallen Bishop", "initial_time": 3600, "bg_image": "Imagenes Secciones/Fallen.gif"},
         {"title": "Beelzebub", "initial_time": 3600, "bg_image": "Imagenes Secciones/Fallen.gif"},
        {"title": "Valkyrie Randgris", "initial_time": 3600, "bg_image": "Imagenes Secciones\Valkyrie.gif"},
        {"title": "Dracula", "initial_time": 960, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Doppelganger1", "initial_time": 780, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Doppelganger2", "initial_time": 780, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Baphomet1", "initial_time": 1200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Baphomet2", "initial_time": 1200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "DarkLord1", "initial_time": 1200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "DarkLord2", "initial_time": 1200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Amon Ra", "initial_time": 3600, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Detale", "initial_time": 900, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Drake", "initial_time": 7200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Eddga1", "initial_time": 900, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Eddga2", "initial_time": 900, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Evil Snake Lord", "initial_time": 1140, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Gloom Under Night", "initial_time": 7200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Moonlight Flower", "initial_time": 1140, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        
        {"title": "Turtle General", "initial_time": 1020, "bg_image": "Imagenes Secciones\Ifrit.gif"},
        {"title": "Tao Gunka", "initial_time": 4800, "bg_image": "Imagenes Secciones/Fallen.gif"},
        {"title": "Vesper", "initial_time": 3600, "bg_image": "Imagenes Secciones\Valkyrie.gif"},
        {"title": "AtroceRachel1", "initial_time": 22200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "AtroceRachel2", "initial_time": 11400, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "AtroceICEDUEGON1", "initial_time": 18600, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "AtroceICEDUEGON2", "initial_time": 11400, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "AtroceICEDUEGON3", "initial_time": 15000, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "RSX-0806", "initial_time": 1020, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Maya", "initial_time": 4800, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Garm", "initial_time": 3000, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Stormy Knight", "initial_time": 1080, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Wounded Morroc", "initial_time": 43200, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Mistress", "initial_time": 7800, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Orc Lord", "initial_time": 2400, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Orc Hero", "initial_time": 1020, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Golden Thifer Bug", "initial_time": 1800, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        {"title": "Incarnation Samurai", "initial_time": 6600, "bg_image": "Imagenes Secciones/RO_DarkLord.webp"},
        
        # Agrega más configuraciones aquí según sea necesario
    ]

    # Crear instancias de TimerApp para cada configuración
    row = 0
    column = 0
    for config in timer_configs:
        app = TimerApp(root, config["title"], config["initial_time"], config["bg_image"], row, column)
        column += 1
        if column % 8 == 0:
            row += 1
            column = 0

     # Configurar el manejador para el evento WM_DELETE_WINDOW
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    root.mainloop()

if __name__ == "__main__":
    main()

input("Presiona Enter para salir...")