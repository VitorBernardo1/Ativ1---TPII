from abc import ABC, abstractmethod

# --- PRODUTOS ABSTRATOS ---

class VeiculoTerrestre(ABC):
    @abstractmethod
    def dirigir(self):
        pass

class VeiculoAereo(ABC):
    @abstractmethod
    def voar(self):
        pass

# --- PRODUTOS CONCRETOS ---

class Carro(VeiculoTerrestre):
    def dirigir(self):
        return "🚗 Dirigindo um Carro pelas ruas de SP."

class Onibus(VeiculoTerrestre):
    def dirigir(self):
        return "🚌 Conduzindo um Ônibus na faixa exclusiva."

class Aviao(VeiculoAereo):
    def voar(self):
        return "✈️ Avião decolando da pista principal."

class Helicoptero(VeiculoAereo):
    def voar(self):
        return "🚁 Helicóptero iniciando voo vertical."

# --- FÁBRICA ABSTRATA ---

class TransporteFactory(ABC):
    @abstractmethod
    def criar_veiculo_terrestre(self) -> VeiculoTerrestre:
        pass

    @abstractmethod
    def criar_veiculo_aereo(self) -> VeiculoAereo:
        pass

# --- FÁBRICAS CONCRETAS ---

class TransporteTerrestreFactory(TransporteFactory):
    def criar_veiculo_terrestre(self):
        return Carro() # Poderia alternar entre Carro ou Onibus conforme a lógica

    def criar_veiculo_aereo(self):
        return None  # Modalidade terrestre não cria veículos aéreos

class TransporteAereoFactory(TransporteFactory):
    def criar_veiculo_terrestre(self):
        return None

    def criar_veiculo_aereo(self):
        return Aviao()

# --- CÓDIGO DO CLIENTE ---

def executar_app(factory: TransporteFactory):
    terrestre = factory.criar_veiculo_terrestre()
    aereo = factory.criar_veiculo_aereo()

    if terrestre:
        print(terrestre.dirigir())
    if aereo:
        print(aereo.voar())

# Testando o sistema
print("--- Usuário escolheu Terrestre ---")
executar_app(TransporteTerrestreFactory())

print("\n--- Usuário escolheu Aéreo ---")
executar_app(TransporteAereoFactory())