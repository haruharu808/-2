/**
 * def on_button_pressed_a():
 */
/**
 * t = 12
 */
/**
 * e = 37.6991118430775
 */
/**
 * print("reset")
 */
let m = 0
let k = 0
let l2 = 1
let l = 1
// print(31.4 / 10)
let t = 12
let e = 37.6991118430775
let d = ["─────────────────────"]
basic.forever(function () {
    l = randint(0.1, 20)
    t = t * l
    e = e * l
    m = e / t
    // print(t + '/' + e)
    // print(k)
    d.push("" + m + "   :=" + ("" + e) + "/" + ("" + t))
    pins.analogPitch(500, 100)
    basic.clearScreen()
    for (let list1 of d) {
        console.log(list1)
    }
    basic.pause(1000)
    led.plot(randint(1, 5), randint(1, 5))
})
