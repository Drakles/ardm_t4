class World:

    def __init__(self, length, height, blocked_tiles, fixed_tiles):
        self.tiles = self.__generate_tiles(length, height, blocked_tiles)
        self.fixed_tiles = fixed_tiles

    def __generate_tiles(self, length, height, blocked_tiles):
        tiles = []
        for i in range(length):
            for j in range(height):
                if (i, j) not in blocked_tiles:
                    tiles.append((i, j))

        return tiles

    def tile_exist(self, position):
        return position in self.tiles
