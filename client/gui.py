"""
This module contains the tkinter-based
GUI for the application. The interface displays information to the users 
about their chia servers.
"""

import tkinter as tk

class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())


# Create Toplevel widget as root
root = tk.Tk()
root.geometry("500x300")
root.configure(bg='#454648')
# Create frame widget with root as background
myapp = App(root)

# Set Toplevel title
myapp.master.title("My Do-Nothing Application")
# Create 'Quit' button
tk.Button(myapp, text="Quit", command=root.destroy).pack()
# Create print_contents button
tk.Button(myapp, text="Show Contents", command=myapp.print_contents(1)).pack()
# Call mainloop of Tk
myapp.mainloop()
"""
Run Chia, specify number of plots you want
Greg uses a plot manager, configures it to use all the drives you have and press go
It selects drives and plots, spins them up in parallel
swar plot manager
plotting generates log files, Chia and swar have log files
Parsing log files provides information
Lots of different statuses provided from log files
Raspberry Pi - make webserver, have page that can be accessed from personal computer e.g. display time or whatever
Have personal pc parse the log then send back relavent data e.g. how many plots are done
Every Chia harvester has debug log
1 computer hosts full node w/ copy of full blockchain. Each server is a Chia harvester"""