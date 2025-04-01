import tkinter as tk

def say_hello():
    label.config(text="Hello, User!")

# Create main window
root = tk.Tk()
root.title("My App")

# Create a button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

# Create a label
label = tk.Label(root, text="Welcome!")
label.pack()

# Run the application
root.mainloop()
