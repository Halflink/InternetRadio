class RotaryEncoder:

    from RPi import GPIO
    from time import sleep

    def __init__(self, clk_GPIO, dt_GPIO, switch_GPIO,  min_counter, max_counter, back_to_front):
        self.clk = clk_GPIO  # 6
        self.dt = dt_GPIO  # 13
        self.switch = switch_GPIO

        self.max_counter = max_counter
        self.min_counter = min_counter
        self.back_to_front = back_to_front

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.clk, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.setup(self.dt, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.setup(self.switch, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)

        self.counter = 0
        self.last_state = "00"

    def check_rotary_counter(self):
        if self.back_to_front and self.counter > self.max_counter:
            self.counter = self.max_counter
        elif self.back_to_front and self.counter < self.min_counter:
            self.counter = self.min_counter
        elif not self.back_to_front and self.counter > self.max_counter:
            self.counter = self.min_counter
        elif not self.back_to_front and self.counter < self.min_counter:
            self.counter = self.max_counter

    def check_rotary_state(self):
        clk_state = self.GPIO.input(self.clk)
        dt_state = self.GPIO.input(self.dt)
        state = "{}{}".format(clk_state, dt_state)
        if state != self.last_state:
            if state == "10":
                # Clockwise
                self.counter += 1
            if state == "01":
                # Counterclockwise
                self.counter -= 1
            print("State: {} counter: {}".format(state, self.counter))

        self.sleep(0.01)
        self.last_state = state

    def check_switch_state(self):
        switch_state = self.GPIO.input(self.switch)
        self.sleep(0.05)
        return switch_state == 0


if __name__ == '__main__':

    rotaryEncoder = RotaryEncoder(clk_GPIO=6, dt_GPIO=13, switch_GPIO=5, min_counter=0, max_counter=100,
                                  back_to_front=False)
    try:

        while True:
            rotaryEncoder.check_rotary_state()
            rotaryEncoder.check_switch_state()
            #if rotaryEncoder.check_switch_state():
            #print(rotaryEncoder.counter)
            rotaryEncoder.sleep(0.01)
    finally:
        rotaryEncoder.GPIO.cleanup()
