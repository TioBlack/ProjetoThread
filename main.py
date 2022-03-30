


class Deposito:
    def __init__(self):
        self.deposito = {'limite_deposito': 0, 'caixas_no_deposito': 0}

    def incrementa_limite_deposito(self):
        if self.deposito['limite_deposito'] < 20:
            self.deposito['limite_deposito'] += 1

    def decrementa_limite_deposito(self):
        if self.deposito['limite_deposito'] > 0:
            self.deposito['limite_deposito'] -= 1


class Trem:
    def __init__(self):
        self.N, self.list_N, self.tv = 0, [], 0
        self.trem = {'viajando': False, 'limite_caixas': 0, 'tempo_viagem': 0}

    def incrementa_limite_trem(self):
        if self.trem['limite_caixas'] < 10:
            self.trem['limite_caixas'] += 1


    def decrementa_limite_trem(self):
        if self.trem['limite_caixas'] > 0:
            self.trem['limite_caixas'] -= 1

    def incrementa_tempo_viagem(self):
        if self.trem['tempo_viagem'] < 10:
            self.trem['tempo_viagem'] += 1

    def decrementa_tempo_viagem(self):
        if self.trem['tempo_viagem'] > 0:
            self.trem['tempo_viagem'] -= 1


class Empacotador:
    def __init__(self):
        self.empacotadores, self.te, self.id = [], 0, 0,




    def incrementa_empacotador(self):
        if len(self.empacotadores) < 10:
            self.empacotadores.append({'empacotando': True, 'tempo_empacotando': 0})
            print(self.empacotadores)





    def decrementa_empacotador(self):
        if len(self.empacotadores) > 0:
            self.empacotadores.pop()





    def incrementa_tempo_empacotamento(self, idd):
        self.empacotadores[idd]['tempo_empacotando'] += 1

        print(self.empacotadores)





    def decrementa_tempo_empacotamento(self, idd):
        if self.empacotadores[idd]['tempo_empacotando'] > 0:
            self.empacotadores[idd]['tempo_empacotando'] -= 1

            print(self.empacotadores)


empacotador = Empacotador()
deposito = Deposito()
trem = Trem()
















