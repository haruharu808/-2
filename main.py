# def on_button_pressed_a():
# t = 12
# e = 37.6991118430775
# print("reset")
# input.on_button_pressed(Button.A, on_button_pressed_a)
k = 0
e = 0
t = 0
l2 = 1
l = 1
# print(31.4 / 10)
t = 12
e = 37.6991118430775
d = ["─────────────────────"]

def on_forever():
    global l, t, e
    l = randint(0.1, 20)
    t = t * l
    e = e * l
    m = e / t
    # print(t + '/' + e)
    # print(k)
    d.append("" + str(m) + "   :=" + ("" + str(e)) + "/" + ("" + str(t)))
    pins.analog_pitch(500, 100)
    basic.clear_screen()
    for list1 in d:
        print(list1)
    basic.pause(1000)
    led.plot(randint(1, 5), randint(1, 5))
basic.forever(on_forever)
