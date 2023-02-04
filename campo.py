import tkinter as tk

class YuGiOhBattleBoard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Crear un frame para el tablero de batalla
        battle_board_frame = tk.Frame(self)
        battle_board_frame.pack(fill="both", expand=True)

        # Crear los labels para las zonas del tablero
        player_field = tk.Label(battle_board_frame, text="Campo del jugador", bg="lightblue")
        player_field.pack(side="left", fill="both", expand=True)
        opponent_field = tk.Label(battle_board_frame, text="Campo del oponente", bg="lightblue")
        opponent_field.pack(side="right", fill="both", expand=True)
        player_hand = tk.Label(battle_board_frame, text="Mano del jugador", bg="white")
        player_hand.pack(side="bottom", fill="both", expand=True)

if __name__ == "__main__":
    app = YuGiOhBattleBoard()
    app.mainloop()