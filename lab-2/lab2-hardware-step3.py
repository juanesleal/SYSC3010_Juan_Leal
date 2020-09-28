#using the led on the sense hat to display a user inputed message using left and right
import sense_hat, time, random

sense = sense_hat.SenseHat()

right_key = sense_hat.DIRECTION_RIGHT
left_key = sense_hat.DIRECTION_LEFT
pressed = sense_hat.ACTION_PRESSED
message_right = input("Enter message for right joystick push:")
message_left = input("Enter message for left joystick push:")
time.sleep(1)
while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    events = sense.stick.get_events()
    if events:
        for e in events:
                print("starting loop")
        if e.direction ==  right_key and e.action == pressed:
                sense.show_message(message_right,text_colour=[r,g,b])
                print("Joystick right press detected")
        elif e.direction ==  left_key and e.action == pressed:
                sense.show_message(message_left,text_colour=[r,g,b])
                print("Joystick left press detected")
        else:
                print("Nothing detected")
    
