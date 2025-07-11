import tkinter as tk

class SpamLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spam Lock App")
        self.root.attributes('-fullscreen', True)  # Fullscreen
        self.root.attributes('-topmost', True)     # Always on top
        self.root.configure(bg="black")

        # Disable close, alt+F4, and other attempts to close
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.root.bind("<Alt-F4>", self.disable_event)
        self.root.bind("<Escape>", self.disable_event)
        self.root.bind("<Control-Key-w>", self.disable_event)
        self.root.bind("<Control-q>", self.disable_event)

        # Label to show spam text
        self.spam_label = tk.Label(self.root, text="", font=("Arial", 48, "bold"), fg="red", bg="black")
        self.spam_label.pack(expand=True)

        # Label for author text at bottom right corner
        self.author_label = tk.Label(self.root, text="made by Lankuchung", font=("Arial", 14), fg="white", bg="black")
        self.author_label.pack(side="bottom", anchor="e", padx=10, pady=10)

        # Messages to spam
        self.messages = ["YOU ARE GAY", "TRUST ME YOU ARE GAY"]
        self.current_index = 0

        # Start spamming
        self.spam_text()

    def spam_text(self):
        self.spam_label.config(text=self.messages[self.current_index])
        self.current_index = (self.current_index + 1) % len(self.messages)
        # Update text every 400 milliseconds
        self.root.after(400, self.spam_text)

    def disable_event(self, event=None):
        # Do nothing to disable window close or attempt to escape
        return "break"

def main():
    root = tk.Tk()
    app = SpamLockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
