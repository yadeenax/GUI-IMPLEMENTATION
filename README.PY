# GUI-IMPLEMENTATION
GRAPHICAL USER INTERFACE
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My GUI")

# Create a button and a label
button = tk.Button(window, text="Click me")
label = tk.Label(window, text="Hello, World!")

# Use a grid layout to arrange the widgets
button.grid(row=0, column=0)
label.grid(row=1, column=0)

# Start the event loop
window.mainloop()
