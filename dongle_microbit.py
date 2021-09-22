def on_received_string(receivedString):
    # Write the device name to the serial port. By pressing the reset button on the micro:bit, the device name will be displayed on the laptop. This helps with debugging, to ensure that the serial port is working
    serial.write_line(receivedString)
radio.on_received_string(on_received_string)

def on_data_received():
    global strings
    strings = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
    basic.show_string(strings)
    radio.send_string(strings)
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

strings = ""
line = ""
key = ""
val = 0
basic.clear_screen()
radio.set_group(33)
# Write the device name to the serial port. By pressing the reset button on the micro:bit, the device name will be displayed on the laptop. This helps with debugging, to ensure that the serial port is working
serial.write_line(control.device_name())
# Every 2 seconds, if the followed variable is set to 1, then send a sensor reading to the serial port

def on_forever():
    followed = 0
    if followed == 1:
        serial.write_value("a_x", input.acceleration(Dimension.X))
    basic.pause(2000)
basic.forever(on_forever)