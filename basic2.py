import tkinter as tk

class YuGiOhBoard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Crear un frame para la sección de reglas del juego
        rules_frame = tk.Frame(self)
        rules_frame.pack(side="left", fill="both", expand=True)

        # Crear un texto con las reglas del juego
        rules_text = tk.Text(rules_frame)
        rules_text.pack(fill="both", expand=True)
        rules_text.insert("1.0", "Reglas del juego de Yu-Gi-Oh!\n\n")
        rules_text.insert("2.0", "1. Cada jugador comienza con 8000 puntos de vida.\n")
        rules_text.insert("3.0", "2. Cada jugador comienza con cinco cartas en su mano.\n")
        rules_text.insert("4.0", "3. Cada jugador puede colocar un número ilimitado de monstruos en el campo.\n")
        rules_text.insert("5.0", "4. Cada jugador puede utilizar un número ilimitado de trampas y magias por turno.\n")
        rules_text.insert("6.0", "5. El objetivo del juego es reducir los puntos de vida del oponente a cero.\n")
        rules_text.config(state="disabled")

if __name__ == "__main__":
    app = YuGiOhBoard()
    app.mainloop()