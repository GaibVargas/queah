class Posicao:
  def __init__(self, selecionavel, peca = None):
    self.selecionavel = selecionavel
    self.peca = peca
  
  def posicionarPeca(self, peca):
    self.peca = peca

  def posicaoVazia(self):
    if (self.peca == None and self.selecionavel):
      return True
    return False

  def jogadorOcupante(self):
    if (self.peca == None):
      return None
    return self.peca.ocupante()

  def removerPeca(self):
    peca = self.peca
    self.peca = None
    return peca
  
  def obterSelecionavel(self):
    return self.selecionavel