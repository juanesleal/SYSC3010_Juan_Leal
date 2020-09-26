import sense_hat, time

sense = sense_hat.SenseHat()

right_key = sense_hat.DIRECTION_RIGHT
left_key = sense_hat.DIRECTION_LEFT
pressed = sense_hat.ACTION_PRESSED
while True:
    events = sense.stick.get_events()
    if events:
        for e in events:
                print("starting loop")
        if e.direction ==  right_key and e.action == pressed:
                sense.show_letter("J",text_colour=[0,100,100])
                print("Joystick right press detected")
        elif e.direction ==  left_key and e.action == pressed:
                sense.show_letter("L",text_colour=[200,0,0])
                print("Joystick left press detected")
        else:
                print("Nothing detected")
    