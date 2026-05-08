import tkinter as tk

class RansomSim:
            def __init__(self, root):
                self.root = root
                self.root.title("SECURITY ALERT")
                self.root.attributes("-fullscreen", True)  
                self.root.configure(bg="black")             
                self.label = tk.Label(root, text="YOUR FILES ARE ENCRYPTED!", 
                                      fg="red", bg="black", font=("Helvetica", 36, "bold"))
                self.label.pack(expand=True)
                self.info = tk.Label(root, text="PAY 0.032 BITCOIN TO THIS ADDRESS TO UNENCRYPT THEM: bc1p6aktp2ruufxuqgv9lfwwgajlckxg2srlle3fe70umrzyu23rhfjsx9jzgx", 
                                     fg="white", bg="red", font=("Helvetica", 18))
                self.info.pack(pady=20)
                self.time_left = 86400  
                self.timer_label = tk.Label(root, text="", fg="white", bg="red", 
                                            font=("Helvetica", 48, "bold"))
                self.timer_label.pack(expand=True)
                self.update_timer()

            def update_timer(self):
                hours, remainder = divmod(self.time_left, 3600)
                minutes, seconds = divmod(remainder, 60)
                time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                self.timer_label.config(text=time_str)
                if self.time_left > 0:
                    self.time_left -= 1
                    self.root.after(1000, self.update_timer)

root = tk.Tk()
app = RansomSim(root)
root.mainloop()