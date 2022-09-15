from Domain.Entities.Piece import Color


class BoardVisualizer:
    COLORS = {
        Color.WHITE: {
            'description': 'Whites',
            'symbol': 'v'
        },
        Color.BLACK: {
            'description': 'Blacks',
            'symbol': '^'
        },
    }

    def __init__(self):
        pass

    @staticmethod
    def visualize(board, captured_white=None, captured_black=None):
        BoardVisualizer.__print_info(Color.WHITE, captured_white)
        BoardVisualizer.__print_index_row(len(board.get_grid()[0]))
        BoardVisualizer.__print_separator(len(board.get_grid()[0]))
        BoardVisualizer.__print_board_state(board.get_grid())
        BoardVisualizer.__print_separator(len(board.get_grid()[0]))
        BoardVisualizer.__print_info(Color.BLACK, captured_black)

    @staticmethod
    def __print_index_row(number_columns):
        col_indices = '   '
        for i in range(number_columns):
            col_indices += ' ' + str(i) + ' '
        print(col_indices)

    @staticmethod
    def __print_info(color, captured):
        print('============ ' + BoardVisualizer.COLORS[color]['description'] +
              ' (' + BoardVisualizer.COLORS[color]['symbol'] + ') ============'
              )
        print('Captured:')
        print('9:  ', '   '.join([str(x) for x in range(len(captured))]))
        print('    ', '  '.join([piece.to_string() for piece in captured]))

    @staticmethod
    def __print_separator(number_columns):
        print('+ ' + '---' * number_columns + ' +')

    @staticmethod
    def __print_board_state(grid):
        for index, row in enumerate(grid):
            row_string = str(index) + '| '
            for square in row:
                row_string += square.to_string() + ' '
            print(row_string)
