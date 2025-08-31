from carro import Carro
from moto import Moto

carro1 = Carro('Ford', 'Focus', True, 5, 'Verde')
carro2 = Carro('Toyota', 'Corolla', False, 4, 'Preto')
moto1 = Moto('Honda', 'CD 179 Titan', True, 'Esportivo')
carro1.ligar()
moto1.ligar()

print(carro1)
print(carro2)
print(moto1)
