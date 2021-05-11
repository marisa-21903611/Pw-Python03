class Automovel:
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo
    
    def quantidadeDeCombustivel(self):
        return (self.quantidade)

    def autonomia(self):
        return (self.quantidade * 100) / self.consumo

    def abastece (self, litros):
        self.quantidade += litros
        if (self.quantidade < self.capacidade):
            return ((self.quantidade * 100) / self.consumo)
        elif (self.quantidade > self.capacidade):
            self.quantidade -= litros
            return ("Erro em encher.")
    
    def percorre(self, kms):
        autonomia = ((self.quantidade * 100) / self.consumo)
        numeroKms = autonomia - kms
        if (numeroKms > 0):
            return numeroKms
        else:
            return ("Erro e o trajeto não é efetuado.")


carro = Automovel (60,10,15)
print (carro.quantidadeDeCombustivel())
print (carro.autonomia())
print (carro.abastece(45))
print (carro.abastece(75))
print (carro.percorre(100))
print (carro.percorre(400))