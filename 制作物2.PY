import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# 盤面のサイズ
BOARD_SIZE = 8

# 石の状態を表す定数
EMPTY = 0
BLACK = 1
WHITE = 2

# 盤面の初期配置
initial_board = [
    [EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)
]
initial_board[3][3] = WHITE
initial_board[3][4] = BLACK
initial_board[4][3] = BLACK
initial_board[4][4] = WHITE

class ReversiBoard(Gtk.DrawingArea):
    def __init__(self):
        super().__init__()

        self.connect("draw", self.draw_callback)

    def draw_callback(self, widget, cr):
        allocation = self.get_allocation()
        width = allocation.width
        height = allocation.height

        cell_width = width / BOARD_SIZE
        cell_height = height / BOARD_SIZE

        # 盤面を描画
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = col * cell_width
                y = row * cell_height

                # セルの背景を描画
                cr.rectangle(x, y, cell_width, cell_height)
                cr.set_source_rgb(0.2, 0.6, 0.2)
                cr.fill()

                # 石を描画
                if board[row][col] == BLACK:
                    cr.set_source_rgb(0, 0, 0)
                    cr.arc(x + cell_width / 2, y + cell_height / 2, cell_width / 3, 0, 2 * 3.14)
                    cr.fill()
                elif board[row][col] == WHITE:
                    cr.set_source_rgb(1, 1, 1)
                    cr.arc(x + cell_width / 2, y + cell_height / 2, cell_width / 3, 0, 2 * 3.14)
                    cr.fill()

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)

board = initial_board

reversi_board = ReversiBoard()
win.add(reversi_board)

win.show_all()
Gtk.main()