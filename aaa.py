import cairo


board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]


def draw_board(context):
    context.set_source_rgb(1, 1, 1)
    context.paint()
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(5)

   
    for x in range(1, 3):
        context.move_to(x * 100, 0)
        context.line_to(x * 100, 300)
        context.stroke()

  
    for y in range(1, 3):
        context.move_to(0, y * 100)
        context.line_to(300, y * 100)
        context.stroke()

 
    for x in range(3):
        for y in range(3):
            if board[y][x] == 'X':
                draw_x(context, x, y)
            elif board[y][x] == 'O':
                draw_o(context, x, y)


def draw_x(context, x, y):
    context.move_to(x * 100 + 20, y * 100 + 20)
    context.line_to(x * 100 + 80, y * 100 + 80)
    context.move_to(x * 100 + 80, y * 100 + 20)
    context.line_to(x * 100 + 20, y * 100 + 80)
    context.stroke()


def draw_o(context, x, y):
    context.arc(x * 100 + 50, y * 100 + 50, 30, 0, 2 * 3.14)
    context.stroke()


def get_cell(x, y):
    cell_x = x // 100
    cell_y = y // 100
    return cell_x, cell_y


def on_click(x, y):
    cell_x, cell_y = get_cell(x, y)
    if board[cell_y][cell_x] == '':
        board[cell_y][cell_x] = 'X'

        redraw()


def redraw():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 300)
    context = cairo.Context(surface)
    draw_board(context)
    surface.write_to_png("board.png") 


def handle_click_event(widget, event):
    if event.type == cairo.EventType.BUTTON_PRESS:
        on_click(event.x, event.y)


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 300)
context = cairo.Context(surface)
draw_board(context)
surface.write_to_png("board.png")