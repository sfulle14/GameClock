import tkinter as tk

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.seconds_left = 0
        self._timer_on = False
        self.home_score = 0
        self.visitor_score = 0
        self.create_widgets()
        self.show_widgets()
        

    def show_widgets(self):
        self.weight_class.grid(row=0, column=1, columnspan=2)
        self.period.grid(row=1, column=1, columnspan=2)

        self.home_score_label.grid(row=1, column=0)
        self.home_score_score.grid(row=2, column=0)
        self.takedown_home.grid(row=3, column=0)
        self.reversal_home.grid(row=4, column=0)
        self.escape_home.grid(row=5, column=0)
        self.nearfall_2_home.grid(row=6, column=0)
        self.nearfall_3_home.grid(row=7, column=0)
        self.penalty_1_home.grid(row=8, column=0)
        self.penalty_2_home.grid(row=9, column=0)
        self.caution_home.grid(row=10, column=0)
        self.stalling_home.grid(row=11, column=0)

        self.visitor_score_label.grid(row=1, column=4)
        self.visitor_score_score.grid(row=2, column=4)
        self.takedown_visitor.grid(row=3, column=4)
        self.reversal_visitor.grid(row=4, column=4)
        self.escape_visitor.grid(row=5, column=4)
        self.nearfall_2_visitor.grid(row=6, column=4)
        self.nearfall_3_visitor.grid(row=7, column=4)
        self.penalty_1_visitor.grid(row=8, column=4)
        self.penalty_2_visitor.grid(row=9, column=4)
        self.caution_visitor.grid(row=10, column=4)
        self.stalling_visitor.grid(row=11, column=4)

        self.clock.grid(row=2, column=1, columnspan=2)

        self.inc_min_button.grid(row=4, column=1)
        self.dec_min_button.grid(row=5, column=1)

        self.inc_sec_button.grid(row=4, column=2)              
        self.dec_sec_button.grid(row=5, column=2)

        self.start_button.grid(row=6, column=1)
        self.stop_button.grid(row=6, column=2)

    def create_widgets(self):
        self.weight_class = tk.Label(self, text="Weight Class")
        self.period = tk.Label(self, text="Period: ")

        self.home_score_label = tk.Label(self, text="Home", font=("Helvetica", 48))
        self.home_score_score = tk.Label(self, textvariable=self.home_score, font=("Helvetica", 48))
        self.takedown_home   = tk.Button(self, text="Takedown", font=("Helvetica", 12))
        self.reversal_home = tk.Button(self, text="Reversal", font=("Helvetica", 12))
        self.escape_home = tk.Button(self, text="Escape", font=("Helvetica", 12))
        self.nearfall_2_home = tk.Button(self, text="Nearfall +2", font=("Helvetica", 12))
        self.nearfall_3_home = tk.Button(self, text="Nearfall +3", font=("Helvetica", 12))
        self.penalty_1_home = tk.Button(self, text="Penalty +1", font=("Helvetica", 12))
        self.penalty_2_home = tk.Button(self, text="Penalty +2", font=("Helvetica", 12))
        self.caution_home = tk.Button(self, text="Caution", font=("Helvetica", 12))
        self.stalling_home = tk.Button(self, text="Stalling", font=("Helvetica", 12))

        self.visitor_score_label = tk.Label(self, text="Visitor", font=("Helvetica", 48))
        self.visitor_score_score = tk.Label(self, textvariable=self.visitor_score, font=("Helvetica", 48))
        self.takedown_visitor   = tk.Button(self, text="Takedown", font=("Helvetica", 12))
        self.reversal_visitor = tk.Button(self, text="Reversal", font=("Helvetica", 12))
        self.escape_visitor = tk.Button(self, text="Escape", font=("Helvetica", 12))
        self.nearfall_2_visitor = tk.Button(self, text="Nearfall +2", font=("Helvetica", 12))
        self.nearfall_3_visitor = tk.Button(self, text="Nearfall +3", font=("Helvetica", 12))
        self.penalty_1_visitor = tk.Button(self, text="Penalty +1", font=("Helvetica", 12))
        self.penalty_2_visitor = tk.Button(self, text="Penalty +2", font=("Helvetica", 12))
        self.caution_visitor = tk.Button(self, text="Caution", font=("Helvetica", 12))
        self.stalling_visitor = tk.Button(self, text="Stalling", font=("Helvetica", 12))

        self.clock = tk.Label(self, text="00:00", font=("Helvetica", 48), relief=tk.SUNKEN, bd=10)

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
        self.clock.configure(text="%02d:%02d" % (minutes, seconds))

if __name__ == "__main__":
    root = tk.Tk()
    countdown = Countdown(root)
    countdown.pack()
    root.mainloop()
    