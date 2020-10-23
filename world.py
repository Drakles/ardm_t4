class World:

    def __init__(self, length, height, blocked_tiles, fixed_tiles):
        self.titles = self.__generate_titles(length,height, blocked_tiles)
        self.fixed_tiles = fixed_tiles

    def __generate_titles(self, length,height, blocked_tiles):
        titles = []
        for i in range(length):
            for j in range(height):
                if (i, j) not in blocked_tiles:
                    titles.append((i, j))

        return titles

    def title_exist(self, position):
        return position in self.titles
