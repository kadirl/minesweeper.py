import pygame
import random
from assets import *

class Cell:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.mine = False
        self.revealed = False ####
        self.flagged = False
        self.neighbors = -1
        self.lost = False ######
        self.font = None

    def scale_sprite(self, sprite, size):
        return pygame.transform.scale(sprite, size)

    def make_mine(self):
        self.mine = True

    def is_mine(self):
        return self.mine

    def reveal(self):
        self.revealed = True
        if self.mine:
            self.lost = True
        return self.mine

    def flag(self):
        self.flagged = True

    def unflag(self):
        self.flagged = False 

    def draw_neighbours(self, surface, size):
        font = pygame.font.Font(FONT, int(size//1.5))
        text_surface = font.render(str(self.neighbors), True, NUMBER_COLOR[self.neighbors])
        text_rect = text_surface.get_rect(center=(size // 2, size // 2))
        surface.blit(text_surface, text_rect)

    def render(self):
        cell_surface = pygame.Surface((self.size, self.size))
        cell_surface.fill((255, 0, 0))

        if not self.lost:
            if self.revealed:
                cell_surface.blit(self.scale_sprite(REVEALED_CELL, (self.size, self.size)), (0, 0))
                if self.neighbors > 0:
                    self.draw_neighbours(cell_surface, self.size)
            else:
                cell_surface.blit(self.scale_sprite(UNREVEALED_CELL, (self.size, self.size)), (0, 0))
                if self.flagged:
                    cell_surface.blit(self.scale_sprite(FLAG, (self.size, self.size)), (0, 0))
        else:
            if self.mine:
                if self.flagged:
                    cell_surface.blit(self.scale_sprite(UNREVEALED_CELL, (self.size, self.size)), (0, 0))
                    cell_surface.blit(self.scale_sprite(FLAG, (self.size, self.size)), (0, 0))
                elif self.revealed:
                    cell_surface.blit(self.scale_sprite(BOMB_CELL, (self.size, self.size)), (0, 0))
                    cell_surface.blit(self.scale_sprite(MINE, (self.size, self.size)), (0, 0))
                else:
                    cell_surface.blit(self.scale_sprite(REVEALED_CELL, (self.size, self.size)), (0, 0))
                    cell_surface.blit(self.scale_sprite(MINE, (self.size, self.size)), (0, 0))

            elif self.flagged:
                cell_surface.blit(self.scale_sprite(REVEALED_CELL, (self.size, self.size)), (0, 0))
                cell_surface.blit(self.scale_sprite(CROSSED_MINE, (self.size, self.size)), (0, 0))

            elif self.revealed:
                cell_surface.blit(self.scale_sprite(REVEALED_CELL, (self.size, self.size)), (0, 0))
                if self.neighbors > 0:
                    self.draw_neighbours(cell_surface, self.size)
            else:
                cell_surface.blit(self.scale_sprite(UNREVEALED_CELL, (self.size, self.size)), (0, 0))
        
        return cell_surface



class Minefield:
    def __init__(self, rows, cols, mines_count, cell_size):
        self.rows = rows
        self.cols = cols
        self.surface_width = cell_size * cols
        self.surface_height = cell_size * rows
        self.mines_count = mines_count
        self.cell_size = cell_size
        self.minefield = []
        self.mines_placed = False
        self.lost = False

    def find_relative_pos(self, pos, screen_size):
        width, height = screen_size
        m_width, m_height = self.surface_width, self.surface_height
        x = width // 2 - m_width // 2
        y = height // 2 - m_height // 2
        return (pos[0] - x, pos[1] - y)

    def generate_field(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(Cell(i, j, self.cell_size))
            self.minefield.append(row)

    def place_mines(self, row, col):
        mine_positions = set()

        excluded_positions = set()
        excluded_positions.add((row, col))

        for i in [-1, 0, 1]:
            if row + i < 0 or row + i >= self.rows : continue
            for j in [-1, 0, 1]:
                if col + j < 0 or col + j >= self.cols : continue
                excluded_positions.add((i, j))

        while len(mine_positions) < self.mines_count:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            if (row, col) not in excluded_positions:
                mine_positions.add((row, col))

        for position in mine_positions:
            row, col = position
            self.minefield[row][col].make_mine()

    def calculate_field(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.minefield[i][j].is_mine():
                    count = 0
                    for x in [-1, 0, 1]:
                        if i + x < 0 or i + x >= self.rows:
                            continue
                        for y in [-1, 0, 1]:
                            if j + y < 0 or j + y >= self.cols:
                                continue
                            if self.minefield[i + x][j + y].is_mine():
                                count += 1
                    self.minefield[i][j].neighbors = count

    def reveal_neighbour_cells(self, row, col, first=False):
        print("reveled", row, col)
        cell = self.minefield[row][col]
        if not first:
            if cell.revealed or cell.flagged:
                return

        cell.reveal()
        print(cell.neighbors)
        if cell.neighbors == 0:
            for i in [-1, 0, 1]:
                if row + i < 0 or row + i >= self.rows:
                    continue
                for j in [-1, 0, 1]:
                    if col + j < 0 or col + j >= self.cols:
                        continue
                    print("neighbour", row + i, col + j)
                    self.reveal_neighbour_cells(row + i, col + j)

    def reveal_cell(self, mouse_pos, screen_size):
        x, y = self.find_relative_pos(mouse_pos, screen_size)
        col = x // self.cell_size
        row = y // self.cell_size
        cell = self.minefield[row][col]

        if not cell.revealed and not cell.flagged:
            if not self.mines_placed:
                self.place_mines(row, col)
                self.calculate_field()
                self.mines_placed = True
                return
            
            if cell.reveal():
                print("lost")
                self.game_lost()
                return #####
            
            self.reveal_neighbour_cells(row, col, first=True)


    def flag_cell(self, mouse_pos, screen_size):
        x, y = self.find_relative_pos(mouse_pos, screen_size)

        col = x // self.cell_size
        row = y // self.cell_size

        print("cell flagged", mouse_pos, x, y)

        if not self.minefield[row][col].revealed:
            if self.minefield[row][col].flagged:
                self.minefield[row][col].unflag()
            else:
                self.minefield[row][col].flag()

    def game_lost(self):
        self.lost = True

        for row in self.minefield:
            for cell in row:
                cell.lost = True

    def render(self):
        field_surface = pygame.Surface((self.surface_width, self.surface_height))
        field_surface.fill(BACKGROUND)

        for i, row in enumerate(self.minefield):
            for j, cell in enumerate(row):
                cell_image = cell.render()
                cell_x = j * self.cell_size
                cell_y = i * self.cell_size
                field_surface.blit(cell_image, (cell_x, cell_y))

        return field_surface