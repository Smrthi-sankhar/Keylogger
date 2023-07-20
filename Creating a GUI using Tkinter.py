import tkinter as tk

def save_to_file():
    text = entry.get()
    if text.strip():  # Ensure there is non-empty text to save
        with open("keystrokes.txt", "a") as file:
            file.write(text + "\n")
        entry.delete(0, tk.END)  # Clear the entry field after saving

root = tk.Tk()
root.title("Keystrokes Logger")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack()

root.mainloop()
