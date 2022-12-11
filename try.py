#!/usr/bin/python


class TryOut:
    from RotaryEncoder import RotaryEncoder

    def __init__(self):
        self.rotaryEncoder = self.RotaryEncoder(clk_GPIO=6, dt_GPIO=13, switch_GPIO=5, min_counter=0, max_counter=10,
                                                back_to_front=False)

    def test(self):
        print('State: {}  Value: {}'.format(self.rotaryEncoder.last_state, self.rotaryEncoder.counter))


if __name__ == '__main__':
    tryOut = TryOut()
