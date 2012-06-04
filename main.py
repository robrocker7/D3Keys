from Tkinter import *
import ImageTk
import Image

class App:


    def __init__(self, master):
        # VARIABLES
        self.master = master
        self.master.wm_attributes("-topmost", 1)
        self.left_down = False
        self.right_down = False

        # SET TITLE
        self.master.title("Diablo 3 Action Keys")

        # DISABLE RESIZE
        self.master.resizable(0,0)

        # BIND MOUSE
        self.master.bind_all('<Any-ButtonPress>', self.button_press)
        self.master.bind_all('<Any-ButtonRelease>', self.button_release)

        # BIND KEYS
        self.master.bind_all('<Any-KeyPress>', self.key_stroke)
        self.master.bind_all('<Any-KeyRelease>', self.key_release)

        # GATHER IMAGES AND WRITE THEM TO APP
        self.gather_resources() 
        self.write_actionbar()

    def button_press(self, event):
        if(event.num == 1):
            self.left_down = True
        elif(event.num == 2):
            self.right_down = True

        self.update_mouse()

    def button_release(self, event):
        if(event.num == 1):
            self.left_down = False
        elif(event.num == 2):
            self.right_down = False

        self.update_mouse()

    def update_mouse(self):
        if self.left_down and self.right_down:
            self.mouse.configure(image=self.both_mouse_click)
        elif self.left_down and not self.right_down:
            self.mouse.configure(image=self.left_mouse_click)
        elif not self.left_down and self.right_down:
            self.mouse.configure(image=self.right_mouse_click)
        elif not self.left_down and not self.right_down:
            self.mouse.configure(image=self.mouse_image)

    def key_stroke(self, event):
        if(event.char == 'a'):
            self.action_key_1.configure(image=self.action_image_down)
        elif(event.char == 's'):
            self.action_key_2.configure(image=self.action_image_down)
        elif(event.char == 'd'):
            self.action_key_3.configure(image=self.action_image_down)
        elif(event.char == 'f'):
            self.action_key_4.configure(image=self.action_image_down)
        elif(event.char == ' '):
            self.hold_key.configure(image=self.hold_image_down)

    def key_release(self, event):
        if(event.char == 'a'):
            self.action_key_1.configure(image=self.action_image)
        elif(event.char == 's'):
            self.action_key_2.configure(image=self.action_image)
        elif(event.char == 'd'):
            self.action_key_3.configure(image=self.action_image)
        elif(event.char == 'f'):
            self.action_key_4.configure(image=self.action_image)
        elif(event.char == ' '):
            self.hold_key.configure(image=self.hold_image)
    
    def gather_resources(self):

        # ACTION COMMAND IMAGES
        self.action_image = ImageTk.PhotoImage(Image.open('img/Key-64.png'))
        self.action_image_down = ImageTk.PhotoImage(Image.open('img/Key-64-down.png'))
        
        # MOUSE IMAGES
        self.mouse_image = ImageTk.PhotoImage(Image.open('img/Mouse-64.png'))
        self.left_mouse_click = ImageTk.PhotoImage(Image.open('img/Mouse-64-left.png'))
        self.both_mouse_click = ImageTk.PhotoImage(Image.open('img/Mouse-64-both.png'))
        self.right_mouse_click = ImageTk.PhotoImage(Image.open('img/Mouse-64-right.png'))
        
        # HOLD COMMAND IMAGES
        self.hold_image = ImageTk.PhotoImage(Image.open('img/Lock-64.png'))
        self.hold_image_down = ImageTk.PhotoImage(Image.open('img/Lock-64-down.png'))

    def write_actionbar(self):
        
        # ACTION KEY 1
        self.action_key_1 = Label(self.master, image=self.action_image)
        self.action_key_1.pack(side=LEFT)
        
        # ACTION KEY 2
        self.action_key_2 = Label(self.master, image=self.action_image)
        self.action_key_2.pack(side=LEFT)
        
        # ACTION KEY 3
        self.action_key_3 = Label(self.master, image=self.action_image)
        self.action_key_3.pack(side=LEFT)
        
        # ACTION KEY 4
        self.action_key_4 = Label(self.master, image=self.action_image)
        self.action_key_4.pack(side=LEFT)

        # MOUSE
        self.mouse = Label(self.master, image=self.mouse_image)
        self.mouse.pack(side=LEFT)

        # HOLD
        self.hold_key = Label(self.master, image=self.hold_image)
        self.hold_key.pack(side=LEFT)

if __name__ == '__main__':

    root = Tk()
    app = App(root)
    root.mainloop()
