from graphics import GraphWin, Point, Rectangle, Line, Text
#from Tkinter import *

class GraphicsGrid():

    global window, sqrt, grid, text1
    
    def __init__(self):
        window = GraphWin("TicTacToe", 320, 400)
        sqr = Rectangle(Point(10, 50), Point(310, 350))
        sqr.draw(window)
        line1 = Line(Point(10, 150), Point(310, 150))
        line2 = Line(Point(10, 250), Point(310, 250))
        line3 = Line(Point(110, 50), Point(110, 350))
        line4 = Line(Point(210, 50), Point(210, 350))
        grid = [line1, line2, line3, line4]
        for line in grid:
            line.draw(window)
        text1 = Text(Point(160, 25), 'Player: X   Computer: O\nPlayer\'s turn!')
        text1.draw(window)
        newButton = Rectangle(Point(70, 370), Point(150, 390))
        newButton.draw(window)
        newText = Text(Point(110, 380), 'New Game')
        newText.draw(window)
        quitButton = Rectangle(Point(170, 370), Point(250, 390))
        quitButton.draw(window)
        quitText = Text(Point(210, 380), 'Quit')
        quitText.draw(window)
        window.getMouse()
        window.close()

    def updateDisplay(self):
        print("update")
        
    def endDisplay(self):
        print("end")
        
    def place(self, marker, location):
        print("place")

gg = GraphicsGrid()
