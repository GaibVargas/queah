from tkinter import *
from Jogador import Jogador

from Tabuleiro import Tabuleiro

LARGURA_JANELA = 746
ALTURA_JANELA = 650

class InterfaceJogador:
  def __init__(self):
    self.janela_principal = Tk()
    self.janela_principal.title("Queah")
    self.janela_principal.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}")
    self.janela_principal.resizable(False, False)

    self.tabuleiro: Tabuleiro
    self.posicoes = []
    self.clickIniciar()
    self.janela_principal.mainloop()
  
  def clickIniciar(self):
    jogador1 = Jogador()
    jogador2 = Jogador()
    self.tabuleiro = Tabuleiro(jogador1, jogador2)
    self.tabuleiro.configuraEstadoInicial()
    self.iniciarGUIJogo()

  def iniciarGUIJogo(self):
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

    self.reserva_jogador2 = Frame(self.janela_principal)
    self.reserva_jogador2.grid(row=0, column=2)
    self.reserva_jogador2_texto = Label(self.reserva_jogador2, text=6, font="Arial 30", image=self.imagem_peca_vermelha, compound="center", padx=20)
    self.reserva_jogador2_texto.grid(row=0, column=0)

    self.mensagem = Label(self.janela_principal, text="Turno do jogador 1", font="Arial, 15", bg="red")
    self.mensagem.grid(row=1, column=1)
    self.botao_reiniciar = Label(self.janela_principal, text="Reiniciar", bg="gray", padx="10", pady="5", font="Arial, 15")
    self.botao_reiniciar.grid(row=1, column=2)
    self.botao_reiniciar.bind("<Button-1>", lambda event:self.clickReiniciar())

    self.tabuleiro_frame = Frame(self.janela_principal, pady=50)
    self.tabuleiro_frame.grid(row=0, column=1)
    self.atualizarGUI()

  def clickReiniciar(self):
    self.tabuleiro.reiniciar()
    self.atualizarGUI()

  def atualizarGUI(self):
    matrizTabuleiro = self.tabuleiro.obterTabuleiro()
    self.mensagem.configure(text=self.tabuleiro.obterMensagem())
    saldos = self.tabuleiro.obterSaldoReservaJogadores()
    self.reserva_jogador1_texto.configure(text=saldos[0])
    self.reserva_jogador2_texto.configure(text=saldos[1])
    imagens = [
      self.imagem_posicao_desabilitada,
      self.imagem_peca_vermelha_tabuleiro,
      self.imagem_peca_azul_tabuleiro,
      self.imagem_posicao
    ]
    for x in range(5):
      for y in range(5):
        place_label = Label(self.tabuleiro_frame, bd=0)
        place_label.configure(image=imagens[matrizTabuleiro[x][y]])
        place_label.grid(row=x, column=y)
        place_label.bind("<Button-1>", lambda event, place_line=x, place_column=y:self.click(place_line, place_column))

  def clickPosicao(self, x, y):
    self.tabuleiro.selecionarPosicao(x, y)
