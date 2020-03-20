from graphics import GraphWin, Point, Rectangle, Line, Text

class GraphicsGrid():

    global window
    
    def initDisplay(self):
        window = GraphWin("TicTacToe", 320, 320)
        pt = Point(10, 10)
        pt.draw(window)
        sqr = Rectangle(pt, Point(310, 310))
        sqr.draw(window)
        line1 = Line(Point(10, 110), Point(310, 110))
        line1.draw(window)
        line2 = Line(Point(10, 210), Point(310, 210))
        line2.draw(window)
        line3 = Line(Point(110, 10), Point(110, 310))
        line3.draw(window)
        line4 = Line(Point(210, 10), Point(210, 310))
        line4.draw(window)
        message = Text(Point(window.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(window)
        window.getMouse()
        window.close()

    def updateDisplay(self):
        print("update")
        
    def endDisplay(self):
        print("end")
        
    def place(self, marker, location):
        print("place")

gg = GraphicsGrid()
gg.initDisplay()
