from time import sleep
import time

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
        self.timee2 = 0
        self.j = 0
        self.trem = {'viajando': False,
         'limite_caixas': 3,
         'caixas': 0,
         'tempo_viagem': 5000,
         'carregando': False,
         'descarregando': False
          }

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

    def carregando(self):
        if deposito.deposito['caixas_no_deposito'] < self.trem['limite_caixas']:
            self.trem['carregando'] = False
        else:
            self.trem['carregando'] = True
        while self.trem['carregando']:
            deposito.deposito['caixas_no_deposito'] -= 1
            self.trem['caixas'] += 1
            print('caixas no deposito:' + str(deposito.deposito['caixas_no_deposito']))
            print('caixas no trem:' + str(self.trem['caixas']))
            sleep(1)
            if self.trem['caixas'] == self.trem['limite_caixas']:
                self.trem['carregando'] = False
                self.trem['viajando_para_B'] = True
                break
                    
            
    def viajando_para_B(self):
        if self.trem['viajando_para_B']:
            self.j = 0
            self.timee2 = 0
            self.timee2 = round(time.time() * 1000)
            print("VIAJANDO PARA B")
            while round(time.time() * 1000) - self.timee2 < self.trem['tempo_viagem']:
                self.j += 1
            
            print("CHEGOU EM B")
            self.trem['descarregando'] = True
            self.trem['viajando_para_B'] = False 
     
     
    def viajando_para_A(self):
        if self.trem['viajando_para_A']:
            self.j = 0
            self.timee2 = 0
            self.timee2 = round(time.time() * 1000)
            print("VIAJANDO PARA A")
            while round(time.time() * 1000) - self.timee2 < self.trem['tempo_viagem']:
                self.j += 1
            
            print("CHEGOU EM A")
            self.trem['carregando'] = True
            self.trem['viajando_para_A'] = False   


    def descarregando(self):
        print(self.trem['caixas'])
        while self.trem['descarregando']:
            if self.trem['caixas'] > 0:
                self.trem['caixas'] -= 1
                
                print("descarregando caixas do trem, caixas:" + str(self.trem['caixas']))
            else:
                self.trem['viajando_para_A'] = True
                self.trem['descarregando'] = False

class Empacotador:
    def __init__(self):
        self.empacotadores = []
        self.timee = 0
        self.k = 0

    def incrementa_empacotador(self):
        if len(self.empacotadores) < 10:
            self.empacotadores.append({'empacotando': False, 'tempo_empacotando': 0})
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

    def empacotando(self, idd):
        if deposito.deposito['caixas_no_deposito'] < deposito.deposito['limite_deposito']:
            self.timee = round(time.time() * 1000)
            self.k = 0
            print("empacotando")
            #print(self.timee)
            while round(time.time() * 1000) - self.timee < self.empacotadores[idd]['tempo_empacotando']:
                self.k += 1
                self.empacotadores[idd]['empacotando'] = True
            if deposito.deposito['caixas_no_deposito'] < deposito.deposito['limite_deposito']:
                while self.empacotadores[idd]['empacotando']:
                    deposito.deposito['caixas_no_deposito'] += 1
                    print("empacotado")
                    print('deposito:' + str(deposito.deposito["caixas_no_deposito"]))
                    self.empacotadores[idd]['empacotando'] = False
        else:
            print("Empacotador"+ str(self.empacotadores[idd]))           


empacotador = Empacotador()
deposito = Deposito()
trem = Trem()



deposito.deposito["caixas_no_deposito"] = 0
deposito.deposito["limite_deposito"] = 10
empacotador.incrementa_empacotador()
empacotador.incrementa_empacotador()
empacotador.incrementa_empacotador()
empacotador.incrementa_empacotador()
empacotador.incrementa_empacotador()
empacotador.empacotadores[0]['tempo_empacotando'] = 5000
empacotador.empacotadores[1]['tempo_empacotando'] = 2000
empacotador.empacotadores[2]['tempo_empacotando'] = 4000
empacotador.empacotadores[3]['tempo_empacotando'] = 9000
empacotador.empacotadores[4]['tempo_empacotando'] = 3000

while True:
    pass
