from main import *
from settings import *
import sys
import threading

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.empacotador, self.trem, self.deposito = Empacotador(), Trem(), Deposito()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "start screen"
        self.mouse = pygame.mouse.get_pos()

    def run(self):
        while self.running:
            if self.state == "start screen":
                self.start_events()
                self.mouse = pygame.mouse.get_pos()
                #print(self.mouse)
                self.start_update()
                self.start_draw()
                print(empacotador.empacotadores)
            elif self.state == "settings":
                self.settings_events()
                #print(self.empacotador.id)
                self.mouse = pygame.mouse.get_pos()
                #print(self.mouse)
                self.settings_update()
                self.settings_draw()
                pass
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

#############################################    HELP FUNCTIONS     ####################################################

    def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0]//2
            pos[1] = pos[1] - text_size[1]//2
        screen.blit(text, pos)


########################################################################################################################

#############################################    SETTINGS FUNCTIONS    #################################################

    def settings_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                ######################## VOLTAR ###########################################
                if 53 <= self.mouse[0] <= 128 and 442 <= self.mouse[1] <= 461:
                    self.state = "start screen"

                ################# LIMITE DE CAIXAS DEPÓSITO ###############################
                if 308 <= self.mouse[0] <= 321 and 84 <= self.mouse[1] <= 94:

                    deposito.decrementa_limite_deposito()

                elif 376 <= self.mouse[0] <= 392 and 76 <= self.mouse[1] <= 97:
                    deposito.incrementa_limite_deposito()

                ################ LIMITE DE CAIXAS TRANSPORTADAS TREM ######################
                elif 308 <= self.mouse[0] <= 321 and 195 <= self.mouse[1] <= 201:
                    trem.decrementa_limite_trem()

                elif 376 <= self.mouse[0] <= 392 and 187 <= self.mouse[1] <= 204:
                    trem.incrementa_limite_trem()


                ################ TEMPO DE VIAGEM ##########################################
                elif 308 <= self.mouse[0] <= 321 and 240 <= self.mouse[1] <= 248:
                    trem.decrementa_tempo_viagem()
                elif 376 <= self.mouse[0] <= 392 and 232 <= self.mouse[1] <= 250:
                    trem.incrementa_tempo_viagem()

                ############### QUANTIDADE DE EMPACOTADORES ###############################
                elif 308 <= self.mouse[0] <= 321 and 330 <= self.mouse[1] <= 337:
                    empacotador.decrementa_empacotador()


                elif 376 <= self.mouse[0] <= 392 and 323 <= self.mouse[1] <= 340:
                    empacotador.incrementa_empacotador()


                ############### TEMPO DE EMPACOTAMENTO ####################################
                elif 441 <= self.mouse[0] <= 451 and 90 <= self.mouse[1] <= 98:
                    empacotador.decrementa_tempo_empacotamento(0)
                elif 480 <= self.mouse[0] <= 494 and 85 <= self.mouse[1] <= 100:
                    empacotador.incrementa_tempo_empacotamento(0)

                elif 520 <= self.mouse[0] <= 530 and 90 <= self.mouse[1] <= 98:
                    empacotador.decrementa_tempo_empacotamento(1)
                elif 560 <= self.mouse[0] <= 574 and 85 <= self.mouse[1] <= 100:
                    empacotador.incrementa_tempo_empacotamento(1)

                elif 600 <= self.mouse[0] <= 609 and 90 <= self.mouse[1] <= 98:
                    empacotador.decrementa_tempo_empacotamento(2)
                elif 640 <= self.mouse[0] <= 654 and 85 <= self.mouse[1] <= 100:
                    empacotador.incrementa_tempo_empacotamento(2)

                elif 440 <= self.mouse[0] <= 451 and 196 <= self.mouse[1] <= 202:
                    empacotador.decrementa_tempo_empacotamento(3)
                elif 480 <= self.mouse[0] <= 494 and 189 <= self.mouse[1] <= 203:
                    empacotador.incrementa_tempo_empacotamento(3)

                elif 521 <= self.mouse[0] <= 529 and 196 <= self.mouse[1] <= 202:
                    empacotador.decrementa_tempo_empacotamento(4)
                elif 561 <= self.mouse[0] <= 573 and 189 <= self.mouse[1] <= 203:
                    empacotador.incrementa_tempo_empacotamento(4)

                elif 601 <= self.mouse[0] <= 609 and 196 <= self.mouse[1] <= 202:
                    empacotador.decrementa_tempo_empacotamento(5)
                elif 641 <= self.mouse[0] <= 653 and 189 <= self.mouse[1] <= 203:
                    empacotador.incrementa_tempo_empacotamento(5)

                elif 441 <= self.mouse[0] <= 449 and 301 <= self.mouse[1] <= 307:
                    empacotador.decrementa_tempo_empacotamento(6)
                elif 481 <= self.mouse[0] <= 494 and 294 <= self.mouse[1] <= 309:
                    empacotador.incrementa_tempo_empacotamento(6)

                elif 521 <= self.mouse[0] <= 529 and 301 <= self.mouse[1] <= 307:
                    empacotador.decrementa_tempo_empacotamento(7)
                elif 561 <= self.mouse[0] <= 573 and 294 <= self.mouse[1] <= 309:
                    empacotador.incrementa_tempo_empacotamento(7)

                elif 601 <= self.mouse[0] <= 609 and 301 <= self.mouse[1] <= 307:
                    empacotador.decrementa_tempo_empacotamento(8)
                elif 641 <= self.mouse[0] <= 653 and 294 <= self.mouse[1] <= 309:
                    empacotador.incrementa_tempo_empacotamento(8)

                elif 441 <= self.mouse[0] <= 449 and 405 <= self.mouse[1] <= 410:
                    empacotador.decrementa_tempo_empacotamento(9)
                elif 481 <= self.mouse[0] <= 494 and 400 <= self.mouse[1] <= 414:
                    empacotador.incrementa_tempo_empacotamento(9)







    def settings_update(self):
        pass

    def settings_draw(self):
        self.screen.fill(BLACK)

        ############################################# DEPÓSITO #########################################################
        self.draw_text("Depósito", self.screen, [WIDTH // 2, HEIGHT - 460], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)

        ############################## QUANTIDADE DE CAIXAS QUE PODEM SER ARMAZENADAS ##################################
        self.draw_text("Limite de Caixas", self.screen, [WIDTH // 2 - 170, HEIGHT - 415], SETTINGS_TEXT_SIZE,
                       (170, 132, 58), START_FONT, centered=True)
        self.draw_text(str(deposito.deposito['limite_deposito']), self.screen, [WIDTH // 2, HEIGHT - 415], START_TEXT_SIZE, (170, 132, 58),
                       START_FONT,
                       centered=True)
        self.draw_text("-", self.screen, [WIDTH // 2 - 35, HEIGHT - 415], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)
        self.draw_text("+", self.screen, [WIDTH // 2 + 35, HEIGHT - 415], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)

        ################################################### TREM #######################################################
        self.draw_text("Trem", self.screen, [WIDTH // 2, HEIGHT - 350], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)

        ################### QUANTIDADE DE CAIXAS QUE DEVEM SER TRANSPORTADAS PELO TREM##################################
        self.draw_text("Limite de Caixas", self.screen, [WIDTH // 2 - 170, HEIGHT - 315],
                       SETTINGS_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text("Transportadas", self.screen, [WIDTH // 2 - 170, HEIGHT - 295],
                       SETTINGS_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text(str(trem.trem['limite_caixas']), self.screen, [WIDTH // 2, HEIGHT - 305], START_TEXT_SIZE, (170, 132, 58),
                       START_FONT,
                       centered=True)
        self.draw_text("-", self.screen, [WIDTH // 2 - 35, HEIGHT - 305], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)
        self.draw_text("+", self.screen, [WIDTH // 2 + 35, HEIGHT - 305], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)

        ################################ TEMPO DE VIAGEM DE A ATÉ B ####################################################
        self.draw_text("Tempo de Viagem", self.screen, [WIDTH // 2 - 170, HEIGHT - 260],
                       SETTINGS_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text(str(trem.trem['tempo_viagem']), self.screen, [WIDTH // 2, HEIGHT - 260], START_TEXT_SIZE, (170, 132, 58),
                       START_FONT,
                       centered=True)
        self.draw_text("-", self.screen, [WIDTH // 2 - 35, HEIGHT - 260], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)
        self.draw_text("+", self.screen, [WIDTH // 2 + 35, HEIGHT - 260], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)

        ################################################### EMPACOTADOR ################################################
        self.draw_text("Empacotador", self.screen, [WIDTH // 2, HEIGHT - 215], START_TEXT_SIZE, (170, 132, 58),
                       START_FONT, centered=True)

        ################################# QUANTIDADE DE EMPACOTADORES ##################################################
        self.draw_text("Empacotadores", self.screen, [WIDTH // 2 - 170, HEIGHT - 170], SETTINGS_TEXT_SIZE,
                       (170, 132, 58), START_FONT, centered=True)
        self.draw_text(str(len(empacotador.empacotadores)), self.screen, [WIDTH // 2, HEIGHT - 170], START_TEXT_SIZE,
                       (170, 132, 58), START_FONT,
                       centered=True)
        self.draw_text("-", self.screen, [WIDTH // 2 - 35, HEIGHT - 170], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)
        self.draw_text("+", self.screen, [WIDTH // 2 + 35, HEIGHT - 170], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)




        ################################ TEMPO DE EMPACOTAMENTO ########################################################
        if len(empacotador.empacotadores) > 0:
            self.screen.blit(EMPACOTADOR_RED, (WIDTH//2 + 65, HEIGHT - 475))
            self.draw_text(str(empacotador.empacotadores[0]['tempo_empacotando']), self.screen, [WIDTH // 2 + 116, HEIGHT - 410],
                           START_TEXT_SIZE,
                           (170, 132, 58), START_FONT,
                           centered=True)
            self.draw_text("-", self.screen, [WIDTH // 2 + 95, HEIGHT - 410], START_TEXT_SIZE, (170, 132, 58),
                           START_FONT,
                           centered=True)
            self.draw_text("+", self.screen, [WIDTH // 2 + 137, HEIGHT - 410], START_TEXT_SIZE, (170, 132, 58),
                           START_FONT,
                           centered=True)

            if len(empacotador.empacotadores) > 1:
                self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 145, HEIGHT - 475))
                self.draw_text(str(empacotador.empacotadores[1]['tempo_empacotando']), self.screen,
                               [WIDTH // 2 + 196, HEIGHT - 410],
                               START_TEXT_SIZE,
                               (170, 132, 58), START_FONT,
                               centered=True)
                self.draw_text("-", self.screen, [WIDTH // 2 + 175, HEIGHT - 410], START_TEXT_SIZE, (170, 132, 58),
                               START_FONT,
                               centered=True)
                self.draw_text("+", self.screen, [WIDTH // 2 + 217, HEIGHT - 410], START_TEXT_SIZE, (170, 132, 58),
                               START_FONT,
                               centered=True)

                if len(empacotador.empacotadores) > 2:
                    self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 225, HEIGHT - 475))
                    self.draw_text(str(empacotador.empacotadores[2]['tempo_empacotando']), self.screen,
                                   [WIDTH // 2 + 276, HEIGHT - 410],
                                   START_TEXT_SIZE,
                                   (170, 132, 58), START_FONT,
                                   centered=True)
                    self.draw_text("-", self.screen, [WIDTH // 2 + 255, HEIGHT - 410], START_TEXT_SIZE, (170, 132, 58),
                                   START_FONT,
                                   centered=True)
                    self.draw_text("+", self.screen, [WIDTH // 2 + 297, HEIGHT - 410], START_TEXT_SIZE, (170, 132, 58),
                                   START_FONT,
                                   centered=True)

                    if len(empacotador.empacotadores) > 3:
                        self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 65, HEIGHT - 370))
                        self.draw_text(str(empacotador.empacotadores[3]['tempo_empacotando']), self.screen,
                                       [WIDTH // 2 + 116, HEIGHT - 305],
                                       START_TEXT_SIZE,
                                       (170, 132, 58), START_FONT,
                                       centered=True)
                        self.draw_text("-", self.screen, [WIDTH // 2 + 95, HEIGHT - 305], START_TEXT_SIZE,
                                       (170, 132, 58),
                                       START_FONT,
                                       centered=True)
                        self.draw_text("+", self.screen, [WIDTH // 2 + 137, HEIGHT - 305], START_TEXT_SIZE,
                                       (170, 132, 58),
                                       START_FONT,
                                       centered=True)

                        if len(empacotador.empacotadores) > 4:
                            self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 145, HEIGHT - 370))
                            self.draw_text(str(empacotador.empacotadores[4]['tempo_empacotando']), self.screen,
                                           [WIDTH // 2 + 196, HEIGHT - 305],
                                           START_TEXT_SIZE,
                                           (170, 132, 58), START_FONT,
                                           centered=True)
                            self.draw_text("-", self.screen, [WIDTH // 2 + 175, HEIGHT - 305], START_TEXT_SIZE,
                                           (170, 132, 58),
                                           START_FONT,
                                           centered=True)
                            self.draw_text("+", self.screen, [WIDTH // 2 + 217, HEIGHT - 305], START_TEXT_SIZE,
                                           (170, 132, 58),
                                           START_FONT,
                                           centered=True)
                            if len(empacotador.empacotadores) > 5:
                                self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 225, HEIGHT - 370))
                                self.draw_text(str(empacotador.empacotadores[5]['tempo_empacotando']), self.screen,
                                               [WIDTH // 2 + 276, HEIGHT - 305],
                                               START_TEXT_SIZE,
                                               (170, 132, 58), START_FONT,
                                               centered=True)
                                self.draw_text("-", self.screen, [WIDTH // 2 + 255, HEIGHT - 305], START_TEXT_SIZE,
                                               (170, 132, 58),
                                               START_FONT,
                                               centered=True)
                                self.draw_text("+", self.screen, [WIDTH // 2 + 297, HEIGHT - 305], START_TEXT_SIZE,
                                               (170, 132, 58),
                                               START_FONT,
                                               centered=True)
                                if len(empacotador.empacotadores) > 6:
                                    self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 65, HEIGHT - 265))
                                    self.draw_text(str(empacotador.empacotadores[6]['tempo_empacotando']), self.screen,
                                                   [WIDTH // 2 + 116, HEIGHT - 200],
                                                   START_TEXT_SIZE,
                                                   (170, 132, 58), START_FONT,
                                                   centered=True)
                                    self.draw_text("-", self.screen, [WIDTH // 2 + 95, HEIGHT - 200], START_TEXT_SIZE,
                                                   (170, 132, 58),
                                                   START_FONT,
                                                   centered=True)
                                    self.draw_text("+", self.screen, [WIDTH // 2 + 137, HEIGHT - 200], START_TEXT_SIZE,
                                                   (170, 132, 58),
                                                   START_FONT,
                                                   centered=True)
                                    if len(empacotador.empacotadores) > 7:
                                        self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 145, HEIGHT - 265))
                                        self.draw_text(str(empacotador.empacotadores[7]['tempo_empacotando']),
                                                       self.screen,
                                                       [WIDTH // 2 + 196, HEIGHT - 200],
                                                       START_TEXT_SIZE,
                                                       (170, 132, 58), START_FONT,
                                                       centered=True)
                                        self.draw_text("-", self.screen, [WIDTH // 2 + 175, HEIGHT - 200],
                                                       START_TEXT_SIZE,
                                                       (170, 132, 58),
                                                       START_FONT,
                                                       centered=True)
                                        self.draw_text("+", self.screen, [WIDTH // 2 + 217, HEIGHT - 200],
                                                       START_TEXT_SIZE,
                                                       (170, 132, 58),
                                                       START_FONT,
                                                       centered=True)
                                        if len(empacotador.empacotadores) > 8:
                                            self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 225, HEIGHT - 265))
                                            self.draw_text(str(empacotador.empacotadores[8]['tempo_empacotando']),
                                                           self.screen,
                                                           [WIDTH // 2 + 276, HEIGHT - 200],
                                                           START_TEXT_SIZE,
                                                           (170, 132, 58), START_FONT,
                                                           centered=True)
                                            self.draw_text("-", self.screen, [WIDTH // 2 + 255, HEIGHT - 200],
                                                           START_TEXT_SIZE,
                                                           (170, 132, 58),
                                                           START_FONT,
                                                           centered=True)
                                            self.draw_text("+", self.screen, [WIDTH // 2 + 297, HEIGHT - 200],
                                                           START_TEXT_SIZE,
                                                           (170, 132, 58),
                                                           START_FONT,
                                                           centered=True)
                                            if len(empacotador.empacotadores) > 9:
                                                self.screen.blit(EMPACOTADOR_RED, (WIDTH // 2 + 65, HEIGHT - 160))
                                                self.draw_text(str(empacotador.empacotadores[9]['tempo_empacotando']),
                                                               self.screen,
                                                               [WIDTH // 2 + 116, HEIGHT - 95],
                                                               START_TEXT_SIZE,
                                                               (170, 132, 58), START_FONT,
                                                               centered=True)
                                                self.draw_text("-", self.screen, [WIDTH // 2 + 95, HEIGHT - 95],
                                                               START_TEXT_SIZE,
                                                               (170, 132, 58),
                                                               START_FONT,
                                                               centered=True)
                                                self.draw_text("+", self.screen, [WIDTH // 2 + 137, HEIGHT - 95],
                                                               START_TEXT_SIZE,
                                                               (170, 132, 58),
                                                               START_FONT,
                                                               centered=True)


        self.draw_text("Voltar", self.screen, [WIDTH // 2 - 260, HEIGHT - 50], START_TEXT_SIZE - 3, (170, 132, 58),
                       START_FONT, centered=True)

        pygame.display.update()

########################################################################################################################

#############################################    INTRO FUNCTIONS    ####################################################


    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 256 <= self.mouse[0] <= 441 and 241 <= self.mouse[1] <= 261:
                    pass
                elif 295 <= self.mouse[0] <= 405 and 291 <= self.mouse[1] <= 312:
                    self.state = "settings"



    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text("Start Process", self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)
        self.draw_text("Settings", self.screen, [WIDTH//2, HEIGHT//2 + 50], START_TEXT_SIZE, (170, 132, 58), START_FONT,
                       centered=True)
        pygame.display.update()


app = App()
app.run()