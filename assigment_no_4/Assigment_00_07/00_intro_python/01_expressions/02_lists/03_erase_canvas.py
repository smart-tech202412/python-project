from graphics import *
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser, cells):
    """Erase objects (change to white) that intersect with the eraser"""
    ex1 = eraser.getP1().getX()
    ey1 = eraser.getP1().getY()
    ex2 = eraser.getP2().getX()
    ey2 = eraser.getP2().getY()

    for cell in cells:
        cx1 = cell.getP1().getX()
        cy1 = cell.getP1().getY()
        cx2 = cell.getP2().getX()
        cy2 = cell.getP2().getY()

        # Check for overlap
        if not (ex2 < cx1 or ex1 > cx2 or ey2 < cy1 or ey1 > cy2):
            cell.setFill("white")

def main():
    win = GraphWin("Eraser Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    win.setCoords(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
    
    cells = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            cell = Rectangle(Point(col, row), Point(col + CELL_SIZE, row + CELL_SIZE))
            cell.setFill("blue")
            cell.draw(win)
            cells.append(cell)

    # Wait for user click to place eraser
    click_point = win.getMouse()
    eraser = Rectangle(click_point, Point(click_point.getX() + ERASER_SIZE, click_point.getY() + ERASER_SIZE))
    eraser.setFill("pink")
    eraser.draw(win)

    # Real-time erasing
    while True:
        mouse_point = win.checkMouse()
        if mouse_point:
            dx = mouse_point.getX() - eraser.getP1().getX()
            dy = mouse_point.getY() - eraser.getP1().getY()
            eraser.move(dx, dy)
            erase_objects(win, eraser, cells)
        update()
        time.sleep(0.05)

main()
