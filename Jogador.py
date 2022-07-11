class Jogador:
  def __init__(self):
    self.pecas_reservas = 6
    self.pecas_tabuleiro = 4
  
  def resetarEstado(self):
    self.pecas_reservas = 7 # Só pra brincar
    self.pecas_tabuleiro = 4

  def decrementarSaldoReserva(self):
    self.pecas_reservas -= 1

  def decrementarSaldoTabuleiro(self):
    self.pecas_tabuleiro -= 1

  def obterSaldoTotal(self):
    return self.pecas_reservas + self.pecas_tabuleiro

  def obterSaldoReserva(self):
    return self.pecas_reservas

  def incrementarSaldoTabuleiro(self):
    self.pecas_tabuleiro += 1