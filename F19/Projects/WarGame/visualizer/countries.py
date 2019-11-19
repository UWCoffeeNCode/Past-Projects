from visualizer.country import Country


import math


TAU = math.pi * 2


class Countries:
    def __init__(self, game_countries, WIDTH, HEIGHT):
        self.countries = []
        country_count = len(game_countries)

        for i, c in enumerate(game_countries):
            perc = (math.sin(i * TAU / country_count) / 2 + 1/2)
            x = (0.1 + 0.8 * perc) * WIDTH

            perc = (math.cos(i * TAU / country_count) / 2 + 1/2)
            y = (0.15 + 0.75 * perc) * HEIGHT

            self.countries.append(Country(c, (x, y)))

    def draw(self, window):
        # Draw countries
        for c in self.countries:
            c.draw(window)

    def get_pos(self, i):
        return self.countries[i].border.center
