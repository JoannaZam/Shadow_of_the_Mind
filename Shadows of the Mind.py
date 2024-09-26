from tkinter import messagebox
import random
import tkinter as tk
import pygame

class ParanormalGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shadows of the Mind")
        self.current_level = 1
        self.sanity = 100  # Estado mental del jugador, empieza en 100
        self.score = 0
        self.username = ""

# Clase para gestionar la aplicación de juego
class ParanormalGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shadows of the Mind")
        self.current_level = 1
        self.sanity = 100  # Estado mental del jugador, empieza en 100
        self.score = 0
        self.username = ""
        self.setup_main_menu()
        self.root = root
        self.root.title("Juego Paranormal")
        self.root.geometry("800x600")
        self.root.configure(bg="#000000")  # Fondo sólido para toda la ventana

        # Inicializar pygame y el mezclador de sonido
        pygame.init()
        pygame.mixer.init()  # Esto inicializa el módulo de sonido

        # Cargar música de fondo y reproducir en bucle
        pygame.mixer.music.load("terror.mp3")  # Reemplaza con el archivo de música correcto
        pygame.mixer.music.play(-1)  # El -1 indica que la música se reproducirá en bucle
        pygame.mixer.music.set_volume(0.1)  # Establece el volumen al 10%

        # Cargar efectos de sonido para éxito y fallo
        self.success_sound = pygame.mixer.Sound("correct.wav")  # Reemplaza con tu archivo de sonido para éxito
        self.failure_sound = pygame.mixer.Sound("error.wav")  # Reemplaza con tu archivo de sonido para fallo
        self.success_sound.set_volume(0.3)  # Volumen del sonido de éxito al 60%
        self.failure_sound.set_volume(0.3)  # Volumen del sonido de fallo al 60%

    # Configuración del menú principal
    def setup_main_menu(self):
        # Crear el menú principal
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        title = tk.Label(self.menu_frame, text="Shadows of the Mind", font=("Eras Bold ITC", 20))
        title.pack(pady=10)
        subtitle = tk.Label(self.menu_frame, text="¡Un viaje donde tu imaginación cobra vida!", font=("Imprint MT Shadow", 18), fg="black")
        subtitle.pack(pady=5)

        # Botón para ingresar nombre de usuario
        username_button = tk.Button(self.menu_frame, text="Iniciar juego", command=self.get_username)
        username_button.pack(pady=5)

        # Salir
        exit_button = tk.Button(self.menu_frame, text="Salir", command=self.root.quit)
        exit_button.pack(pady=5)

    # Función para obtener el nombre de usuario
    def get_username(self):
        self.menu_frame.pack_forget()  # Ocultar el menú principal
        self.username_frame = tk.Frame(self.root)
        self.username_frame.pack(pady=20)

        label = tk.Label(self.username_frame, text="Ingresa tu nombre de usuario:", font=("Arial", 12))
        label.pack(pady=10)

        self.username_entry = tk.Entry(self.username_frame)
        self.username_entry.pack(pady=5)

        continue_button = tk.Button(self.username_frame, text="Continuar", command=self.set_username)
        continue_button.pack(pady=10)

    # Función para establecer el nombre de usuario
    def set_username(self):
        self.username = self.username_entry.get()
        if not self.username:
            messagebox.showwarning("Advertencia", "¡Debes ingresar un nombre de usuario!")
            return
        self.username_frame.pack_forget()
        self.pre_game_story()

    # Mostrar el cuadro de estado (puntaje y cordura)
    def show_status_frame(self):
        self.status_frame = tk.Frame(self.root)
        self.status_frame.pack(pady=10)

        self.sanity_label = tk.Label(self.status_frame, text=f"Cordura: {self.sanity}", font=("Arial", 12))
        self.sanity_label.pack(side="left", padx=10)

        self.score_label = tk.Label(self.status_frame, text=f"Puntaje: {self.score}", font=("Arial", 12))
        self.score_label.pack(side="right", padx=10)

    # Actualizar el cuadro de estado
    def update_game_status(self):
        self.sanity_label.config(text=f"Cordura: {self.sanity}")
        self.score_label.config(text=f"Puntaje: {self.score}")

    # Función para mostrar la historia de introducción
    def pre_game_story(self):
        self.menu_frame.pack_forget()  # Ocultar el menú principal
        self.story_frame = tk.Frame(self.root)
        self.story_frame.pack(pady=20)

        intro = (f"¡Bienvenid@, {self.username}, valiente explorador de lo paranormal!\n\n"
                 "Te han llamado a investigar una casa que tiene más misterios que un rompecabezas de mil piezas.\n"
                 "Los dueños escuchan ruidos extraños por la noche y juran haber visto sombras en los espejos.\n"
                 "Te encuentras justo en la entrada de esta mansión, donde las ventanas parecen ojos que te miran... inquietos.\n\n"
                 "¿Estás list@? Porque no hay vuelta atrás.")
        story_label = tk.Label(self.story_frame, text=intro, font=("Arial", 12))
        story_label.pack(pady=10)

        continue_button = tk.Button(self.story_frame, text="¡Que comience la locura!", command=self.show_instructions)
        continue_button.pack(pady=10)

    # Función para mostrar instrucciones después de la historia
    def show_instructions(self):
        self.story_frame.pack_forget()  # Ocultar la historia
        self.instructions_frame = tk.Frame(self.root)
        self.instructions_frame.pack(pady=20)

        instructions = ("¡Atención, intrépido aventurero!\n\n"
                        "Aquí van las reglas para sobrevivir en este tenebroso viaje:\n\n"
                        "1. Todo es cuestión de tomar decisiones. ¿Sabes esas malas decisiones que te llevan a problemas? ¡Aquí las sentirás!\n\n"
                        "2. Cada elección afecta tu 'estado mental', así que si empiezas a ver cosas raras... ya sabes por qué.\n\n"
                        "3. ¡Sorpresas inesperadas garantizadas! Ten los nervios de acero porque el suspenso no te dará tregua.\n\n"
                        "4. El objetivo: resolver el misterio antes de que tu 'cordura' se derrumbe y te conviertas en un desastre emocional.")
        instructions_label = tk.Label(self.instructions_frame, text=instructions, font=("Arial", 12))
        instructions_label.pack(pady=10)

        start_button = tk.Button(self.instructions_frame, text="Iniciar Aventura", command=self.start_game)
        start_button.pack(pady=10)

    # Función para comenzar el juego
    def start_game(self):
        self.instructions_frame.pack_forget()  # Ocultar las instrucciones
        self.current_level = 1
        self.sanity = 100
        self.score = 0

        # Mostrar el cuadro de estado al iniciar el juego
        self.show_status_frame()

        self.play_level()

    # Función para mostrar el puntaje actual
    def show_score(self):
        messagebox.showinfo("Puntaje", f"¡Buen trabajo, {self.username}! Nivel alcanzado: {self.current_level}\n"
                                       f"Cordura actual: {self.sanity}\n\n"
                                       f"Puntaje total: {self.score}\n\n ¿ya escuchas voces?\n\n")


    # Función para avanzar al siguiente nivel
    def play_level(self):
        if self.sanity <= 5:
            messagebox.showinfo("Fin del Juego", "Te has vuelto loco y has perdido tu sentido de la realidad!")
            self.end_game()
            return

        if self.current_level > 12:
            self.end_game()
            return

        self.level_frame = tk.Frame(self.root)
        self.level_frame.pack(pady=20)

        # Descripción del nivel actual con variaciones
        level_descriptions = {
            1: "Nivel 1: Te encuentras en la entrada de la casa. Todo está en calma, pero el aire se siente pesado. ¿Qué harás?",
            2: "Nivel 2: Las luces comienzan a parpadear mientras avanzas por el pasillo. Un susurro te llama desde la oscuridad.",
            3: "Nivel 3: Un espejo antiguo refleja algo que no está en la habitación. Sientes que algo te observa, pero no puedes verlo.",
            4: "Nivel 4: El crujido de la madera bajo tus pies te sigue, aunque no hay nadie detrás. ¿O tal vez sí?",
            5: "Nivel 5: Las sombras en las esquinas parecen moverse, pero cada vez que te giras, desaparecen. Empiezas a dudar de tu percepción.",
            6: "Nivel 6: Un reloj de pared marca una hora incorrecta y deja caer una llave más pequeña.\n\nEncuentras una caja cerrada en la cocina que encaja con la llave, revelando una foto de un ritual en el sótano.",
            7: "Nivel 7: La casa comienza a distorsionarse a medida que te acercas al sótano.\n\nLas paredes parecen moverse, pero logras encontrar una puerta secreta que conduce a la misteriosa habitación del mapa.",
            8: "Nivel 8: La habitación secreta está llena de símbolos antiguos.\n\nEn el centro, encuentras una urna rota y una figura oscura que desaparece rápidamente, dejando una pista final: 'Todo empezó aquí'.",
            9: "Nivel 9: El sótano es oscuro y frío. Encuentras evidencia de un ritual fallido.\n\nUna figura fantasmal se aparece y te revela que la familia hizo un pacto para salvarse, pero algo salió mal.",
            10: "Nivel 10: Las piezas encajan. Descubres que la familia intentó traer de vuelta a un ser querido\n\npero liberaron algo mucho más peligroso. Ahora debes encontrar una salida antes de que la casa colapse.",
            11: "Nivel 11: Usando los objetos y pistas que has encontrado, logras abrir una salida oculta.\n\nLa casa tiembla a tu alrededor mientras los espíritus buscan venganza. Corres hacia la salida, sintiendo el aliento helado de lo desconocido detrás de ti.",
            12: "Nivel 12: Finalmente, logras escapar de la casa. Afuera, la noche parece más oscura de lo normal\n\ny aunque estás libre, una sensación inquietante recorre tu espalda... ¿realmente has escapado?"
        }

        description = tk.Label(self.level_frame, text=level_descriptions.get(self.current_level, "Sigue explorando, pero algo te dice que ya no estás solo..."),
                               font=("Arial", 14))
        description.pack(pady=10)

        # Decisiones ajustadas y divertidas según el nivel
        if self.current_level == 1:
            action_button1 = tk.Button(self.level_frame, text="Toca la puerta con un 'Hola, ¿alguien en casa?'", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Rodea la casa... porque sí, mejor ver todo desde fuera primero.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Entra directamente. ¿Qué podría salir mal?", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 2:
            action_button1 = tk.Button(self.level_frame, text="Investigar el susurro... porque claramente es una gran idea.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame,text="Ignorar el susurro y seguir caminando. Mejor no meterse.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="¡Sal corriendo de ahí como si tu vida dependiera de ello!", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 3:
            action_button1 = tk.Button(self.level_frame, text="Mirar el espejo de cerca. A lo mejor encuentras un reflejo que te guste...", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Dar la espalda al espejo. ¡No te la juegues con cosas raras!",  command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Romper el espejo. ¡No más cosas espeluznantes, aunque sean 7 años de mala suerte!", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 4:
            action_button1 = tk.Button(self.level_frame, text="Detente y escucha el crujido... porque eso es normal, ¿verdad?", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Corre, corre y sigue corriendo. No mires atrás.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Grita '¿Quién anda ahí?', aunque sabes que no hay respuesta buena.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 5:
            action_button1 = tk.Button(self.level_frame,
                                       text="Acércate a las sombras... porque ¿quién no querría saber qué hay allí?",
                                       command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Cierra los ojos y espera que todo desaparezca.",
                                       command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Sal del lugar, sin mirar atrás. Mejor no tentar la suerte.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 6:
            action_button1 = tk.Button(self.level_frame, text="Investigar el reloj de pared. ¿Qué puede salir mal con el tiempo?", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Abrir la caja en la cocina. Quizás haya un tesoro escondido.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Ignorar todo y salir de la cocina. Mejor no tentar al destino.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 7:
            action_button1 = tk.Button(self.level_frame, text="Seguir adelante hacia el sótano, a ver qué hay ahí.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Explorar la puerta secreta. ¿Qué podría ocultar?", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Retroceder y buscar una salida. Mejor prevenir que lamentar.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 8:
            action_button1 = tk.Button(self.level_frame, text="Examinar los símbolos antiguos. Quizás te ayuden a entender el misterio.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Acercarte a la urna rota. ¿Qué puede pasar si la tocas?", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Saltar la habitación y seguir buscando respuestas en otro lugar.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 9:
            action_button1 = tk.Button(self.level_frame, text="Investigar la evidencia del ritual fallido. Tal vez encuentres pistas.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Confrontar a la figura fantasmal. ¿Realmente estás listo para esto?", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Correr hacia la salida. ¡Olvídate de lo que has visto!", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 10:
            action_button1 = tk.Button(self.level_frame,text="Revisar los objetos que encontraste para encontrar el ritual correcto.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Intentar deshacer el pacto, arriesgándote a liberar algo más peligroso.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Buscar una salida rápida. No vale la pena arriesgarse más.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 11:
            action_button1 = tk.Button(self.level_frame, text="Completar el contrarritual con cuidado. Cada detalle cuenta.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Gritar para distraer a los espíritus. Tal vez eso funcione.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Correr hacia la salida antes de que sea demasiado tarde.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

        elif self.current_level == 12:
            action_button1 = tk.Button(self.level_frame, text="Mirar atrás antes de salir. Tal vez veas algo importante.", command=lambda: self.handle_choice(1))
            action_button1.pack(pady=5)

            action_button2 = tk.Button(self.level_frame, text="Seguir corriendo y no mirar atrás. Es mejor dejar todo atrás.", command=lambda: self.handle_choice(2))
            action_button2.pack(pady=5)

            action_button3 = tk.Button(self.level_frame, text="Reflexionar sobre lo que has vivido. Todo ha cambiado.", command=lambda: self.handle_choice(3))
            action_button3.pack(pady=5)

    # Manejo de la elección del jugador
    def handle_choice(self, choice):
        outcome = random.choice([True, False])  # Simulación de éxito o fracaso aleatorio
        if choice == 1:  # Nivel 1
            if outcome:
                messagebox.showinfo("Evento", "Nada inusual sucede... ¡por ahora! Aunque sientes escalofríos.")
                self.score += 10
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "¡Mala elección! Algo raro te sigue y tu estado de estar cuerdo disminuye.")
                self.sanity -= 10
                self.failure_sound.play()

        elif choice == 2:  # Nivel 2
            if outcome:
                messagebox.showinfo("Evento", "Decidiste jugarlo a salvo... esta vez, funcionó.")
                self.score += 5
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "¡Sentiste un toque en el hombro! Tu mente se debilita un poco.")
                self.sanity -= 15
                self.failure_sound.play()

        elif choice == 3:  # Nivel 3
            if outcome:
                messagebox.showinfo("Evento", "¡Audaz! Pero esta vez, la suerte estuvo de tu lado.")
                self.score += 15
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "¡Ay no! Esa valentía te costó caro. Sientes cómo tu sensatez se desvanece.")
                self.sanity -= 20
                self.failure_sound.play()

        elif choice == 4:  # Nivel 4
            if outcome:
                messagebox.showinfo("Evento", "Te detuviste a escuchar... y descubriste un secreto. Aumenta tu puntaje.")
                self.score += 10
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Una sombra se mueve detrás de ti. ¡Tu sensatez disminuye!")
                self.sanity -= 10
                self.failure_sound.play()

        elif choice == 5:  # Nivel 5
            if outcome:
                messagebox.showinfo("Evento", "Te acercaste a las sombras y encontraste un objeto útil. Aumenta tu puntaje.")
                self.score += 15
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Te dio un escalofrío al acercarte. Tu mente se debilita.")
                self.sanity -= 20
                self.failure_sound.play()

        elif choice == 6:  # Nivel 6
            if outcome:
                messagebox.showinfo("Evento", "¡Increíble! Investigaste el reloj y descubriste un secreto escondido. Tu puntaje aumenta.")
                self.score += 10
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Al tocar el reloj, algo extraño sucede... ¡te sientes un poco menos cuerdo!")
                self.sanity -= 10
                self.failure_sound.play()

        elif choice == 7:  # Nivel 7
            if outcome:
                messagebox.showinfo("Evento", "Te adentraste en el sótano y descubriste un pasadizo secreto. Aumenta tu puntaje.")
                self.score += 10
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Una sombra oscura se acerca... ¡tu sensatez se desvanece!")
                self.sanity -= 10
                self.failure_sound.play()

        elif choice == 8:  # Nivel 8
            if outcome:
                messagebox.showinfo("Evento", "Los símbolos antiguos te dan claridad. ¡Tus habilidades de investigación mejoran!")
                self.score += 5
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Un símbolo te lanza una maldición. ¡Ay, qué mala suerte!")
                self.sanity -= 15
                self.failure_sound.play()

        elif choice == 9:  # Nivel 9
            if outcome:
                messagebox.showinfo("Evento", "La evidencia del ritual te guía. Tu valentía te premia.")
                self.score += 15
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Una figura fantasmal aparece y te asusta. ¡Tu mente se debilita!")
                self.sanity -= 20
                self.failure_sound.play()

        elif choice == 10:  # Nivel 10
            if outcome:
                messagebox.showinfo("Evento", "Revisaste los objetos y encontraste la clave del ritual. ¡Bien hecho!")
                self.score += 10
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Deshacer el pacto fue un error. Algo oscuro se libera.")
                self.sanity -= 15
                self.failure_sound.play()

        elif choice == 11:  # Nivel 11
            if outcome:
                messagebox.showinfo("Evento", "¡Lo lograste! Completar el contrarritual te da más poder. Aumenta tu puntaje.")
                self.score += 20
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "El contrarritual falla... ¡y ahora estás atrapado con los espíritus!")
                self.sanity -= 25
                self.failure_sound.play()

        elif choice == 12:  # Nivel 12
            if outcome:
                messagebox.showinfo("Evento", "Miras atrás y ves que los espíritus te agradecen. Aumenta tu puntaje.")
                self.score += 15
                self.success_sound.play()
            else:
                messagebox.showinfo("Evento", "Olvidaste algo importante y ahora sientes la carga de la culpa.")
                self.sanity -= 20
                self.failure_sound.play()

        # Actualizar el estado del juego
        self.update_game_status()

        # Limpiar la pantalla del nivel y continuar
        self.level_frame.pack_forget()
        self.current_level += 1
        self.play_level()

    # Fin del juego
    def end_game(self):
        self.level_frame.pack_forget()
        self.status_frame.pack_forget()  # Ocultar el cuadro de estado
        self.end_frame = tk.Frame(self.root)
        self.end_frame.pack(pady=20)

        end_message = f"¡Felicidades, {self.username}, has completado el juego!\n" if self.sanity > 0 else f"¡{self.username}\n"
        end_label = tk.Label(self.end_frame, text=end_message, font=("Arial", 14))
        end_label.pack(pady=10)

        if self.sanity <= 45:
            messagebox.showinfo(":(", f"Fin del juego\n\n ¡Te has vuelto loc@!\n\n"
                                                 f"Puntaje final: {self.score}")

        show_score_button = tk.Button(self.end_frame, text="Ver Puntaje Final", command=self.show_score)
        show_score_button.pack(pady=10)

        reset_button = tk.Button(self.end_frame, text="Reiniciar Juego", command=self.reset_game)
        reset_button.pack(pady=5)

        exit_button = tk.Button(self.end_frame, text="Salir", command=self.root.quit)
        exit_button.pack(pady=5)

    # Reiniciar el juego
    def reset_game(self):
        self.end_frame.pack_forget()
        self.setup_main_menu()

# Crear la ventana principal
root = tk.Tk()
app = ParanormalGameApp(root)
root.mainloop()

