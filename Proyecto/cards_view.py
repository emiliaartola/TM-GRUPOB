import pygame

import constant
from market import Market

class CardView:

    class CardUI:

        def __init__(self, card, pos, cardView):
            self.cardView = cardView
            self.card = card
            self.background_color = constant.COLORS.WHITE
            self.background_color_description = constant.COLORS.GRAY75
            self.title_color = constant.COLORS.BLACK

            self.size = (240, 360)
            self.pos = pos
            self.title = card.name
            self.description = card.description
            self.price = card.price

            self.rect_ui = None

        def draw(self, screen_ref):
            rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
            rectTitle = (self.pos[0]+20, self.pos[1]+50, self.size[0], self.size[1]-20)
            rectDescription = (self.pos[0]+20, self.pos[1]+120, self.size[0]-40, self.size[1]-140)
            marginContainer = 5
            rectDescriptionContainer = (rectDescription[0] - marginContainer, rectDescription[1] - marginContainer,
                                        rectDescription[2] + marginContainer*2, rectDescription[3] + marginContainer*2)
            rectPrice = (self.pos[0]+100, self.pos[1]+10, self.size[0], self.size[1])

            self.rect_ui = pygame.draw.rect(screen_ref, self.background_color, rect, border_radius=10)
            self.rect_ui = pygame.draw.rect(screen_ref, self.background_color_description, rectDescriptionContainer,
                                            border_radius=marginContainer)

            self.cardView.drawText(screen_ref, self.title, constant.COLORS.BLACK, rectTitle, constant.FONTS.TITLE_FONT)
            self.cardView.drawText(screen_ref, self.description, constant.COLORS.BLACK, rectDescription, constant.FONTS.NORMAL_FONT)
            self.cardView.drawText(screen_ref, str(self.price), constant.COLORS.BLUE, rectPrice, constant.FONTS.SUBTITLE_FONT)

        def check_collider(self, point):
            return self.rect_ui.collidepoint(point)

        def click(self):
            self.cardView.market.buy_card(self.card)

    def __init__(self):

        pygame.init()

        screen_size = (800, 600)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("MERCADO DE CARTAS")
        self.menuActive = True

        pygame.display.flip()

        restart_button_size = (155, 45)
        restart_button_pos = (35, 45)
        restart_button_pos2 = (40, 60)
        restart_button_rect = (restart_button_pos[0], restart_button_pos[1], restart_button_size[0], restart_button_size[1])
        self.restart_button = pygame.draw.rect(self.screen, (255, 0, 0), restart_button_rect, border_radius=5)
        restart_label = constant.FONTS.NORMAL_FONT.render('Reiniciar Mercado', True, constant.COLORS.WHITE)
        self.screen.blit(restart_label, restart_button_pos2)

        self.market = Market()
        self.card_ui_list = []


    def draw_market(self):
        self.card_ui_list.clear()
        pygame.draw.rect(self.screen, constant.COLORS.BLACK, (0, 120, 800, 600))
        for i in range(len(self.market.marketCards)):
            card_ui_item = self.CardUI(self.market.marketCards[i], (20 + 260 * i, 120), self)
            card_ui_item.draw(self.screen)
            self.card_ui_list.append(card_ui_item)

        pygame.display.update()


    # para acomodar el texto dentro de cada carta
    def drawText(self, surface, text, color, rect, font, aa=True, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # altura de la fuente
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1
            # determina si la fila está fuera del área
            if y + fontHeight > rect.bottom:
                break

            # determina el ancho maximo de la linea
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # ajustar el texto a la ultima palabra
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # elimina el texto que borramos
            text = text[i:]

        return text



    def draw_card_view(self):
        self.draw_market()

        while self.menuActive:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    #pygame.quit()
                    self.menuActive = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.restart_button.collidepoint(mouse_pos):
                        self.market.prepare_market(3)
                        self.draw_market()
                    for card_ui in self.card_ui_list:
                        if card_ui.check_collider(mouse_pos):
                            card_ui.click()
                            self.draw_market()

#card = CardView()
#card.draw_card_view()