class Card:
    last_id = 0

    def __init__(self, price, name, description, image):
        Card.last_id += 1
        self.id = Card.last_id
        self.price = int(price)
        self.name = name
        self.description = description
        self.image = image
        self.used = False

    def action(self):
        self.used = True

    @staticmethod
    def create_cards():
        kot_cards = []
        kot_cards.extend([
            Card(4, 'Más vida', 'Tu vida máxima se incrementa en 2 y ganas 2 de vida', ''),
            Card(5, 'Vida', 'Recuperas 4 de vida', ''),
            Card(3, 'Vida', 'Recuperas 2 de vida', ''),

            Card(4, 'Muerte y recompensa', 'Si alguien muere ganas 3 puntos de victoria', ''),
            Card(8, 'Victoria', 'Ganas 3 puntos de victoria inmediatamente', ''),
            Card(5, 'Victoria', 'Ganás 2 puntos de victoria y entrás en Tokyo ', ''),
            Card(2, 'Victoria', 'Ganas 1 punto de victoria', ''),

            Card(4, 'Daño', 'Le haces 2 de daño a tus oponentes', ''),
            Card(9, 'Fatality', 'le infliges 5 de daño a un oponente a elección', ''),
            Card(8, 'Daño', 'Haces 2 daños adicionales cada turno hasta el final del juego', ''),
            Card(6, 'Daño', 'Haces 1 daño adicional cada turno hasta el final del juego', ''),

            Card(6, 'Energía', 'Ganas 1 de energía adicional cada ronda', ''),
            Card(4, 'Energía', 'Compras 6 energías', ''),
            Card(8, 'Name', 'Expulsas al mounstruo que se encuentre en tokyo', ''),
            Card(3, 'Name', 'c12', ''),
            Card(4, 'M', 'c13', ''),
            Card(4, 'M', 'c14', ''),
            Card(4, 'M', 'c15', ''),
            Card(4, 'M', 'c16', ''),
            Card(4, 'M', 'c17', '')])
        return kot_cards
