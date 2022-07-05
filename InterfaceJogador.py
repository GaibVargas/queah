from tkinter import *
from Jogador import Jogador

from Tabuleiro import Tabuleiro

LARGURA_JANELA = 746
ALTURA_JANELA = 650

class InterfaceJogador:
  def __init__(self):
    self.janela_principal = Tk()
    self.tabuleiro = Tabuleiro(Jogador(), Jogador())
    self.fill_main_window()
    self.janela_principal.mainloop()

  def fill_main_window(self):
    self.janela_principal.title("Queah")
    self.janela_principal.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}")
    self.janela_principal.resizable(False, False)
    self.turn = True

    self.imagem_posicao_desabilitada = PhotoImage(file="images/disable_board_place.png")
    self.imagem_posicao = PhotoImage(file="images/board_place.png")
    self.imagem_peca_azul_tabuleiro = PhotoImage(file="images/blue_piece_board.png")
    self.imagem_peca_vermelha_tabuleiro = PhotoImage(file="images/red_piece_board.png")
    self.imagem_peca_azul = PhotoImage(file="images/blue_piece.png")
    self.imagem_peca_vermelha = PhotoImage(file="images/red_piece.png")

    self.reserva_jogador1 = Frame(self.janela_principal)
    self.reserva_jogador1.grid(row=0, column=0)
    self.reserva_jogador1_texto = Label(self.reserva_jogador1, text=6, font="Arial 30", image=self.imagem_peca_azul, compound="center", padx=20)
    self.reserva_jogador1_texto.grid(row=0, column=0)

    self.reserva_jogador2 = Frame(self.janela_principal, bg="yellow")
    self.reserva_jogador2.grid(row=0, column=2)
    self.reserva_jogador2_texto = Label(self.reserva_jogador2, text=6, font="Arial 30", image=self.imagem_peca_vermelha, compound="center", padx=20)
    self.reserva_jogador2_texto.grid(row=0, column=0)

    self.mensagem_frame = Frame(self.janela_principal)
    self.mensagem_frame.grid(row=1, column=1)
    self.mensagem = Label(self.mensagem_frame, text="Turno do jogador 1", font="Arial, 15")
    self.mensagem.grid(row=0, column=1)

    self.tabuleiro_frame = Frame(self.janela_principal, pady=50)
    self.tabuleiro_frame.grid(row=0, column=1)
    self.posicoes_desabilitadas = [(0, 0), (0,1), (1,0), (0,3), (0,4), (1,4), (3,0), (4,0), (4,1), (4,3), (4,4), (3,4)]
    self.posicoes_iniciais_pecas_vermelhas = [(2, 0), (2, 1), (1, 1), (1, 2)]
    self.posicoes_iniciais_pecas_azuis = [(2, 4), (2, 3), (3, 3), (3, 2)]
    self.posicoes: list[list[Label]] = []

    for x in range(5):
      line = []
      for y in range(5):
        place_label = Label(self.tabuleiro_frame, bd=0)
        if ((x,y) in self.posicoes_desabilitadas):
          place_label.configure(image=self.imagem_posicao_desabilitada)
        else:
          if ((x,y) in self.posicoes_iniciais_pecas_vermelhas):
            place_label.configure(image=self.imagem_peca_vermelha_tabuleiro)
          elif ((x,y) in self.posicoes_iniciais_pecas_azuis):
            place_label.configure(image=self.imagem_peca_azul_tabuleiro)
          else:
            place_label.configure(image=self.imagem_posicao)
        place_label.grid(row=x, column=y)
        place_label.bind("<Button-1>", lambda event, place_line=x, place_column=y:self.click(event, place_line, place_column))
        line.append(place_label)
      self.posicoes.append(line)
  
  def clickIniciar(self):
    pass

  def iniciarGUIJogo(self):
    pass

  def clickReiniciar(self):
    pass

  def atualizarGUI(self):
    pass

  def clickPosicao(self):
    pass

  def click(self, event, x, y):
    print(self.posicoes[x][y]['imag'])
    if ((x,y) not in self.posicoes_desabilitadas):
      image: PhotoImage
      if (self.turn):
        image = self.imagem_peca_vermelha_tabuleiro
      else:
        image = self.imagem_peca_azul_tabuleiro
      self.posicoes[x][y].configure(image=image)
      self.turn = not self.turn
      self.changeMessage()

  def changeMessage(self):
    if (self.turn):
      self.mensagem.configure(text="Turno do jogador 1")
    else:
      self.mensagem.configure(text="Turno do jogador 2")
