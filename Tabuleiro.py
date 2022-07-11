from Posicao import Posicao 
from Peca import Peca

class Tabuleiro:
  def __init__(self, jogador1, jogador2):
    self.jogador1 = jogador1
    self.jogador2 = jogador2
    self.posicoes: list[list[Posicao]] = []

    posicoes_desabilitadas = [(0, 0), (0,1), (1,0), (0,3), (0,4), (1,4), (3,0), (4,0), (4,1), (4,3), (4,4), (3,4)]
    for i in range(5):
      linha = []
      for j in range(5):
        if (i, j) in posicoes_desabilitadas:
          selecionavel = False
        else:
          selecionavel = True
        posicao = Posicao(selecionavel)
        linha.append(posicao)
      self.posicoes.append(linha[:])

  def configuraEstadoInicial(self):
    self.estado = 0
    self.coord_peca_para_mover = []
    self.mensagem = 'Oba oba'
    self.iniciarTabuleiro()
    self.definirVencedor(None)
    self.definirJogadorTurno()

  def iniciarTabuleiro(self):
    posicoes_jogador1 = [(2, 0), (2, 1), (1, 1), (1, 2)]
    posicoes_jogador2 = [(2, 4), (2, 3), (3, 3), (3, 2)]
    for x in range(5):
      for y in range(5):
        posicao = self.recuperarPosicao(x, y)
        if (x, y) in posicoes_jogador1:
          peca = Peca(self.jogador1)
          posicao.posicionarPeca(peca)
        elif (x, y) in posicoes_jogador2:
          peca = Peca(self.jogador2)
          posicao.posicionarPeca(peca)
        else:
          posicao.removerPeca()

  def reiniciar(self):
    self.jogador1.resetarEstado()
    self.jogador2.resetarEstado()
    self.configuraEstadoInicial()

  def selecionarPosicao(self, x, y):
    print(f"{x}, {y}")

  def recuperarPosicao(self, x, y):
    return self.posicoes[x][y]
  
  def selecionarPecaMover(self, x, y, posicao):
    pass

  def selecionarDestino(self, x, y, posicao):
    pass

  def posicionarPecaReserva(self, posicao):
    pass

  def salvarCoordPosicaoSelecionada(self, x, y):
    self.coord_peca_para_mover = [x, y]
  
  def atualizarEstado(self, valor):
    self.estado = valor
  
  def posicaoValidaPosicionarReserva(self, posicao):
    pass

  def definirMensagem(self, mensagem):
    self.mensagem = mensagem
  
  def definirJogadorTurno(self):
    self.turno_jogador = self.jogador1

  def verificarMovimento(self, x, y):
    pass

  def moverPeca(self, x, y):
    pass

  def removerPecaAdversario(self, x, y):
    pass

  def verificarVencedor(self):
    return self.vencedor
  
  def definirVencedor(self, jogador):
    self.vencedor = jogador
  
  def obterTabuleiro(self):
    tabuleiro: list[list[int]] = []
    for i in range(5):
      linha = []
      for j in range(5):
        posicao = self.recuperarPosicao(i, j)
        if not posicao.obterSelecionavel():
          linha.append(0)
        elif posicao.posicaoVazia():
          linha.append(3)
        elif not posicao.posicaoVazia():
          if posicao.jogadorOcupante() == self.jogador1:
            linha.append(1)
          else:
            linha.append(2)
      tabuleiro.append(linha[:])
    return tabuleiro

  def obterMensagem(self):
    return self.mensagem
  
  def obterSaldoReservaJogadores(self):
    return [self.jogador1.obterSaldoReserva(), self.jogador2.obterSaldoReserva()]