def on_button_pressed_a():
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    radio.send_string("Hello")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    radio.send_string("Bye")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(33)

def on_forever():
    pass
basic.forever(on_forever)
