# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "log_viewer.py" program of Project
# of Programming Principles in Semester 1, 2022.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.

# Import the required modules.
import tkinter as tk
from tkinter import ttk
import json # Used to convert between JSON-formatted text and Python variables.
from tkinter import messagebox
class ProgramGUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}
        try:
            with open("log.txt") as f:
                self.json_data = json.load(f)
        except:
              messagebox.showerror("Error","Missing/Invalid file!")
              quit()
        self.currentindex=0
        self.maxlength=len(self.json_data)
        if(self.maxlength==0):
            messagebox.showerror("Error","Missing/Invalid file!")
            quit()
        self.logcount=str(self.currentindex+1)+"/"+str(self.maxlength)
        self.current_letters=",".join(self.json_data[self.currentindex]['letters'])
        self.current_words=",".join(self.json_data[self.currentindex]['words'])
        self.current_score=self.json_data[self.currentindex]['score']
        # Letter label
        self.letter_label = ttk.Label(self, text='Letters : ')
        self.letter_label.grid(column=0, row=0, sticky=tk.W, **options)
        # Letter values
        self.letter_values = ttk.Label(self, text=self.current_letters)
        self.letter_values.grid(column=1, row=0, sticky=tk.W, **options)

         # Word label
        self.word_label = ttk.Label(self, text='Words : ')
        self.word_label.grid(column=0, row=1, sticky=tk.W, **options)
         # Word values
        self.word_values = ttk.Label(self, text=self.current_words)
        self.word_values.grid(column=1, row=1, sticky=tk.W, **options)

         # Score label
        self.score_label = ttk.Label(self, text='Score  : ')
        self.score_label.grid(column=0, row=2, sticky=tk.W, **options)
         # Score values
        self.score_values = ttk.Label(self, text=self.current_score)
        self.score_values.grid(column=1, row=2, sticky=tk.W, **options)

        # Previous Button
        self.convert_button = ttk.Button(self, text='Prev')
        self.convert_button['command'] = self.previous_log
        self.convert_button.grid(column=0, row=3, sticky=tk.W, **options)

        #Numbers
        self.log_label = ttk.Label(self, text=self.logcount)
        self.log_label.grid(column=1,row=3, sticky=tk.W, **options)
        
        # Next Button
        self.convert_button = ttk.Button(self, text='Next')
        self.convert_button['command'] = self.next_log
        self.convert_button.grid(column=2, row=3, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def previous_log(self):
        #         # This method is called when the user clicks the "Previous" button.
        try:
            if(self.maxlength==1):
                messagebox.showerror("End of File","No previous log.")
            elif(self.currentindex==0):
                messagebox.showerror("End of File","No previous log.")
            else:
                self.currentindex=self.currentindex-1
                self.letter_values['text'] = ",".join(self.json_data[self.currentindex]['letters'])
                self.word_values['text']=",".join(self.json_data[self.currentindex]['words'])
                self.score_values['text']=self.json_data[self.currentindex]['score']
                self.log_label['text']=str(self.currentindex+1)+"/"+str(self.maxlength)
        except:
             messagebox.showerror("Error","Error Occured!")


    def next_log(self):
         #         # This method is called when the user clicks the "Next" button.
        try:
            if(self.maxlength==1):
                messagebox.showerror("End of File","No next log.")
            elif(self.currentindex==self.maxlength-1):
                messagebox.showerror("End of File","No next log.")
            else:
                self.currentindex=self.currentindex+1
                self.letter_values['text'] = ",".join(self.json_data[self.currentindex]['letters'])
                self.word_values['text']=",".join(self.json_data[self.currentindex]['words'])
                self.score_values['text']=self.json_data[self.currentindex]['score']  
                self.log_label['text']=str(self.currentindex+1)+"/"+str(self.maxlength)
        except:
            messagebox.showerror("Error","Error Occured!")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Word Find Log Viewer')
        self.geometry('500x170')
        self.resizable(True, False)


if __name__ == "__main__":
    app = App()
    ProgramGUI(app)
    app.mainloop()