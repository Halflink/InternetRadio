class RotaryEncoder:

    from RPi import GPIO
    from time import sleep

    def __init__(self, clk_GPIO, dt_GPIO, switch_GPIO,  min_counter, max_counter, back_to_front, call_back=None,
                 call_back_switch=None):
        self.clk = clk_GPIO  # 6
        self.dt = dt_GPIO  # 13
        self.switch = switch_GPIO
        self.max_counter = max_counter
        self.min_counter = min_counter
        self.back_to_front = back_to_front
        self.call_back = call_back
        self.call_back_switch = call_back_switch
        self.counter = 0
        self.last_state = "00"

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.clk, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.setup(self.dt, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.setup(self.switch, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.add_event_detect(self.clk, self.GPIO.BOTH, callback=self.check_rotary_state)
        self.GPIO.add_event_detect(self.dt, self.GPIO.BOTH, callback=self.check_rotary_state)
        self.GPIO.add_event_detect(self.switch, self.GPIO.BOTH, callback=self.check_switch_state)

    def check_rotary_counter(self):
        if self.back_to_front and self.counter > self.max_counter:
            self.counter = self.min_counter
        elif self.back_to_front and self.counter < self.min_counter:
            self.counter = self.max_counter
        elif not self.back_to_front and self.counter > self.max_counter:
            self.counter = self.max_counter
        elif not self.back_to_front and self.counter < self.min_counter:
            self.counter = self.min_counter

    def check_rotary_state(self, channel):
        clk_state = self.GPIO.input(self.clk)
        dt_state = self.GPIO.input(self.dt)
        state = "{}{}".format(clk_state, dt_state)
        if state != self.last_state and state == '11':
            if self.last_state == '10':
                # Clockwise
                self.counter += 1
            elif self.last_state == '01':
                # Counterclockwise
                self.counter -= 1
            self.check_rotary_counter()
            self.call_back()

        self.last_state = state

    def check_switch_state(self, channel):
        state = self.GPIO.input(self.switch)
        if state == 1:
            selected = self.counter
            self.call_back_switch(selected)
        self.sleep(0.05)


