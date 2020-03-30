from Tkinter import *

class GraphicsGrid():

    global window, sqrt, grid, text1
    sqSize = 100
    gapSize = 5
    topSize = 50
    bottomSize = 50
    
    def __init__(self):
        master = Tk()
        window = Canvas(master, width=self.sqSize*3+self.gapSize*4, height=self.sqSize*3+self.gapSize*4+self.topSize+self.bottomSize)
        window.pack()
        sq1 = window.create_rectangle(self.gapSize, self.topSize+self.gapSize, self.sqSize+self.gapSize, self.topSize+self.sqSize+self.gapSize, fill="light blue", activefill="sky blue", outline="white")
        sq2 = window.create_rectangle(self.sqSize+self.gapSize*2, self.topSize+self.gapSize, self.sqSize*2+self.gapSize*2, self.topSize+self.sqSize+self.gapSize, fill="light blue", activefill="sky blue", outline="white")
        sq3 = window.create_rectangle(self.sqSize*2+self.gapSize*3, self.topSize+self.gapSize, self.sqSize*3+self.gapSize*3, self.topSize+self.sqSize+self.gapSize, fill="light blue", activefill="sky blue", outline="white")
        sq4 = window.create_rectangle(self.gapSize, self.topSize+self.sqSize+self.gapSize*2, self.sqSize+self.gapSize, self.topSize+self.sqSize*2+self.gapSize*2, fill="light blue", activefill="sky blue", outline="white")
        sq5 = window.create_rectangle(self.sqSize+self.gapSize*2, self.topSize+self.sqSize+self.gapSize*2, self.sqSize*2+self.gapSize*2, self.topSize+self.sqSize*2+self.gapSize*2, fill="light blue", activefill="sky blue", outline="white")
        sq6 = window.create_rectangle(self.sqSize*2+self.gapSize*3, self.topSize+self.sqSize+self.gapSize*2, self.sqSize*3+self.gapSize*3, self.topSize+self.sqSize*2+self.gapSize*2, fill="light blue", activefill="sky blue", outline="white")
        sq7 = window.create_rectangle(self.gapSize, self.topSize+self.sqSize*2+self.gapSize*3, self.sqSize+self.gapSize, self.topSize+self.sqSize*3+self.gapSize*3, fill="light blue", activefill="sky blue", outline="white")
        sq8 = window.create_rectangle(self.sqSize+self.gapSize*2, self.topSize+self.sqSize*2+self.gapSize*3, self.sqSize*2+self.gapSize*2, self.topSize+self.sqSize*3+self.gapSize*3, fill="light blue", activefill="sky blue", outline="white")
        sq9 = window.create_rectangle(self.sqSize*2+self.gapSize*3, self.topSize+self.sqSize*2+self.gapSize*3, self.sqSize*3+self.gapSize*3, self.topSize+self.sqSize*3+self.gapSize*3, fill="light blue", activefill="sky blue", outline="white")
        topText = window.create_text(10, 10, anchor="nw", text="Player: X  Computer: O", fill="royal blue", font="avenir")
        newGameText = window.create_text(self.sqSize*3+self.gapSize*3, self.sqSize*3+self.gapSize*4+self.topSize+5, anchor="ne", text="New Game", fill="midnight blue", activefill="slate blue", font="avenir")
        QuitText = window.create_text(self.sqSize*3+self.gapSize*3, self.sqSize*3+self.gapSize*4+self.topSize+21, anchor="ne", text="Quit", fill="midnight blue", activefill="pale violet red", font="avenir")
        """newButton = Rectangle(Point(70, 370), Point(150, 390))
        newButton.draw(window)
        newText = Text(Point(110, 380), 'New Game')
        newText.draw(window)
        quitButton = Rectangle(Point(170, 370), Point(250, 390))
        quitButton.draw(window)
        quitText = Text(Point(210, 380), 'Quit')
        quitText.draw(window)"""
        mainloop()

    def updateDisplay(self):
        print("update")
        
    def endDisplay(self):
        print("end")
        
    def place(self, marker, location):
        print("place")

gg = GraphicsGrid()
