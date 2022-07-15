from random import choice
from Posicao import Posicao 
from Peca import Peca

class Tabuleiro:
  def __init__(self, jogador1, jogador2):
    self.jogador1 = jogador1
    self.jogador2 = jogador2
    self.turno_jogador = None
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
    self.iniciarTabuleiro()
    self.definirVencedor(None)
    self.definirJogadorTurno(reset=True)
    self.mensagem = f'{self.turno_jogador.obterNome()}\n Selecione peça para mover'

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
    posicao = self.recuperarPosicao(x, y)
    valido = posicao.obterSelecionavel()
    if valido:
      if self.estado == 0:
        self.selecionarPecaMover(x, y, posicao)
      elif self.estado == 1:
        self.selecionarDestino(x, y, posicao)
      elif self.estado == 2:
        self.posicionarPecaReserva(posicao)
    else:
      self.definirMensagem(f'Posição inválida.\n Jogador do turno: {self.turno_jogador.obterNome()}')

  def recuperarPosicao(self, x, y):
    return self.posicoes[x][y]
  
  def selecionarPecaMover(self, x, y, posicao: Posicao):
    ocupante = posicao.jogadorOcupante()
    if self.turno_jogador != ocupante or ocupante == None:
      self.definirMensagem(f'Jogada inválida\n {self.turno_jogador.obterNome()}\n Selecione peça para mover')
    else:
      self.salvarCoordPosicaoSelecionada(x, y)
      self.atualizarEstado(1)
      self.definirMensagem(f'{self.turno_jogador.obterNome()}\n Selecione uma posição destino')

  def selecionarDestino(self, x, y, posicao: Posicao):
    vazia = posicao.posicaoVazia()
    if not vazia:
      jogador_ocupante = posicao.jogadorOcupante()
      if jogador_ocupante != self.turno_jogador:
        self.definirMensagem(f'Jogada inválida.\n {self.turno_jogador.obterNome()} escolha uma posição destino')
      else:
        self.salvarCoordPosicaoSelecionada(x, y)
        self.definirMensagem(f'{self.turno_jogador.obterNome()}\n Selecione uma posição destino')
    else:
      tipo_movimento = self.verificarMovimento(x, y)
      if tipo_movimento == 0:
        self.definirMensagem(f'Jogada inválida\n {self.turno_jogador.obterNome()}\n Escolha uma posição destino')
      elif tipo_movimento == 1 or tipo_movimento == 2:
        self.moverPeca(posicao)
        if tipo_movimento == 2:
          self.removerPecaAdversario(x, y)
          vencedor = self.verificarVencedor()
          self.definirVencedor(vencedor)
          if self.vencedor != None:
            self.definirMensagem(f'{self.turno_jogador.obterNome()} venceu!')
            return
          if self.turno_jogador == self.jogador1:
            adversario = self.jogador2
          else:
            adversario = self.jogador1
          saldo_adversario = adversario.obterSaldoReserva()
          self.definirJogadorTurno()
          if saldo_adversario > 0:
            self.atualizarEstado(2)
            self.definirMensagem(f'{self.turno_jogador.obterNome()}\n Selecione posição para repor peça')
          else:
            self.atualizarEstado(0)
            self.definirMensagem(f'{self.turno_jogador.obterNome()}\n Selecione peça para mover')
        else:
          self.definirJogadorTurno()
          self.atualizarEstado(0)
          self.definirMensagem(f'{self.turno_jogador.obterNome()}\n Selecione peça para mover')

  def posicionarPecaReserva(self, posicao: Posicao):
    posicao_valida = posicao.posicaoVazia()
    if not posicao_valida:
      self.definirMensagem(f'Jogada inválida\n{self.turno_jogador.obterNome()}\n Selecione posição para repor peça')
    else:
      peca = Peca(self.turno_jogador)
      posicao.posicionarPeca(peca)
      self.turno_jogador.decrementarSaldoReserva()
      self.turno_jogador.incrementarSaldoTabuleiro()
      self.definirJogadorTurno()
      self.atualizarEstado(0)
      self.definirMensagem(f'{self.turno_jogador.obterNome()}\n Selecione peça para mover')

  def salvarCoordPosicaoSelecionada(self, x, y):
    self.coord_peca_para_mover = [x, y]
  
  def atualizarEstado(self, valor):
    self.estado = valor

  def definirMensagem(self, mensagem):
    self.mensagem = mensagem
  
  def definirJogadorTurno(self, reset = False):
    if reset: # iniciando jogo
      self.turno_jogador = choice([self.jogador1, self.jogador2])
    else: # trocar turno
      if self.turno_jogador == self.jogador2:
        self.turno_jogador = self.jogador1
      else:
        self.turno_jogador = self.jogador2

  def verificarMovimento(self, x, y):
    distancia = abs(x - self.coord_peca_para_mover[0]) + abs(y - self.coord_peca_para_mover[1])
    if distancia == 1:
      return 1
    elif distancia == 2:
      x = x + self.coord_peca_para_mover[0]
      y = y + self.coord_peca_para_mover[1]

      if (x % 2 != 0) or (y % 2 != 0):
        return 0
      else:
        x = x/2
        y = y/2
        posicao_adversario = self.recuperarPosicao(int(x), int(y))
        jogador_ocupante = posicao_adversario.jogadorOcupante()
        if jogador_ocupante == self.turno_jogador or jogador_ocupante == None:
          return 0
        else:
          return 2
    else:
      return 0

  def moverPeca(self, posicao: Posicao):
    posicao_origem = self.recuperarPosicao(self.coord_peca_para_mover[0], self.coord_peca_para_mover[1])
    peca = posicao_origem.removerPeca()
    posicao.posicionarPeca(peca)

  def removerPecaAdversario(self, x, y):
    x = (x + self.coord_peca_para_mover[0])/2
    y = (y + self.coord_peca_para_mover[1])/2
    posicao = self.recuperarPosicao(int(x), int(y))
    adversario = posicao.jogadorOcupante()
    posicao.removerPeca()
    adversario.decrementarSaldoTabuleiro()

  def verificarVencedor(self):
    if self.turno_jogador == self.jogador1:
      jogador_adversario = self.jogador2
    else:
      jogador_adversario = self.jogador1
    saldo_adversario = jogador_adversario.obterSaldoTotal()
    if saldo_adversario == 0:
      return self.turno_jogador
    else:
      return None
  
  def definirVencedor(self, jogador):
    self.vencedor = jogador
  
  def possuiVencedor(self):
    if self.vencedor == None:
      return False
    return True
  
  def obterMatrizTabuleiro(self):
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