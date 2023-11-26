import tkinter as tk

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.seconds_left = 120
        self._timer_on = False
        self.home_score = 0
        self.visitor_score = 0
        self.caution_home_count = 0
        self.caution_visitor_count = 0
        self.penalty_home_count = 0
        self.penalty_visitor_count = 0
        self.stalling_home_count = 0
        self.stalling_visitor_count = 0
        self.create_widgets()
        self.show_widgets()
        

    def show_widgets(self):
        self.weight_class.grid(row=0, column=1, columnspan=2)
        self.period.grid(row=1, column=1, columnspan=2)

        #home score and scoring buttons
        self.home_score_label.grid(row=1, column=0)
        self.home_score_score.grid(row=2, column=0)
        self.takedown_home_bt.grid(row=3, column=0)
        self.reversal_home_bt.grid(row=4, column=0)
        self.escape_home_bt.grid(row=5, column=0)
        self.nearfall_2_home_bt.grid(row=6, column=0)
        self.nearfall_3_home_bt.grid(row=7, column=0)
        self.penalty_home_bt.grid(row=8, column=0)
        self.caution_home_bt.grid(row=9, column=0)
        self.stalling_home_bt.grid(row=10, column=0)
        self.minus_1_home_bt.grid(row=11, column=0)

        #visitor score and scoring buttons
        self.visitor_score_label.grid(row=1, column=4)
        self.visitor_score_score.grid(row=2, column=4)
        self.takedown_visitor_bt.grid(row=3, column=4)
        self.reversal_visitor_bt.grid(row=4, column=4)
        self.escape_visitor_bt.grid(row=5, column=4)
        self.nearfall_2_visitor_bt.grid(row=6, column=4)
        self.nearfall_3_visitor_bt.grid(row=7, column=4)
        self.penalty_visitor_bt.grid(row=8, column=4)
        self.caution_visitor_bt.grid(row=9, column=4)
        self.stalling_visitor_bt.grid(row=10, column=4)
        self.minus_1_visitor_bt.grid(row=11, column=4)

        #game clock
        self.clock.grid(row=2, column=1, columnspan=2)

        #buttons to change game time
        self.minutes_label.grid(row=3, column=1)
        self.inc_min_button.grid(row=4, column=1)
        self.dec_min_button.grid(row=5, column=1)
        self.seconds_label.grid(row=3, column=2)
        self.inc_sec_button.grid(row=4, column=2)              
        self.dec_sec_button.grid(row=5, column=2)

        #start and stop game clock
        self.start_button.grid(row=6, column=1)
        self.stop_button.grid(row=6, column=2)

    def create_widgets(self):
        self.weight_class = tk.Label(self, text="Weight Class")
        self.period = tk.Label(self, text="Period: ")

        #home score and scoring buttons
        self.home_score_label = tk.Label(self, text="Home", font=("Helvetica", 48))
        self.home_score_score = tk.Label(self, text=self.home_score, font=("Helvetica", 48))
        self.takedown_home_bt   = tk.Button(self, text="Takedown", font=("Helvetica", 12), command=self.takedown_home)
        self.reversal_home_bt = tk.Button(self, text="Reversal", font=("Helvetica", 12), command=self.reversal_home)
        self.escape_home_bt = tk.Button(self, text="Escape", font=("Helvetica", 12), command=self.escape_home)
        self.nearfall_2_home_bt = tk.Button(self, text="Nearfall +2", font=("Helvetica", 12), command=self.nearfall_2_home)
        self.nearfall_3_home_bt = tk.Button(self, text="Nearfall +3", font=("Helvetica", 12), command=self.nearfall_3_home)
        self.penalty_home_bt = tk.Button(self, text="Penalty", font=("Helvetica", 12), command=self.penalty_home)
        self.caution_home_bt = tk.Button(self, text="Caution", font=("Helvetica", 12), command=self.caution_home)
        self.stalling_home_bt = tk.Button(self, text="Stalling", font=("Helvetica", 12), command=self.stalling_home)
        self.minus_1_home_bt = tk.Button(self, text="-1", command=self.dec_home_score)

        #visitor score and scoring buttons
        self.visitor_score_label = tk.Label(self, text="Visitor", font=("Helvetica", 48))
        self.visitor_score_score = tk.Label(self, text=self.visitor_score, font=("Helvetica", 48))
        self.takedown_visitor_bt = tk.Button(self, text="Takedown", font=("Helvetica", 12), command=self.takedown_visitor)
        self.reversal_visitor_bt = tk.Button(self, text="Reversal", font=("Helvetica", 12), command=self.reversal_visitor)
        self.escape_visitor_bt = tk.Button(self, text="Escape", font=("Helvetica", 12), command=self.escape_visitor)
        self.nearfall_2_visitor_bt = tk.Button(self, text="Nearfall +2", font=("Helvetica", 12), command=self.nearfall_2_visitor)
        self.nearfall_3_visitor_bt = tk.Button(self, text="Nearfall +3", font=("Helvetica", 12), command=self.nearfall_3_visitor)
        self.penalty_visitor_bt = tk.Button(self, text="Penalty", font=("Helvetica", 12), command=self.penalty_visitor)
        self.caution_visitor_bt = tk.Button(self, text="Caution", font=("Helvetica", 12), command=self.caution_visitor)
        self.stalling_visitor_bt = tk.Button(self, text="Stalling", font=("Helvetica", 12), command=self.stalling_visitor)
        self.minus_1_visitor_bt = tk.Button(self, text="-1", command=self.dec_visitor_score)

        #game clock
        self.clock = tk.Label(self, text="02:00", font=("Helvetica", 48), relief="solid", bd=5)

        #buttons to change game clock
        self.minutes_label = tk.Label(self, text="Minutes")
        self.inc_min_button = tk.Button(self, text="^", command=self.inc_min, font=("Helvetica", 15))
        self.dec_min_button = tk.Button(self, text="ˇ", command=self.dec_min, font=("Helvetica", 15))
        self.seconds_label = tk.Label(self, text="Seconds")
        self.inc_sec_button = tk.Button(self, text="^", command=self.inc_sec, font=("Helvetica", 15))
        self.dec_sec_button = tk.Button(self, text="ˇ", command=self.dec_sec, font=("Helvetica", 15))

        #buttons to start and stop game clock
        self.start_button = tk.Button(self, text="Start", command=self.start, bg="green")
        self.stop_button = tk.Button(self, text="Stop", command=self.stop, bg="red")


    #clock functions
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

    def _update_clock(self):
        self._set_time(self.seconds_left)
        if self._timer_on and self.seconds_left:
            self.seconds_left -= 1
            self.after(1000, self._update_clock)

    def _set_time(self, seconds_left):
        minutes, seconds = divmod(seconds_left, 60)
        hours, minutes = divmod(minutes, 60)
        self.clock.configure(text="%02d:%02d" % (minutes, seconds))    
    

    #scoreboard functions
    #home scoring functions
    def takedown_home(self):
        self.home_score += 2
        self._set_home_score(self.home_score)

    def reversal_home(self):
        self.home_score += 2
        self._set_home_score(self.home_score)

    def escape_home(self):
        self.home_score += 1
        self._set_home_score(self.home_score)

    def nearfall_2_home(self):
        self.home_score += 2
        self._set_home_score(self.home_score)

    def nearfall_3_home(self):
        self.home_score += 3
        self._set_home_score(self.home_score)

    def penalty_home(self):
        self.penalty_home_count += 1
        if self.penalty_home_count < 3:
            self.visitor_score += 1
            self._set_visitor_score(self.visitor_score)
        else:
            self.visitor_score += 2
            self._set_visitor_score(self.visitor_score)

    def caution_home(self):
        self.caution_home_count += 1
        if self.caution_home_count >= 3 and (self.caution_home_count <4 or self.penalty_home_count < 2):
            self.visitor_score += 1
            self.penalty_home_count += 1
            self._set_visitor_score(self.visitor_score)
        elif self.caution_home_count >=4 or self.penalty_home_count >= 2:
            self.visitor_score += 2
            self.penalty_home_count += 1
            self._set_visitor_score(self.visitor_score)

    def stalling_home(self):
        self.stalling_home_count += 1
        if self.stalling_home_count > 1 and self.stalling_home_count <= 3:
            self.visitor_score += 1
            self._set_visitor_score(self.visitor_score)
        elif self.stalling_home_count > 3:
            self.visitor_score += 2
            self._set_visitor_score(self.visitor_score)

    def dec_home_score(self):
        self.home_score -= 1
        self._set_home_score(self.home_score)
    
    #visitor scoring functions
    def takedown_visitor(self):
        self.visitor_score += 2
        self._set_visitor_score(self.visitor_score)

    def reversal_visitor(self):
        self.visitor_score += 2
        self._set_visitor_score(self.visitor_score)

    def escape_visitor(self):
        self.visitor_score += 1
        self._set_visitor_score(self.visitor_score)

    def nearfall_2_visitor(self):
        self.visitor_score += 2
        self._set_visitor_score(self.visitor_score)

    def nearfall_3_visitor(self):
        self.visitor_score += 3
        self._set_visitor_score(self.visitor_score)

    def penalty_visitor(self):
        self.penalty_visitor_count += 1
        if self.penalty_visitor_count < 3:
            self.home_score += 1
            self._set_home_score(self.home_score)
        else:
            self.home_score += 2
            self._set_home_score(self.home_score)

    def caution_visitor(self):
        self.caution_visitor_count += 1
        if self.caution_visitor_count >= 3 and (self.caution_visitor_count <4 or self.penalty_visitor_count < 2):
            self.home_score += 1
            self.penalty_visitor_count += 1
            self._set_home_score(self.home_score)
        elif self.caution_visitor_count >=4 or self.penalty_visitor_count >= 2:
            self.home_score += 2
            self.penalty_visitor_count += 1
            self._set_home_score(self.home_score)

    def stalling_visitor(self):
        self.stalling_visitor_count += 1
        if self.stalling_visitor_count > 1 and self.stalling_visitor_count <= 3:
            self.home_score += 1
            self._set_home_score(self.home_score)
        elif self.stalling_visitor_count > 3:
            self.home_score += 2
            self._set_home_score(self.home_score)

    def dec_visitor_score(self):
        self.visitor_score -= 1
        self._set_visitor_score(self.visitor_score)

    #refreshing the scores after each scoreboard button press 
    def _set_home_score(self, home_score):
        self.home_score_score.configure(text="%02d" % home_score)
    
    def _set_visitor_score(self, visitor_score):
        self.visitor_score_score.configure(text="%02d" % visitor_score)

    

if __name__ == "__main__":
    root = tk.Tk()
    countdown = Countdown(root)
    countdown.pack()
    root.mainloop()
    