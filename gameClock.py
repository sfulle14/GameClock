import tkinter as tk

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False
        self.home_score = 0
        self.visitor_score = 0

    def show_widgets(self):
        self.home_score_label.grid(row=0, column=0)
        self.visitor_score_label.grid(row=0, column=1)
        self.inc_min_button.grid(row=1, column=0)
        self.inc_sec_button.grid(row=1, column=1)
        self.label.grid(row=2, column=0, columnspan=2)
        self.dec_min_button.grid(row=3, column=0)
        self.dec_sec_button.grid(row=3, column=1)
        self.start_button.grid(row=4, column=0)
        self.stop_button.grid(row=4, column=1)

    def create_widgets(self):
        self.home_score_label = tk.Label(self, text="Home: 0", font=("Helvetica", 48))
        self.visitor_score_label = tk.Label(self, text="Visitor: 0", font=("Helvetica", 48))
        self.label = tk.Label(self, text="00:00:00", font=("Helvetica", 48), relief=tk.SUNKEN, bd=10)
        self.inc_min_button = tk.Button(self, text="^ mins", command=self.inc_min)
        self.dec_min_button = tk.Button(self, text="Decrease mins", command=self.dec_min)
        self.inc_sec_button = tk.Button(self, text="^ secs", command=self.inc_sec)
        self.dec_sec_button = tk.Button(self, text="Decrease secs", command=self.dec_sec)
        self.start_button = tk.Button(self, text="Start", command=self.start, bg="green")
        self.stop_button = tk.Button(self, text="Stop", command=self.stop, bg="red")

    def inc_min(self):
        self.seconds_left += 60
        self._set_time(self.seconds_left)

    def dec_min(self):
        self.seconds_left -= 60
        self._set_time(self.seconds_left)

    def inc_sec(self):
        self.seconds_left += 1
        self._set_time(self.seconds_left)

    def dec_sec(self):
        self.seconds_left -= 1
        self._set_time(self.seconds_left)

    def start(self):
        self._timer_on = True
        self._update_clock()

    def stop(self):
        self._timer_on = False

    def inc_home_score(self):
        self.home_score +=1
    
    def dec_home_score(self):
        self.home_score -= 1

    def inc_visitor_score(self):
        self.visitor_score += 1

    def dec_visitor_score(self):
        self.visitor_score -= 1

    def _update_clock(self):
        self._set_time(self.seconds_left)
        if self._timer_on and self.seconds_left:
            self.seconds_left -= 1
            self.after(1000, self._update_clock)

    def _set_time(self, seconds_left):
        minutes, seconds = divmod(seconds_left, 60)
        hours, minutes = divmod(minutes, 60)
        self.label.configure(text="%02d:%02d:%02d" % (hours, minutes, seconds))

if __name__ == "__main__":
    root = tk.Tk()
    countdown = Countdown(root)
    countdown.pack()
    root.mainloop()