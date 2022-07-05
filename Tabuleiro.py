class Tabuleiro:
  def __init__(self, jogador1, jogador2):
    self.jogador1 = jogador1
    self.jogador2 = jogador2
    self.posicoes = []
    self.turno_jogador = None
    self.estado = None
    self.coord_peca_para_mover = []
    self.mensagem = ''
    self.vencedor = None
  
  def configuraEstadoInicial(self):
    pass

  def iniciarTabuleiro(self):
    pass

  def reiniciar(self):
    pass

  def selecionarPosicao(self, x, y):
    pass

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
    pass

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
    pass

  def obterMensagem(self):
    return self.mensagem
  
  def obterSaldoReservaJogadores(self):
    return [self.jogador1.obterSaldoReserva(), self.jogador2.obterSaldoReserva()]