from email.mime import image
from tkinter import *

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 650

class PlayerInterface:
  def __init__(self):
    self.main_window = Tk()
    self.fill_main_window()
    self.main_window.mainloop()

  def fill_main_window(self):
    self.main_window.title("Queah")
    self.main_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    self.main_window.resizable(False, False)

    self.blue_piece = PhotoImage(file="images/blue_piece.png")
    self.reserve_frame_player1 = Frame(self.main_window)
    self.reserve_frame_player1.grid(row=1, column=0)
    self.reserve_text1 = Label(self.reserve_frame_player1, text=6, font="Arial 30", image=self.blue_piece, compound="center", padx=25)
    self.reserve_text1.grid(row=0, column=0)

    self.table_frame = Frame(self.main_window, pady=50)
    self.table_frame.grid(row=1, column=1)
    self.disable_board_place_image = PhotoImage(file="images/disable_board_place.png")
    self.board_place_image = PhotoImage(file="images/board_place.png")
    self.disable_positions = [(0, 0), (0,1), (1,0), (0,3), (0,4), (1,4), (3,0), (4,0), (4,1), (4,3), (4,4), (3,4)]
    self.board_view = []
    for x in range(5):
      line = []
      for y in range(5):
        place_label = Label(self.table_frame, bd=0)
        if ((x,y) in self.disable_positions):
          place_label.configure(image=self.disable_board_place_image)
        else:
          place_label.configure(image=self.board_place_image)
        place_label.grid(row=x, column=y)
        place_label.bind("<Button-1>", lambda event, place_line=x, place_column=y:self.click(event, place_line, place_column))
        line.append(place_label)
      self.board_view.append(line)
    self.red_piece = PhotoImage(file="images/red_piece.png")
    self.reserve_frame_player2 = Frame(self.main_window, bg="yellow")
    self.reserve_frame_player2.grid(row=1, column=2)
    self.reserve_text2 = Label(self.reserve_frame_player2, text=6, font="Arial 30", image=self.red_piece, compound="center", padx=25)
    self.reserve_text2.grid(row=0, column=0)
  
  def click(self, event, x, y):
    self.board_view[x][y].configure(image=self.red_piece)
    print(f"Click: {x}x{y}")
