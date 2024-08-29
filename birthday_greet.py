import customtkinter as ctk
from tkinter import *
from time import sleep
from PIL import ImageTk, Image, ImageSequence

class HappyBirthday(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("HAPPY BIRTHDAY, GEYSHA!!")
        self.geometry('1200x890')
        self.geometry("+100+0") #position of the frame 

        #for the gif 
        self.gif_frames = [] 
        self.frame_durations = []  
        self.gif_label = None

        bg_color = self.cget('bg')  
        self.canvas = Canvas(self, width=0, height=0, bg=bg_color, highlightthickness=0)
        self.canvas.pack(side=RIGHT, padx=180, pady= 20)  

        self.load_gif()
        self.bday()

    def load_gif(self):
        
        gif = Image.open("images/cat.gif")
        for frame in ImageSequence.Iterator(gif):
            frame = frame.resize((200, 300))  
            self.gif_frames.append(ImageTk.PhotoImage(frame))
            self.frame_durations.append(frame.info.get('duration', 100))  

        # Create a label to display the GIF inside a Canvas
        self.gif_label = ctk.CTkLabel(self.canvas, width=100, height=100, text= '')
        self.gif_label.pack(fill=BOTH, expand=YES)

    def animate_gif(self):
        def update_frame(frame_index=0):

            frame = self.gif_frames[frame_index]
            self.gif_label.configure(image=frame)
            self.update()

            # Setting time for the next frame update
            next_frame = (frame_index + 1) % len(self.gif_frames)
            delay = self.frame_durations[frame_index]
            self.after(delay, update_frame, next_frame)

        update_frame() 

    def pic(self):
        cupcake = PhotoImage(file=r'images/cupcake.png')
        cupcake_pic = ctk.CTkLabel(self, image=cupcake, compound=TOP, anchor=N, text='')
        cupcake_pic.place(x=660, y=5)
        mau = PhotoImage(file=r'images/mau.png')
        mau_pic = ctk.CTkLabel(self, image=mau, compound=TOP, anchor=N, text='')
        mau_pic.place(x=750, y=550)

    def display(self):
        lines = [

            ("\tGREETINGS!!", 0.07, 50),   # 1                                     
            ("HAPPY BIRTHDAY", 0.06, 30),   # 2                            
            ("to you", 0.03, 22),           # 3
            ("and to your family ", 0.05, 20), # 4
            ("\talways remember to love your parents ", 0.04, 30),     # 5
            ("because they are the ones who pregnancy for you ", 0.04, 25), # 6
            ("AND", 0.04, 30),   # 7
            ("always promote ", 0.06, 20), # 8
            ("\tPEACE and ORDER ", 0.09, 22), # 9     
            ("take good care of yourself", 0.05, 26), # 10
            ("\tSTUDY HARD.", 0.06, 45),  # 11
            ("We wish you a.. ", 0.06, 25),  # 12
            ("\tHappy BirthdaAay!", 0.05, 40), # 13
            ("We wish you a..", 0.06, 25), # 14
            ("\tHappy BirthdaAaAaay!!", 0.06, 40), # 15
            ("We wish you a..", 0.06, 25),  # 16
            ("\tHappy BirthdaAaaaAAy!!!", 0.06, 40), # 17
            ("HAPPY BIRTHDAY,", 0.05, 45),  # 18
            ("BIRTHDAY celebraAaaAaAnt!!!", 0.07, 50), # 19
            ("RAAAAWR!!", 0.07, 60)   # 20
        ]

        display_line = [

                        0.09,  # 1
                        0.04,  # 2
                        0.03,  # 3
                        0.06,  # 4
                        0.08,  # 5
                        0.05,  # 6
                        0.01,  # 7
                        0.09,  # 8
                        0.07,  # 9
                        0.08,  # 10
                        0.09,  # 11
                        0.04,  # 12
                        0.05,  # 13
                        0.04,  # 14
                        0.06,  # 15
                        0.05,  # 16
                        0.07,  # 17
                        0.06,  # 18
                        0.09,  # 19
                        0.09   # 20
        ]

        for mau, (line, line_delay, size) in enumerate(lines):
            name = ctk.CTkLabel(self, text='', font=('Georgia', size), anchor="w", justify="left")
            name.pack(pady=2, padx=20, anchor="w")

            for char in line:
                name.configure(text=name.cget('text') + char)
                self.update()
                sleep(line_delay)
            sleep(display_line[mau])

            if mau == 0:  # Show picture and animate gif after the first line
                self.pic()
                self.animate_gif()

    def bday(self):
        self.display()

if __name__ == "__main__":
    bday = HappyBirthday()
    bday.mainloop()
