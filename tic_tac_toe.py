import random

import sys

EMPTY_CELL = ' '


class WrongCellError(Exception):
    pass


class Game:
    def __init__(self) -> None:

        self.moves = 9
        self.board = [[EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, ] for _ in range(3)]
        self.user_symbol = self.comp_symbol = None
        self.win_sequence = None
        self.loss_sequence = None
        self.indexes_list = (
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((2, 0), (1, 1), (0, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
        )

    def display_board(self) -> None:
        for row in self.board:
            print(''.join((lambda x: f'[{x}]', row)))  # noqa: T201

    def check_win(self) -> None:
        for indexes in self.indexes_list:
            if [self.board[i[0]][i[1]] for i in indexes] == self.win_sequence:
                self.display_board()
                sys.exit('Поздравляем с победой')
            if [self.board[i[0]][i[1]] for i in indexes] == self.loss_sequence:
                self.display_board()
                sys.exit('Вы проиграли')

    def set_option(self, row: int, column: int, symbol: str) -> None:
        if self.board[row][column] != EMPTY_CELL:
            raise WrongCellError
        self.board[row][column] = symbol
        self.moves -= 1
        if self.moves < 1:
            self.display_board()
            sys.exit('Игра окончена - ничья')

    def get_user_choice(self) -> None:
        while True:
            try:
                row = int(input('Введите номер строки: ')) - 1
                column = int(input('Введите номер столбца: ')) - 1
                self.set_option(row, column, self.user_symbol)  # type: ignore # А как же делать?! В __init__ self.user_symbol = None
                self.check_win()
                break
            except (TypeError, WrongCellError, IndexError, ValueError):
                print('Невалидный ввод!')  # noqa: T201
                self.display_board()

    def comp_choice(self) -> None:
        while True:
            try:
                self.set_option(random.randint(0, 2), random.randint(0, 2), self.comp_symbol)  # noqa: S311
            except WrongCellError:
                pass
            else:
                self.check_win()
                return

    def choice_symbol(self) -> None:
        while True:
            symbol = input('Введите чем хотите ходить Х или 0: ').upper()
            if symbol in ('X', 'O', 'Х', 'О', '0'):
                self.user_symbol, self.comp_symbol = ('X', '0') if symbol in 'XxХх' else ('0', 'X')
                self.win_sequence = [self.user_symbol] * 3
                self.loss_sequence = [self.comp_symbol] * 3
                return

    def run(self) -> None:
        self.choice_symbol()
        while True:
            self.display_board()
            self.get_user_choice()
            self.comp_choice()


if __name__ == '__main__':
    Game().run()
