from email.mime import image
import tkinter as Tk
from tkinter import Canvas, ttk
from typing import Text
from PIL import Image, ImageTk
import glob

height = 600 
width = 1000 
images = [Image.open(file) for file in glob.glob('images/*.png')]

d=[]
def printer():
    print(list(set(d)))


def show(event):
    print(event.x,event.y)

class App(Tk.Tk):
    def __init__(self,title):
        super().__init__()
        
        geometry = str(width) + 'x' + str(height)
        self.geometry(geometry)
        self.title(title)
        self.resizable(0,0)
        self.nok=Tk.IntVar()
        self.np=Tk.StringVar()

        self.check= Tk.Checkbutton(variable=self.nok,onvalue = 1, offvalue = 0)
        self.check.pack()
        self.np.set("1/"+str(len(images)))
        self.page =Tk.Label(textvariable=self.np).pack() 
        self.submit=Tk.Button(text="Submit",command=printer)
        self.submit.pack()

        self.bind('<Left>',moveImageLeft)
        self.bind('<Right>',moveImageRight)


class Carousel(Tk.Canvas):
    def __init__(self,master):
        super().__init__()
        self.config(width=width,height=height)
        self.pack()
        self.stitchImages()
        self.showPhoto()
        self.loadIndicator()
        self.current = 1


    def stitchImages(self):
        # Stitch Image
       
        widths, heights = zip(*(i.size for i in images))
        print(len(images))
        total_width = sum(widths)
        max_height = max(heights)
        self.stitched = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for im in images:
          self.stitched.paste(im, (x_offset,0))
          x_offset += im.size[0]
        self.stitched = self.stitched.resize((len(images)*1000,600))
        self.length = len(images)

    def showPhoto(self):
        # Show Stitched Image
        self.stitched = ImageTk.PhotoImage(self.stitched)
        self.Photo = self.create_image((0,0),image=self.stitched,anchor='nw')

    def loadIndicator(self):
        # Indicator
        self.ind = self.create_rectangle(1,590,1000/len(images),600,fill='white',outline='white')
    
       



    def moveImageRight(self):
        global app

        if self.current < len(images):
            for i in range(25):
                self.after(0,self.move(self.Photo,-40,0))
                self.update()
                self.after(1,self.move(self.ind,(1000/len(images))/25,0))
            self.current += 1
        if self.current>=len(images):
            self.current=len(images)
        app.np.set(str(self.current)+"/"+str(len(images)))
        print(d)

       

    def moveImageLeft(self):
        global app
        if self.current > 0:
            for i in range(25):
                self.after(0,self.move(self.Photo,40,0))
                self.after(1,self.move(self.ind,-(1000/len(images))/25,0))
                self.update()
            self.current -= 1
        if self.current<=0:
            self.current=0
        
        app.np.set(str(self.current)+"/"+str(len(images)))

        print(d)

        


car = None

def moveImageRight(event):
    global car
    global app



    if app.nok.get()==1:
        d.append(car.current)
    if app.nok.get()==0:
        if car.current in d:
            d.remove(car.current)

    
    if car.current == len(images):
        print(list(set(d)))
        pass
    else:
        car.moveImageRight()
    
    if car.current not in d:
        app.nok.set(0)
    else:
        app.nok.set(1)
    


def moveImageLeft(event):
    global car
    global app

    if app.nok.get()==1:
        d.append(car.current)
    if app.nok.get()==0:
        if car.current in d:
            d.remove(car.current)
        

    if car.current == 1:
        pass    
    else:
        car.moveImageLeft()

    if car.current not in d:
        app.nok.set(0)
    else:
        app.nok.set(1)
   


def main():
    global car
    global app
    app = App('Carousel')
    car = Carousel(app)
    app.mainloop()

main()