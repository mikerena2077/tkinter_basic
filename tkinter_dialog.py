import tkinter as tk
from tkinter import font

# Create the main window
window = tk.Tk()
window.geometry("300x300")

# Define the font size for the buttons
button_font = font.Font(size=20)

# Create the buttons
button1 = tk.Button(window, text="Button 1", font=button_font)
button2 = tk.Button(window, text="Button 2", font=button_font)
button3 = tk.Button(window, text="Button 3", font=button_font)

# Place the buttons on the window using grid layout
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()
