class RotaryEncoder:

    from RPi import GPIO
    from time import sleep

    def __init__(self):
        self.clk = 13
        self.dt = 6

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.clk, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.setup(self.dt, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)

        self.counter = 0
        self.clkLastState = self.GPIO.input(self.clk)


if __name__ == '__main__':

    rotaryEncoder = RotaryEncoder()
    try:

        while True:
            clkState = rotaryEncoder.GPIO.input(rotaryEncoder.clk)
            dtState = rotaryEncoder.GPIO.input(rotaryEncoder.dt)
            if clkState != rotaryEncoder.clkLastState:
                if dtState != clkState:
                    rotaryEncoder.counter += 1
                else:
                    rotaryEncoder.counter -= 1
                print(rotaryEncoder.counter)
            rotaryEncoder.clkLastState = clkState
            rotaryEncoder.sleep(0.01)
    finally:
        rotaryEncoder.GPIO.cleanup()
