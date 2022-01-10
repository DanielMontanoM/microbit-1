def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                # # # # #
                # . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                # . . . #
                . # . # .
                # . . . #
    """)
basic.forever(on_forever)
